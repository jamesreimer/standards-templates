import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, readFileSync, rmSync, symlinkSync, unlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { test } from 'node:test';
import { markdownPolicy } from '../tools/check-repository-markdown.mjs';
const source = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const inventory = ['README.md', 'docs/README.md', 'docs/target.md', 'image.png'];
for (const [label, text, fails] of [
  ['one H1', '# Title\n', false],
  ['no headings', 'Text\n', false],
  ['first H2', '## Title\n', true],
  ['two H1', '# First\n\n# Second\n', true],
  ['setext H1', 'Title\n=====\n', false],
  ['code headings excluded', '# Title\n\n```md\n# Example\n```\n', false],
  ['frontmatter headings excluded', '---\nnote: "# text"\n---\n# Title\n', false],
  ['local target', '# Title\n\n[Target](docs/target.md)\n', false],
  ['inventory directory', '# Title\n\n[Docs](docs/)\n', false],
  ['external', '# Title\n\n[External](https://example.invalid)\n', false],
  ['absolute', '# Title\n\n[Target](/docs/target.md)\n', true],
  ['encoded absolute', '# Title\n\n[Target](%2Fdocs/target.md)\n', true],
  ['escape', '# Title\n\n[Target](../outside.md)\n', true],
  ['encoded escape', '# Title\n\n[Target](%2e%2e/outside.md)\n', true],
  ['missing image', '# Title\n\n![Image](missing.png)\n', true],
  ['reference link', '# Title\n\n[Target][ref]\n\n[ref]: /docs/target.md\n', true],
  ['reference image', '# Title\n\n![Image][ref]\n\n[ref]: ../outside.png\n', true],
  ['collapsed reference', '# Title\n\n[ref][]\n\n[ref]: absent.md\n', true],
  ['shortcut reference', '# Title\n\n[ref]\n\n[ref]: absent.md\n', true],
  ['code destinations excluded', '# Title\n\n```md\n[Target](absent.md)\n```\n', false],
]) test(`repository Markdown policy: ${label}`, () => assert.equal(markdownPolicy('README.md', text, inventory).length > 0, fails));

function fixture(t) {
  const root = mkdtempSync(join(tmpdir(), 'repository-markdown-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  execFileSync('git', ['init', '-q'], { cwd: root });
  writeFileSync(join(root, 'README.md'), '# Title\n');
  execFileSync('git', ['add', '.'], { cwd: root });
  return root;
}
function run(root) {
  return spawnSync(process.execPath, [join(source, 'tools/check-repository-markdown.mjs')], { cwd: root, encoding: 'utf8', timeout: 30000 });
}
test('new unignored Markdown enters full released validation; ignored-only targets fail', t => {
  const root = fixture(t);
  assert.equal(run(root).status, 0);
  writeFileSync(join(root, 'new.md'), '# New\n\n[Missing](#missing)\n');
  assert.notEqual(run(root).status, 0);
  unlinkSync(join(root, 'new.md'));
  writeFileSync(join(root, '.gitignore'), 'ignored.md\n');
  writeFileSync(join(root, 'ignored.md'), '# Ignored\n');
  writeFileSync(join(root, 'README.md'), '# Title\n\n[Ignored](ignored.md)\n');
  const result = run(root);
  assert.equal(result.status, 1);
  assert.match(result.stderr, /absent from repository inventory/u);
});
test('cross-file heading change and staged deletion invalidate unchanged source', t => {
  const root = fixture(t);
  writeFileSync(join(root, 'target.md'), '# Target\n');
  writeFileSync(join(root, 'README.md'), '# Title\n\n[Target](target.md#target)\n');
  execFileSync('git', ['add', '.'], { cwd: root });
  assert.equal(run(root).status, 0);
  writeFileSync(join(root, 'target.md'), '# Changed\n');
  assert.notEqual(run(root).status, 0);
  execFileSync('git', ['rm', '-f', 'target.md'], { cwd: root });
  assert.match(run(root).stderr, /absent from repository inventory/u);
});
for (const [label, content] of [
  ['hierarchy skip', '# Title\n\n### Skip\n'],
  ['unclosed fence', '# Title\n\n```sh\ncode\n'],
  ['unresolved reference', '# Title\n\n[Missing][absent]\n'],
  ['duplicate reference', '# Title\n\n[Link][ref]\n\n[ref]: README.md\n[ref]: README.md\n'],
  ['malformed reference', '# Title\n\n[Link][ref]\n\n[ref]:\n'],
]) test(`released mechanisms reject ${label} through whole-repository adapter`, t => {
  const root = fixture(t);
  writeFileSync(join(root, 'README.md'), content);
  assert.notEqual(run(root).status, 0);
});
test('direct Markdown invocation rejects unsafe metadata before content reads', t => {
  const root = fixture(t);
  mkdirSync(join(root, 'docs'));
  symlinkSync('/dev/zero', join(root, 'docs/README.md'));
  const result = run(root);
  assert.equal(result.status, 1);
  assert.match(result.stderr, /symbolic links/u);
});

test('existing directory destinations remain valid through the complete adapter', t => {
  const root = fixture(t);
  mkdirSync(join(root, 'docs'));
  writeFileSync(join(root, 'docs/README.md'), '# Documentation\n');
  writeFileSync(join(root, 'README.md'), '# Title\n\n[Documentation](docs/)\n');
  const result = run(root);
  assert.equal(result.status, 0, result.stdout + result.stderr);
});

for (const [label, target, index, status] of [
  ['directory without slash', 'docs', false, 0],
  ['missing directory', 'absent/', false, 1],
  ['real index fragment', 'docs/#present', true, 0],
  ['missing real index fragment', 'docs/#absent', true, 1],
  ['generated listing fragment contract', 'docs/#absent', false, 0],
]) test(`directory destination behavior: ${label}`, t => {
  const root = fixture(t);
  mkdirSync(join(root, 'docs'));
  writeFileSync(join(root, 'docs/README.md'), '# Documentation\n');
  if (index) writeFileSync(join(root, 'docs/index.html'), '<h1 id="present">Present</h1>\n');
  const content = `# Title\n\n[Directory](${target})\n\n[External](https://example.invalid/)\n`;
  writeFileSync(join(root, 'README.md'), content);
  const result = run(root);
  assert.equal(result.status, status, result.stdout + result.stderr);
  assert.equal(readFileSync(join(root, 'README.md'), 'utf8'), content);
  if (status === 0) {
    const data = JSON.parse(result.stdout.split('\n').find(line => line.startsWith('{"result":')));
    assert.ok(data.result.links.some(link => link.url === 'https://example.invalid/' && link.state === 'SKIPPED'));
  }
});
