# Architectural Reasoning Standard

## 1. Purpose

This standard defines architectural reasoning that prevents work from consistently implementing an incorrect model of authority, responsibility, system boundaries, or intended final state.

It governs how the model is established and reconsidered, including whether the selected architecture remains proportionate across the affected system and its dependents.

## 2. Scope

This standard applies to decisions that establish or materially change system responsibility, authority interpretation, system identity, design or control complexity, durable state, or dependencies. It applies equally to human, delegated, and automated reasoning across domains.

It does not require a fresh architectural assessment for every routine action under an unchanged, applicable model. Reasoning depth and retained evidence SHOULD be proportionate to the consequence and uncertainty of the decision.

This standard does not grant execution authority, select operational execution paths, define escalation or stop rules, establish standards-adoption authority, prescribe repository topology, or govern shared-asset propagation and publication lifecycle.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html). Lowercase forms retain their ordinary English meaning.

## 3. Definitions

**Normative Authority**: Applicable, active requirements that define what must be true within their legitimately assigned scope.

**Implementation Authority**: An applicable system specification, contract, workflow, or other legitimate source that defines how requirements are realized within its assigned scope.

**Explanatory Context**: History, examples, rationale, or observations that help explain a system without defining its current governing requirements or implementation.

**Architectural Unit**: The responsibility being evaluated, such as a system, subsystem, capability, workflow, governance surface, runtime behavior, migration, validation mechanism, product feature, platform concern, or artifact. These examples are not mandatory classification labels.

**Transition Mechanism**: A means of reaching an intended durable state, such as migration tooling, temporary compatibility behavior, or bootstrap scaffolding, whose presence does not itself make it part of that durable state.

**Justified Complexity**: Design or control complexity beyond the least complex design that satisfies identified requirements, supported by one or more of the tests in Section 8.

## 4. Applicable Authority

Before choosing an implementation model, the reasoning MUST identify the relevant authority, its scope, and the relationships that determine which requirements and implementation decisions govern.

Sources relied on in the decision MUST be distinguished as Normative Authority, Implementation Authority, or Explanatory Context according to their actual role. A document can contain more than one role; its filename, location, or format does not establish authority.

The most specific active authority MUST govern within its legitimately assigned scope, subject to the applicable authority hierarchy. Specificity alone MUST NOT be treated as permission to override a governing requirement or invent delegated authority.

Material conflicts or uncertainty about authority MUST remain explicit until resolved through the applicable authority model; the architectural conclusion MUST NOT present an unresolved conflict as settled authority.

The authority relationships MAY be expressed in prose or existing review records. A formal graph or a new registry is not required.

## 5. Architectural Unit and System Identity

The reasoning MUST identify the Architectural Unit and its responsibility before choosing which artifact or repository should change. Ownership MUST follow the system responsibility, rather than the location of the symptom or the tool that exposed it.

When execution or analysis exposes a separate architectural, structural, validation, control, implementation, deployment, or similar defect with its own responsibility or consequence, the reasoning MUST model that defect as a separate Architectural Unit rather than silently absorb it into the original unit.

When determining whether work refines an existing system or establishes a new one, the reasoning MUST compare the relevant:

- responsibility;
- authority;
- lifecycle;
- validation path;
- runtime or operating behavior;
- meaning of the intended final state.

A new system MUST be justified by a material distinction in at least one of these characteristics. When no such distinction exists, the work MUST be modeled as a refinement of the existing system. A material distinction permits consideration of separation; it does not automatically require another system or repository.

## 6. Boundary Reclassification

When evidence changes the ownership, authority, or system boundary, the reasoning MUST reconsider the model rather than merely redirecting the same plan to a different artifact.

Reclassification MUST re-evaluate the responsible system, applicable authority, validation path, architectural completion conditions, affected adjacent and dependent systems, and assumptions that relied on the prior classification.

A plan based on a superseded boundary MUST NOT be represented as a valid implementation model without that re-evaluation. Whether execution pauses, changes scope, or requires additional authority is governed by the applicable execution contract.

## 7. Failure Evidence and Historical Precedent

A failure or limitation of one actor, identity, session, interface, tool, or workflow MUST NOT by itself establish that the underlying system capability is unavailable.

Before reclassifying the capability, the reasoning MUST distinguish evidence about the failed execution context from evidence about the system itself. Relevant previously validated behavior MUST be considered when assessing what the system can do under the applicable conditions.

Historical precedent MUST be treated as evidence rather than permanent authority. Changed requirements, changed system state, or direct validation MAY supersede it; prior success alone does not establish current validity.

These rules govern the capability model. Selection of an authorized execution path and justification for escalation are separate execution questions.

## 8. Proportional Architecture

The design MUST use the least complex architecture that fully satisfies identified requirements for safety, correctness, recoverability, maintainability, and reasonably anticipated evolution, unless additional complexity meets the justification tests below.

The evaluation MUST account for the Architectural Unit, its dependents, and the system as a whole. It MUST consider value, risk reduction, durability, anticipated evolution, operational burden, and lifecycle cost rather than judging complexity by the immediate change's size alone.

Additional complexity MAY be adopted only when supported by concrete reasoning that it:

- addresses a present risk or known structural weakness;
- materially improves security, correctness, recoverability, or maintainability;
- reduces total lifecycle or operational cost;
- prevents a reasonably anticipated failure;
- enables a reasonably anticipated capability whose later introduction would otherwise require disruptive rework; or
- materially improves the architecture of the system as a whole.

Speculative reuse, historical convenience, or ease of completing the immediate task MUST NOT substitute for such justification. A broader refactor, preventive control, or structural correction that meets these tests MUST NOT be rejected solely because a smaller local change is possible.

Repeated defects, exceptions, synchronization failures, or control failures across related units SHOULD prompt review at the enclosing system, workflow, or capability when isolated corrections could hide a shared structural cause. Several reasonable local fixes do not establish that their combined architecture is proportionate.

Reasoning SHOULD retain a clear connection to the capability, responsibility, or objective that caused the work. Enabling, governance, validation, transition, and control mechanisms SHOULD be evaluated by their contribution to that objective and the system's durable responsibilities. When those mechanisms substantially outweigh the capability they enable, reviewers SHOULD reconsider the decomposition while accounting for risks that justify substantial safeguards.

### 8.1 Controls and Safeguards

A control, safeguard, or validation mechanism MUST itself be evaluated as an Architectural Unit under this section.

A mechanism that repeatedly rejects valid governed state, imposes disproportionate operator burden, or no longer represents the architecture it protects MUST be treated as a candidate for architectural review. Additional layers MUST NOT substitute for evaluating that defect.

An architectural correction MUST preserve or improve protection against the governed risk. Identifying a defective control does not establish that accepting the state it was intended to reject is safe. This design review supplies no authority to bypass or disable protection; the applicable execution controls govern intervention while a correction is pending.

## 9. Final State and Transition Mechanisms

The intended durable state MUST be distinguished from Transition Mechanisms. A migration tool, compatibility layer, fallback, import process, temporary workflow, review packet, or bootstrap mechanism MUST NOT become part of the durable model merely because it was used to reach it. Retention as a permanent capability requires a basis in active authority and identified requirements.

Before recording a final-state conclusion, the reasoning MUST identify whether the work creates, replaces, refines, invalidates, or implements an already-decided state.

When current authority supersedes earlier assumptions, incompatible assumptions MUST be retired from the current model. Historical material MAY explain earlier behavior but MUST NOT remain an alternative current truth unless active authority preserves it.

When a pattern is replaced, the intended final state MUST exclude the replaced pattern unless active authority preserves it for a defined compatibility, migration, rollback, or phased-adoption need. A completed replacement MUST NOT be claimed while incompatible superseded state remains outside that retained scope.

Retained transitional behavior SHOULD have reviewable conditions for retirement. Historical convenience, uncertainty, or speculative future reuse MUST NOT be treated as a compatibility commitment.

These requirements define the intended state and the truth of architectural completion claims. They do not authorize removal, prescribe rollout sequencing, or define how copies are propagated.

## 10. Cross-System and Dependency Impact

When authority, responsibility, behavior, or intended state changes, the reasoning MUST identify affected dependent and adjacent systems and determine which earlier assumptions cease to be valid elsewhere.

Impact analysis MUST follow responsibility and dependency relationships, including relationships not represented by file references. It MUST consider relevant effects on:

- information or data ownership;
- runtime or operating responsibility;
- delivery or deployment assumptions;
- rollback and recovery assumptions;
- validation requirements;
- documentation and recorded decisions;
- consuming systems and artifacts;
- fallback, compatibility, and migration behavior.

When an architectural decision introduces, changes, or removes a required dependency, the reasoning MUST identify the capability or responsibility supplied by the target, the consumers that rely on it, and the consequences if that target is absent, incompatible, or changed. A valid reference alone does not establish that the dependency meets the architectural need.

This analysis determines the required relationship and its consequences. Shared-source identity, immutable consumed state, content correspondence, and target propagation or resolution mechanics belong to shared-asset provenance where applicable. This standard does not define a general link checker or publication process.

## 11. Architectural Completion Review

Before an implementation model is treated as settled, and before architectural completion is claimed, the review MUST establish that:

1. applicable authority and material conflicts have been identified and resolved for the conclusion being claimed;
2. the Architectural Unit and responsibility-based owner are clear;
3. existing-system or new-system identity is justified where that decision arises;
4. changed boundaries and the assumptions dependent on them have been reconsidered;
5. capability conclusions distinguish context-specific failure from system failure and account for relevant precedent;
6. the architecture, including controls, has been evaluated at the appropriate system scope under Section 8;
7. durable state is distinguished from transitions and superseded assumptions or patterns;
8. affected systems and required dependencies have been evaluated;
9. evidence supports the state claimed, including any retained transition or unresolved limitation.

The review MUST distinguish a settled design from an implemented and verified final state. Unresolved material assumptions MUST NOT be hidden by a completion claim.

Before architectural completion is claimed, material review findings MUST receive an explicit disposition appropriate to their consequence. A finding is material here when its loss or silent dismissal could affect architectural truthfulness, completion, responsibility, boundaries, dependencies, or later reasoning.

Classification as blocking or non-blocking describes whether a finding prevents architectural completion from proceeding; classification alone is not a disposition. A non-blocking finding MAY allow architectural completion to proceed, but MUST NOT be silently discarded merely because it is non-blocking. Dispositions MAY include correction within the current work, retention for bounded follow-up, explicit acceptance or deferral with rationale, or dismissal as not actionable or not applicable with rationale. A disposition does not replace the other completion conditions in this section.

Disposition evidence SHOULD be proportionate to the finding's consequence and MAY use existing review records. This requirement does not prescribe a universal severity taxonomy, ticketing system, separate issue for each finding, particular record format, or formal documentation for trivial stylistic observations that are not material to the architectural conclusion. Whether a finding requires execution to stop, changes authorized scope, or permits remediation remains governed by the applicable execution contract.

Evidence SHOULD be retained where losing it would materially impair later review or cause a superseded model to be treated as current. Existing design documents, change reviews, or equivalent records MAY provide that evidence. This standard does not require a separate checklist artifact or universal record format.

Architectural completion does not grant approval to execute, publish, deploy, or broaden work.

## 12. Boundaries with Related Standards

- [`operational-execution-contract`](../operational-execution-contract/standard.md) owns consequential execution authority, protected boundaries, authorized scope, and completion or stop conditions. Execution-path selection, escalation, and the execution disposition of newly discovered defects belong to that subject.
- [`shared-asset-provenance`](../shared-asset-provenance/standard.md) owns shared-material source identity, consumed state, relationship meaning, and correspondence; shared-target integrity mechanics belong there where applicable.
- [`standards-adoption-model`](../standards-adoption-model/standard.md) owns deliberate organizational adoption and the independent authority and lifecycle of adopted material.
- [`project-repository-model`](../project-repository-model/standard.md) owns repository responsibility, placement of durable artifacts and work state, and repository separation.
- [`standards-authoring`](../standards-authoring/standard.md) owns normative drafting and requirement calibration.

These references clarify ownership. They do not require adoption of the siblings or make an external source authoritative.

## 13. Basis

The architectural rules are synthesized organization-neutral standards decisions. BCP 14 supplies the normative-keyword interpretation, not the architectural model or an organizational authority hierarchy.

## 14. Default Standard

Unless concrete organizational requirements demonstrate otherwise:

> **Establish authority, responsibility, and system identity before selecting an implementation.**
>
> **Reconsider the whole model when its boundary changes, and distinguish execution-context evidence from system-capability evidence.**
>
> **Evaluate architecture and controls by their justified contribution across the system and its dependents.**
>
> **Separate durable state from transitions, retire superseded assumptions, and trace effects through responsibilities and dependencies.**
>
> **Claim only the architectural state supported by the completion review.**
