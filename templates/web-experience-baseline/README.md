# Web Experience Baseline Template

Stable template ID: `web-experience-baseline`

Human-facing title:

> **Web Experience Baseline Standard**

## Purpose

Use this template when an organization needs one narrow composition standard for assessing and claiming a coherent web-experience Baseline across the six required core Web Standards.

The reusable template is [standard.md](standard.md).

The Baseline coordinates exact dependency versions, applicability, result preservation, complete mandatory coverage, and truthful suite-level claims. It does not duplicate the substantive requirements owned by the companion standards.

## Adoption

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. Organizational authority, existing protections, conflicts, destination, provenance, migration, protected effects, and later-source review are handled there, not replaced by this subject-specific guidance.

The questions below are informative review aids. They do not create a prescribed approval ceremony.

## Required companion set

The unchanged Baseline composes exactly:

- [Web Accessibility](../web-accessibility/README.md)
- [Web Content and Semantics](../web-content-semantics/README.md)
- [Web Design Foundations](../web-design-foundations/README.md)
- [Responsive Web Layout](../responsive-web-layout/README.md)
- [Web Interface and Interaction](../web-interface-interaction/README.md)
- [Web Quality and Verification](../web-quality-verification/README.md)

Each companion remains independently adoptable outside a Baseline assessment.

Web Styling Architecture is not a required Baseline dependency.

## Subject-specific adoption review

In addition to the universal review, determine:

1. Which exact Baseline revision and exact companion revisions are proposed for adoption?
2. Do existing organizational standards already compose some or all of these subjects, and what protections must survive?
3. What web experience, artifact/release, pages/views/processes, audiences, environments, and states will a Baseline claim cover?
4. Which material exclusions are necessary, and what claim limitations do they create?
5. How will each companion resolve applicability and not-applicable obligations under its own rules?
6. Which companion adaptations or external dependencies differ from the unchanged upstream package?
7. Do any selected companion versions or adaptations create a material conflict that must be resolved before a Baseline claim?
8. Which existing evidence can be reused, and is its relevance to the exact companion version and current artifact justified?
9. Where are assessment gaps, inaccessible environments, unresolved conflicts, stale results, or known failures?
10. How will individual-standard results remain visible rather than being collapsed into one aggregate score?
11. Are any organizational exceptions being proposed, and do they prevent an unchanged Baseline conformance claim?
12. Are optional standards such as Styling Architecture being adopted separately without accidentally becoming hidden Baseline dependencies?

## Likely adaptation choices

An adopter may need to define:

- exact dependency revisions;
- reporting format and terminology;
- assessment coordination and ownership;
- evidence references and shared context;
- local exception handling;
- stronger local requirements;
- optional standards reported alongside the Baseline;
- an adapted dependency set, if deliberately departing from the unchanged upstream Baseline.

These choices are not requirements of the unchanged upstream template. Record adaptations and provenance through the adopter's existing standards system.

## Important boundaries

This template:

- owns Baseline composition and suite-level claim integrity;
- requires the six core companions for unchanged Baseline conformance;
- preserves each companion's substantive requirements, evidence model, external dependencies, and result meanings;
- permits shared evidence and centralized orchestration without merging requirement ownership;
- does not prescribe implementation technology, evidence tooling, dashboards, badges, registries, or public claims;
- does not require Web Styling Architecture;
- does not define Enhanced conformance or domain profiles;
- does not establish legal, organizational approval, brand, security, deployment, or whole-company governance authority;
- does not make later upstream changes automatically authoritative downstream.

## Verification considerations

A Baseline review should verify composition before looking for a one-number summary.

Useful checks include:

- exact Baseline and companion version identities;
- exact assessed artifact revision and scope;
- presence of all six required companions;
- applicability basis for conditional or not-applicable obligations;
- unresolved, inaccessible, stale, or conflicting evidence;
- known mandatory failures;
- adaptations and exceptions;
- evidence reused across multiple requirements;
- preservation of Accessibility's external WCAG result distinctions;
- absence of aggregate-score substitution;
- correct separation of individual-standard and Baseline conclusions;
- reassessment after material implementation, scope, dependency, or evidence changes.

A spreadsheet, issue tracker, evidence database, test orchestrator, or generated report can help coordinate a Baseline assessment, but none is required and none independently establishes conformance.

## Related templates

The six core companions above are required only for a claim to the unchanged Web Experience Baseline. Each remains independently adoptable and governable on its own.

A future Web Styling Architecture template may be adopted separately if independently justified. It is not a Baseline dependency unless a deliberately adopted later Baseline revision changes the dependency model.

Enhanced conformance and domain profiles remain deferred pending evidence from separately authorized pilots.
