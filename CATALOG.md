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

**Project Repository Responsibility Standard**

Defines where durable project artifacts, actionable work, dynamic planning state, exploratory reasoning, and repository responsibilities belong.

Important boundaries:

- determines when repository separation is justified;
- does not determine how a justified repository should be named;
- defers organizational adoption and canonical governance of reusable standards material to `standards-adoption-model`.

### `repository-naming`

**Repository Naming Standard**

Defines rules for durable, portable, and appropriately scoped repository identities across types of work.

Important boundaries:

- governs what to name a repository once its responsibility exists;
- does not determine whether an additional repository is justified;
- does not govern file or directory naming.

### `filesystem-naming`

**File and Directory Naming Standard**

Defines rules for portable, readable, and durable human-managed file and directory names while preserving legitimate tool, ecosystem, generated, and external conventions.

Important boundaries:

- governs files, directories, and path components;
- does not govern repository identities;
- yields to stronger legitimate technical or external naming requirements.

### `web-accessibility`

**Web Accessibility Standard**

Defines a declared web-accessibility target, incorporating dated WCAG 2.2 Level AA requirements by default, with local assessment, evidence, and truthful-claim discipline.

Important boundaries:

- independently adoptable without a web-suite umbrella or other companion;
- retains accessibility-specific verification without owning broader design, layout, interaction, content, or quality conventions;
- distinguishes external WCAG conformance from local-standard conformance and incomplete assessment;
- does not provide legal certification, complete inclusive-design coverage, organizational approval authority, or automatic downstream updates.

### `web-content-semantics`

**Web Content and Semantics Standard**

Defines requirements for preserving intended content meaning, semantic structure, audience understanding, and representation integrity, with reviewable evidence and truthful content-semantic claims.

Important boundaries:

- independently adoptable without a web-suite umbrella or other companion;
- covers media as content without owning accessibility alternatives, responsive presentation, or control behavior;
- distinguishes content-semantic results from accessibility, platform-specification, legal, editorial, and whole-suite conclusions;
- does not prescribe brand voice, house style, a universal reading level, editorial workflows, or automatic downstream updates.

## Relationship Summary

```text
standards-authoring
    governs how reusable normative standards and policies are authored and calibrated

standards-adoption-model
    governs deliberate organizational adoption of reusable normative material

project-repository-model
    governs project repository responsibility, project-state boundaries,
    and when additional repositories are justified

repository-naming
    governs the identity of a repository once its existence is justified

filesystem-naming
    governs file, directory, and path-component naming
```

Relationships communicate conceptual boundaries and useful dependencies. They do not make one template automatically authoritative over another; authority arises only through an adopting organization's own standards system.
