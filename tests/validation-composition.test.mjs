import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { test } from 'node:test';
import { parse, stringify } from 'yaml';
import { checkRepository, requiredFiles } from '../tools/check-repository-policy.mjs';

const source = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const configPath = join(source, '.pre-commit-config.yaml');
const config = parse(readFileSync(configPath, 'utf8'));
const localRunner = join(source, '.venv/bin/pre-commit');
const runner = existsSync(localRunner) ? localRunner : 'pre-commit';
function fixture(t) {
  const root = mkdtempSync(join(tmpdir(), 'validation-composition-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  execFileSync('git', ['init', '-q'], { cwd: root });
  return root;
}
function run(root, configFile, hook) {
  const result = spawnSync(runner, ['run', ...(hook ? [hook] : []), '--config', configFile, '--all-files'],
    { cwd: root, encoding: 'utf8', timeout: 60000 });
  assert.ifError(result.error);
  assert.equal(result.signal, null);
  return result;
}
for (const defect of ['symlink', 'snapshot drift']) {
  test(`actual pre-commit composition stops before content hooks on ${defect}`, t => {
    assert.equal(config.fail_fast, true);
    assert.equal(config.repos[0].repo, 'local');
    const first = config.repos[0].hooks;
    assert.equal(first.length, 1);
    assert.equal(first[0].id, 'repository-policy');
    assert.equal(first[0].always_run, true);
    assert.equal(first[0].pass_filenames, false);
    const root = fixture(t);
    for (const file of requiredFiles) writeFileSync(join(root, file), '');
    // Use the actual configured first hook; replace later hooks with a sentinel.
    // If fail_fast or ordering changes, either this assertion or the probe fails.
    const probe = { fail_fast: config.fail_fast, repos: [{ repo: 'local', hooks: [
      { ...first[0], entry: `node "${join(source, 'tools/check-repository-policy.mjs')}"` },
      { id: 'sentinel', name: 'Content-reading sentinel', language: 'system',
        entry: 'node sentinel.cjs', always_run: true, pass_filenames: false },
    ] }] };
    writeFileSync(join(root, 'sentinel.cjs'), "require('node:fs').writeFileSync('was-read', 'unsafe');\n");
    const probePath = join(root, '.pre-commit-config.yaml');
    writeFileSync(probePath, stringify(probe));
    assert.deepEqual(checkRepository(root, { writeSnapshot: true }), []);
    if (defect === 'symlink') symlinkSync('/dev/zero', join(root, 'linked.md'));
    else writeFileSync(join(root, 'new.md'), '# New\n');
    execFileSync('git', ['add', '.'], { cwd: root });
    const result = run(root, probePath);
    assert.equal(result.status, 1, result.stdout + result.stderr);
    assert.match(result.stdout, defect === 'symlink' ? /symbolic links/ : /snapshot differs/);
    assert.equal(existsSync(join(root, 'was-read')), false);
    assert.doesNotMatch(result.stdout, /Content-reading sentinel/);
  });
}
test('native pinned YAML hook accepts streams and rejects malformed streams', t => {
  const root = fixture(t);
  const path = join(root, 'stream.yaml');
  writeFileSync(path, readFileSync(join(source, 'tests/fixtures/yaml-stream.yaml')));
  execFileSync('git', ['add', '.'], { cwd: root });
  assert.equal(run(root, configPath, 'check-yaml').status, 0);
  writeFileSync(path, 'first: valid\n---\nsecond: [broken\n');
  const result = run(root, configPath, 'check-yaml');
  assert.equal(result.status, 1, result.stdout + result.stderr);
});
