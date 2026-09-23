import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, readFileSync, rmSync, symlinkSync, unlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { test } from 'node:test';
import { assertSafeInputs, checkRepository, isCredential, isJunk, isSelectedText, renderSnapshot, repositoryFiles, requiredFiles, validName } from '../tools/check-repository-policy.mjs';

const source = resolve(dirname(fileURLToPath(import.meta.url)), '..');
function fixture(t) {
  const root = mkdtempSync(join(tmpdir(), 'repository-policy-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  execFileSync('git', ['init', '-q'], { cwd: root });
  for (const file of requiredFiles) writeFileSync(join(root, file), '');
  assert.deepEqual(checkRepository(root, { writeSnapshot: true }), []);
  return root;
}
function put(root, path, content = '\n') {
  mkdirSync(dirname(join(root, path)), { recursive: true });
  writeFileSync(join(root, path), content);
}

test('established root documents and ordinary new Markdown names pass repository policy', t => {
  const root = fixture(t);
  for (const path of ['ADOPTION.md', 'AGENTS.md', 'CATALOG.md', 'CODE_OF_CONDUCT.md', 'CONTRIBUTING.md', 'MAINTAINING.md', 'NAMING.md', 'README.md', 'SECURITY.md', 'new-guidance.md', 'docs/new-guidance.md', 'docs/README.md']) put(root, path);
  assert.deepEqual(checkRepository(root, { writeSnapshot: true }), []);
  assert.deepEqual(checkRepository(root), []);
});
for (const path of ['Bad Name.md', 'NEW_GUIDANCE.md', 'PROVENANCE.md', 'docs/Bad Name.md', 'docs/MAINTAINING.md', 'MAINTAINING.md/notes.md']) {
  test(`snapshot cannot conceal invalid naming: ${path}`, t => {
    const root = fixture(t);
    put(root, path);
    const invalid = path === 'MAINTAINING.md/notes.md' ? 'MAINTAINING.md' : path;
    const finding = `${invalid}: invalid path name`;
    const snapshot = join(root, 'repository-structure.txt');
    const original = readFileSync(snapshot);
    assert.ok(checkRepository(root, { writeSnapshot: true }).includes(finding));
    assert.deepEqual(readFileSync(snapshot), original, 'invalid names must prevent snapshot writes');
    // Even a manually updated, matching inventory cannot authorize a bad name.
    writeFileSync(snapshot, renderSnapshot(repositoryFiles(root)));
    assert.deepEqual(checkRepository(root), [finding]);
    const result = spawnSync(process.execPath, [join(source, 'tools/check-repository-policy.mjs')], { cwd: root, encoding: 'utf8', timeout: 5000 });
    assert.equal(result.status, 1, result.stdout + result.stderr);
    assert.ok(result.stderr.includes(finding));
  });
}

for (const path of ['tests/link-validation/README.md', 'tests/other/README.md', 'tests/link-validation/notes.md', 'README.md', '.pre-commit-config.yaml', 'templates/example/standard.md', 'scripts/validate_local.py', 'tests/__init__.py', '.github/ISSUE_TEMPLATE/task.yml']) {
  test(`allowed naming: ${path}`, () => assert.equal(validName(path), true));
}
for (const path of ['tests/link-validation/NOTES.md', 'tests/link-validation/My-Notes.md', 'tests/other/LICENSE', 'tests/other/CHANGELOG.md', 'tests/other/CONTRIBUTING.md', 'tests/other/SECURITY.md', 'scripts/Bad_Name.py', 'notes/My-Notes.txt', '.unknown']) {
  test(`rejected naming: ${path}`, () => assert.equal(validName(path), false));
}
test('README convention exempts a file, not directory ancestors or siblings', t => {
  const root = fixture(t);
  put(root, 'Bad-Directory/README.md');
  assert.ok(checkRepository(root).some(finding => finding === 'Bad-Directory: invalid path name'));
  assert.equal(validName('nested/README.md', false), false);
});
for (const file of requiredFiles) {
  test(`required root: ${file}`, t => {
    const root = fixture(t);
    unlinkSync(join(root, file));
    assert.ok(checkRepository(root).includes(`${file}: required root file is missing`));
  });
}
test('tracked, unignored and ignored selection with missing tracked failure', t => {
  const root = fixture(t);
  put(root, '.gitignore', 'ignored.md\n');
  put(root, 'ignored.md');
  put(root, 'tracked.md');
  execFileSync('git', ['add', '.'], { cwd: root });
  put(root, 'new.md');
  assert.ok(repositoryFiles(root).includes('new.md'));
  assert.ok(!repositoryFiles(root).includes('ignored.md'));
  unlinkSync(join(root, 'tracked.md'));
  assert.throws(() => checkRepository(root), /tracked.md: metadata unavailable/u);
});
test('snapshot is explicit, deterministic and never auto-written on validation', t => {
  const root = fixture(t);
  const initial = readFileSync(join(root, 'repository-structure.txt'));
  put(root, 'notes/details.md');
  assert.ok(checkRepository(root).some(finding => finding.includes('snapshot differs')));
  assert.deepEqual(readFileSync(join(root, 'repository-structure.txt')), initial);
  assert.deepEqual(checkRepository(root, { writeSnapshot: true }), []);
  const updated = readFileSync(join(root, 'repository-structure.txt'));
  assert.match(updated.toString(), /notes\/\nnotes\/details.md/u);
  assert.deepEqual(checkRepository(root, { writeSnapshot: true }), []);
  assert.deepEqual(readFileSync(join(root, 'repository-structure.txt')), updated);
  assert.deepEqual(checkRepository(root), []);
});
test('selected text rejects invalid UTF-8 and missing newline, accepts empty/nonselected binary', t => {
  const root = fixture(t);
  put(root, 'bad.txt', Buffer.from([255]));
  put(root, 'last.py', 'pass');
  put(root, 'empty.md', '');
  put(root, 'image.bin', Buffer.from([255]));
  const findings = checkRepository(root);
  assert.ok(findings.some(finding => finding.startsWith('bad.txt: cannot read UTF-8')));
  assert.ok(findings.includes('last.py: missing final newline'));
  assert.ok(!findings.some(finding => finding.startsWith('empty.md:') || finding.startsWith('image.bin:')));
  for (const extension of ['cfg','css','html','ini','js','json','jsonc','jsx','md','mjs','py','sh','toml','ts','tsx','txt','xml','yaml','yml']) assert.equal(isSelectedText(`new/file.${extension}`), true);
  for (const path of ['.editorconfig', 'nested/.gitignore', '.gitattributes', '.githooks/pre-commit']) assert.equal(isSelectedText(path), true);
});
test('junk patterns and credential allow/reject boundaries survive independently of ignores', t => {
  const root = fixture(t);
  const junk = ['.DS_Store', 'Thumbs.db', 'desktop.ini', 'x.pyc', 'x.pyo', 'x.orig', 'x.rej', 'x~', '__pycache__/file.txt'];
  for (const path of junk) { assert.equal(isJunk(path), true); put(root, `nested/${path}`); }
  const secrets = ['.env', '.env.prod', 'x.pem', 'x.p12', 'x.pfx', 'x.jks', 'x.keystore', 'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519', '.env.prod.sample'];
  for (const path of secrets) { assert.equal(isCredential(path), true); put(root, `nested/${path}`); }
  for (const path of ['.env.example', '.env.sample', '.env.prod.example', 'id_rsa.pub', 'notes.md']) assert.equal(isCredential(`nested/${path}`), false);
  assert.equal(isJunk('cache/file.py'), false);
  const findings = checkRepository(root);
  for (const path of junk) assert.ok(findings.includes(`nested/${path}: junk artifact is not allowed`));
  for (const path of secrets) assert.ok(findings.includes(`nested/${path}: credential-shaped filename is not allowed`));
});
for (const target of ['README.md', '/dev/zero', 'absent.md']) {
  test(`metadata gate rejects symlink without reading target: ${target}`, t => {
    const root = fixture(t);
    symlinkSync(target, join(root, 'linked.md'));
    const result = spawnSync(process.execPath, [join(source, 'tools/check-repository-policy.mjs')], { cwd: root, encoding: 'utf8', timeout: 5000 });
    assert.equal(result.status, 1);
    assert.match(result.stderr, /symbolic links are not allowed/u);
  });
}
test('metadata gate rejects symlink ancestors and snapshot symlink in write mode', t => {
  const root = fixture(t);
  symlinkSync(tmpdir(), join(root, 'linked'));
  assert.throws(() => assertSafeInputs(root, ['linked/nonexistent.md']), /linked: symbolic links/u);
  unlinkSync(join(root, 'repository-structure.txt'));
  symlinkSync('/dev/zero', join(root, 'repository-structure.txt'));
  assert.throws(() => checkRepository(root, { writeSnapshot: true }), /symbolic links/u);
});

test('metadata gate rejects an outside-root path before filesystem reads', t => {
  const root = fixture(t);
  assert.throws(() => assertSafeInputs(root, ['../outside.md']), /path escapes repository/u);
});
