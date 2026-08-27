# Standards Templates

Reusable, organization-neutral templates for standards and policies.

This repository provides source templates that organizations may deliberately adopt into their own standards repositories. The templates here are **not authoritative for any organization by themselves**. Once an organization adopts a template, the organization owns the resulting standard or policy, its scope, its lifecycle, and any later changes.

## Repository responsibility

This repository owns:

- reusable standards and policy templates;
- stable template identities;
- guidance for deliberate organizational adoption;
- repository-level naming rules for templates and their human-facing titles.

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
organization-owned standard or policy
    ↓ independent lifecycle
accept / adapt / reject later template changes
```

Adoption creates a new organization-owned artifact. The upstream template remains provenance and a possible source of future improvements, not continuing authority over the adopted standard or policy.

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
    ├── standard.md
    └── template.yaml
```

Each template directory contains the reusable document, adoption guidance specific to that template, and intentionally thin metadata.

## Current templates

- [`project-repository-model`](templates/project-repository-model/) — responsibility model for durable project artifacts, repositories, issues, planning systems, and related project state.
- [`standards-adoption-model`](templates/standards-adoption-model/) — policy for deliberate organizational adoption, ownership, provenance, and independent lifecycle of reusable standards material.
- [`repository-naming`](templates/repository-naming/) — domain-neutral standard for durable, portable, and appropriately scoped repository names.
- [`filesystem-naming`](templates/filesystem-naming/) — domain-neutral standard for portable, readable file and directory names and path components.

## License

Unless otherwise noted, the standards templates and documentation in this repository are dedicated to the public domain under [CC0 1.0 Universal](LICENSE).

Materials released under CC0 remain available under CC0 for those released versions. Software or other materials added later may be licensed separately where explicitly indicated; adding separately licensed material does not change the CC0 status of template and documentation versions already released under it.

The repository may preserve provenance and source relationships for adopted templates, but downstream attribution is not required by CC0. Organizational adoption creates an independently governed standard or policy rather than an ongoing authority relationship with this repository.

## Design principle

Keep this repository deliberately small. Add structure, metadata, validation, automation, or taxonomy only when concrete use demonstrates the need for it.
