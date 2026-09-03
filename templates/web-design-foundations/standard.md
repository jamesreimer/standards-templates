# Web Design Foundations Standard

## 1. Purpose and Scope

This standard defines baseline requirements for a legible, coherent, and reviewable visual foundation for a declared web experience.

The operative question is whether the delivered presentation uses typography, spacing, color, and other visual treatments to communicate priority, grouping, emphasis, and related visual roles without material ambiguity or contradiction.

It applies to default rendered typography, reading composition, spacing relationships, functional color roles, surfaces, boundaries, icons, decorative imagery, themes, and other visual treatments within the declared scope.

It is independently adoptable. It does not depend on a web-suite umbrella, a design system, or another companion standard. Browser defaults, custom styles, design tokens, component libraries, and other mechanisms can satisfy it when the delivered result and evidence meet the applicable requirements.

This standard does not prescribe a brand identity, aesthetic style, font, type scale, spacing scale, grid, color palette, token format, design tool, component library, CSS methodology, class-naming convention, or framework.

Accessibility conformance, content semantics, responsive layout behavior, interaction behavior, performance, editorial authority, and legal duties remain subject to separately selected authorities where applicable. Adoption, exceptions to local organizational rules, publication, and approval remain subject to the adopting organization's existing authority. Publication of this source does not adopt or update any downstream artifact.

## 2. Interpretation and Definitions

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html)) when, and only when, they appear in this uppercase form. Lowercase uses have their ordinary meaning.

`WEB-DES-NNN` identifies a local requirement synthesized by this template, independently of section numbers. Numbered local requirements are normative. Sections explicitly marked informative are not.

**Visual role** means the declared purpose served by a visual treatment, independently of any particular raw value or implementation mechanism. Examples can include primary text, secondary text, emphasis, boundary, surface, grouping, warning, or decorative accent; this list neither requires those roles nor reserves their names.

**Visual treatment** means a perceptible presentation choice such as typeface, size, weight, line height, spacing, alignment, color, border, shape, iconography, imagery, or elevation.

**Reading text** means continuous text intended to be read beyond a short label, isolated value, heading, caption, or brief message.

**Material** means capable of changing visual understanding, reading, grouping, priority, a reasonable decision or action by the declared audience, an assessment result, or a conformance claim.

The [Web Accessibility Standard](../web-accessibility/standard.md) and [Web Content and Semantics Standard](../web-content-semantics/standard.md) retain their own identifiers, conditions, evidence, and results. Evidence MAY support more than one assessment when it actually addresses each obligation, but one result MUST NOT be represented as another.

## 3. Declared Visual Context and Roles

**WEB-DES-001 — Declared assessment scope.** An assessment MUST identify the evaluated web experience, artifact or release revision, covered pages, views and relevant states, declared audience or audiences, represented languages and writing systems (including writing direction and orientation where materially different), material presentation contexts, material themes or variants, and material exclusions. Any difference between assessed coverage and a claimed scope MUST be explicit.

**WEB-DES-002 — Reviewable visual roles.** Material repeated visual treatments MUST have reviewable intended roles sufficient to evaluate their use and consistency. Roles MAY be expressed through rendered examples, style documentation, tokens, design files, source conventions, component guidance, assessment records, or another suitable mechanism. A particular token system, naming syntax, or documentation format is not required.

**WEB-DES-003 — Role and treatment integrity.** A delivered visual treatment MUST correspond to the role it is represented as serving. The same material role MUST NOT be applied with conflicting meaning within the declared context, and materially different roles MUST NOT be made indistinguishable where the distinction is necessary to understand priority, grouping, or state. Reuse of one raw value for different purposes is permitted when the resulting roles remain clear.

**WEB-DES-004 — Contextual variation.** A theme, brand expression, page type, embedded context, or other visual variant MAY use different treatments, but it MUST preserve the material purposes and distinctions of applicable roles or explicitly declare and justify the changed role. Exact values need not remain identical across variants.

## 4. Typography and Reading Composition

**WEB-DES-005 — Discernible typographic hierarchy.** Typographic treatments MUST make material differences in priority, grouping, and emphasis reasonably discernible to the declared audience and MUST NOT visually contradict the content relationships they are intended to express. This requirement evaluates visual communication; it does not establish semantic-markup correctness or accessible exposure.

**WEB-DES-006 — Legible rendered text.** Text necessary to understand or use the declared scope MUST render with sufficient size, weight, spacing, line distinction, and character clarity for its purpose under the assessed presentation contexts. It MUST NOT be materially obscured, clipped, collided, or made ambiguous by the chosen visual treatment. Nominal font size or a design-file specimen alone MUST NOT establish this result.

**WEB-DES-007 — Typeface, script, and fallback fitness.** Selected typefaces and their delivered fallbacks MUST support the represented characters and writing systems needed within the declared scope and preserve material legibility and hierarchy when used. An assessment MUST include materially different scripts, weights, styles, variable-font settings, and fallback conditions that can affect the result. This requirement does not prescribe how fonts are licensed, hosted, loaded, or technically substituted.

**WEB-DES-008 — Reading measure.** Reading text MUST use a line measure that supports reasonable tracking from one line to the next in its actual language, writing system, typeface, size, line height, content, and presentation context. Short text, code, data, captions, display text, and intentionally non-continuous reading contexts can require different measures. No universal character count, physical width, or token is prescribed.

**WEB-DES-009 — Typographic composition.** Line height, word spacing, letter spacing, paragraph spacing, alignment, and emphasis MUST work together without materially impairing reading or falsely changing the apparent grouping or priority of text. Different content roles MAY use different composition. Conformance to this requirement does not establish compliance with accessibility requirements for user override, resizing, reflow, contrast, or text spacing.

## 5. Spatial and Other Visual Relationships

**WEB-DES-010 — Spatial grouping and separation.** Spacing MUST reinforce the intended relationship among elements. Related items MUST remain perceptibly grouped, and materially distinct groups MUST remain perceptibly separated. Spatial proximity MUST NOT create a materially false association or conceal a necessary boundary.

**WEB-DES-011 — Coherent repeated spacing.** Repeated spacing relationships SHOULD use a limited and reviewable set of values or rules appropriate to their purposes. A departure is legitimate when content, language, density, composition, or another concrete condition requires it and the resulting grouping remains clear. This requirement does not prescribe a mathematical scale, unit, breakpoint, or token.

**WEB-DES-012 — Functional color roles.** Color used as a functional visual role MUST be applied consistently enough that its purpose is not materially misleading within the declared context. Brand and decorative colors MAY share raw values with functional roles when their uses remain distinguishable. This requirement does not establish color contrast, non-color redundancy, or accessibility conformance.

**WEB-DES-013 — Supporting cues and visual priority.** Borders, shapes, surfaces, elevation, icons, decorative imagery, and other supporting treatments MUST NOT materially contradict the roles they accompany or obscure content needed to understand or use the declared scope. Content-bearing media, accessible alternatives, interaction behavior, and responsive media fitting remain outside this requirement.

## 6. Verification and Results

**WEB-DES-014 — Reviewable evidence.** Evidence MUST be proportionate to the obligation and sufficient to trace a result to the assessed scope and revision, applicable requirement, relevant role or treatment, method and presentation context, expected and observed result, reviewer or tool, date, limitations, and unresolved findings. Shared context MAY be referenced rather than repeated. A design file, token inventory, stylesheet, screenshot, automated measurement, or component catalog MUST NOT be treated as proof of a delivered conclusion it cannot establish.

Automated inspection MAY establish detectable values, repetitions, font facts, or rendered measurements. Human review is required where deciding visual hierarchy, legibility, grouping, role meaning, materiality, or contextual fitness exceeds the method's capability. Representative-reader or specialist review MAY support difficult conclusions. No vendor, evidence format, storage system, or universal review ceremony is prescribed.

**WEB-DES-015 — Distinct and truthful results.** Results MUST distinguish local-standard conformance, partial assessment, nonconformance, and undetermined obligations. An obligation is undetermined when it is applicable but the available evidence is missing, incomplete, conflicting, or otherwise insufficient; this differs from an obligation outside the declared scope. Local-standard conformance requires the declared scope to satisfy every applicable mandatory requirement of the identified adopted version. Partial coverage is not a reduced conformance level, and missing evidence MUST NOT be converted into a pass.

Any conformance claim MUST identify the adopted standard version, evaluated artifact revision, assessed scope, material exclusions, and conclusion. A design-foundation result MUST NOT be represented as accessibility conformance, content-semantic conformance, responsive-layout conformance, interaction quality, brand approval, legal compliance, or whole-suite conformance.

**WEB-DES-016 — Change and reassessment.** A material change to typography, font or fallback behavior, visual roles, spacing, color, supporting treatments, content composition, represented language, writing system, writing direction or orientation, theme, assessed scope, or relevant evidence MUST trigger reassessment of the obligations whose results may be affected before a current conclusion is asserted. Unaffected evidence MAY be reused when its applicability to the current revision and obligation is justified; reuse MUST NOT conceal stale or invalidated results.

## 7. Informative Verification Guidance

This section is informative.

Useful verification combines inspection of the delivered experience with computed styles or equivalent presentation facts, actual font and fallback behavior, representative content and languages, narrow and wide presentation contexts, themes, zoom or magnification where relevant to the selected accessibility authority, and comparisons among repeated visual roles.

Typography variables interact. A nominal size that works for one typeface may not work for another because optical size, x-height, weight, character design, and font metrics differ. Reading measure likewise depends on the language, script, typeface, size, line height, and kind of content. USWDS publishes context-sensitive measure and line-height guidance, while GOV.UK and Carbon use internally calibrated type systems. Those values can inform local decisions without becoming universal requirements of this template.

Spacing can be evaluated by asking whether distance reinforces the intended grouping and whether similar relationships receive similar treatment. A limited scale can reduce arbitrary variation, but an exact mathematical progression is neither necessary nor sufficient. A dense operational display can remain clear, while a spacious page can still group unrelated items misleadingly.

Purpose-based color names, typographic roles, or spacing roles can improve reviewability. Tokens are one possible implementation, but raw values, token existence, or adherence to a draft token exchange format do not by themselves establish correct visual use.

Browser defaults can provide a coherent foundation. Conversely, a sophisticated design system can fail this standard when its delivered implementation contradicts or bypasses the documented roles.

## 8. Adaptation and Boundaries

An adopting organization MAY define fonts, scales, palettes, visual roles, density modes, themes, brand rules, evidence forms, numerical defaults, or stronger requirements through its existing authority. Such adaptations MUST identify their scope and consequences and MUST NOT be represented as requirements of an unchanged upstream template.

Accessibility requirements for contrast, color dependence, text resizing, reflow, text-spacing override, focus appearance, and assistive-technology exposure remain with the adopter's selected accessibility authority. Intended content meaning and semantic relationships remain with the selected content-semantic authority. Layout transitions, interaction behavior, performance, CSS architecture, and organizational design approval remain outside this standard.

Motion is not governed by this version. Where motion communicates feedback, state, navigation, or task progression, interaction and accessibility authorities should govern the applicable outcomes. A future revision should add motion only if evidence demonstrates a distinct visual-foundation obligation that cannot be owned coherently elsewhere.

This standard does not require an adopter to use either published sibling standard. Cross-references clarify boundaries and do not create a whole-standard adoption dependency.

### Strength and ownership rationale — informative

Mandatory requirements protect visual meaning, legibility, grouping, role integrity, and truthful claims. The recommendation for a limited repeated spacing set preserves a strong coherence default while allowing small, content-driven, or intentionally irregular systems to demonstrate the required outcome without formal scale machinery. Permissions preserve legitimate variation in brand, language, content, technology, tools, and implementation.
