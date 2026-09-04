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

## Naming

Each template has:

- a short, stable folder ID that identifies its durable subject; and
- a separate human-facing title that describes the document clearly and accurately.

See [NAMING.md](NAMING.md) for the **template naming** standard used inside this repository. Repository naming and filesystem naming are separate reusable subjects covered by the [`repository-naming`](templates/repository-naming/) and [`filesystem-naming`](templates/filesystem-naming/) templates.

## Repository structure

```text
templates/
└── <template-id>/
    ├── README.md
    └── standard.md
```

Each template directory contains the reusable document and adoption guidance specific to that template.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contributor path and [MAINTAINING.md](MAINTAINING.md) for the repository's maintenance and review path.

Automated coding agents should also follow [AGENTS.md](AGENTS.md), which routes agent work through the repository's maintainer, contribution, and applicable naming and authoring guidance.

## Template catalog

See [CATALOG.md](CATALOG.md) for the current reusable template inventory, each template's durable subject, and important boundaries between existing templates.

The catalog describes only templates that currently exist; it is not a roadmap or backlog.

## Non-normative Web Standards Suite guidance

See [Web Standards Suite Assessment Guidance](WEB_STANDARDS_ASSESSMENT_GUIDANCE.md) for non-normative assistance with assessment and evidence recording. It does not create adoption or conformance authority or a normative dependency.

## Repository validation

Run the unit tests and validator, which require Python 3 and Git but no third-party Python packages, before submitting or merging changes:

```bash
python3 -m unittest discover -s tests
python3 scripts/validate.py
```

Validation checks template structure, IDs, catalog membership and titles, local Markdown links and anchors, heading and fence structure, UTF-8 and final newlines, junk artifacts, repository symlinks, and obvious malformed uppercase BCP 14 keyword spellings. Repository symlinks are rejected rather than followed, whether their targets are internal or external. The validator does not evaluate normative strength, applicability, conceptual boundaries, citation correctness, external evidence, legal interpretation, or prose quality.

The validator also compares the current visible repository paths with `repository-structure.txt`. After an intentional structural change, regenerate that deterministic snapshot explicitly:

```bash
python3 scripts/update_repository_structure.py
```

Git hooks are optional and are not installed by validation or CI. To run the same tests and validator before local commits, opt in once per checkout:

```bash
python3 scripts/setup_git_hooks.py
```

Setup is idempotent when `core.hooksPath` already names `.githooks`. It refuses
to replace a different existing hooks path unless you explicitly run
`python3 scripts/setup_git_hooks.py --force`.

## License

Unless otherwise noted, all repository-authored material in this repository is dedicated to the public domain under [CC0 1.0 Universal](LICENSE). This includes the standards templates and documentation; maintenance tooling under `scripts/`, `tests/`, and `.githooks/`; repository automation and contribution configuration under `.github/`; editor and Git configuration in `.editorconfig`, `.gitattributes`, `.gitignore`, and `.vscode/`; and the generated `repository-structure.txt` snapshot.

The existing [`LICENSE`](LICENSE) file provides the CC0 legal code for this scope. No separate software license applies to the current repository material.

Materials released under CC0 remain available under CC0 for those released versions. Software or other materials added later may be licensed separately where explicitly indicated; adding separately licensed material does not change the CC0 status of material already released under it.

The repository may preserve provenance and source relationships for adopted templates, but downstream attribution is not required by CC0. Organizational adoption creates an independently governed standard or policy rather than an ongoing authority relationship with this repository.

## Design principle

Keep this repository deliberately small. Use this decision model for additions to templates, repository structure, metadata, validation, automation, taxonomy, or related machinery:

- **Build now:** Add something only when the need is concrete or imminent, confidence is high, the change is proportionate, and it naturally belongs to the repository's current responsibility.
- **Name a trigger:** When a real need depends on a specific future condition, record that trigger rather than implementing the addition prematurely. A named trigger is not a roadmap commitment.
- **Leave speculative needs unbuilt:** Do not add something without a concrete forcing function.

Prior success, repetition, or convenience does not automatically justify expansion. A concrete failure may still demonstrate that an addition is needed. This model governs whether to add repository material; it does not determine the authority or normative content of a standard or policy.
