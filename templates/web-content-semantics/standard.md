# Web Content and Semantics Standard

## 1. Purpose and Scope

This standard defines baseline requirements for preserving the intended meaning, structure, identity, and understandability of content delivered through a web experience.

The operative question is whether the declared audience can determine that meaning from the delivered content and its declared semantics without material distortion, omission, contradiction, or unsupported inference.

It applies to human-readable content, semantic structure, language and direction metadata, links and referenced resources, data relationships, images, audio, video, downloads, embedded resources, alternate or localized representations, and machine-readable descriptions when those items occur within the declared scope.

It is independently adoptable. It does not depend on a web-suite umbrella or another companion standard. It does not prescribe a brand voice, house style, content-management system, component library, editorial approval workflow, analytics strategy, search-marketing strategy, or legal-compliance regime.

This standard does not establish accessibility conformance. Accessibility-specific requirements and claims remain within the [Web Accessibility Standard](../web-accessibility/standard.md) or another legitimately selected accessibility authority. Responsive presentation, visual typography, interaction behavior, and shared quality systems are addressed by separately selected authorities where an adopter has chosen one, and remain outside this standard in their absence.

Adoption, exceptions to local organizational rules, publication, and approval remain subject to the adopting organization's existing authority. Publication of this source does not adopt or update any downstream artifact.

## 2. Interpretation and External Basis

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html)) when, and only when, they appear in this uppercase form. Lowercase uses have their ordinary meaning.

`WEB-CONT-NNN` identifies a local requirement synthesized by this template, independently of section numbers. Numbered local requirements are normative. Sections explicitly marked informative are not.

**Intended meaning** is the meaning supported by the delivered content, its declared purpose, applicable authoritative source material, and available reviewable authoring evidence. Where those sources materially conflict or are insufficient to establish the meaning, the affected conclusion is undetermined. Not every listed source exists or applies for every item of content. Intended meaning is undetermined only when the sources that are actually available or applicable materially conflict or remain insufficient to establish it, not merely because one category of source, such as authoritative source material, does not exist for the content in question. Intended meaning MUST NOT be supplied or changed after assessment merely to excuse a conflicting implementation.

**Material** means capable of changing applicability, intended meaning, a reasonable decision or action by the declared audience, an assessment result, or a conformance claim.

The [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/) supplies relevant platform semantics for HTML documents. It is a living external specification, not a fixed wholesale dependency incorporated by this standard. An assessment MUST identify the delivered content technologies and the applicable specifications or declared semantic conventions used to evaluate them. Conformance to this standard does not replace conformance to those specifications, and syntactic validity alone does not establish that implemented semantics match the content's intended meaning.

External accessibility specifications and that independently adoptable sibling standard retain their own identifiers, conditions, evidence, and results. Evidence MAY support both a content-semantic assessment and an accessibility assessment when it actually addresses both, but one result MUST NOT be represented as the other.

## 3. Declared Content Context

**WEB-CONT-001 — Declared assessment scope.** An assessment MUST identify the evaluated web experience, artifact or release revision, covered pages, views, resources and relevant states, intended audience or audiences, represented languages, material content variants, and material exclusions. A declared audience MUST correspond to the content's actual or reasonably foreseeable audience within the declared distribution and use and MUST NOT be narrowed to avoid an otherwise applicable requirement. Any difference between assessed coverage and a claimed scope MUST be explicit.

**WEB-CONT-002 — Identifiable content purpose.** Each assessed page, view, or independently used resource MUST communicate enough identity and context for its declared audience to determine its primary purpose and distinguish it from materially different content. A title, heading, label, surrounding context, metadata, or another suitable mechanism MAY provide that identity; the mechanism is not required to be identical for every content type.

**WEB-CONT-003 — Conditional, current, and state-reporting content.** Content whose meaning or use materially depends on time, revision, location, eligibility, price, availability, audience, or another condition MUST communicate the applicable condition where omission could change a reasonable reader's understanding or action. Content MUST NOT be represented as current, available, applicable, or complete when the assessment evidence establishes that representation to be materially false or stale for the declared scope. A message that asserts the outcome, status, or result of an action, including a confirmation, error, or availability message, MUST NOT misrepresent that outcome to the declared audience. Interaction behavior that produces such a message remains outside this requirement; only the truthfulness of its content is addressed here.

## 4. Semantic Correspondence

**WEB-CONT-004 — Meaning represented in semantics.** The delivered content MUST represent its intended roles, relationships, groupings, and distinctions using conforming semantics available in the selected content technology or another declared mechanism that preserves those meanings. Visual appearance, source order, punctuation, or spatial position alone MUST NOT substitute for a required semantic relationship when the delivered technology can represent it.

This requirement concerns correspondence between intended meaning and implemented semantics. It does not by itself establish accessible exposure, user-agent support, or WCAG conformance.

**WEB-CONT-005 — Hierarchy and grouping.** Headings, sections, landmarks, lists, quotations, figures, captions, and other structural groupings MUST correspond to the content relationships they claim to represent. Heading rank or grouping MUST NOT be selected solely to obtain a visual appearance. A document is not required to use every available structural feature or one universal heading pattern.

**WEB-CONT-006 — Tabular and structured data.** Content that claims row, column, header, sequence, hierarchy, or other data relationships MUST preserve those relationships in the delivered representation. Data tables MUST identify the relationships needed to interpret their cells using applicable table semantics or an equally reviewable representation. Tables MUST NOT be used solely to create visual layout when doing so falsely represents content as tabular data.

**WEB-CONT-007 — Links and referenced resources.** A hyperlink or referenced resource MUST be represented accurately enough in its text and applicable context for the declared audience to understand its destination, resource, or purpose without a materially misleading inference. Material format, access, download, language, or destination differences MUST be disclosed when omission would foreseeably change the reader's decision to follow the reference. This requirement does not prescribe link styling or interaction behavior.

**WEB-CONT-008 — Language and direction integrity.** The actual default language of human-readable content and material language changes MUST be identified through applicable content-language semantics. Base direction and directional isolation MUST be supplied where needed to preserve intended reading order and punctuation for bidirectional or directionally uncertain content. Language or direction metadata MUST NOT knowingly contradict the content it describes.

## 5. Understandable and Equivalent Content

**WEB-CONT-009 — Audience-appropriate understanding.** Content necessary to understand the page, resource, decision, or task MUST be written and organized so the declared audience can reasonably understand its material meaning. Necessary unfamiliar terms, abbreviations, assumptions, and prerequisites MUST be explained or made available in context unless evidence supports that the declared audience can be expected to understand them. Specialized language is permitted when appropriate to that audience. A readability score, word count, grammar tool, or simplified vocabulary alone MUST NOT establish conformance. This requirement addresses comprehension of meaning; sufficiency of instructions, conditions, and consequences needed to act is addressed by `WEB-CONT-010`.

**WEB-CONT-010 — Instructions, conditions, and consequences.** When content asks or enables a person to decide, provide information, complete a task, or rely on a stated outcome, it MUST communicate the material instructions, prerequisites, conditions, consequences, and next steps needed for that use. The content MAY rely on previously established context when that reliance remains clear and available. This requirement presumes the general comprehension required by `WEB-CONT-009` and adds the task-specific completeness needed to act. Interaction behavior and recovery mechanics remain outside this requirement.

**WEB-CONT-011 — Media as content.** A resource is content-bearing when its removal would change what the declared audience could understand or do; it is decorative when its removal would not. Content-bearing images, audio, video, downloads, and embedded resources MUST have enough identity and context for the declared audience to understand what content they provide and how they relate to the surrounding material. Content MUST NOT be classified as decorative or purely presentational when it carries material meaning that is not otherwise disclosed to the declared audience. A caption, transcript, or audio description supplied for media content is an alternate representation under `WEB-CONT-012`. This requirement does not determine when an accessibility alternative is required, prescribe media controls or formats, or govern responsive media layout.

**WEB-CONT-012 — Alternate, summarized, and localized representations.** A representation described as translated, localized, summarized, equivalent, current, or an alternative to another representation MUST preserve the material meaning needed for its stated purpose and MUST identify material divergence that could change understanding or action. The relationship, revisions, languages, and relevant limitations MUST be reviewable. This local content-equivalence requirement does not establish a WCAG conforming alternate version.

**WEB-CONT-013 — Generated and externally supplied content.** Generated, third-party, syndicated, embedded, localized, or user-provided origin does not by itself exempt content from applicable requirements. An assessment MUST identify material limitations that prevent the source content's meaning, currency, or semantic representation from being verified. Source labels, generation method, or provider reputation MUST NOT substitute for content evidence.

**WEB-CONT-014 — Human and machine-readable consistency.** When structured data or other machine-readable metadata represents human-facing content, it MUST use its declared vocabulary or convention consistently and MUST NOT materially contradict the corresponding human-facing identity, facts, conditions, relationships, or current state. This standard does not require a particular vocabulary or require structured data where none is otherwise needed.

## 6. Verification and Results

**WEB-CONT-015 — Reviewable content evidence.** Evidence MUST be proportionate to the obligation and sufficient to trace a result to the assessed scope and revision, applicable requirement, method, content technology or representation, expected and observed result, reviewer or tool, date, limitations, and unresolved findings. Shared context MAY be referenced rather than repeated. No vendor, file format, storage system, or universal review ceremony is prescribed.

Automated validation MAY establish detectable syntax, metadata, or structural facts. Human review is required where deciding intended meaning, audience understanding, materiality, equivalence, accuracy, or context exceeds the method's capability. User research or specialist review MAY support difficult questions. A validator, readability score, language detector, link checker, AI-generated review, or metadata test MUST NOT be treated as proof of conclusions it cannot establish.

**WEB-CONT-016 — Distinct and truthful results.** Results MUST distinguish local-standard conformance, partial assessment, nonconformance, and undetermined obligations. An obligation is undetermined when it is applicable but the available evidence is missing, incomplete, conflicting, or otherwise insufficient to reach a conclusion; this differs from an obligation outside the declared scope. Local-standard conformance requires the declared scope to satisfy all applicable mandatory requirements of the identified adopted version. Partial coverage is not a reduced conformance level. Evidence of a specific failure MUST remain visible when other obligations are undetermined, and missing evidence MUST NOT be converted into a pass.

Any conformance claim MUST identify the adopted standard version, evaluated artifact revision, assessed scope, material exclusions, and conclusion. A content-semantic result MUST NOT be represented as accessibility conformance, platform-specification conformance, legal compliance, editorial approval, factual certification beyond the assessed evidence, or whole-suite conformance.

**WEB-CONT-017 — Change and reassessment.** A material change to content, semantic structure, represented language or direction, referenced resource, media, alternate representation, machine-readable description, assessed scope, applicable convention, or relevant evidence MUST trigger reassessment of the obligations whose results may be affected before a current conclusion is asserted. Unaffected evidence MAY be reused when its applicability to the current revision and obligation is justified; reuse MUST NOT conceal stale or invalidated results.

## 7. Informative Verification Guidance

This section is informative.

Useful verification combines inspection of rendered content, source or document structure, applicable platform semantics, language and direction behavior, links and referenced resources, content variants, and any machine-readable representations. The relevant methods depend on the claim being tested.

Representative readers can reveal ambiguity or missing context that authors and automated tools overlook. Their participation is evidence for the tested audience and context, not proof that every audience will understand the content. Domain review may be necessary for specialized claims, translations, instructions, or data relationships.

Indicators of conditional or stale content can include an expired stated validity period, a superseding authoritative revision, a mismatch between a resource and the conditions it references, or missing information needed for the content's declared purpose. A representation described as complete can be evaluated against the material elements it states or needs to include for that purpose. Historical or archival content can remain accurate to its purpose when its historical context is clear and it is not represented as current. An equivalent representation need not be word-for-word identical, but it should preserve the material meaning needed for its stated purpose.

For example, a page can declare the correct language while a mistranslation reverses an eligibility condition; the language declaration and the translated content require distinct conclusions. Likewise, correct interaction behavior can still present a false status message. Access controls or payment gates do not automatically remove content from scope; an assessment should identify any authorized-access limitation and avoid conclusions about content it could not evaluate.

The [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/) defines platform semantics for HTML. Its [sections and headings](https://html.spec.whatwg.org/multipage/sections.html), [links](https://html.spec.whatwg.org/multipage/links.html#links-created-by-a-and-area-elements), [tables](https://html.spec.whatwg.org/multipage/tables.html), [images](https://html.spec.whatwg.org/multipage/images.html), [media](https://html.spec.whatwg.org/multipage/media.html), [language](https://html.spec.whatwg.org/multipage/dom.html#attr-lang), and [directionality](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute) sections provide relevant implementation facts. They do not turn every example into a local requirement.

W3C Internationalization guidance on [declaring language in HTML](https://www.w3.org/International/questions/qa-html-language-declarations) and [inline bidirectional text](https://www.w3.org/International/articles/inline-bidi-markup/) can support implementation and review. These informative resources are not independently incorporated normative dependencies.

GOV.UK and USWDS content guidance illustrates tested practices within particular public-service systems. Such guidance can inform an adopter's choices without making one government's terminology, reading level, workflow, or component rules universal.

## 8. Adaptation and Boundaries

An adopting organization MAY define audience conventions, terminology, review methods, content-risk tiers, evidence forms, approved vocabularies, translation practices, or stronger content requirements through its existing authority. Such adaptations MUST identify their scope and consequences and MUST NOT be represented as requirements of an unchanged upstream template.

Accessibility consequences remain subject to the adopter's selected accessibility authority. Visual hierarchy and typography, responsive composition and media presentation, controls and state behavior, and shared performance and evidence-system rules remain outside this standard. An adopter MAY govern those matters through separately selected design, layout, interaction, quality, or other competent authority; the absence of such an authority does not bring them within this standard.

This standard does not determine legal duties, certify factual truth beyond assessed evidence, grant rights to publish content, establish editorial approval authority, or prescribe retention, moderation, translation, content-management, or records workflows.

### Strength and ownership rationale — informative

The mandatory rules protect content meaning, semantic correspondence, material context, equivalence, and truthful claims. Permissions preserve legitimate variation in technologies, structures, terminology, evidence mechanisms, and organization-specific adaptation. Requirements avoid universal readability levels, heading formulas, media formats, metadata vocabularies, and content workflows because the current evidence does not justify those prescriptions across web contexts.
