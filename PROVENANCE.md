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
| Release | [`v1.2.1`](https://github.com/jamesreimer/repo-template/releases/tag/v1.2.1) |
| Immutable repository revision | `de0fd9206cf0448d50e0dd0f58f858eea46697ad` |

The commit is the binding identity; the tag is its human-facing label. A moving
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
  and preservation-test hooks, including the local template-edition transition check.
- `.github/workflows/validate.yml`: inherit the released runtime, action pins,
  permissions, concurrency, timeout and aggregate command; add `git diff --check`
  and full checkout history (`fetch-depth: 0`) for edition transitions. The local
  validator consumes the runner's event payload and checked-out parent evidence
  to verify PR/push comparison bases; it runs through the same pre-commit hook
  locally and in CI.
- `AGENTS.md`, `CONTRIBUTING.md`, `README.md`: retain standards-library governance
  and responsibility while adopting the current tooling and maintenance model.
- `.github/pull_request_template.md`: retain scope, evidence and adoption review
  questions and update validation expectations.
- `ruff.toml`: retain local style and import checks; use the Python 3.10 floor.
- `MAINTAINING.md` release procedure: incorporate upstream release preparation,
  annotated-tag and remote-object verification, and partial-publication recovery.
  Retain edition-derived library versioning and notes, exact SHA/path adoption
  provenance, squash-tree correspondence, independent downstream lifecycle,
  optional GitHub Release metadata, and this repository's historical tag treatment.

Adapted copies are intentionally different and must not be overwritten as exact.

The v1.2.0 reconciliation covers both intervening upstream changes: release
maintenance guidance and the restored default-branch ruleset. All 16 exact copies
remain byte-identical to this basis; unchanged adapted tooling retains its local
responsibilities. Upstream instructions for creating new repositories are not
copied into this established standards library. Generic baseline version semantics,
mandatory GitHub Release publication, and upstream-specific historical tag facts
are replaced by the library's explicit release adaptations above. These exclusions
do not exclude the applicable release verification safeguards.

The v1.2.1 update adds the complete-tag release-title convention to the adapted
release procedure, command example, and publication verification. Its only source
change is release-maintenance documentation; exact copies, other adaptations, and
the installed host configuration remain aligned. The temporary controls were
reassessed and retain the same absent-upstream-capability justification below.

### Historical copies retained independently

`SECURITY.md`, `.gitignore`, and `.gitattributes` retain their historical adapted
relationship to `4318faa00cd6d02c78247ed799fbcae61210a43c`; no exact-copy claim against
the current baseline is made. `.vscode/settings.json` retains its earlier exact-copy bytes but
is now maintained as a historical adapted copy: the continuing exact-copy
obligation is deliberately retired because the current baseline no longer
supplies it. Explicit Git attributes and editor behavior remain preserved.

### Local and generated material

Standards templates, catalog/adoption/naming guidance, LICENSE, other governance
content, `scripts/validate_local.py`, `scripts/check_template_editions.py`, and their
Python tests remain
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

These controls were reassessed against v1.2.0. Its validation machinery is unchanged
from the preceding consumed basis and still does not provide the complete policy,
whole-repository selection, metadata-first safety, and composition protections
listed above. The controls therefore remain transitional under the same retirement
conditions; no standards-domain responsibility moves upstream or into these guards.

`repository-structure.txt` is generated from the tracked plus unignored inventory
by `node tools/check-repository-policy.mjs --write-snapshot`. Both generator and
input inventory are downstream-owned working state until committed together;
ordinary validation only compares the reviewed snapshot.

### Installed material

The default-branch ruleset is consumed as installed GitHub host configuration from
`rulesets/default-branch.json` at the recorded revision, not as a copied directory.
Repository ruleset `21741829` matches that baseline, including the GitHub Actions
app binding for `Repository validation`; adoption and verification evidence is in
[issue #141](https://github.com/jamesreimer/standards-templates/issues/141).
Host settings remain repository-owned and require deliberate reconciliation and
read-back verification; see [CONTRIBUTING.md](CONTRIBUTING.md#validation). Copying
upstream `rulesets/` files would not install or prove protection and is unnecessary.

npm dependencies are bound by the exact package manifest and lockfile. The
pre-commit runner is pinned in `requirements-dev.txt`; hook source revisions and
isolated environments are selected by `.pre-commit-config.yaml`. Installation
paths alone are not identity evidence. Follow the
[validation and maintenance instructions](CONTRIBUTING.md#validation).

## Verification and updates

Compare exact copies against Git objects at the full upstream SHA, not mutable
checkout bytes. For example, from this repository with an independently verified
upstream clone:

```sh
git -C /path/to/repo-template show de0fd9206cf0448d50e0dd0f58f858eea46697ad:tools/check-links.mjs | cmp - tools/check-links.mjs
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
