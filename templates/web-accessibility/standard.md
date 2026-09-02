# Web Accessibility Standard

## 1. Purpose and Scope

This standard defines an accessibility target for a declared web experience and the assessment, evidence, and claim integrity needed to determine whether that target is met.

It is independently adoptable. It does not depend on a web-suite umbrella or another companion standard. It addresses accessibility consequences of design, layout, interaction, content, semantics, and media without owning their broader design conventions or general quality practices.

This template does not itself establish organizational authority, approve a release, or certify a web experience. Adoption, changes, exceptions to local organizational rules, and publication remain subject to the adopting organization's existing authority. Publication of this source does not adopt or update any downstream artifact.

This standard provides neither legal certification nor a determination of applicable legal obligations. It does not claim complete inclusive-design coverage.

## 2. Interpretation and External Dependency

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` have their BCP 14 meanings under RFC 2119 and RFC 8174, as described by the [Standards and Policy Authoring Standard](../standards-authoring/standard.md#4-normative-keywords). Lowercase uses have their ordinary meaning.

`WEB-A11Y-NNN` identifies a local requirement synthesized by this template, independently of section numbers. It is not a WCAG identifier. External identifiers such as WCAG 1.1.1 retain their source meaning. Numbered local requirements below are normative; sections explicitly marked informative are not. Incorporation does not turn source notes, examples, or supporting guidance into requirements.

The fixed normative external dependency is [Web Content Accessibility Guidelines (WCAG) 2.2, W3C Recommendation, 12 December 2024](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). The default technical target is Level AA.

### Incorporated-source map

This map locates the external obligations; it does not replace their text, definitions, conditions, or exceptions.

| Subject | Controlling location in the dated Recommendation |
| --- | --- |
| Normative versus informative material | [§5.1](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#interpreting-normative-requirements) |
| Level AA: all Level A and AA criteria, or a qualifying AA alternate version | [§5.2.1](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#cc1) |
| Full pages, complete processes, accessibility-supported uses, non-interference | [§§5.2.2–5.2.5](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#cc2) |
| Optional claims and required claim components | [§5.3](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#conformance-claims) |
| Third-party-content and language partial-conformance statements | [§5.4](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#conformance-partial), [§5.5](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#conformance-partial-lang) |
| Accessibility support and conforming alternate versions | [§6 accessibility-supported definition](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#dfn-accessibility-supported), [alternate-version definition](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#dfn-conforming-alternate-versions) |

## 3. Scope, Target, and Complete Coverage

**WEB-A11Y-001 — Declared assessment scope.** An assessment MUST identify the evaluated web experience, artifact or release revision, covered pages or routes, relevant states, complete processes, and material exclusions. Any difference between the assessment's coverage and an intended conformance claim's scope MUST be explicit. Scope descriptions MUST NOT exclude a page fragment or process step while asserting conformance for the containing full page or complete process.

**WEB-A11Y-002 — Target incorporation.** Unless an adopted adaptation expressly changes the target under section 8, the evaluated scope MUST meet WCAG 2.2 Level AA under the fixed Recommendation. This incorporates every Level A and Level AA success criterion, evaluated according to its source-defined conditions, together with the complete §5.2 conformance requirements and the definitions and source conditions needed to apply them. Applicable §5.3–§5.5 conditions MUST govern any claim or partial-conformance statement made. A selected checklist MUST NOT substitute for this incorporation.

**WEB-A11Y-003 — Coverage mapping.** Assessment evidence MUST map the selected target’s complete success-criterion inventory using the original WCAG identifiers, together with the conformance requirements that are not success criteria. For each success criterion and conformance requirement, it MUST identify the result and supporting evidence, or the specific unresolved coverage. When there is no content to which a success criterion applies, the mapping MUST record that applicability basis and the criterion’s satisfied result under the WCAG conformance model. It MUST NOT omit the criterion or confuse absence of applicable content with an unperformed or unresolved check.

For the fixed target, the inventory is 31 Level A and 24 Level AA criteria. WCAG 2.2 [removed 4.1.1 Parsing](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#parsing); it is not part of that inventory. This does not automatically change separate obligations tied to earlier editions.

**WEB-A11Y-004 — Source conditions, not local waivers.** Use of a source-defined exception or conforming alternate version MUST identify and satisfy its applicable source conditions. A local waiver or organizational risk acceptance MUST NOT be represented as a WCAG exception or as proof of WCAG conformance. A different implementation route is permitted only to the extent that it satisfies the selected target; the existence of an alternative alone is not proof.

**WEB-A11Y-005 — Technology and context.** The assessment MUST identify the technologies relied upon, the relevant user-agent and assistive-technology context, and the evidence supporting accessibility-supported uses. It MUST address non-interference as well as the relied-upon implementation. A technology name or a successful test in one environment MUST NOT be treated as unconditional support for every use, state, language, or environment.

## 4. Verification Responsibilities and Evidence

**WEB-A11Y-006 — Reviewable evidence.** Evidence MUST be proportionate to the obligation and sufficient to trace a conclusion to the assessed scope and revision, method, environment, expected and observed result, evaluator or tool, date, limitations, and unresolved findings. Shared context MAY be referenced rather than repeated for each result. No particular file format, vendor, storage system, or retention period is prescribed.

**WEB-A11Y-007 — Method coverage.** The assessment MUST distinguish automated checks, manual evaluation, assistive-technology verification, and any specialist review, identifying who or what performed each and which obligations it supports. Methods MUST cover the judgments needed for the assessed obligations; an automated clean scan alone MUST NOT establish full conformance. Human judgment is required where the chosen automated method cannot establish the necessary result.

**WEB-A11Y-008 — Actual manual and assistive-technology results.** Manual and assistive-technology conclusions MUST be supported by performed evaluation or by applicable, reviewable evidence whose reuse is justified under section 7. Relevant interaction, state, language, and environment limitations MUST remain visible. A planned test, an AI-generated prediction, or an inaccessible test environment MUST NOT be reported as an observed passing result. Assistive-technology verification MUST address the uses relied upon for accessibility support; this standard does not prescribe a universal browser or device matrix.

**WEB-A11Y-009 — Competence limits.** When an assessment question exceeds the evaluator's competence or the available method's capability, the conclusion MUST remain undetermined unless adequate evidence is obtained. Specialist review MAY resolve such questions; it is not a universal audit ceremony, a required job title, or a substitute for evidence. The reviewer resolving the question MUST have the competence needed for that question.

**WEB-A11Y-010 — Sampling limits.** Sampling MAY support assessment planning and evidence collection. Its coverage, selection basis, and limits MUST be explicit. A sampled page or state MUST NOT by itself establish conformance of unexamined scope. Any broader conclusion MUST have a justified evidence basis covering the claimed scope and all applicable conformance conditions.

**WEB-A11Y-011 — Evaluation timing.** Accessibility evaluation SHOULD begin while material design and implementation choices remain changeable and recur during development. A bounded assessment of an existing artifact may legitimately start later; that timing does not relax the target or claim conditions.

## 5. Results and Truthful Claims

**WEB-A11Y-012 — Distinct outcomes.** Results MUST distinguish the following meanings rather than collapse them into one pass/fail badge:

- **Local-standard conformance:** the declared scope meets the selected technical target and all applicable mandatory local requirements of the identified adopted version. Departures from recommendations are considered under BCP 14; a local waiver does not satisfy an unchanged mandatory requirement.
- **WCAG conformance:** the external target's own conformance conditions are satisfied, independently of whether this local assessment discipline was followed.
- **Partial assessment:** assessment coverage is incomplete. This describes coverage, not a reduced conformance level.
- **Nonconformance:** evidence establishes failure of an applicable requirement. The affected local or external requirement is identified.
- **Source-defined partial-conformance statement:** a statement made under the applicable WCAG conditions, not a full-conformance result.
- **Undetermined:** evidence is insufficient to decide an obligation or the overall result. It is not a pass.

Coverage and findings may coexist: a partial assessment can reveal known nonconformance and leave other obligations undetermined. An assessment conducted faithfully under this standard can report failures; that does not make the evaluated web experience locally conforming.

**WEB-A11Y-013 — No unsupported completion claims.** A conformance conclusion MUST be supported for its entire declared scope. Missing, stale, unperformed, or unresolved evidence MUST NOT be converted into a passing result. A result based on there being no content to which a success criterion applies MUST be reported only when the applicability basis required by `WEB-A11Y-003` is established; it is not an evidence gap. Known failures MUST remain visible even if other coverage is incomplete. Claims about approval, evaluation completion, or effectiveness MUST be true at the time made; text intended to survive publication MUST use stable or explicitly event-conditioned wording when the relevant act has not yet occurred. Wording does not create the underlying act or authority.

**WEB-A11Y-014 — Optional WCAG claims.** A WCAG conformance claim MAY be made when substantiated. If made, it MUST include every required §5.3 component and accurately identify its date, guidelines title, WCAG version and URI, level, page scope including subdomain coverage, and relied-upon technologies. Optional claim information remains optional. Adoption of this template alone MUST NOT be presented as WCAG conformance, and no badge or public claim is required.

**WEB-A11Y-015 — Partial-conformance statements.** A WCAG third-party-content or language partial-conformance statement MUST satisfy its source conditions and retain its nonconforming meaning. It MUST NOT be confused with partial assessment or permission to claim full conformance. Third-party involvement alone MUST NOT serve as an exclusion or waiver; any determination using the separate monitored-content route in §5.4 MUST satisfy that route's conditions in full.

## 6. Informative Verification Guidance

This section is informative. W3C's [Evaluating Web Accessibility Overview](https://www.w3.org/WAI/test-evaluate/) explains that tools alone cannot determine accessibility and that knowledgeable human evaluation is needed. Useful evidence combines complementary methods rather than treating any method as universal.

For example, automation can identify some detectable defects; manual review can evaluate meaning and task behavior; assistive-technology evaluation can examine actual supported interactions; and specialist input can address difficult interpretation or implementation questions. None of these labels guarantees adequate coverage or evaluator competence.

The [Understanding Conformance guidance](https://www.w3.org/WAI/WCAG22/Understanding/conformance.html) explains the source model but is informative. In particular, responsive variations, complete task journeys, alternate-version access, and interfering content merit explicit review. The fixed Recommendation, not this reminder or a tool's rule set, controls the conditions.

W3C Understanding documents, Techniques, and the [ARIA Authoring Practices Guide introduction](https://www.w3.org/WAI/ARIA/apg/about/introduction/) support interpretation and implementation. They are not additional normative dependencies here. Using a technique or copying an APG pattern does not independently establish that the implemented experience conforms.

Inclusive-use research and participation by people with disabilities can reveal barriers beyond this target. Such findings are valuable informative input, not evidence of complete inclusive-design conformance or an unannounced extension of the WCAG target.

## 7. Changes and Reassessment

**WEB-A11Y-016 — Affected-obligation reassessment.** Changes to implementation, assessed scope, target edition, local requirements, or relevant evidence MUST trigger reassessment of the obligations whose results may be affected before a current conformance conclusion is asserted. The assessment MUST identify the impact basis and any remaining uncertainty. Unaffected evidence MAY be reused when its relevance to the current revision, environment, and obligation is justified; reuse MUST NOT conceal stale or invalidated results.

## 8. Adaptation, Source Maintenance, and Boundaries

**WEB-A11Y-017 — Explicit alternative targets.** An organization MAY adopt a stronger, different, or weaker technical target through its existing authority. An adapted standard MUST identify the chosen edition, level or other target, altered local requirements, and consequences for its claims. A weaker or different target MUST NOT be described as unchanged WCAG 2.2 AA conformance. Stronger local requirements do not rename external WCAG levels; an external claim remains dependent on independently satisfying the claimed edition and level. Changing this source does not change an adopted target automatically.

**WEB-A11Y-018 — Fixed-source integrity.** The dated Recommendation MUST remain the normative dependency unless deliberately changed in the adopted standard. Editorial errata MAY inform interpretation and avoid reproducing known defects, but MUST NOT be presented as a new conformance level or as independently authored local obligations. A proposed substantive correction MUST NOT be treated as normative WCAG text before its inclusion in a revised W3C Recommendation. Any later source change requires an explicit dependency and affected-evidence review rather than silent synchronization.

### Errata disposition — informative

The [official WCAG 2.2 errata](https://www.w3.org/WAI/WCAG22/errata/) were reviewed as of 2 September 2026. All 17 entries listed after 12 December 2024 were classified Editorial; no substantive correction was listed. Some editorial corrections touch normative wording, so “editorial” does not mean merely visual. They do not replace this standard's dated dependency. W3C's stated errata process withholds normative status from substantive corrections until a revised Recommendation.

### Strength and ownership rationale — informative

The mandatory local rules protect target completeness, reproducible assessment, truthful claims, and source integrity. The timing recommendation permits legitimate retrospective assessment. Permissions preserve proportionate choice of methods, evidence reuse, and explicitly governed adaptation without weakening external conformance conditions.

Accessibility-specific verification stays with this standard. Broader design foundations, responsive-layout conventions, interaction patterns, content practices, general evidence systems, legal compliance, and organizational approval authority retain their own owners. No companion, workflow, certification, approval role, or records regime is created by this document.
