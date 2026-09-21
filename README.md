# Standards Templates

Reusable, organization-neutral templates for standards and policies.

This repository provides source templates that organizations may deliberately adopt into their own standards repositories. The templates here are **not authoritative for any organization by themselves**. Once an organization adopts a template, the organization governs the resulting standard or policy, its scope, its lifecycle, and any later changes. This canonical governance does not by itself transfer copyright or other intellectual-property rights in source material.

## Repository responsibility

This repository owns:

- reusable standards and policy templates;
- stable template identities;
- guidance for deliberate organizational adoption;
- repository-level naming rules for templates and their human-facing titles;
- maintenance guidance for evaluating and reviewing changes to this library.

This repository does not own:

- company or client standards;
- downstream organizational lifecycle state;
- automatic synchronization of adopted standards;
- project planning or work tracking for adopting organizations;
- organization-specific rules that have not been generalized into an organization-neutral template.

## Adoption model

The default relationship is:

```text
source template
    ↓ deliberate adoption
organizational standard or policy
    ↓ independent lifecycle
accept / adapt / reject later template changes
```

Adoption creates a new organizational artifact governed by the adopter. The upstream template remains provenance and a possible source of future improvements, not continuing authority over the adopted standard or policy.

See [ADOPTION.md](ADOPTION.md) for the adoption and relationship model.

## Repository validation

Repository validation composes the maintained generic tools from
`repo-template v1.0.1` with independently executable standards-specific checks.
Install Python 3.10 or later, Git, and Node.js 24.18.1 (including npm), then run:

```sh
npm ci --ignore-scripts
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/pre-commit run --all-files --show-diff-on-failure
git diff --check
```

On Windows, use `.venv\Scripts\python.exe` and
`.venv\Scripts\pre-commit.exe` instead. CI runs the same pre-commit composition,
using Python 3.12 and Node 24.18.1. Initial dependency and hook installation needs
network access; required link checking is offline. Stage intended new files
before the all-files run so native hooks see them.

The aggregate first rejects unsafe file metadata and checks repository policy
and the reviewed structure snapshot. It stops on failure before later hooks read
repository content. Native hooks check syntax, hygiene, Markdown authoring,
local links and fragments, Python, and workflows. Additional whole-repository
checks include tracked and new unignored inputs, so an unchanged document is
rechecked when its target is changed or removed.

Standards-specific validation remains standard-library Python and can run alone:

```sh
python3 scripts/validate_local.py
python3 -m unittest discover -s tests
```

It checks template structure and stable IDs, catalog membership and title
agreement, declared local requirement schemes and references in template
`standard.md` files, and obvious uppercase BCP 14 keyword near misses. Input and
runtime failures prevent success. No old generic Python engine is involved.

Linkinator owns local destinations and fragments; Markdownlint owns authoring
rules, with MD051 disabled. Directory links need no `index.html`; missing
locations fail. Real `index.html` fragments are checked, but generated directory
listings provide no fragment-validation contract. Use an explicit file link
when a fragment must be checked. External HTTP/HTTPS links are excluded.

These checks do not establish normative strength, applicability, conceptual
boundaries, citation correctness, external evidence, legal interpretation,
editorial quality, or prose quality. Requirement references outside template
`standard.md` files and semantic cross-standard dependency correctness remain
outside automated domain validation.

After an intentional structural change, explicitly regenerate the snapshot:

```sh
node tools/check-repository-policy.mjs --write-snapshot
```

Validation compares the snapshot and never silently rewrites it. Optional commit
hooks use `.venv/bin/pre-commit install`; they are not installed by validation or
CI. See [CONTRIBUTING.md](CONTRIBUTING.md) for hook migration, selection, and
maintenance details, and [PROVENANCE.md](PROVENANCE.md) for current and historical
source relationships and temporary preservation controls.

## Template catalog

See [CATALOG.md](CATALOG.md) for the current reusable template inventory, each template's durable subject, and important boundaries between existing templates.

The catalog describes only templates that currently exist; it is not a roadmap or backlog.

## Repository structure

```text
templates/
└── <template-id>/
    ├── README.md
    └── standard.md
```

Each template directory contains the reusable document and adoption guidance specific to that template.

## Naming

Each template has:

- a short, stable folder ID that identifies its durable subject; and
- a separate human-facing title that describes the document clearly and accurately.

See [NAMING.md](NAMING.md) for the **template naming** standard used inside this repository. Repository naming and filesystem naming are separate reusable subjects covered by the [`repository-naming`](templates/repository-naming/) and [`filesystem-naming`](templates/filesystem-naming/) templates.

## Non-normative Web Standards Suite guidance

See [Web Standards Suite Assessment Guidance](web-standards-assessment-guidance.md) for non-normative assistance with assessment and evidence recording. It does not create adoption or conformance authority or a normative dependency.

## Contributing and maintenance

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contributor path and [MAINTAINING.md](MAINTAINING.md) for the repository's maintenance and review path.

Automated coding agents should also follow [AGENTS.md](AGENTS.md), which routes agent work through the repository's maintainer, contribution, and applicable naming and authoring guidance.

## License

Unless otherwise noted, all repository-authored material in this repository is dedicated to the public domain under [CC0 1.0 Universal](LICENSE). This includes the standards templates and documentation; maintenance tooling under `scripts/`, `tools/`, `markdownlint-rules/`, and `tests/`; repository automation and contribution configuration under `.github/`; editor and Git configuration in `.editorconfig`, `.gitattributes`, `.gitignore`, and `.vscode/`; and the generated `repository-structure.txt` snapshot.

The existing [`LICENSE`](LICENSE) file provides the CC0 legal code for this scope. No separate software license applies to the current repository material.

Materials released under CC0 remain available under CC0 for those released versions. Software or other materials added later may be licensed separately where explicitly indicated; adding separately licensed material does not change the CC0 status of material already released under it.

The repository may preserve provenance and source relationships for adopted templates, but downstream attribution is not required by CC0. Organizational adoption creates an independently governed standard or policy rather than an ongoing authority relationship with this repository.

## Design principle

This repository grows only through demonstrated need. Its eventual size is not a target in either direction: restraint, not smallness, is the objective. Apply this decision model to every addition — templates, repository structure, metadata, validation, automation, taxonomy, or related machinery:

- **Build now:** Add something only when the need is concrete or imminent, confidence is high, the change is proportionate, and it naturally belongs to the repository's current responsibility.
- **Name a trigger:** When a real need depends on a specific future condition, record that trigger rather than implementing the addition prematurely. A named trigger is not a roadmap commitment.
- **Leave speculative needs unbuilt:** Do not add something without a concrete forcing function.

Repeated use within one context, convenience, or an apparent gap in the catalog does not by itself justify expansion. Demonstrated, independent reuse across genuinely different contexts is exactly the evidence this model looks for. A concrete failure may also show that an addition is needed.

This model governs whether to add repository material; it does not determine the authority or normative content of a standard or policy.
