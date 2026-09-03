# Responsive Web Layout Template

Stable template ID: `responsive-web-layout`

Human-facing title:

> **Responsive Web Layout Standard**

## Purpose

Use this template when an organization needs a reusable standard for usable composition, layout adaptation, container fitness, overflow handling, and media fitting across changing available space and presentation contexts.

The reusable template is [standard.md](standard.md).

This template is independently adoptable. It does not require a Web Standards Suite umbrella, the Web Accessibility Standard, the Web Content and Semantics Standard, the Web Design Foundations Standard, a design system, a responsive framework, or another companion template.

## Adoption

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. Organizational authority, existing protections, conflicts, destination, provenance, migration, protected effects, and later-source review are handled there, not replaced by this subject-specific guidance.

The questions below are informative review aids. They do not create a prescribed approval ceremony.

## Subject-specific adoption review

In addition to the universal review, determine:

1. Which existing responsive-layout rules, grids, breakpoint systems, component libraries, design systems, browser defaults, or legacy conventions already govern the proposed scope?
2. Which pages, components, widgets, embedded surfaces, or third-party contexts operate in available space materially different from the viewport?
3. Which languages, writing systems, localization patterns, user-provided values, generated content, or content-length variations materially change layout dimensions?
4. Which intermediate widths or container ranges are likely to expose failures that endpoint screenshots or named device classes miss?
5. Which fixed, sticky, floating, anchored, or overlaid regions can reduce usable space or obscure material content?
6. Which tables, diagrams, maps, editors, timelines, or other intentionally two-dimensional content require bounded overflow rather than forced linearization?
7. Which images, video, diagrams, embeds, canvases, or other media require art direction, scaling, cropping, substitution, or preserved aspect relationships?
8. Which themes, density modes, white-label variants, orientation changes, or host environments materially alter composition?
9. Which accessibility authority governs reflow, orientation, zoom, focus visibility, target exposure, and other accessibility-specific layout consequences?
10. Which content-semantic and design-foundation authorities govern intended sequence, meaning, typography, hierarchy, reading measure, and visual-role integrity?
11. Which performance, compatibility, browser-support, or layout-shift requirements must remain outside this Standard?
12. Would adopting new breakpoints, grids, container-query rules, or responsive utilities preserve existing protections, or would they introduce an unnecessary implementation mandate?

## Likely adaptation choices

An adopter may need to define:

- representative available-space and container ranges;
- existing or revised breakpoints;
- layout roles, regions, and grid conventions;
- component embedding expectations;
- localization and variable-content test samples;
- bounded-overflow conventions for two-dimensional content;
- fixed, sticky, and overlay spatial constraints;
- media fitting and art-direction conventions;
- themes, density modes, and orientation policies;
- representative transition and intermediate-range checks;
- stronger numerical defaults or evidence requirements where justified;
- ownership and review routing for brand-specific composition decisions.

These choices are not requirements of the unchanged upstream template. Record adaptations and provenance through the adopter's existing standards system.

## Important boundaries

This template:

- governs delivered layout outcomes, not whether a responsive framework or layout system exists;
- treats available space and containing context as more fundamental than named device categories;
- permits media queries, container queries, Grid, Flexbox, intrinsic sizing, responsive-image markup, browser defaults, scripts, or other mechanisms;
- does not prescribe breakpoints, devices, a grid, column count, “mobile-first” implementation, CSS architecture, or framework;
- does not establish WCAG or legal accessibility conformance;
- does not establish content-semantic, design-foundation, interaction, performance, compatibility, brand-approval, or whole-suite conformance;
- does not make upstream changes automatically authoritative downstream.

## Verification considerations

Plan representative transition and content testing rather than relying on breakpoint documentation or endpoint screenshots alone.

Useful coverage commonly includes:

- narrow, intermediate, and wide available-space conditions selected from actual layout behavior;
- nested containers and embedded contexts whose available space differs from the viewport;
- represented languages and materially longer or shorter content;
- user-supplied, generated, or dynamic values;
- page regions and components before, during, and after layout transitions;
- fixed, sticky, floating, anchored, and overlaid regions;
- intentional and accidental overflow;
- tables and other two-dimensional content;
- images, video, diagrams, embeds, and varied media dimensions;
- themes, density modes, orientation changes, and other material variants;
- differences between documented breakpoints and shipped implementation.

Automated tools can inventory dimensions, detect intersections or overflow, compare screenshots, and record computed layout facts. Human review remains necessary for material relationships, content priority, intentionality, and contextual usability. Do not claim devices, widths, containers, languages, states, or content variants that were not actually evaluated.

## Related templates

- [Web Accessibility](../web-accessibility/README.md) owns its selected accessibility target and accessibility-specific reflow, orientation, zoom, focus, and related evidence and claims.
- [Web Content and Semantics](../web-content-semantics/README.md) owns intended content meaning, semantic sequence, and content-bearing-media meaning.
- [Web Design Foundations](../web-design-foundations/README.md) owns typography, reading measure, visual hierarchy, spacing-role integrity, and functional visual roles.
- A future Interface and Interaction template may govern state behavior, feedback, recovery, and task transitions.
- A future Quality and Verification template may govern performance, compatibility, resilience, and shared evidence-system requirements without taking over this template's specific layout findings.
- A future Styling Architecture template may govern selectors, class naming, cascade layers, style ownership, and change containment if independently justified.

Future references describe boundaries only. They neither require those templates nor claim that unpublished companions already exist.
