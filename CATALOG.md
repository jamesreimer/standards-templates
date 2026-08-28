# Template Catalog

## Scope

This catalog describes the reusable templates that currently exist under `templates/` and the important boundaries between them.

Root-level repository guidance such as `README.md`, `ADOPTION.md`, `NAMING.md`, and `MAINTAINING.md` governs this template repository itself and is not part of the reusable template catalog.

This file is a current-state catalog, not a roadmap. Planned, deferred, or merely possible templates do not belong here until they exist.

## Templates

### `standards-authoring`

**Standards and Policy Authoring Standard**

Defines how normative standards and policies are written, scoped, calibrated, distinguished from informative material, and revised when concrete evidence shows a rule is miscalibrated.

Important boundaries:

- governs authoring discipline and normative strength;
- does not determine who has authority to adopt a standard or policy;
- does not define a complete controlled-document lifecycle or a separate approval workflow.

### `standards-adoption-model`

**Organizational Standards Adoption and Ownership Policy**

Defines how external or reusable normative source material becomes organizational authority through deliberate adoption while retaining provenance without continuing upstream authority.

Important boundaries:

- governs adoption, canonical governance, provenance, and independent lifecycle after adoption;
- does not determine repository topology;
- does not make upstream template changes automatically authoritative downstream.

### `project-repository-model`

**Software Project Repository Responsibility Standard**

Defines where durable project artifacts, actionable work, dynamic planning state, exploratory reasoning, and repository responsibilities belong.

Important boundaries:

- determines when repository separation is justified;
- does not determine how a justified repository should be named;
- defers organizational adoption and canonical governance of reusable standards material to `standards-adoption-model`.

### `repository-naming`

**Repository Naming Standard**

Defines domain-neutral rules for durable, portable, and appropriately scoped repository identities.

Important boundaries:

- governs what to name a repository once its responsibility exists;
- does not determine whether an additional repository is justified;
- does not govern file or directory naming.

### `filesystem-naming`

**File and Directory Naming Standard**

Defines domain-neutral rules for portable, readable, and durable human-managed file and directory names while preserving legitimate tool, ecosystem, generated, and external conventions.

Important boundaries:

- governs files, directories, and path components;
- does not govern repository identities;
- yields to stronger legitimate technical or external naming requirements.

## Relationship Summary

```text
standards-authoring
    authoring discipline applied to the reusable normative templates
    and available for adoption into an organization's own standards system

standards-adoption-model
    governs deliberate organizational adoption of reusable normative material

project-repository-model (software-specific)
    governs software-project artifact/work-state responsibility and repository separation

repository-naming (domain-neutral)
    governs the identity of a repository once its existence is justified
    boundary: software projects may use project-repository-model to decide whether
              a separate repository is justified

filesystem-naming (domain-neutral)
    governs ordinary file/directory names within repositories and other versioned trees
```

Relationships communicate conceptual boundaries and useful dependencies. They do not make one template automatically authoritative over another; authority arises only through an adopting organization's own standards system.
