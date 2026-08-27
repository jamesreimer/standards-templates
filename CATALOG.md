# Template Catalog

## Scope

This catalog describes the reusable templates that currently exist under `templates/` and the important boundaries between them.

Root-level repository guidance such as `README.md`, `ADOPTION.md`, and `NAMING.md` governs this template repository itself and is not part of the reusable template catalog.

This file is a current-state catalog, not a roadmap. Planned, deferred, or merely possible templates do not belong here until they exist.

## Templates

### `project-repository-model`

**Software Project Repository Responsibility Standard**

Defines where durable project artifacts, actionable work, dynamic planning state, exploratory reasoning, and repository responsibilities belong.

Important boundaries:

- determines when repository separation is justified;
- does not determine how a justified repository should be named;
- defers organizational adoption and ownership of reusable standards material to `standards-adoption-model`.

### `standards-adoption-model`

**Organizational Standards Adoption and Ownership Policy**

Defines how external or reusable normative source material becomes organization-owned authority through deliberate adoption while retaining provenance without continuing upstream authority.

Important boundaries:

- governs adoption, ownership, provenance, and independent lifecycle after adoption;
- does not determine repository topology;
- does not make upstream template changes automatically authoritative downstream.

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
standards-adoption-model
    governs deliberate organizational adoption of reusable normative material

project-repository-model
    governs project artifact/work-state responsibility and repository separation
        |
        +--> repository-naming
        |       governs the identity of a repository once justified
        |
        +--> filesystem-naming
                governs ordinary file/directory names within repositories and other versioned trees
```

Relationships communicate conceptual boundaries and useful dependencies. They do not make one template automatically authoritative over another; authority arises only through an adopting organization's own standards system.
