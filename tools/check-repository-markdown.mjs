// Temporary repository selection/authoring policy, not a Markdown/link engine.
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, posix, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkFrontmatter from 'remark-frontmatter';
import { visit } from 'unist-util-visit';
import { assertSafeInputs, repositoryFiles } from './check-repository-policy.mjs';

const sourceRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(import.meta.url);
const parser = unified().use(remarkParse).use(remarkFrontmatter, ['yaml', 'toml']);

export function markdownPolicy(file, content, files) {
  const findings = [];
  const tree = parser.parse(content);
  const headings = [];
  visit(tree, 'heading', node => { headings.push(node); });
  if (headings.length && headings[0].depth !== 1) findings.push(`${file}:${headings[0].position.start.line}: first heading must be H1`);
  if (headings.length && headings.filter(node => node.depth === 1).length !== 1) findings.push(`${file}: document must have exactly one H1`);
  // Definitions supply destinations for full, collapsed and shortcut references,
  // including images. Markdownlint owns reference integrity; Linkinator owns fragments.
  visit(tree, node => {
    if (!['link', 'image', 'definition'].includes(node.type)) return;
    const destination = node.url;
    if (!destination || destination.startsWith('#') || destination.startsWith('//') || /^[A-Za-z][A-Za-z0-9+.-]*:/u.test(destination)) return;
    let target;
    try { target = decodeURIComponent(destination.split('#')[0]); }
    catch { findings.push(`${file}:${node.position.start.line}: invalid URL encoding`); return; }
    const resolved = posix.normalize(posix.join(posix.dirname(file), target)).replace(/\/$/u, '');
    let reason;
    if (target.startsWith('/') || target.includes('\\')) reason = 'absolute or platform-dependent destination';
    else if (resolved === '..' || resolved.startsWith('../')) reason = 'destination escapes repository';
    else if (resolved !== '.' && !files.includes(resolved) && !files.some(path => path.startsWith(`${resolved}/`))) reason = 'destination absent from repository inventory';
    if (reason) findings.push(`${file}:${node.position.start.line}: ${reason}: ${destination}`);
  });
  return findings;
}

export function checkMarkdown(root) {
  const files = repositoryFiles(root);
  assertSafeInputs(root, files);
  const markdown = files.filter(file => file.endsWith('.md'));
  const findings = markdown.flatMap(file => markdownPolicy(file, new TextDecoder('utf-8', { fatal: true }).decode(readFileSync(resolve(root, file))), files));
  if (findings.length) { findings.forEach(finding => console.error(finding)); return 1; }
  if (!markdown.length) return 0;
  const cliRoot = dirname(require.resolve('markdownlint-cli2'));
  const cliPackage = JSON.parse(readFileSync(resolve(cliRoot, 'package.json'), 'utf8'));
  const cli = resolve(cliRoot, cliPackage.bin['markdownlint-cli2']);
  // Explicit repository inventory also includes new, unignored Markdown. Prefix
  // paths so filenames cannot become CLI options. No shell command construction.
  for (const args of [
    [cli, '--config', resolve(sourceRoot, '.markdownlint-cli2.jsonc'), ...markdown.map(file => `./${file}`)],
    [resolve(sourceRoot, 'tools/check-links.mjs'), ...markdown.map(file => `./${file}`)],
  ]) {
    const result = spawnSync(process.execPath, args, { cwd: root, stdio: 'inherit' });
    if (result.error) throw result.error;
    if (result.status !== 0) return result.status || 1;
  }
  return 0;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  try { process.exitCode = checkMarkdown(process.cwd()); }
  catch (error) { console.error(error.message); process.exitCode = 1; }
}
