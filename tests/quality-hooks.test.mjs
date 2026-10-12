import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import {
  copyFileSync,
  existsSync,
  readdirSync,
  mkdirSync,
  mkdtempSync,
  readFileSync,
  rmSync,
  symlinkSync,
  writeFileSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";
import { parse, stringify } from "yaml";
import { getFileInfo, resolveConfig } from "prettier";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const tools = [
  {
    id: "lint-js",
    package: "eslint",
    bin: "bin/eslint.js",
    options: ["--max-warnings=0", "--"],
    invalid: "missingName();\n",
  },
  {
    id: "format-check",
    package: "prettier",
    bin: "bin/prettier.cjs",
    options: ["--check", "--"],
    invalid: "console.log('bad')\n",
  },
];
const names = [
  "ordinary.mjs",
  "nested/example.mjs",
  "file with spaces.mjs",
  "meta[ab].mjs",
  "choice{a,b}.mjs",
  "!bang.mjs",
  "--option.mjs",
];
const decoys = ["metaa.mjs", "metab.mjs", "choicea.mjs", "choiceb.mjs"];
const valid = 'console.log("ok");\n';

// A shell-backed npm entry can expand braces before either tool sees argv.
// Keep this wiring assertion alongside actual CLI path/decoy behavior.
test("quality hooks invoke root package binaries directly with selected filenames", () => {
  const config = parse(
    readFileSync(join(root, ".pre-commit-config.yaml"), "utf8"),
  );
  const localHooks = config.repos
    .filter((repo) => repo.repo === "local")
    .flatMap((repo) => repo.hooks);
  for (const tool of tools) {
    const hooks = localHooks.filter((hook) => hook.id === tool.id);
    assert.equal(hooks.length, 1);
    const hook = hooks[0];
    assert.equal(hook.language, "system");
    assert.equal(
      hook.entry,
      `node node_modules/${tool.package}/${tool.bin} ${tool.options.join(" ")}`,
    );
    assert.notEqual(hook.always_run, true);
    assert.notEqual(hook.pass_filenames, false);
    const manifest = JSON.parse(
      readFileSync(join(root, "node_modules", tool.package, "package.json")),
    );
    const declared =
      typeof manifest.bin === "string"
        ? manifest.bin
        : manifest.bin[tool.package];
    assert.equal(declared.replace(/^\.\//, ""), tool.bin);
    const extensions =
      tool.id === "lint-js"
        ? ["js", "cjs", "mjs"]
        : ["js", "cjs", "mjs", "json", "jsonc", "yaml", "yml", "md"];
    for (const extension of extensions)
      assert.match(`example.${extension}`, new RegExp(hook.files));
    for (const extension of [
      "html",
      "css",
      "py",
      "toml",
      "txt",
      ...(tool.id === "lint-js" ? ["json", "jsonc", "yaml", "yml", "md"] : []),
    ]) {
      assert.doesNotMatch(`example.${extension}`, new RegExp(hook.files));
    }
    if (tool.id === "format-check") {
      for (const name of [
        "package-lock.json",
        "tests/link-validation/contract.json",
        "tests/fixtures/yaml-stream.yaml",
      ]) {
        assert.match(name, new RegExp(hook.exclude));
      }
      for (const name of [
        "README.md",
        "tools/example.mjs",
        ".prettierrc.json",
      ]) {
        assert.doesNotMatch(name, new RegExp(hook.exclude));
      }
    }
  }
});

for (const tool of tools) {
  test(`${tool.package} checks literal filenames and rejects invalid batches without selecting decoys`, (t) => {
    const dir = mkdtempSync(join(tmpdir(), "quality-filenames-"));
    t.after(() => rmSync(dir, { recursive: true, force: true }));
    for (const name of [
      "eslint.config.mjs",
      ".prettierrc.json",
      ".prettierignore",
    ]) {
      copyFileSync(join(root, name), join(dir, name));
    }
    // The copied ESLint config imports @eslint/js from the same installed graph.
    symlinkSync(
      join(root, "node_modules"),
      join(dir, "node_modules"),
      "junction",
    );
    for (const name of names) {
      mkdirSync(dirname(join(dir, name)), { recursive: true });
      writeFileSync(join(dir, name), valid);
    }
    function check(selected, expected) {
      const result = spawnSync(
        process.execPath,
        [
          join(root, "node_modules", tool.package, tool.bin),
          ...tool.options,
          ...selected,
        ],
        { cwd: dir, encoding: "utf8", timeout: 30000 },
      );
      assert.ifError(result.error);
      assert.equal(result.signal, null);
      const output = result.stdout + result.stderr;
      assert.equal(result.status, expected, output);
      for (const decoy of decoys) assert.ok(!output.includes(decoy), output);
      return output;
    }
    for (const name of names) {
      // Invalid unselected siblings must not make a valid literal path fail.
      for (const decoy of decoys) writeFileSync(join(dir, decoy), tool.invalid);
      check([name], 0);
      // Valid decoys must not hide an invalid selected filename.
      for (const decoy of decoys) writeFileSync(join(dir, decoy), valid);
      writeFileSync(join(dir, name), tool.invalid);
      assert.ok(check([name], 1).includes(name));
      assert.equal(readFileSync(join(dir, name), "utf8"), tool.invalid);
      writeFileSync(join(dir, name), valid);
    }
    for (const decoy of decoys) writeFileSync(join(dir, decoy), tool.invalid);
    check(names, 0);
    for (const decoy of decoys) writeFileSync(join(dir, decoy), valid);
    writeFileSync(join(dir, "choice{a,b}.mjs"), tool.invalid);
    for (const selected of [names, [...names].reverse()]) {
      assert.ok(check(selected, 1).includes("choice{a,b}.mjs"));
    }
  });
}

const localRunner = join(root, ".venv/bin/pre-commit");
const runner = existsSync(localRunner) ? localRunner : "pre-commit";
const hooks = parse(readFileSync(join(root, ".pre-commit-config.yaml"), "utf8"))
  .repos.filter((repo) => repo.repo === "local")
  .flatMap((repo) => repo.hooks);
function stagedFixture(t, selectedHooks) {
  const dir = mkdtempSync(join(tmpdir(), "quality-staged-"));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  for (const name of [
    "eslint.config.mjs",
    ".prettierrc.json",
    ".prettierignore",
  ])
    copyFileSync(join(root, name), join(dir, name));
  symlinkSync(
    join(root, "node_modules"),
    join(dir, "node_modules"),
    "junction",
  );
  writeFileSync(join(dir, ".gitignore"), "node_modules/\n");
  writeFileSync(
    join(dir, ".pre-commit-config.yaml"),
    stringify({ repos: [{ repo: "local", hooks: selectedHooks }] }),
  );
  const git = (args) =>
    execFileSync("git", args, { cwd: dir, encoding: "utf8" });
  git(["init", "-q"]);
  git(["add", "."]);
  git([
    "-c",
    "user.name=Test",
    "-c",
    "user.email=test@example.invalid",
    "-c",
    "core.hooksPath=/dev/null",
    "commit",
    "-qm",
    "Fixture",
  ]);
  const run = (id) => {
    const result = spawnSync(runner, ["run", id, "--verbose"], {
      cwd: dir,
      encoding: "utf8",
      timeout: 60000,
      maxBuffer: 8 * 1024 * 1024,
    });
    assert.ifError(result.error);
    assert.equal(result.signal, null);
    return { status: result.status, output: result.stdout + result.stderr };
  };
  return { dir, git, run };
}
for (const tool of tools) {
  test(`actual ${tool.package} hook checks staged literal names and restores unstaged contents`, (t) => {
    const { dir, git, run } = stagedFixture(t, [
      hooks.find((hook) => hook.id === tool.id),
    ]);
    const literal = "choice{a,b}.mjs";
    for (const name of [literal, ...decoys])
      writeFileSync(join(dir, name), valid);
    git(["add", "."]);
    git([
      "-c",
      "user.name=Test",
      "-c",
      "user.email=test@example.invalid",
      "-c",
      "core.hooksPath=/dev/null",
      "commit",
      "-qm",
      "Literal paths",
    ]);
    writeFileSync(join(dir, literal), tool.invalid);
    git(["add", "--", literal]);
    writeFileSync(join(dir, literal), valid);
    const invalid = run(tool.id);
    assert.equal(invalid.status, 1, invalid.output);
    assert.ok(invalid.output.includes(literal), invalid.output);
    assert.match(invalid.output, /Stashing unstaged files/u);
    assert.equal(readFileSync(join(dir, literal), "utf8"), valid);
    writeFileSync(join(dir, literal), 'console.log("changed");\n');
    git(["add", "--", literal]);
    writeFileSync(join(dir, literal), tool.invalid);
    const positive = run(tool.id);
    assert.equal(positive.status, 0, positive.output);
    assert.match(positive.output, /Stashing unstaged files/u);
    assert.equal(readFileSync(join(dir, literal), "utf8"), tool.invalid);
  });
}
test("Prettier independently ignores every normative path and preserves manual and staged source", async (t) => {
  const hook = hooks.find((hook) => hook.id === "format-check");
  const current = readdirSync(join(root, "templates"))
    .filter((name) => existsSync(join(root, "templates", name, "standard.md")))
    .map((name) => `templates/${name}/standard.md`);
  assert.equal(current.length, 19);
  const normative = [...current, "templates/future-standard/standard.md"];
  const config = await resolveConfig(join(root, "README.md"));
  assert.equal(config.proseWrap, "preserve");
  assert.equal(config.embeddedLanguageFormatting, "off");
  const { dir, git, run } = stagedFixture(t, [hook]);
  const original = new Map();
  for (const name of normative) {
    assert.match(name, new RegExp(hook.exclude));
    mkdirSync(dirname(join(dir, name)), { recursive: true });
    const content = current.includes(name)
      ? readFileSync(join(root, name))
      : Buffer.from("# Future\n\n|a|b|\n|-|-|\n|c|d|\n");
    original.set(name, content);
    writeFileSync(join(dir, name), content);
    assert.equal(
      (
        await getFileInfo(join(dir, name), {
          ignorePath: join(dir, ".prettierignore"),
        })
      ).ignored,
      true,
      name,
    );
  }
  for (const name of [
    "templates/future-standard/README.md",
    "templates/deep/nested/standard.md",
    "README.md",
    "tools/example.mjs",
  ]) {
    assert.doesNotMatch(name, new RegExp(hook.exclude));
    assert.equal(
      (
        await getFileInfo(join(dir, name), {
          ignorePath: join(dir, ".prettierignore"),
        })
      ).ignored,
      false,
      name,
    );
  }
  // Direct CLI has no pre-commit exclusion; only .prettierignore protects it.
  const manual = spawnSync(
    process.execPath,
    [
      join(root, "node_modules/prettier/bin/prettier.cjs"),
      "--check",
      "--",
      ...normative,
    ],
    { cwd: dir, encoding: "utf8", timeout: 30000 },
  );
  assert.ifError(manual.error);
  assert.equal(manual.status, 0, manual.stdout + manual.stderr);
  // Remove the ignore rule so the staged-hook exclusion must work on its own.
  writeFileSync(join(dir, ".prettierignore"), "node_modules/\n");
  git(["add", "."]);
  const staged = run("format-check");
  assert.equal(staged.status, 0, staged.output);
  for (const [name, content] of original)
    assert.deepEqual(readFileSync(join(dir, name)), content, name);
  // Sensitivity control: absent BOTH exclusions, the future path must fail.
  const exposed = spawnSync(
    process.execPath,
    [
      join(root, "node_modules/prettier/bin/prettier.cjs"),
      "--check",
      "--",
      normative.at(-1),
    ],
    { cwd: dir, encoding: "utf8", timeout: 30000 },
  );
  assert.equal(exposed.status, 1, exposed.stdout + exposed.stderr);
  assert.deepEqual(
    readFileSync(join(dir, normative.at(-1))),
    original.get(normative.at(-1)),
  );
});

for (const tool of tools) {
  test(`${tool.package} rejects a defect in the final forced pre-commit partition`, (t) => {
    // Fixture-only serial execution fixes ordering. The argv size, not CPU count,
    // forces splitting; production hooks keep pre-commit's default concurrency.
    const hook = {
      ...hooks.find((hook) => hook.id === tool.id),
      require_serial: true,
    };
    const { dir, git, run } = stagedFixture(t, [hook]);
    const marker =
      tool.id === "lint-js" ? "Quality batch" : "Checking formatting...";
    if (tool.id === "lint-js") {
      const config = join(dir, "eslint.config.mjs");
      writeFileSync(
        config,
        readFileSync(config, "utf8") + '\nconsole.log("Quality batch");\n',
      );
      git(["add", "eslint.config.mjs"]);
      git([
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.invalid",
        "-c",
        "core.hooksPath=/dev/null",
        "commit",
        "-qm",
        "Observe fixture partitions",
      ]);
    }
    const names = Array.from(
      { length: 800 },
      (_, index) =>
        `batch-${String(index).padStart(4, "0")}-${"a".repeat(180)}.mjs`,
    );
    assert.ok(names.join(" ").length > 2 ** 17);
    for (const name of names) writeFileSync(join(dir, name), valid);
    git(["add", "."]);
    const positive = run(tool.id);
    assert.equal(positive.status, 0, positive.output);
    const count = positive.output.split(marker).length - 1;
    assert.ok(count > 1, positive.output);
    const last = names.at(-1);
    writeFileSync(join(dir, last), tool.invalid);
    git(["add", "--", last]);
    const invalid = run(tool.id);
    assert.equal(invalid.status, 1, invalid.output);
    const partitions = invalid.output.split(marker).slice(1);
    assert.equal(partitions.length, count);
    for (const earlier of partitions.slice(0, -1))
      assert.ok(!earlier.includes(last), earlier);
    assert.ok(partitions.at(-1).includes(last), invalid.output);
    assert.equal(readFileSync(join(dir, last), "utf8"), tool.invalid);
  });
}
