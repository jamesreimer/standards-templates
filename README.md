# Standards Templates

Reusable, organization-neutral templates for engineering and software-development standards.

This repository provides source templates that organizations may deliberately adopt into their own standards repositories. The templates here are **not authoritative for any organization by themselves**. Once an organization adopts a template, the organization owns the resulting standard, its scope, its lifecycle, and any later changes.

## Repository responsibility

This repository owns:

- reusable standards templates;
- stable template identities;
- guidance for deliberate organizational adoption;
- repository-level naming rules for templates and their human-facing titles.

This repository does not own:

- company or client standards;
- downstream organizational lifecycle state;
- automatic synchronization of adopted standards;
- project planning or work tracking for adopting organizations;
- implementation-specific policy that has not been generalized into an organization-neutral template.

## Adoption model

The default relationship is:

```text
source template
    ↓ deliberate adoption
organization-owned standard
    ↓ independent lifecycle
accept / adapt / reject later template changes
```

Adoption creates a new organization-owned artifact. The upstream template remains provenance and a possible source of future improvements, not continuing authority over the adopted standard.

See [ADOPTION.md](ADOPTION.md) for the adoption and relationship model.

## Naming

Each template has:

- a short, stable folder ID that identifies its durable subject; and
- a separate human-facing title that describes the document clearly and accurately.

See [NAMING.md](NAMING.md) for the repository naming standard.

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

- [`project-repository-model`](templates/project-repository-model/) — template for a software project repository, documentation, and work-tracking standard.

## Design principle

Keep this repository deliberately small. Add structure, metadata, validation, automation, or taxonomy only when concrete use demonstrates the need for it.
