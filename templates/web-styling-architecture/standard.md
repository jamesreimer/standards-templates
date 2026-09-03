# Web Styling Architecture Standard

## 1. Purpose and Scope

This standard defines baseline requirements for predictable style ownership, influence, overrides, containment, and change boundaries within a declared web experience.

The operative question is whether material styling effects occur through intentional and reviewable relationships between style sources and their declared targets, rather than through accidental global reach, hidden precedence, or undocumented coupling.

It applies to authored and generated stylesheets, inline styles, component-local styles, global/shared styles, themes, resets, utility styles, third-party styles, framework styles, shadow or scoped styles, inherited/cascading values, and other styling sources within the declared scope.

It is independently adoptable and is not a required dependency of the Web Experience Baseline. It does not depend on a framework, CSS methodology, preprocessor, component system, cascade-layer scheme, scoping technology, or another companion standard.

This standard does not prescribe BEM, utility classes, CSS Modules, CSS-in-JS, Shadow DOM, `@scope`, `@layer`, Sass, selector conventions, a token system, or a ban on `!important`, inline styles, IDs, global selectors, or any other styling mechanism. Such mechanisms are evaluated only by whether their delivered architectural effects satisfy the applicable requirements.

Visual-design correctness, responsive-layout correctness, accessibility conformance, content semantics, interaction correctness, performance/compatibility outcomes, application architecture beyond styling, security, backend behavior, infrastructure, and deployment remain separately owned.

Adoption, exceptions to local organizational rules, publication, and approval remain subject to the adopting organization's existing authority. Publication of this source does not adopt or update any downstream artifact.

## 2. Interpretation and Definitions

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html)) when, and only when, they appear in this uppercase form. Lowercase uses have their ordinary meaning.

`WEB-STY-NNN` identifies a local requirement synthesized by this template, independently of section numbers. Numbered local requirements are normative. Sections explicitly marked informative are not.

**Style source** means a stylesheet, style block, inline declaration, generated style output, imported style package, component-local style definition, theme, reset, utility set, third-party style resource, or other mechanism capable of contributing author-controlled presentation within the assessed scope.

**Style ownership boundary** means a declared architectural boundary that identifies which styling concern or source is permitted to influence a target scope and under what override relationship.

**Influence boundary** means the elements, components, states, descendants, properties, layers, themes, or other declared target area a style source is intended to affect. It describes architectural reach, not a required implementation mechanism.

**Override contract** means a reviewable relationship under which one style source is intentionally permitted to take precedence over another for a declared scope or condition.

**Material** means capable of changing a style ownership relationship, the intended influence of a style source, a protected visual or functional outcome, an assessment result, or a conformance claim.

The [Web Design Foundations Standard](../web-design-foundations/standard.md), [Responsive Web Layout Standard](../responsive-web-layout/standard.md), [Web Interface and Interaction Standard](../web-interface-interaction/standard.md), [Web Accessibility Standard](../web-accessibility/standard.md), [Web Content and Semantics Standard](../web-content-semantics/standard.md), and [Web Quality and Verification Standard](../web-quality-verification/standard.md) retain their own substantive requirements and results. Evidence MAY support several assessments when it actually addresses each obligation, but one result MUST NOT be represented as another.

## 3. Declared Styling Architecture

**WEB-STY-001 — Declared styling scope.** An assessment MUST identify the evaluated web experience, artifact or release revision, covered pages/views/components, material style sources, material styling states or themes, material third-party style inputs, and material exclusions. Any difference between assessed coverage and a claimed scope MUST be explicit.

**WEB-STY-002 — Reviewable style-source inventory.** Material style sources MUST be identifiable well enough to determine their origin, loading or application context, intended role, and relevant relationship to other style sources. A build artifact MAY combine or transform sources, but the transformation MUST NOT make material style ownership or precedence impossible to review.

**WEB-STY-003 — Declared style ownership boundaries.** Material styling concerns MUST have reviewable ownership boundaries sufficient to determine which source or concern may influence a target scope and which cross-boundary relationships are permitted. The boundary MAY be represented through code structure, naming, scoping, layering, module relationships, documentation, generated metadata, tests, or another suitable mechanism.

**WEB-STY-004 — Intended influence boundaries.** A material style source MUST NOT influence elements, components, states, or other target scope outside its declared architectural role solely because of accidental selector reach, inheritance, cascade interaction, source order, or build composition. Broad or global influence is permitted when that broad influence is itself the declared role.

**WEB-STY-005 — Explicit override contracts.** A material override across style ownership boundaries MUST correspond to a reviewable override contract. The contract MUST establish the intended target and circumstance sufficiently to distinguish a deliberate override from accidental precedence. No particular override syntax or hierarchy is required.

**WEB-STY-006 — Deterministic precedence.** Material precedence among competing style sources MUST be reviewable and reproducible for the assessed revision. A required result MUST NOT depend solely on incidental file discovery, unstable bundling order, undocumented injection order, or accidental specificity escalation whose precedence cannot be justified from the declared architecture.

## 4. Influence and Containment Boundaries

**WEB-STY-007 — Global and shared style boundaries.** A style source whose declared role is global, shared, foundational, reset-like, theme-wide, or utility-wide MUST keep its material influence within that declared role and MUST NOT silently assume ownership of independently governed local concerns. Local exceptions or overrides MAY exist through explicit contracts.

**WEB-STY-008 — Local and component containment.** A style source declared as local, component-scoped, feature-scoped, or otherwise bounded MUST NOT materially influence unrelated scope outside that boundary unless an explicit cross-boundary contract permits the influence. This requirement does not prescribe native scoping, generated class names, naming conventions, Shadow DOM, or any other containment mechanism.

**WEB-STY-009 — Third-party and external style containment.** Third-party, framework, vendor, embedded, or externally supplied styles that materially participate in the declared scope MUST have reviewable influence and override boundaries relative to adopter-owned styles. Their presence MUST NOT be treated as self-authorizing unrestricted precedence, and adopter overrides MUST likewise respect the declared relationship.

**WEB-STY-010 — Intentional inherited and cascading influence.** Material inherited, cascading, custom-value, theme, or ancestor-derived styling that crosses an ownership boundary MUST be intentional within the declared architecture. A shared inherited value MAY affect many descendants when that propagation is part of the contract; accidental cross-boundary propagation MUST NOT be represented as contained architecture.

**WEB-STY-011 — Reviewable escape hatches.** An exceptional precedence mechanism or boundary crossing, including `!important`, inline style, unusually strong specificity, framework escape hatch, runtime injection, or another mechanism, MAY be used when appropriate. When material to an architectural boundary, its purpose and precedence effect MUST be reviewable and MUST NOT serve as an undocumented substitute for an override contract.

**WEB-STY-012 — Change containment.** A material change within one declared style ownership boundary MUST NOT produce unintended styling effects in unrelated ownership boundaries solely because of hidden selector reach, undeclared inheritance, accidental precedence, or other undocumented styling coupling. A deliberately shared source MAY create coordinated change across its declared consumers.

## 5. Verification and Results

**WEB-STY-013 — Reviewable architecture evidence.** Evidence MUST be proportionate to the obligation and sufficient to trace a result to the assessed scope and revision, applicable requirement, relevant style source and boundary, method/environment, expected and observed influence or precedence, reviewer or tool, date, limitations, and unresolved findings. Shared context MAY be referenced rather than repeated. Source inspection, computed-style traces, cascade inspection, screenshots, generated CSS, lint output, dependency graphs, or regression tests MUST NOT be treated as proof of conclusions they cannot establish.

Automated tools MAY establish detectable selectors, style origins, precedence, generated output, computed values, dependency edges, or regression differences. Human review is required where deciding intended ownership, architectural role, permitted influence, or whether coupling is intentional exceeds the method's capability. No linter, bundler, framework, evidence format, naming convention, or review ceremony is prescribed.

**WEB-STY-014 — Distinct and truthful results.** Results MUST distinguish local-standard conformance, partial assessment, nonconformance, and undetermined obligations. An obligation is undetermined when applicable evidence is missing, inaccessible, incomplete, conflicting, stale, or otherwise insufficient. Local-standard conformance requires the declared scope to satisfy every applicable mandatory requirement of the identified adopted version. Partial coverage is not a reduced conformance level, and missing evidence MUST NOT be converted into a pass.

Any conformance claim MUST identify the adopted standard version, evaluated artifact revision, assessed scope, material exclusions, and conclusion. A styling-architecture result MUST NOT be represented as design-foundation conformance, responsive-layout conformance, accessibility conformance, interaction conformance, content-semantic conformance, quality/performance certification, Web Experience Baseline conformance, security approval, legal compliance, or brand approval.

**WEB-STY-015 — Change and reassessment.** A material change to style sources, style ownership, influence boundaries, override contracts, precedence, build or loading order, scoping/encapsulation, third-party styles, inherited/cascading relationships, assessed scope, or relevant evidence MUST trigger reassessment of the obligations whose results may be affected before a current conclusion is asserted. Unaffected evidence MAY be reused when its applicability to the current revision and obligation is justified; reuse MUST NOT conceal stale or invalidated results.

## 6. Informative Verification Guidance

This section is informative.

The cascade itself is not a defect. Global styles, inheritance, source order, specificity, inline styles, and `!important` are all legitimate parts of CSS and related styling systems. The architectural question is whether their material effects match an intentional ownership and override model.

Native cascade layers can make concern precedence explicit. `@scope` or Shadow DOM can bound selector reach. CSS Modules can localize names. BEM can encode ownership through naming. Utility-first systems can reduce shared custom-selector reach. Sass modules can namespace authoring dependencies. These techniques solve overlapping problems through different mechanisms; none is required by this standard.

A current visual result can pass Design and Layout while still failing this Standard. For example, two unrelated components may coincidentally share the same color today even though one component is accidentally controlling the other's style. Styling Architecture can identify the hidden coupling before a later change turns it into a visible regression.

Conversely, a broad global style is not automatically a failure. A reset, theme, typography foundation, or utility set can intentionally influence many components when that broad role is declared and the local override relationship remains reviewable.

## 7. Adaptation and Boundaries

An adopting organization MAY define style layers, namespaces, naming conventions, ownership maps, component boundaries, third-party override policies, exception processes, lint rules, specificity budgets, or stronger containment requirements through its existing authority. Such adaptations MUST identify their scope and consequences and MUST NOT be represented as requirements of an unchanged upstream template.

This standard does not choose brand values, visual outcomes, accessibility targets, responsive behavior, task-state behavior, application state architecture, performance targets, build systems, deployment patterns, or backend responsibilities. Those remain separately governed where applicable.

This standard is not a required dependency of the unchanged Web Experience Baseline. Cross-references clarify boundaries only.

### Strength and ownership rationale — informative

Mandatory requirements protect predictable style influence, deliberate overrides, containment, and change isolation. Permissions preserve legitimate variation in CSS mechanisms, frameworks, preprocessors, naming conventions, utility systems, runtime styling, and architecture. The Standard deliberately avoids blanket bans because the same mechanism can be architecturally safe or unsafe depending on its declared ownership and influence role.
