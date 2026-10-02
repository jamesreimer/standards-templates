# Review Integrity Standard

## 1. Purpose

This standard governs correspondence between a Review's claimed conclusion and the scope, reviewed state, evidence, method capability, limitations, and findings that actually support that conclusion.

It protects against a Review result that appears broader, cleaner, more certain, more authoritative, or more complete than the Review established.

## 2. Scope and Interpretation

This standard applies to Reviews across subjects and organizational contexts. It governs the integrity of evaluative conclusions and their representation in later reliance claims.

It does not determine architecture, execution authority, publication authority, adoption authority, or the substantive rules of the reviewed subject. It does not prescribe universal audit procedures, severity taxonomies, report formats, independent-review requirements, or reviewer organizational structures.

### 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html). Lowercase forms retain their ordinary English meaning.

### 2.2 More Specific Applicable Requirements

Where a more specific applicable requirement governs a matter addressed by this standard, conformance to that specific requirement constitutes conformance to the corresponding Review Integrity requirement for that matter. Review Integrity continues to govern matters the more specific requirement does not address.

This standard MUST NOT be applied to weaken, reinterpret, supplement, or duplicate the more specific requirement for the same governed matter. Satisfying one specific requirement does not establish conformance to all Review Integrity requirements.

If independently adopted requirements genuinely conflict, the adopter resolves the conflict under its own authority and applicable adoption model.

## 3. Definitions

**Review**: An evaluation that produces a conclusion about a subject on which another decision, claim, or act may rely, regardless of whether the activity is called a review, assessment, audit, verification, inspection, or another label.

A check, test, or inspection used inside a Review is evidence. Where the result of that step is itself represented as the evaluative conclusion being relied on, that evaluative result is the Review. Performing a check does not automatically make it a Review.

For example, CI output used by a reviewer is evidence. If “CI passed” is itself represented as the evaluative conclusion supporting readiness, that claim falls within this standard. An approval's evaluative conclusion may likewise fall within this standard; the authority granted by that approval remains governed elsewhere. These examples are informative.

**Material Finding**: A finding identified during a Review whose omission, misclassification, or unresolved status is capable of changing the Review conclusion, responsibility, a disposition required for later reliance, or a decision that the Review's identified purpose is intended to support.

## 4. Subject, Purpose, Scope, and Coverage

A Review MUST identify its subject, the purpose or conclusion it supports, and enough scope and coverage information to interpret its conclusion. This information MAY be identified directly or by reference to existing context, such as a request, work item, change record, assessment plan, publication record, or equivalent record. A duplicate review document is not required.

A Review MUST NOT represent its conclusion as covering dimensions beyond what its scope and evidence support. Relevant dimensions may include subject matter, populations, environments, obligations, states, or sampled coverage.

Where bounded, partial, sampled, or otherwise non-exhaustive coverage could change interpretation of the conclusion, that limitation MUST remain visible. No fixed coverage vocabulary is required.

## 5. Reviewed-State Identity

Where the reviewed subject can materially change, the Review MUST identify the reviewed state sufficiently to distinguish materially different states.

The mechanism may be an immutable revision, edition or version, publication identity, deployed revision, dated state or configuration, or an equivalent domain-appropriate identity. Applicable source-identity and correspondence mechanics remain governed by the relevant provenance model, as described in Section 16. Section 13 governs continued applicability when the subject or state changes.

## 6. Evidence and Method Capability

Evidence MUST be sufficient for the Review conclusion actually claimed.

A Review MUST NOT represent a test, check, sample, observation, prior result, tool output, or evidence source as establishing more than it can support. Passing checks do not by themselves establish global correctness.

Where material to interpretation, the Review MUST preserve distinctions among established or observed evidence, inference, unavailable or unperformed evidence, unresolved or conflicting evidence, and matters outside the method's capability.

Missing or insufficient evidence MUST NOT be converted into a pass. Section 11 governs how to bound a result when evidence cannot establish a broader conclusion.

### 6.1 Conflicting Evidence

Material conflicting or contrary evidence MUST NOT be silently discarded when doing so could change the Review conclusion. The Review MUST resolve enough of the conflict to support the claim or retain the limitation or unresolved result visibly.

This applies regardless of whether the evidence comes from people, tools, methods, observations, or historical or current sources. It does not require consensus, multiple reviewers, or a prescribed disagreement procedure.

## 7. Proportionality

Review depth SHOULD be proportionate to the consequence of an incorrect conclusion, uncertainty, breadth of the claim, novelty or change, and practical difficulty of correcting false reliance.

Low-consequence, narrow Reviews MAY be brief. Proportionality does not relax any applicable requirement of this standard.

## 8. Claim Discipline and Authority

A Review MUST NOT represent terms or conclusions such as “clean,” “no findings,” “approved,” “accepted,” “ready,” “conforming,” “verified,” or “independent” as establishing more than the actual scope, evidence, method capability, reviewed state, and applicable authority support. These words are examples, not reserved vocabulary.

A Review conclusion is evaluative. It does not itself grant authority to implement, execute, publish, deploy, adopt, accept risk, or waive requirements.

## 9. Finding Attribution

A Review MUST NOT attribute a Material Finding, limitation, satisfactory result, or other material condition to the reviewed subject, a change, surrounding state, or another cause more strongly than the evidence supports when the attribution could change responsibility, disposition, or reliance.

A limitation of the Review or its evidence MUST NOT be represented as a defect in the reviewed subject merely because the Review could not establish the result.

For example, a change review may distinguish a pre-existing defect, a defect introduced by the change, and a defect exposed by interaction with surrounding state when evidence supports those distinctions. These informative examples do not require particular labels or make that classification universal.

## 10. Material Findings and Later Reliance

Before Review completion, every Material Finding identified in scope MUST be reported, and its effect on the Review conclusion MUST be stated. A Review may complete with findings.

Classification does not equal disposition. A reviewer MAY recommend a disposition. A recommendation is not itself a disposition unless the reviewer also holds the applicable authority and acts in that capacity.

A later readiness, completion, acceptance, publication, or similar reliance claim MUST NOT represent the Review as supporting that claim while omitting Material Findings that affect that reliance and have neither been accurately disclosed in that reliance claim nor received a valid disposition under the applicable authority or subject-specific standard.

This standard does not require the reviewer to disposition findings and grants no authority to correct, accept, defer, waive, or continue. Depending on applicable authority, later treatment might include correction, acceptance under competent authority, authorized deferral recorded where needed, qualification, or dismissal with rationale. These are informative examples, not a universal disposition scheme.

## 11. Bounded and Unresolved Results

A Review MAY return a partial, bounded, qualified, unresolved, undetermined, or another truthful bounded result. Material limitations MUST remain visible.

A Review MUST NOT claim an established conclusion where an unresolved limitation could defeat that conclusion. It MUST instead narrow or qualify the conclusion, or leave the affected result unresolved or undetermined.

## 12. Adjacent and Dependent Surfaces

Where an adjacent or dependent surface could materially invalidate the Review conclusion, the Review MUST examine enough evidence about that surface to support the conclusion or narrow the claim so that it does not depend on that surface.

Examples include dependencies, authority boundaries, lifecycle or completion relationships, cross-references, and generated or published derivatives. These examples are informative; they do not establish a universal checklist. Purpose-specific review procedures remain separately governed.

## 13. Change and Reassessment

A prior Review conclusion MUST NOT be represented as applying to a materially changed reviewed subject or state except where evidence establishes that the earlier conclusion remains applicable.

Reassessment depth SHOULD scale with what changed, the affected review dimensions, consequence, and uncertainty. Unaffected evidence MAY be reused when its applicability is established.

Where applicable, Shared Asset Provenance governs correspondence, Operational Execution Contract governs Mechanical Correction, and Standards Authoring governs renewed review of changed approved publication content. These requirements retain their ownership under Section 2.2; the permission to reuse evidence does not weaken them.

## 14. Independence Claims

A Review MUST NOT be represented as independent when its conclusion rests solely on the reviewed subject producer's conclusion, evidence summary, or assertion that required checks passed.

Trustworthy evidence MAY be reused. Independent review need not reproduce every check. This standard does not define organizational independence generally or determine whether independence is required; those matters remain with applicable authority.

## 15. Review Completion

A Review is complete when the applicable requirements above have been satisfied for the conclusion being returned. A complete Review MAY conclude that there are no Material Findings within scope, that findings exist, that assessment is partial, that a result is unresolved or undetermined, or another truthful bounded result.

Review completion does not imply work readiness, implementation completion, publication authorization, or execution authority.

The Review result SHOULD retain enough information for later reliance to determine what was reviewed, which state, the purpose and scope, the conclusion, limitations, and Material Findings and their effects. This standard does not require a universal report format.

### 15.1 Informative Examples: Overclaim and Honest Miss

This subsection is informative.

A bounded review that calls an entire subject “clean” beyond the scope and evidence it established is nonconforming. For example, inspecting selected records cannot establish that every record is correct without evidence supporting that broader claim.

A properly bounded, proportionate Review that misses a defect outside what its declared and evidenced scope established is not automatically nonconforming. Review Integrity governs truthful claims, not omniscience. Discovery of a defect does not by itself establish that the earlier Review overclaimed.

## 16. Boundaries with Related Standards

The allocation by matter in Section 2.2 preserves the following responsibilities where those standards are applicable:

- [Architectural Reasoning](../architectural-reasoning/standard.md) owns architectural conclusion validation, assumptions, contrary evidence, failure cases, architectural limitation accounting, and architectural finding disposition.
- [Operational Execution Contract](../operational-execution-contract/standard.md) owns execution authority, execution validation, execution completion and stop conditions, and Mechanical Correction.
- [Standards Authoring](../standards-authoring/standard.md) owns normative drafting, requirement calibration, and renewed review of changed approved publication content.
- [Shared Asset Provenance](../shared-asset-provenance/standard.md) owns source identity, consumed identity, correspondence, and relationship meaning.
- [Publication and Release Integrity](../publication-release-integrity/standard.md) owns publication verification, publication claims, and publication identity and state binding.
- [Standards Adoption](../standards-adoption-model/standard.md) owns organizational adoption, authority, and the independent lifecycle of adopted normative material.
- [Web Quality and Verification](../web-quality-verification/standard.md) and the [Web Standards Suite companions](../../CATALOG.md#web-standards-suite) retain their domain-specific evidence, result, and reassessment rules and substantive subject requirements.

These references clarify ownership and do not require adoption of the sibling templates.

## 17. Basis

The review-integrity requirements are synthesized organization-neutral standards decisions. BCP 14 supplies the normative-keyword interpretation, not the review model.

Mandatory requirements protect correspondence between the conclusion and its support. Recommendations allow proportionate judgment about review depth, reassessment depth, and retained information. Permissions preserve legitimate bounded outcomes and reuse without prescribing a review method or organization.
