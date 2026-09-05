# Template Catalog

## Scope

This catalog describes the reusable templates that currently exist under `templates/` and the important boundaries between them.

Templates are grouped by related subject area to improve discovery. These groupings do not create authority, adoption dependencies, or shared lifecycle. Any actual dependency is established only by the applicable template itself.

Root-level repository guidance such as `README.md`, `ADOPTION.md`, `NAMING.md`, and `MAINTAINING.md` governs this template repository itself and is not part of the reusable template catalog.

This file is a current-state catalog, not a roadmap. Planned, deferred, or merely possible templates do not belong here until they exist.

## Templates

Repository validation machine-reads this single section. Its subject and suite hierarchy structures discovery, and its backticked stable-ID headings identify template entries. Grouping does not itself create authority, adoption dependency, or shared lifecycle.

### Standards Governance and Authoring

These related subjects are grouped for discovery; they do not form a suite or adoption bundle.

#### `standards-authoring`

**Standards and Policy Authoring Standard**

Defines how normative standards and policies are written, scoped, calibrated, distinguished from informative material, and revised when concrete evidence shows a rule is miscalibrated.

Important boundaries:

- governs authoring discipline and normative strength;
- does not determine who has authority to adopt a standard or policy;
- does not define a complete controlled-document lifecycle or a separate approval workflow.

#### `standards-adoption-model`

**Organizational Standards Adoption and Ownership Policy**

Defines how external or reusable normative source material becomes organizational authority through deliberate adoption while retaining provenance without continuing upstream authority.

Important boundaries:

- governs adoption, canonical governance, provenance, and independent lifecycle after adoption;
- does not determine repository topology;
- does not make upstream template changes automatically authoritative downstream.

### Repository Architecture and Naming

These templates are independently adoptable. Their order below is a discovery or reading aid, not a required adoption sequence.

#### `project-repository-model`

**Project Repository Responsibility Standard**

Defines where durable project artifacts, actionable work, dynamic planning state, exploratory reasoning, and repository responsibilities belong.

Important boundaries:

- determines when repository separation is justified;
- does not determine how a justified repository should be named;
- defers organizational adoption and canonical governance of reusable standards material to `standards-adoption-model`.

#### `repository-naming`

**Repository Naming Standard**

Defines rules for durable, portable, and appropriately scoped repository identities across types of work.

Important boundaries:

- governs what to name a repository once its responsibility exists;
- does not determine whether an additional repository is justified;
- does not govern file or directory naming.

#### `filesystem-naming`

**File and Directory Naming Standard**

Defines rules for portable, readable, and durable human-managed file and directory names while preserving legitimate tool, ecosystem, generated, and external conventions.

Important boundaries:

- governs files, directories, and path components;
- does not govern repository identities;
- yields to stronger legitimate technical or external naming requirements.

### Web Standards Suite

This catalog describes the suite relationship already established by the templates; placement here does not create authority or dependency.

#### Web Experience Baseline

##### `web-experience-baseline`

**Web Experience Baseline Standard**

Defines how the six required core Web Standards compose into a truthful Baseline assessment and conformance conclusion while preserving each companion's ownership and result model.

Important boundaries:

- requires exact versions of the six core companions only for unchanged Baseline conformance; each companion remains independently adoptable;
- governs composition, complete mandatory coverage, evidence reuse, conflict handling, and Baseline claim integrity without duplicating companion requirements;
- does not require Web Styling Architecture, define Enhanced conformance or domain profiles, or automatically incorporate later companion revisions;
- does not establish organizational authority, release approval, legal certification, public claims, tooling, reporting infrastructure, or automatic downstream updates.

#### Required Core Companions

The six core companions are required only for conformance to the unchanged Web Experience Baseline. Each core companion remains independently adoptable.

##### `web-accessibility`

**Web Accessibility Standard**

Defines a declared web-accessibility target, incorporating dated WCAG 2.2 Level AA requirements by default, with local assessment, evidence, and truthful-claim discipline.

Important boundaries:

- independently adoptable without a web-suite umbrella or other companion;
- retains accessibility-specific verification without owning broader design, layout, interaction, content, or quality conventions;
- distinguishes external WCAG conformance from local-standard conformance and incomplete assessment;
- does not provide legal certification, complete inclusive-design coverage, organizational approval authority, or automatic downstream updates.

##### `web-content-semantics`

**Web Content and Semantics Standard**

Defines requirements for preserving intended content meaning, semantic structure, audience understanding, and representation integrity, with reviewable evidence and truthful content-semantic claims.

Important boundaries:

- independently adoptable without a web-suite umbrella or other companion;
- covers media as content without owning accessibility alternatives, responsive presentation, or control behavior;
- distinguishes content-semantic results from accessibility, platform-specification, legal, editorial, and whole-suite conclusions;
- does not prescribe brand voice, house style, a universal reading level, editorial workflows, or automatic downstream updates.

##### `web-design-foundations`

**Web Design Foundations Standard**

Defines requirements for legible typography, coherent visual hierarchy, spacing relationships, and functional visual roles, with reviewable evidence and truthful design-foundation claims.

Important boundaries:

- independently adoptable without a web-suite umbrella, design system, or other companion;
- governs delivered visual outcomes without prescribing a brand, font, scale, grid, palette, token format, tool, or framework;
- does not own accessibility, content semantics, responsive layout, interaction behavior, motion, CSS architecture, or design-system governance;
- does not establish legal, brand-approval, or whole-suite conformance or automatic downstream updates.

##### `responsive-web-layout`

**Responsive Web Layout Standard**

Defines requirements for preserving usable access, material layout relationships, and intentional presentation across available space, containing contexts, and content variability, with reviewable evidence and truthful responsive-layout claims.

Important boundaries:

- independently adoptable without a web-suite umbrella, design system, responsive framework, or other companion;
- covers layout transitions, embedding, variable content, overflow, overlays, and media fitting without prescribing devices, breakpoints, grids, or implementation mechanisms;
- does not own accessibility, content semantics, visual-foundation calibration, interaction behavior, performance, or CSS architecture;
- does not establish legal, compatibility, brand-approval, or whole-suite conformance or automatic downstream updates.

##### `web-interface-interaction`

**Web Interface and Interaction Standard**

Defines requirements for reliable action outcomes, understandable interaction states, task continuity, recovery, and truthful interface-and-interaction claims.

Important boundaries:

- independently adoptable without a web-suite umbrella, component library, framework, accessibility pattern library, or other companion;
- governs delivered interaction behavior without prescribing component APIs, focus algorithms, keyboard bindings, confirmation dialogs, undo systems, or state-management architecture;
- does not own accessibility, content semantics and wording, visual-foundation calibration, responsive layout, performance, security policy, transaction authority, or backend correctness;
- does not establish legal, brand-approval, or whole-suite conformance or automatic downstream updates.

##### `web-quality-verification`

**Web Quality and Verification Standard**

Defines requirements for credible performance, compatibility, resilience, and verification claims tied to declared profiles, environments, methods, revisions, and limitations.

Important boundaries:

- independently adoptable without a web-suite umbrella, analytics or monitoring vendor, test framework, browser-automation system, or other companion;
- distinguishes field, lab, synthetic, and directly observed evidence while leaving target and mechanism selection to the adopter;
- does not prescribe universal performance thresholds, browser/device matrices, tooling, service workers, caching, fallbacks, or offline support;
- does not own sibling substantive conformance, security, privacy, infrastructure operations, deployment, legal conclusions, or automatic downstream updates.

#### Optional Companion

Web Styling Architecture remains optional and independently adoptable.

##### `web-styling-architecture`

**Web Styling Architecture Standard**

Defines requirements for predictable style ownership, influence, overrides, containment, and change boundaries, with reviewable evidence and truthful styling-architecture claims.

Important boundaries:

- independently adoptable without a web-suite umbrella, CSS methodology, framework, naming system, scoping technology, linter, build tool, or other companion;
- governs intentional and reviewable relationships between style sources and their declared targets without prescribing `@layer`, `@scope`, Shadow DOM, CSS Modules, BEM, utility classes, Sass modules, CSS-in-JS, inline styles, `!important`, IDs, global selectors, or another styling mechanism;
- does not own visual correctness, responsive layout, interface behavior, accessibility, content semantics, performance, compatibility, resilience, JavaScript state, general module architecture, backend systems, infrastructure, or deployment;
- remains optional and outside the unchanged Web Experience Baseline dependency set, and does not establish legal, whole-suite, or automatic downstream conclusions.

## Relationship Summary

**Standards Governance and Authoring**

`standards-authoring` governs how reusable normative standards and policies are authored and calibrated. `standards-adoption-model` governs how reusable normative material becomes organizational authority and then follows an independent lifecycle. Their conceptual relationship does not require adopting them together or in a particular order.

**Repository Architecture and Naming**

- `project-repository-model` governs project repository responsibility, project-state boundaries, and when repository separation is justified.
- `repository-naming` governs the identity of a repository once its responsibility exists.
- `filesystem-naming` governs file, directory, and path-component naming.

These responsibilities are distinct. Their presentation order is a discovery aid, not a mandatory sequence or dependency chain.

**Web Standards Suite**

- Web Experience Baseline requires results from the six core companions for conformance to the unchanged Baseline.
- Each core companion remains independently adoptable outside a Baseline assessment.
- Web Styling Architecture is optional, independently adoptable, and outside the unchanged Baseline dependency set.

These statements summarize relationships established by the templates themselves. Catalog placement does not make one template authoritative over another; authority arises only through an adopting organization's own standards system.
