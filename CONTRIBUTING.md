# Contributing

Keep contributions bounded to a concrete or imminent need that is high-confidence, proportionate, and within the repository's current responsibility, or to a concrete defect. Use [MAINTAINING.md](MAINTAINING.md) for the maintainer review criteria, [NAMING.md](NAMING.md) for template identity and titles, and [CATALOG.md](CATALOG.md) to check current ownership and boundaries.

## Branch names and pull request titles

Use a conventional type prefix that describes the work for new contribution branches and pull request titles. Use the same type for the branch and its pull request:

| Type | Work | Branch example | Pull request title example |
| --- | --- | --- | --- |
| `feat` | New or extended functionality or normative requirements | `feat/execution-path-rules` | `feat: extend execution-path rules` |
| `fix` | Corrections to defects | `fix/broken-catalog-link` | `fix: correct broken catalog link` |
| `docs` | Documentation and guidance changes | `docs/contribution-naming` | `docs: document contribution naming` |
| `chore` | Repository maintenance or configuration | `chore/update-validation-config` | `chore: update validation configuration` |
| `refactor` | Restructuring without changing behavior or normative meaning | `refactor/validator-helpers` | `refactor: simplify validator helpers` |

Format branch names as `<type>/<short-kebab-case-description>` and pull request titles as `<type>: <concise description>`. Choose the type from the substance of the change; a normative requirement change is not merely documentation work because it is written in Markdown.

## Addition decisions

Apply the repository-wide [addition-decision model](README.md#design-principle) before adding templates, repository structure, metadata, validation, automation, taxonomy, or related machinery.

## New template

```text
identify a concrete or imminent reusable need
    ↓
check whether an existing template already owns the subject
    ↓
apply NAMING.md
    ↓
author against standards-authoring
    ↓
separate external facts from synthesized rules
    ↓
update CATALOG.md
    ↓
update repository structure snapshot if needed
    ↓
run tests and validation
    ↓
submit a reviewable change
```

A subject does not earn a template merely because an external standards body covers it. General applicability is the default unless the protected consequence genuinely depends on a narrower domain. Do not annex neighboring conceptual territory for completeness. Apply the addition decision model before creating new metadata, taxonomy, validation, automation, or tooling.

Author normative documents against the [`standards-authoring`](templates/standards-authoring/) template and follow the repository structure in [README.md](README.md).

## Existing template revision

```text
identify concrete defect or need
    ↓
open or reference an issue/proposal when warranted
    ↓
modify the canonical template
    ↓
review scope, boundaries, and normative calibration
    ↓
reverify affected external claims
    ↓
run tests and validation
    ↓
submit for review
```

Keep the change within the template's established responsibility unless the proposal explicitly justifies a scope correction. Reverify any external claim or citation affected by the revision.

## Validation

Follow the runtime and setup instructions in [README.md](README.md), stage new
files, and run the authoritative local/CI composition:

```sh
.venv/bin/pre-commit run --all-files --show-diff-on-failure
git diff --check
```

The independent standards-domain command and tests remain available:

```sh
python3 scripts/validate_local.py
python3 -m unittest discover -s tests
```

The pre-commit runner is pinned in `requirements-dev.txt`. npm installs the exact
validation dependencies from `package-lock.json` using `npm ci --ignore-scripts`.
Pre-commit owns pinned Markdownlint, Ruff, actionlint, syntax and hygiene hooks;
there is no separate CI-only validation path. Review hook autofixes and rerun.
Neither green checks nor provenance confer permission to merge or publish.

After intentionally adding, removing, or moving paths, regenerate the reviewed
snapshot before validation:

```sh
node tools/check-repository-policy.mjs --write-snapshot
```

Ordinary validation never writes the snapshot. The inventory contains tracked
and unignored files, including untracked additions, with deterministic ordering.
Missing tracked files fail closed; stage intended removals before regeneration.

## Validator architecture

The current immutable upstream baseline and exact/adapted relationships are in
[PROVENANCE.md](PROVENANCE.md). `repo-template` owns generic mechanics;
standards-specific semantics remain local.

| Responsibility | Mechanism |
| --- | --- |
| Aggregate local/CI composition | Adapted upstream `.pre-commit-config.yaml` |
| Syntax, hygiene, authoring, links/fragments, Python, workflows | Maintained upstream-selected tools and exact-copy regression assets |
| Standards-domain structure, IDs, catalog/title agreement, requirements, BCP 14 spelling | Standard-library Python `scripts/validate_local.py` and `tests/test_validate_local.py` |
| Missing upstream repository policies | Temporary `tools/check-repository-policy.mjs` and tests |
| Whole-repository Markdown selection, heading and destination policy | Temporary `tools/check-repository-markdown.mjs` and tests using the maintained AST |

The temporary generic controls preserve requirements not supplied by the current
baseline; they are not standards-domain tooling. Their protected outcomes and
retirement conditions are recorded in PROVENANCE. Do not rebuild a generic
validator, custom Markdown parser, fragment resolver, or extension framework.
Evaluate generic defects at their owning source; consume qualified corrections
through an explicit baseline update. A standards-domain check belongs in the
independent Python validator and must remain testable without Node or pre-commit.

### Selection and safety

The first hook performs a metadata-only pass over inventory paths and ancestors,
rejecting every symlink before any validation input is read. `fail_fast: true`
prevents later content hooks after that failure. This protects validation input
reads, not pre-commit's bootstrap read of its own configuration. Independent
policy, Markdown, and domain entry points also inspect metadata before content.

Native hooks retain tracked/staged selection. Additional always-run checks read
the full tracked plus unignored inventory, preserving new-document and cross-file
or deletion effects even when a referring document is unchanged. Ignored-only
link targets are not repository destinations. Required root files, scoped names,
UTF-8 and final-newline selection, junk and credential-shaped filenames, and the
snapshot are enforced separately from native syntax and private-key checks.

Repository Markdown requires its first heading to be H1 and exactly one H1 when
headings exist; no-heading documents remain allowed. Local repository-absolute
and escaping destinations are rejected. The maintained AST supplies links,
images and definitions; Linkinator alone checks fragments. Baseline synthetic
fixtures run their own upstream contract, without repository heading policy.

Directory destinations use the exact v1.0.1 wrapper, with native listings enabled.
Existing inventoried directories need no index document; missing ones fail.
Real `index.html` fragments are checked. Generated listings have no native
fragment-validation contract; link explicitly to a Markdown or HTML file when
that validation is required. External HTTP/HTTPS is skipped, including redirects
leaving Linkinator's serving origin. YAML streams use the native multi-document
syntax option. Validation preserves source bytes except explicit native hook
formatting/hygiene fixes, which must be reviewed.

### Scoped naming

| Scope | Convention |
| --- | --- |
| `.github/`, `.githooks/`, `.vscode/` | Owning tool conventions |
| `scripts/*.py`, `tests/*.py` | Lowercase snake_case |
| File basename `README.md` at any depth | Conventional documentation basename |
| `templates/*/standard.md` | Fixed template-owned document |
| Established root documents and explicit tool configuration | Existing named exceptions |
| Other files and directory components | Lowercase kebab-case |

The README exception does not exempt its ancestors, siblings, or unrelated
uppercase basenames such as nested `NOTES.md`, `CHANGELOG.md`, or `SECURITY.md`.
The fixed policy lives in the temporary policy guard; no arbitrary configuration
schema replaces the retired `validate.json`.

### Optional commit hooks

Run `.venv/bin/pre-commit install` to opt in. If an older checkout has a
repository-local `core.hooksPath=.githooks`, inspect
`git config --show-origin --get-all core.hooksPath` and remove only that obsolete
local setting before installation. Preserve unrelated hook owners and
higher-precedence settings. Validation and CI do not change Git configuration.
Commit hooks do not replace the full all-files command before a PR.

### Maintenance and evidence

Dependabot covers Actions, pip, and npm monthly. Update hook revisions with
`.venv/bin/pre-commit autoupdate --freeze`, reviewing revisions and compatibility.
Keep the Markdownlint hook and npm test version aligned. Update dependency pins
and lock together; retain the effective-renderer startup probe rather than
assuming a hoisted Marked identity. Run `npm audit` and the complete suite.

When validation changes, exercise valid and injected-invalid cases in isolated
Git repositories. Preserve the domain tests, released link/authoring tests,
repository-policy/selection tests, and composition tests. The composition suite
verifies actual pre-commit fail-fast behavior and native YAML stream handling.
Manually review affected external claims and governing semantics as described in
[MAINTAINING.md](MAINTAINING.md); automated checks do not establish those facts.
