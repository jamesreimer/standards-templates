# Provenance

This repository consumes generic repository mechanics from
[`jamesreimer/repo-template`](https://github.com/jamesreimer/repo-template).
The source relationship is governed by
[`shared-asset-provenance`](templates/shared-asset-provenance/standard.md).
Validation is Authoritative Consumption: source identity, immutable state, and
actual content correspondence must all be established. Provenance does not confer
organizational authority or permission to publish.

## Current consumed baseline

| Identity | Value |
| --- | --- |
| Source | `jamesreimer/repo-template` |
| Release basis | `v1.0.1` plus unreleased cleanup |
| Immutable repository revision | `5d59902e900f593c5535839371b2e4bba884afce` |

The commit is the binding identity. This untagged revision includes the
post-v1.0.1 link-test documentation and metadata cleanup in
[upstream PR #36](https://github.com/jamesreimer/repo-template/pull/36). A moving
branch, sibling checkout, or local path does not prove immutable consumption.

Generic mechanics were extracted from this repository into `repo-template`,
which now owns their maintenance. The adoption record is
[PR #129](https://github.com/jamesreimer/standards-templates/pull/129).

## Current relationship classes

### Exact copies at the recorded revision

Each file below has the same path upstream and must be byte-identical to the
current immutable revision:

- `.editorconfig`
- `.github/dependabot.yml`
- `.markdownlint-cli2.jsonc`
- `requirements-dev.txt`
- `package.json`
- `package-lock.json`
- `markdownlint-rules/fenced-code-closed.cjs`
- `tools/check-links.mjs`
- `tools/link-frontmatter.mjs`
- `tests/fixtures/yaml-stream.yaml`
- `tests/markdown-rules.test.cjs`
- `tests/link-validation.test.mjs`
- `tests/link-validation/README.md`
- `tests/link-validation/contract.json`
- `tests/link-validation/import-control.mjs`
- `tests/link-validation/native-control.mjs`

### Adapted copies reviewed against the recorded revision

- `.pre-commit-config.yaml`: preserve every baseline hook and add a first,
  fail-fast metadata/policy guard plus independent domain, whole-repository,
  and preservation-test hooks.
- `.github/workflows/validate.yml`: inherit the released runtime, action pins,
  permissions, concurrency, timeout and aggregate command; add `git diff --check`.
- `AGENTS.md`, `CONTRIBUTING.md`, `README.md`: retain standards-library governance
  and responsibility while adopting the current tooling and maintenance model.
- `.github/pull_request_template.md`: retain scope, evidence and adoption review
  questions and update validation expectations.
- `ruff.toml`: retain local style and import checks; use the Python 3.10 floor.

Adapted copies are intentionally different and must not be overwritten as exact.

### Historical copies retained independently

`SECURITY.md`, `.gitignore`, and `.gitattributes` retain their historical adapted
relationship to `4318faa00cd6d02c78247ed799fbcae61210a43c`; no v1.0.1 byte-copy
claim is made. `.vscode/settings.json` retains its earlier exact-copy bytes but
is now maintained as a historical adapted copy: the continuing exact-copy
obligation is deliberately retired because the current baseline no longer
supplies it. Explicit Git attributes and editor behavior remain preserved.

### Local and generated material

Standards templates, catalog/adoption/naming guidance, LICENSE, other governance
content, `scripts/validate_local.py`, and `tests/test_validate_local.py` remain
local. Their standards semantics are not transferred upstream.

The generic preservation controls and their tests are local **transitional**
material, not permanently standards-specific responsibilities:

| Files | Protected outcomes |
| --- | --- |
| `tools/check-repository-policy.mjs`, `tests/repository-policy.test.mjs` | Required roots, scoped names and README basename convention, snapshot integrity, selected UTF-8/newlines, junk/credential filenames, metadata-first rejection of all symlinks |
| `tools/check-repository-markdown.mjs`, `tests/repository-markdown-selection.test.mjs` | Tracked plus unignored Markdown, cross-file effects, repository headings, destination containment and inventory membership through maintained AST parsing |
| `tests/validation-composition.test.mjs` | Aggregate fail-fast ordering and native YAML multi-document behavior |

Generic responsibility remains with repo-template. This repository maintains
these narrowly bounded controls until an upstream/native replacement satisfies
the same protected outcomes, or legitimate authority explicitly retires a policy.
Re-evaluate them whenever adopting a new baseline; compare behavior and injected
defect evidence before retiring a control. Do not synchronize them automatically,
turn them into a generic framework, or move standards semantics into them.
They add no runtime or dependency beyond the inherited tooling stack.

`repository-structure.txt` is generated from the tracked plus unignored inventory
by `node tools/check-repository-policy.mjs --write-snapshot`. Both generator and
input inventory are downstream-owned working state until committed together;
ordinary validation only compares the reviewed snapshot.

### Installed material

npm dependencies are bound by the exact package manifest and lockfile. The
pre-commit runner is pinned in `requirements-dev.txt`; hook source revisions and
isolated environments are selected by `.pre-commit-config.yaml`. Installation
paths alone are not identity evidence. Use locked installation and retain the
front-matter effective-renderer startup probe.

## Verification and updates

Compare exact copies against Git objects at the full upstream SHA, not mutable
checkout bytes. For example, from this repository with an independently verified
upstream clone:

```sh
git -C /path/to/repo-template show 5d59902e900f593c5535839371b2e4bba884afce:tools/check-links.mjs | cmp - tools/check-links.mjs
```

Verify every declared exact path before accepting a candidate. Resolve the source
repository and immutable commit separately from content comparison; a matching
filename is not evidence. Inspect adapted copies against that same commit and
retain their deliberate local responsibilities. Record correspondence and test
results in the implementation/review record.

For future adoption, review upstream changes, verify the new exact copies,
reconcile adaptations and temporary controls, exercise preserved defect classes,
run the full validation composition, and update this record in the same candidate.
A newer upstream release does not authorize automatic propagation or replace
this repository's authority. A successful mechanical check does not alone prove
architecture, prose quality, or publication readiness.
