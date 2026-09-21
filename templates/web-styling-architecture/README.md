# Web Styling Architecture Template

Stable template ID: `web-styling-architecture`

Human-facing title:

> **Web Styling Architecture Standard**

## Purpose

Use this template when an organization needs a reusable standard for predictable style ownership, influence, override, containment, and change boundaries in web experiences.

The reusable template is [standard.md](standard.md).

This template is independently adoptable and is not a required dependency of the Web Experience Baseline. It does not require a CSS methodology, framework, preprocessor, component system, utility system, CSS Modules, Shadow DOM, cascade layers, or another companion template.

## Adoption

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. Organizational authority, existing protections, conflicts, destination, provenance, migration, protected effects, and later-source review are handled there, not replaced by this subject-specific guidance.

The questions below are informative review aids. They do not create a prescribed approval ceremony.

## Subject-specific adoption review

In addition to the universal review, determine:

1. Which authored, generated, global, local, third-party, framework, theme, reset, utility, and inline style sources materially affect the proposed scope?
2. Which style ownership boundaries already exist in code, components, teams, packages, or build output?
3. Which styles are intentionally global or shared, and which are expected to remain local?
4. Which override relationships are deliberate, and which currently depend on source order or specificity accidents?
5. Which third-party styles can influence adopter-owned content, and which adopter overrides are expected to reach third-party surfaces?
6. Which inherited values, custom properties, theme values, or ancestor styles intentionally cross component or ownership boundaries?
7. Which escape hatches such as `!important`, inline styles, runtime injection, or framework overrides are necessary and why?
8. Which build, bundling, code-splitting, runtime injection, or loading behavior can materially alter precedence?
9. Which independently maintained components or packages need change containment from one another?
10. Which current visual regressions or near misses reveal hidden style coupling?
11. Which companion standards own the visual, layout, interaction, accessibility, content, or quality consequences of those styles?
12. Which existing architecture rules must be preserved rather than replaced by a new methodology?

## Likely adaptation choices

An adopter may need to define:

- global/shared versus local style roles;
- component or package ownership boundaries;
- cascade-layer or precedence policy;
- selector/naming conventions;
- third-party style policy;
- override and exception rules;
- custom-property/theme propagation boundaries;
- linting or static-analysis rules;
- specificity or selector-complexity budgets;
- generated-style and runtime-injection conventions;
- evidence and regression-review practices.

These choices are not requirements of the unchanged upstream template. Record adaptations and provenance through the adopter's existing standards system.

## Important boundaries

This template:

- governs style ownership, influence, override, containment, and change boundaries;
- permits global styles, local styles, inline styles, `!important`, cascade layers, scoping, CSS Modules, BEM, utilities, preprocessors, CSS-in-JS, Shadow DOM, and other mechanisms when their architectural effects conform;
- does not prescribe a methodology, framework, naming system, linter, build tool, selector budget, or token model;
- does not establish visual-design, responsive-layout, accessibility, interaction, content-semantic, performance, Web Experience Baseline, legal, security, or brand conformance;
- is not a required Web Experience Baseline dependency;
- does not make upstream changes automatically authoritative downstream.

## Verification considerations

Review the shipped cascade and generated output, not only the source-file organization.

Useful coverage commonly includes:

- style-source inventory;
- global/shared style reach;
- local/component containment;
- competing selector precedence;
- loading and injection order;
- third-party style interactions;
- inherited and custom-property propagation;
- theme/reset/utility influence;
- exceptional `!important` or inline-style use;
- generated class/scoping output;
- cross-component regression scenarios;
- changes to shared style sources;
- source-versus-built-output differences.

Automated tools can inspect selectors, computed styles, origins, cascade order, generated CSS, dependencies, and regressions. Human review remains necessary for intended ownership, architectural role, permitted override relationships, and whether a cross-boundary effect is deliberate. Do not infer architecture solely from a passing screenshot or a linter score.

## Related templates

- [Web Design Foundations](../web-design-foundations/README.md) owns visual hierarchy and design-foundation outcomes.
- [Responsive Web Layout](../responsive-web-layout/README.md) owns responsive composition and spatial outcomes.
- [Web Interface and Interaction](../web-interface-interaction/README.md) owns task-state and interaction outcomes.
- [Web Accessibility](../web-accessibility/README.md) owns accessibility-specific outcomes.
- [Web Content and Semantics](../web-content-semantics/README.md) owns content meaning and semantic outcomes.
- [Web Quality and Verification](../web-quality-verification/README.md) owns performance, compatibility, resilience, and quality-evidence outcomes.
- [Web Experience Baseline](../web-experience-baseline/README.md) composes the six required core standards and does not require this template.

A later Baseline revision could only add Styling Architecture through deliberate revision and adoption; this template's publication does not alter the existing Baseline dependency set.
