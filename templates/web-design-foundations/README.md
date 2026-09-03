# Web Design Foundations Template

Stable template ID: `web-design-foundations`

Human-facing title:

> **Web Design Foundations Standard**

## Purpose

Use this template when an organization needs a reusable standard for legible typography, coherent visual hierarchy, spacing relationships, functional visual roles, and evidence-backed design-foundation claims across web experiences.

The reusable template is [standard.md](standard.md).

This template is independently adoptable. It does not require a Web Standards Suite umbrella, the Web Accessibility Standard, the Web Content and Semantics Standard, a design system, or another companion template.

## Adoption

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. Organizational authority, existing protections, conflicts, destination, provenance, migration, protected effects, and later-source review are handled there, not replaced by this subject-specific guidance.

The questions below are informative review aids. They do not create a prescribed approval ceremony.

## Subject-specific adoption review

In addition to the universal review, determine:

1. Which existing brand standards, design systems, visual identities, component libraries, user-agent defaults, or legacy conventions already govern the proposed scope?
2. Which of those artifacts are canonical, and could adoption create competing authority over the same visual roles?
3. Which languages, writing systems, writing directions and orientations, typefaces, weights, variable-font settings, and fallback conditions occur in the real experience?
4. Which content types require extended reading, compact operational density, tabular comparison, code presentation, display typography, or other materially different composition?
5. Which themes, embedded contexts, brands, white-label variants, or user-selectable modes change visual values while needing to preserve role meaning?
6. Which third-party widgets, hosted content, document viewers, or generated surfaces are within the adopter's control and assessment scope?
7. Which accessibility authority governs contrast, color dependence, resizing, reflow, text-spacing tolerance, focus appearance, and other accessibility-specific outcomes?
8. Which content-semantic authority governs intended meaning, semantic hierarchy, language metadata, and content-bearing media?
9. Which brand approvals, legal constraints, font licenses, performance budgets, and publication controls must remain outside this Standard?
10. Would adopting a formal token, type, color, or spacing system preserve current protections, or would it introduce an unnecessary implementation mandate?

## Likely adaptation choices

An adopter may need to define:

- canonical fonts and fallback stacks;
- locally tested typographic roles and scales;
- reading-measure guidance for represented languages and content;
- spacing roles or scales;
- functional and decorative color roles;
- themes, density modes, and brand variants;
- approved icon, imagery, border, surface, or elevation conventions;
- representative pages, states, languages, and fallback conditions for assessment;
- stronger numerical defaults or evidence requirements where justified;
- ownership and review routing for brand-specific decisions.

These choices are not requirements of the unchanged upstream template. Record adaptations and provenance through the adopter's existing standards system.

## Important boundaries

This template:

- governs the delivered visual foundation, not whether a design-system artifact exists;
- permits browser defaults, custom styles, tokens, components, or other mechanisms;
- does not prescribe a brand, aesthetic, font, type scale, spacing scale, grid, palette, token format, tool, or framework;
- does not govern CSS class names, selectors, cascade layers, or stylesheet architecture;
- does not establish WCAG or legal accessibility conformance;
- does not establish content-semantic, responsive-layout, interaction, performance, brand-approval, or whole-suite conformance;
- does not make upstream changes automatically authoritative downstream.

Motion is intentionally excluded from this version. Its durable feedback, state, navigation, cognitive-load, and reduced-motion consequences are better evaluated through interaction and accessibility authorities unless later evidence demonstrates a distinct foundations-owned obligation.

## Verification considerations

Plan a representative review rather than relying on a design-file or token audit alone.

Useful coverage commonly includes:

- delivered typography and computed presentation facts;
- actual font loading and fallback behavior;
- represented languages, writing systems, directions, and orientations;
- extended reading, short interface text, headings, tables, and dense views;
- repeated roles across pages and components;
- themes, variants, and embedded contexts;
- spatial grouping and visual priority;
- decorative treatments that could obscure necessary content;
- differences between documented roles and shipped implementation.

Automated tools can inventory values, calculate measurements, compare screenshots, and identify detectable variation. Human review remains necessary for hierarchy, legibility, grouping, role meaning, and contextual fitness. Do not claim tests, readers, environments, or content variants that were not actually evaluated.

## Related templates

- [Web Accessibility](../web-accessibility/README.md) owns its selected accessibility target and accessibility-specific evidence and claims.
- [Web Content and Semantics](../web-content-semantics/README.md) owns intended content meaning, semantic correspondence, and content-semantic claims.
- A future Responsive Layout template may govern layout transitions, containers, reflow beyond incorporated accessibility requirements, and responsive media fitting.
- A future Interface and Interaction template may govern state behavior, feedback, task transitions, and purposeful motion.
- A future Styling Architecture template may govern selectors, class naming, cascade layers, style ownership, and change containment if independently justified.
- A future Quality and Verification template may govern performance, compatibility, resilience, and shared evidence-system requirements without taking over this template's specific visual findings.

Future references describe boundaries only. They neither require those templates nor claim that unpublished companions already exist.
