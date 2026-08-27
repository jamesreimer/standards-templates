# Standards and Policy Authoring Standard

## 1. Purpose

This standard defines default rules for authoring organization-owned standards and policies so that normative documents remain clear, scoped, reviewable, internally consistent, and proportionate to the consequences they are intended to protect against.

It is intentionally domain-neutral. The same authoring discipline may be used for engineering, media, operations, research, publishing, security, governance, records, production, or other organizational subjects.

## 2. Scope

This standard governs:

- document type and normative register;
- scope statements;
- normative keywords and requirement strength;
- requirements, recommendations, and permissions;
- informative material and examples;
- definitions and terminology;
- external sources and evidentiary basis;
- exceptions and rule calibration;
- cross-document boundaries;
- change discipline for authoring rules.

It does not by itself determine:

- who has authority to adopt a standard or policy;
- the complete lifecycle model for controlled documents;
- repository topology;
- retention or records-management requirements;
- the exact approval workflow used by an organization.

## 3. Document Type and Register

The human-facing document type SHOULD accurately describe what the document is intended to do.

A **Standard** ordinarily defines repeatable requirements, constraints, defaults, or conventions that apply across a defined scope.

A **Policy** ordinarily expresses an organizational rule, authority decision, or required behavioral boundary that the adopting organization intends to enforce within a defined scope.

A **Guide**, **Guideline**, **Practice**, or similar label ordinarily communicates advisory material rather than binding normative force.

A **Workflow** or **Process** ordinarily implies prescribed procedural steps and SHOULD NOT be used when the document only defines required conditions or outcomes.

A **Model** ordinarily names a conceptual or structural subject and does not, by itself, communicate normative force. A stable identifier may use `model` while the human-facing adopted document is titled as a Standard or Policy when that accurately reflects its role.

Do not strengthen or weaken a document's apparent authority merely for stylistic effect.

## 4. Normative Keywords

When the following words appear in uppercase, they are to be interpreted using the meanings established by BCP 14, RFC 2119 and RFC 8174:

- `MUST` and `MUST NOT` indicate requirements;
- `SHOULD` and `SHOULD NOT` indicate strong recommendations for which legitimate exceptions may exist;
- `MAY` indicates permission.

Lowercase forms such as `must`, `should`, and `may` retain their ordinary English meaning and SHOULD NOT be relied upon when precise normative strength matters.

Normative text does not require BCP 14 keywords in every sentence. Direct imperatives and clearly scoped prohibitions MAY be used when their force is unambiguous. However, authors SHOULD use explicit normative keywords where readers need to distinguish mandatory requirements from recommendations or permissions.

Do not mix competing keyword systems inside one document without an explicit reason and interpretation rule.

## 5. Requirement Strength Must Be Calibrated

A rule's normative strength MUST be justified by the consequence it protects against, not by a preference for strict wording.

Use `MUST` or `MUST NOT` when violating the rule would defeat a non-negotiable requirement of the document's scope, create an unacceptable integrity or authority failure, break required interoperability, or otherwise produce a consequence the standard does not permit.

Use `SHOULD` or `SHOULD NOT` when the rule is a strong default and departures may be legitimate when concrete circumstances justify them.

Use `MAY` when the document intentionally grants permission without requiring the permitted action.

A rule MUST NOT be strengthened merely because stricter wording feels safer.

A rule MUST NOT be weakened merely because compliance creates inconvenience.

Repeated successful practice does not automatically promote a recommendation into a requirement.

Repeated friction does not automatically demote a requirement into a recommendation.

## 6. Calibration Under Concrete Pressure

When a concrete case creates meaningful friction with a rule, reviewers SHOULD determine which of the following is true before bypassing or changing the rule:

### A. The protected failure is real

The rule is correctly scoped and the concrete friction is the cost of preventing the failure the rule exists to prevent.

The rule SHOULD be followed.

### B. The rule is materially overbroad, underbroad, or incorrectly scoped

The concrete case demonstrates that the written rule does not accurately protect the intended consequence.

The canonical rule SHOULD be revised through the normal review and document-change path rather than silently worked around.

### C. The case is a legitimate exception within the rule's intended scope

The standard permits exceptions, and the concrete case satisfies the exception conditions or receives approval from the role legitimately authorized to grant the exception.

The exception SHOULD be visible and proportionate to its consequence.

Convenience alone does not establish A, B, or C.

The purpose of this review is not to prefer strictness or looseness. It is to make the normative-strength decision deliberately and visibly.

## 7. Scope and Applicability

Every normative document SHOULD define its scope clearly enough that a reader can determine what subjects, repositories, teams, systems, projects, organizations, artifacts, or activities it is intended to govern.

A document SHOULD also state material exclusions where omission would create a realistic risk of over-application.

Do not use broad titles or scope language to annex neighboring subjects merely for completeness.

A document SHOULD remain narrow enough that its requirements share a coherent center of consequence.

If a section develops materially different ownership, lifecycle, applicability, or enforcement consequences from the rest of the document, reviewers SHOULD test whether it belongs in a separate standard rather than preserving breadth for convenience.

## 8. Requirements Should State What Must Be True

Normative requirements SHOULD state the required condition, constraint, evidence, or outcome rather than prescribe an exact procedure unless the procedure itself is legitimately part of the requirement.

Prefer:

```text
A canonical document MUST preserve reviewable revision history.
```

over:

```text
Run these exact five commands before every document update.
```

when the specific commands are only one possible implementation.

Procedure MAY be normative when method choice itself carries the relevant consequence, such as a legal, safety, interoperability, contractual, or technical requirement.

## 9. Normative and Informative Material Must Remain Distinguishable

Examples, rationale, implementation notes, external platform facts, historical context, and explanatory diagrams MAY support a normative document without becoming normative requirements themselves.

Authors SHOULD make the distinction clear when a reader could reasonably mistake informative material for a requirement.

An example MUST NOT silently narrow or broaden the normative rule it illustrates.

A citation to an external source does not automatically incorporate every statement from that source as an organizational requirement.

External material becomes binding only when the adopting authority legitimately incorporates or adopts the relevant requirement within its scope.

## 10. Definitions and Terminology

A document SHOULD define terms when ordinary language is insufficiently precise for the consequence of the rule.

Definitions SHOULD be:

- necessary to interpret the document;
- internally consistent;
- no broader than required;
- stable enough to support later use;
- free of circular dependency where practical.

Do not redefine an externally governed term merely for local convenience when the document is intended to rely on the external definition.

Do not create terminology solely to make a document appear more formal.

The same term SHOULD carry the same meaning throughout one document unless a different meaning is explicitly distinguished.

## 11. External Basis and Synthesized Rules

When a standard relies on external platform constraints, published standards, laws, specifications, or other authoritative facts, it SHOULD distinguish those external facts from rules synthesized by the adopting organization.

A useful pattern is:

```text
external constraint or evidence
    establishes a fact or compatibility boundary

organizational standard decision
    chooses how the organization responds to that fact
```

Do not present a synthesized organizational convention as though an external source directly mandates it when the source does not.

Do not make a citation claim more than the cited source supports.

Where an external fact is load-bearing and reasonably likely to change, the document SHOULD identify the source clearly enough for later verification.

## 12. Examples and Counterexamples

Examples SHOULD demonstrate the intended rule without becoming the rule's only definition.

Counterexamples MAY be used to show prohibited or misleading patterns.

Examples SHOULD be chosen to clarify the durable principle rather than overfit the standard to the organization, platform, industry, or implementation that happened to motivate it.

An example drawn from one domain SHOULD NOT imply that the standard applies only to that domain unless the scope says so.

## 13. Exceptions

A standard SHOULD state whether exceptions are possible when that question materially affects interpretation.

Where exceptions are permitted, the document SHOULD identify at least one of:

- the conditions that make an exception legitimate;
- the authority that may approve an exception;
- the evidence or reasoning that should accompany the exception;
- the mechanism by which the exception remains visible.

A `SHOULD` does not require a ceremonial exception workflow every time a justified departure occurs unless the consequence warrants one.

A `MUST` SHOULD NOT contain an implied unwritten exception. If a legitimate exception exists, either state the exception or recalibrate the requirement.

Temporary exceptions MUST NOT silently become permanent changes to the standard.

## 14. Cross-Document Boundaries

A standard SHOULD reference a neighboring standard when the reader needs that relationship to apply the boundary correctly.

Cross-references SHOULD clarify ownership of the question rather than duplicate the neighboring document's requirements.

For example:

```text
one standard decides whether a separate repository is justified
another standard decides how a justified repository is named
```

Do not copy a neighboring standard's normative content merely to make the local document feel self-contained when a stable reference is sufficient.

## 15. Change Discipline

When concrete evidence demonstrates that an authoring rule is wrong, incomplete, or materially miscalibrated, the rule SHOULD be changed rather than silently bypassed.

The change itself SHOULD follow the organization's normal canonical-artifact change process.

For project-repository contexts, the `project-repository-model` template defines a general pattern in which an issue or proposal tracks the work while the canonical document carries the settled outcome.

This standard does not create a separate standards-revision workflow merely for authoring corrections.

The reasoning behind a material rule change SHOULD be retained where forgetting it would create a realistic risk of repeating the same mistake, but the current standard itself SHOULD remain focused on the rule that now governs rather than becoming a chronological changelog.

## 16. Anti-Patterns

Avoid:

- using `MUST` because strict language sounds professional rather than because the consequence is non-negotiable;
- weakening a requirement solely because a concrete case is inconvenient;
- leaving legitimate exceptions unwritten while treating them as common practice;
- treating repeated precedent as automatic authority to strengthen a rule;
- treating repeated friction as automatic authority to weaken a rule;
- mixing normative and informative language so readers cannot tell what governs;
- presenting external facts as organizational mandates they do not actually impose;
- using examples as hidden requirements;
- prescribing procedure when only an outcome or condition needs to be governed;
- broadening one standard until it annexes neighboring subjects;
- duplicating another standard's requirements instead of defining a clear boundary;
- silently working around a canonical rule without reviewing whether the rule or the case is wrong.

## 17. Basis and External References

This standard combines established drafting practices with organization-neutral authoring decisions.

The external sources inform the authoring model; they do not automatically become organizational authority merely because they are cited.

### BCP 14

RFC 2119 and RFC 8174 define widely used uppercase normative keywords such as `MUST`, `SHOULD`, and `MAY`. RFC 8174 clarifies that the special meanings apply when the keywords appear in uppercase.

Sources:

- https://www.rfc-editor.org/rfc/rfc2119.html
- https://www.rfc-editor.org/rfc/rfc8174.html

### ISO drafting guidance

ISO drafting guidance emphasizes that standards should be clear, precise, unambiguous, and terminologically consistent. ISO uses its own verbal-form system, including `shall`, `should`, `may`, and `can`.

This template adopts BCP 14-style uppercase keywords instead of reproducing ISO's verbal-form system, while retaining the general clarity and precision discipline.

Sources:

- https://www.iso.org/drafting-standards.html
- https://www.iso.org/ISO-house-style.html

### Synthesized conventions

The following are authoring decisions in this template rather than claims that the external sources prescribe them exactly:

- the document-type distinctions used here;
- the A/B/C calibration test for rule friction;
- the requirement that normative strength follow protected consequence;
- the rule against silent promotion or demotion through precedent or friction;
- the separation of external evidence from synthesized organizational rules;
- the boundary discipline for splitting neighboring standards;
- the cross-reference and change-discipline model.

## 18. Default Standard

Unless concrete organizational requirements demonstrate otherwise:

> **Use a document type whose register matches the normative role the document actually performs.**
>
> **Use explicit normative strength where readers need to distinguish requirements, strong recommendations, and permissions.**
>
> **Calibrate `MUST`, `SHOULD`, and `MAY` according to the consequence the rule protects against, not according to stylistic preference.**
>
> **Do not silently strengthen rules through precedent or weaken them through friction.**
>
> **When a concrete case conflicts with a rule, determine deliberately whether the rule is correctly protective, materially miscalibrated, or legitimately excepted.**
>
> **State required conditions and outcomes rather than exact procedures unless the procedure itself is legitimately normative.**
>
> **Keep normative requirements distinguishable from examples, rationale, implementation notes, and external evidence.**
>
> **Keep standards scoped around coherent consequences and split neighboring subjects when their ownership, lifecycle, applicability, or enforcement meaning materially differs.**
>
> **Distinguish external facts from organizational rules synthesized in response to those facts.**
>
> **Revise a miscalibrated canonical rule through the normal document-change path rather than silently working around it.**
