# Responsive Web Layout Standard

## 1. Purpose and Scope

This standard defines baseline requirements for a usable, coherent, and reviewable web layout across the available space and presentation contexts within a declared scope.

The operative question is whether the delivered composition preserves material content, actions, relationships, and intentional presentation as available space, containing context, content dimensions, and applicable layout conditions change.

It applies to page and component composition, layout transitions, container relationships, content fitting, overflow, fixed and overlaid regions, media fitting, embedded contexts, themes or variants that materially affect layout, and other spatial adaptation within the declared scope.

It is independently adoptable. It does not depend on a web-suite umbrella, a design system, a responsive framework, or another companion standard. Media queries, container queries, Grid, Flexbox, intrinsic sizing, responsive-image markup, browser defaults, script-assisted layout, and other mechanisms can satisfy it when the delivered result and evidence meet the applicable requirements.

This standard does not prescribe device classes, breakpoint values, a grid, column count, “mobile-first” implementation, media-query syntax, container-query use, CSS framework, component library, stylesheet architecture, or responsive-image technique.

Accessibility conformance, content semantics, visual-foundation calibration, interaction behavior, performance, editorial authority, and legal duties remain subject to separately selected authorities where applicable. Adoption, exceptions to local organizational rules, publication, and approval remain subject to the adopting organization's existing authority. Publication of this source does not adopt or update any downstream artifact.

## 2. Interpretation and Definitions

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html)) when, and only when, they appear in this uppercase form. Lowercase uses have their ordinary meaning.

`WEB-LAY-NNN` identifies a local requirement synthesized by this template, independently of section numbers. Numbered local requirements are normative. Sections explicitly marked informative are not.

**Available space** means the usable spatial context in which an assessed page, region, component, embedded surface, or other layout participant is rendered. It can differ from the viewport because of containing regions, browser or host chrome, neighboring content, embedding, orientation, or other constraints.

**Layout relationship** means an intended spatial relationship such as sequence, grouping, adjacency, containment, alignment, priority, fitting, or separation that is material to understanding or using the declared scope.

**Layout transition** means a material change in composition caused by available space, containing context, content dimensions, presentation mode, or another declared layout condition.

**Material** means capable of changing visual or spatial understanding, access to content or an action, a reasonable decision or action by the declared audience, an assessment result, or a conformance claim.

The [Web Accessibility Standard](../web-accessibility/standard.md), [Web Content and Semantics Standard](../web-content-semantics/standard.md), and [Web Design Foundations Standard](../web-design-foundations/standard.md) retain their own identifiers, conditions, evidence, and results. Evidence MAY support more than one assessment when it actually addresses each obligation, but one result MUST NOT be represented as another.

## 3. Declared Layout Context and Adaptation

**WEB-LAY-001 — Declared assessment scope.** An assessment MUST identify the evaluated web experience, artifact or release revision, covered pages, views, components and relevant states, declared audience or audiences, represented languages and writing systems where they materially affect layout, material available-space and containing contexts, material orientations or presentation modes, material themes or variants, and material exclusions. Any difference between assessed coverage and a claimed scope MUST be explicit.

**WEB-LAY-002 — Reviewable layout relationships.** Material layout relationships MUST be reviewable sufficiently to evaluate their intended purpose and delivered behavior. Relationships MAY be expressed through rendered examples, design documentation, source conventions, component guidance, layout rules, assessment records, or another suitable mechanism. A particular grid, breakpoint model, token system, or documentation format is not required.

**WEB-LAY-003 — Usable adaptation across available space.** The delivered layout MUST preserve material usability and presentation relationships throughout the assessed available-space contexts. A change in composition MUST NOT by itself cause necessary content or actions to become unintentionally obscured, clipped, collided, unreachable, or materially ambiguous. This requirement addresses layout-level presentation and reachability; it does not establish WCAG reflow, zoom, or accessible-target conformance, which remain governed by the selected accessibility authority.

**WEB-LAY-004 — Intermediate transition integrity.** Assessment MUST include material transition ranges between selected endpoint contexts where the layout can change or fail. Passing a set of named device sizes, screenshots, or breakpoint endpoints MUST NOT establish conformance for unassessed intermediate conditions when a material failure can occur between them.

**WEB-LAY-005 — Container and embedding fitness.** A page region, component, widget, embedded surface, or other layout participant that is intended to operate in materially different containing contexts MUST preserve its applicable material relationships within those declared contexts. An assessment MUST NOT assume that viewport dimensions alone establish the available space of a nested or embedded participant.

## 4. Composition Continuity and Variable Content

**WEB-LAY-006 — Material content and action continuity.** Layout adaptation MUST preserve access to content and actions necessary to understand or use the declared scope. Material content or actions MAY be relocated, collapsed, progressively disclosed, or represented through another layout treatment, but they MUST NOT become unintentionally unavailable solely because the layout context changed. This requirement does not determine whether the content or action is semantically, interactively, or accessibly correct.

**WEB-LAY-007 — Variable-content fitness.** The delivered layout MUST accommodate material content variability that is present or reasonably represented within the declared scope, including applicable localization, user-supplied or generated values, ordinary text expansion or contraction, and materially different media dimensions. Testing only idealized placeholder content MUST NOT establish this result where real variability can change the layout outcome.

**WEB-LAY-008 — Layout-order integrity.** Visual or spatial reordering MUST NOT materially contradict the intended sequence, grouping, or relationship of presented content where that contradiction could change understanding or use. Different compositions MAY use different positions or arrangements when the material relationship remains clear. Semantic sequence, programmatic reading order, and keyboard navigation order remain subject to their separately selected authorities.

**WEB-LAY-009 — Region and boundary integrity.** Material regions and boundaries MUST remain spatially usable as composition changes. Layout adaptation MUST NOT unintentionally merge, overlap, separate, or detach a region from content or controls whose relationship is necessary to understand or use the declared scope.

**WEB-LAY-010 — Fixed, sticky, and overlaid content.** Fixed, sticky, floating, anchored, or overlaid regions MUST NOT unintentionally obscure or prevent access to material content or actions in the assessed layout contexts. Intentional temporary covering MAY be used when its purpose and recovery are governed by the applicable interaction and accessibility authorities; this requirement addresses the delivered spatial result, not the behavioral semantics of the overlay.

## 5. Overflow and Media Composition

**WEB-LAY-011 — Intentional overflow.** Material overflow MUST be intentional and usable within the declared context. Content MUST NOT be materially clipped, hidden, or made unreachable by accidental overflow or by a container that cannot accommodate or expose the necessary content. Deliberate scrolling, clipping, pagination, or other overflow handling MAY be used when appropriate to the content and context. Accessibility-specific reflow requirements and exceptions remain separately owned.

**WEB-LAY-012 — Media fitting and composition.** Images, video, canvas, diagrams, embeds, and other media whose dimensions participate materially in layout MUST fit the assessed composition without unintended distortion, collision, or loss of material content needed for their declared purpose. Cropping, art direction, scaling, scrolling, substitution, or alternate resources MAY be used when they preserve the applicable material purpose. Content-bearing meaning, accessible alternatives, interaction behavior, and performance remain outside this requirement.

**WEB-LAY-013 — Contextual layout variation.** A theme, brand expression, page type, orientation, embedding mode, density mode, or other declared variant MAY use a materially different composition, but the variant MUST satisfy the applicable layout obligations for its own declared context. Exact arrangement, breakpoint values, and mechanisms need not remain identical across variants.

## 6. Verification and Results

**WEB-LAY-014 — Reviewable evidence.** Evidence MUST be proportionate to the obligation and sufficient to trace a result to the assessed scope and revision, applicable requirement, relevant layout relationship or condition, method and presentation context, expected and observed result, reviewer or tool, date, limitations, and unresolved findings. Shared context MAY be referenced rather than repeated. A design file, breakpoint list, stylesheet, component catalog, screenshot set, automated measurement, or device emulator MUST NOT be treated as proof of a delivered conclusion it cannot establish.

Automated inspection MAY establish detectable dimensions, overflow, intersections, computed layout facts, or screenshot differences. Human review is required where deciding material relationships, usable composition, content priority, intentionality, or contextual fitness exceeds the method's capability. Representative-reader, specialist, or interactive review MAY support difficult conclusions. No vendor, device list, evidence format, storage system, or universal review ceremony is prescribed.

**WEB-LAY-015 — Distinct and truthful results.** Results MUST distinguish local-standard conformance, partial assessment, nonconformance, and undetermined obligations. An obligation is undetermined when it is applicable but the available evidence is missing, incomplete, conflicting, or otherwise insufficient; this differs from an obligation outside the declared scope. Local-standard conformance requires the declared scope to satisfy every applicable mandatory requirement of the identified adopted version. Partial coverage is not a reduced conformance level, and missing evidence MUST NOT be converted into a pass.

Any conformance claim MUST identify the adopted standard version, evaluated artifact revision, assessed scope, material exclusions, and conclusion. A responsive-layout result MUST NOT be represented as accessibility conformance, content-semantic conformance, design-foundation conformance, interaction quality, performance or compatibility certification, legal compliance, brand approval, or whole-suite conformance.

**WEB-LAY-016 — Change and reassessment.** A material change to layout rules, available-space assumptions, containers, embedded contexts, content dimensions or localization, visual ordering, overflow behavior, fixed or overlaid regions, media fitting, orientation or presentation mode, assessed scope, or relevant evidence MUST trigger reassessment of the obligations whose results may be affected before a current conclusion is asserted. Unaffected evidence MAY be reused when its applicability to the current revision and obligation is justified; reuse MUST NOT conceal stale or invalidated results.

## 7. Informative Verification Guidance

This section is informative.

Useful verification samples the delivered experience across material available-space ranges rather than only a few named devices. Breakpoints can be useful inspection points, but failures frequently occur immediately before or after a transition or within a nested container whose width differs from the viewport.

Content is itself a layout input. Representative localization, long labels, user-provided values, dynamic results, media aspect ratios, and other real content variation can expose failures that placeholder text or idealized design fixtures cannot. Testing should remain proportionate to the declared audience and actual variability.

Media queries, container queries, Grid, Flexbox, intrinsic sizing, responsive image selection, and script-assisted measurement can all support responsive outcomes. The existence or absence of any one technique does not determine conformance.

Intentional two-dimensional content can legitimately preserve width and use bounded scrolling rather than collapse into a linear layout. Whether an accessibility exception applies is determined by the selected accessibility authority, not by this Standard.

Fixed and sticky regions deserve testing at transition boundaries and in states where browser or host UI changes available space. An overlay can be behaviorally correct yet spatially obscure content, or spatially sound while failing interaction or accessibility requirements; those conclusions remain distinct.

## 8. Adaptation and Boundaries

An adopting organization MAY define representative width ranges, container classes, layout roles, grids, breakpoints, density modes, orientation policies, media treatments, evidence forms, or stronger requirements through its existing authority. Such adaptations MUST identify their scope and consequences and MUST NOT be represented as requirements of an unchanged upstream template.

Accessibility requirements for reflow, orientation, zoom, focus visibility, target exposure, and assistive-technology access remain with the adopter's selected accessibility authority. Intended content meaning and semantic sequence remain with the selected content-semantic authority. Typography, reading measure, visual hierarchy, and visual-role integrity remain with the selected design-foundation authority. Interaction behavior, performance, compatibility, CSS architecture, and organizational design approval remain outside this standard.

This standard does not require an adopter to use any published sibling standard. Cross-references clarify boundaries and do not create a whole-standard adoption dependency.

### Strength and ownership rationale — informative

Mandatory requirements protect access to material content and actions, usable composition through layout transitions, container fitness, variable-content resilience, spatial relationship integrity, intentional overflow, media fitting, and truthful claims. Permissions preserve legitimate variation in technology, brand, content, layout strategy, responsive techniques, and adopter-selected presentation contexts.
