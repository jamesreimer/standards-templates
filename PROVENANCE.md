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
| Release | `v1.0.1` |
| Immutable repository revision | `4877171f3a45ed98645e8be7af8fa5e32e5b6a90` |

The commit is the binding identity; the tag is its human-facing label. A moving
branch, sibling checkout, or local path does not prove immutable consumption.
The reconciliation is based on downstream revision
`ec6df67afd53387b132cd29d6b64bbe1fe0e715f`.

## Historical consumed states

The earlier completed adoption consumed
`4318faa00cd6d02c78247ed799fbcae61210a43c` on 2026-09-16. At that revision,
`scripts/validate.py`, `scripts/update_repository_structure.py`,
`scripts/setup_git_hooks.py`, `tests/test_validate.py`, `.githooks/pre-commit`,
`.editorconfig`, `.vscode/settings.json`, and `.github/dependabot.yml` were
recorded as exact copies. Those relationships remain historical evidence.

This reconciliation first staged generic assets from the first stable release,
`v1.0.0 @ f677c176b5573c1a51f4bfb91650c0bde09d6a48`, without completing or publishing
that adoption. Real downstream integration exposed a generic directory-link
correctness defect. It was corrected at the owning upstream source, reviewed,
and published as v1.0.1. The deliberate rebinding consumes that correction and
the already-merged setup-node v7 maintenance update. It does not rewrite the
v1.0.0 baseline or the preceding adoption history.

The old generic Python engine, generator, installer, hook shim, test harness,
and `validate.json` have been retired. They are not hidden dependencies of the
new aggregate. Their absence upstream is not represented as an exact-copy claim.

## History of ownership

The mechanics in this repository did not originate upstream.

They were written here first. `repo-template` was created afterwards, by
generalizing them out of this repository into a reusable foundation, and this
repository was its first consumer. Adoption therefore transferred ownership
upstream rather than recording a dependency that always existed.

That transfer is legitimate and deliberate: ownership follows system
responsibility rather than file history, and a repository whose purpose is
publishing standards templates was never the right long-term owner of generic
repository mechanics. But §4.1 forbids silently redefining a source or
reversing a declared maintenance relationship, and §12 requires distinguishing
historical provenance from continuing ownership. Both directions are recorded
here so neither is mistaken for the other.

Adoption also pushed capability upstream rather than only pulling it down. Nine
generic checks that existed only here were contributed to `repo-template`
across two reconciliation rounds, so that they would be owned once rather than
duplicated: committed symlinks, reference-label resolution, heading-level
skips, per-scope path naming, a single leading H1, fenced code block balance,
reference-definition validity and uniqueness, and correct loading of a local
check module.

## Current relationship classes

### Exact copies at v1.0.1

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

### Adapted copies reviewed against v1.0.1

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
git -C /path/to/repo-template show 4877171f3a45ed98645e8be7af8fa5e32e5b6a90:tools/check-links.mjs | cmp - tools/check-links.mjs
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
