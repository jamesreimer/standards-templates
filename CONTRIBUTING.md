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

Do not use actor or tool names such as `codex/` as branch prefixes. This convention applies to human and automated contributions alike.

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

Run both checks before submitting a change:

```bash
python3 -m unittest discover -s tests
python3 scripts/validate.py
```

CI also checks Markdown hygiene, Python lint and formatting, and GitHub Actions workflows. When a contribution affects those files, run the applicable supplemental checks locally:

```bash
markdownlint-cli2
ruff check scripts tests
ruff format --check scripts tests
actionlint .github/workflows/*.yml
```

`markdownlint-cli2` may be run through `npx markdownlint-cli2` without a separate local install. Ruff (Python) and actionlint (Go) must be installed separately; npm packages named `ruff` or `actionlint` are unrelated projects; do not use them as substitutes. CI pins the supplemental tool versions in `.github/workflows/validate.yml`; match those pins locally when installing Ruff or actionlint so local results do not diverge from CI.

When an intentional change adds, removes, or moves repository paths, regenerate the reviewed structure snapshot before validation:

```bash
python3 scripts/update_repository_structure.py
```

Automated validation checks mechanical repository invariants. Human review remains responsible for normative calibration, applicability, conceptual boundaries, external evidence, and prose quality as described in [MAINTAINING.md](MAINTAINING.md).

## Validator architecture

Validation has two owners, and the boundary between them matters when adding a check.

| File | Owner | Rule |
| --- | --- | --- |
| `scripts/validate.py` | [`jamesreimer/repo-template`](https://github.com/jamesreimer/repo-template) | Exact copy. Never edit it here. |
| `scripts/update_repository_structure.py` | `repo-template` | Exact copy. Never edit it here. |
| `tests/test_validate.py` | `repo-template` | Exact copy. Never edit it here. |
| `validate.json` | this repository | Selects which generic checks run, and over which paths. |
| `scripts/validate_local.py` | this repository | Standards-domain checks only. |
| `tests/test_validate_local.py` | this repository | Covers `scripts/validate_local.py`. |

The adopted revision is recorded in [PROVENANCE.md](PROVENANCE.md).

### Adding a check

Decide first whether the check is generic or standards-specific.

A check is **standards-specific** when it would be meaningless in a repository that is not a library of standards templates: anything about template directories, stable template IDs, the catalog, human-facing titles, local requirement schemes, or BCP 14 keyword spelling. Add it to `scripts/validate_local.py` with tests in `tests/test_validate_local.py`.

A check is **generic** when it would apply to any repository: encoding, newlines, path naming, Markdown structure, link resolution, junk artifacts, credential-shaped filenames, symlinks. It does not belong here even if this repository is the only one that currently wants it. Raise it as an issue in `repo-template`, and adopt the result.

Do not fork `scripts/validate.py` to add either kind. If a check genuinely cannot be expressed through `validate.json` or `scripts/validate_local.py`, that is a defect in the template and belongs upstream. Every generic capability this repository once had was moved upstream rather than reimplemented locally, and `scripts/validate_local.py` is deliberately not a place for checks that could not find another home.

### Configuring the generic checks

`validate.json` selects which checks run. Every key is optional and omitted keys take the default; keys beginning with `_` are ignored and may be used as comments. An unknown check or option is an error rather than a silent no-op.

This repository enables `required-files`, `structure-snapshot`, and `path-names`. The naming policy is expressed entirely as configuration, using ordered per-scope rules: the first rule whose `scope` matches a path decides it, so rules are listed most specific first.

| Scope | Convention |
| --- | --- |
| `.github/`, `.githooks/`, `.vscode/` | whatever the owning tool requires |
| `scripts/*.py`, `tests/*.py` | lowercase `snake_case`, per PEP 8 |
| `templates/*/README.md`, `templates/*/standard.md` | the two fixed template documents |
| root documents and tool configuration | as named |
| everything else | lowercase kebab-case |

Changing a naming convention is a `validate.json` edit, not a code change.

### Writing a local check

`scripts/validate_local.py` defines `extra_checks(context)` and returns `(path, line, reason)` tuples. `context` carries `root`, `files`, and `text`. It is imported as an ordinary module, so `dataclasses`, `typing`, and `from __future__ import annotations` all work. A local check that raises is reported as a finding rather than aborting the run.
