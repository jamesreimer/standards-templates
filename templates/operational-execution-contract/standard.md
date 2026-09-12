# Operational Execution Contract Standard

## 1. Purpose

This standard defines how consequential operational work is bounded by an explicit execution contract before a person, agent, automation, process, or tool exercises authority that could materially affect systems, data, services, published state, shared infrastructure, or other protected operational interests.

Its purpose is to prevent execution authority from expanding through momentum, convenience, nearby work, prior discussion, implementation progress, or successful intermediate validation.

The central principle is:

```text
planning, implementation, publication, and live operation
are distinct execution boundaries
```

Crossing one boundary does not by itself authorize crossing the next.

## 2. Scope

This standard applies when work can materially affect, for example:

- live or production systems;
- shared infrastructure or services;
- runtime configuration;
- production or protected data;
- secrets or credentials;
- external provider state;
- deployment or activation behavior;
- backup, restore, migration, or recovery state;
- consequential administrative state;
- published or externally consumed artifacts;
- security-sensitive configuration;
- irreversible or difficult-to-reverse operations;
- other systems where unintended execution could create material operational harm.

This standard does not require an execution contract for every repository edit, document change, formatting correction, local experiment, or low-consequence administrative action.

The adopting organization SHOULD apply execution-contract overhead in proportion to the consequence of the work.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, RFC 2119 and RFC 8174. Lowercase forms retain their ordinary English meaning.

## 3. Definitions

**Execution Contract**

A reviewed statement that defines the authorized objective, execution scope, protected boundaries, completion or stop conditions, required validation, and other controls necessary to perform consequential work safely.

**Execution Scope**

The actions, systems, environments, artifacts, or state that the execution is authorized to affect.

**Protected Boundary**

A system, file, path, service, data set, secret, artifact, environment, resource, behavior, or other interest that the execution is not authorized to modify.

**Completion Boundary**

The condition at which the authorized work is complete and execution must stop unless further authority is granted.

**Authority Boundary**

A distinction between classes of action for which one authorization does not automatically grant another.

Examples may include planning, repository implementation, publication, deployment, live operation, destructive mutation, or recovery action.

**Executor**

A person, agent, automation, tool, process, or service performing work under an Execution Contract.

**Material Scope Expansion**

A change that would authorize materially different systems, actions, consequences, protected interests, or execution authority beyond the reviewed contract.

**Mechanical Correction**

A non-substantive adjustment needed to make already authorized work conform to ordinary repository, formatting, linting, serialization, packaging, or tooling requirements without changing the intended outcome, normative meaning, protected boundaries, or authorized consequence.

**Established Path**

A previously validated operating pattern, interface, identity, tool, or workflow for the relevant capability and authority boundary. Prior validation is evidence of suitability, not continuing authorization or proof that current conditions are unchanged.

## 4. When an Execution Contract Is Required

Consequential work within the scope of this standard MUST have an Execution Contract before execution crosses into the consequential activity.

The contract MAY be brief when the work is narrow and low in complexity.

The amount of process SHOULD be proportionate to:

- consequence of error;
- reversibility;
- breadth of affected state;
- sensitivity of affected data or systems;
- difficulty of validating success;
- difficulty of recovering from failure;
- degree of delegated or automated execution.

A contract MUST NOT be required merely because work is technically complex if the execution itself cannot materially affect a protected operational interest.

Likewise, apparently simple work MUST NOT bypass an Execution Contract when its consequences are material.

## 5. Minimum Contract Content

An Execution Contract MUST define:

- the intended objective;
- the authorized Execution Scope;
- the Completion Boundary;
- required validation;
- any Protected Boundaries whose accidental modification would create a material risk.

The contract SHOULD also define, where relevant:

- explicit non-goals;
- acceptance criteria;
- material operational risks;
- rollback or recovery expectations;
- prerequisites;
- required evidence;
- sequencing constraints;
- dependencies on another authorized action.

A contract does not need empty sections for concepts that are genuinely irrelevant to the work.

The form MAY vary according to the adopting organization's systems and practices.

## 6. Authority Must Be Explicit

Execution authority MUST be explicit enough that an Executor can determine what actions are permitted and where execution must stop.

Authority to perform one class of work MUST NOT be treated as authority for materially different or higher-consequence work.

For example:

- permission to plan does not itself authorize implementation;
- permission to implement repository changes does not itself authorize publication;
- publication does not itself authorize deployment or live activation;
- permission to deploy one approved artifact does not itself authorize unrelated live changes;
- validation success does not itself broaden execution authority.

The adopting organization MAY combine several authority boundaries into one authorization when doing so is deliberate and unambiguous.

This standard does not require a particular number of approval stages.

## 7. Executor Authority

An Executor MUST operate within the approved Execution Contract.

Authority to execute MUST NOT by itself grant authority to:

- redefine the objective;
- materially broaden Execution Scope;
- remove or weaken Protected Boundaries;
- redefine success after execution begins;
- bypass required validation;
- authorize a higher-consequence action not already within scope.

The same person MAY define, approve, and execute work where the adopting organization's authority model permits it.

This standard requires clarity of authority, not ceremonial separation of people or roles.

Delegated agents, automation, tools, or services MAY perform authorized work.

Delegation does not expand the authority granted by the Execution Contract.

## 8. Scope Expansion and Escalation

If execution reveals that a Material Scope Expansion is required, the Executor MUST stop before crossing the existing authority boundary.

The Execution Contract MUST then be updated, replaced, or otherwise explicitly extended through the organization's appropriate authority path before the broader work proceeds.

Discovery of additional nearby work does not itself constitute authorization.

A Material Scope Expansion includes, for example:

- modifying an additional production system;
- changing protected data not included in the original scope;
- moving from repository implementation into live activation;
- adding a destructive operation;
- weakening a protected boundary;
- changing the intended operational outcome.

### 8.1 Established Paths and Evidence-Driven Escalation

When selecting an execution path, the Executor MUST consider relevant Established Paths and whether they can satisfy the current Execution Contract. Among paths that satisfy its authority, safety, validation, and completion requirements, the Executor SHOULD prefer the least disruptive validated path.

Failure or limitation of one actor, identity, session, interface, tool, or workflow MUST NOT by itself authorize a more privileged, invasive, exceptional, bypass, recovery, or emergency execution path.

Before selecting such a path, the Executor MUST:

- consider whether another Established Path, including an alternative interface or identity, can satisfy the contract within existing authority;
- identify affirmative evidence that the relevant Established Paths are unavailable, insufficient, or no longer authorized under current conditions;
- establish that the proposed path is authorized for its actual scope and consequence, obtaining any required Material Scope Expansion before crossing the existing boundary.

Escalation MUST be justified by evidence about the available paths and the contract's requirements, rather than by the fact that an attempt failed. An available alternative identity or credential does not itself confer permission to use it. Prior success does not override changed authority or current validation evidence.

Consideration does not require trying every possible path, repeating an unsafe or known ineffective attempt, or creating a registry of execution paths. The evidence SHOULD be reviewable in the existing execution record in proportion to the consequence. Section 16 governs urgent action when delay would create greater material harm; path assessment MUST NOT be treated as a requirement to exhaust alternatives before action permitted by that exception.

### 8.2 Separately Discovered Defects

Discovery of a separate architectural, implementation, validation, packaging, deployment, control, or similar defect MUST NOT retroactively redefine the original authorized objective or silently broaden its Execution Scope. The defect's remediation MUST be distinguished from the original work when assessing authority, scope, and consequence.

If remediation requires materially different scope, consequence, mutation of a Protected Boundary, or execution authority, it MUST be treated as separately authorized work or explicit Material Scope Expansion under this section before that remediation proceeds. The importance or complexity of the surrounding system does not itself change the authority required for the original action.

When a separate defect blocks safe execution under the current contract, the affected execution MUST pause before violating its required conditions or Protected Boundaries. Such a pause does not change the substantive identity of the original work or authorize correction of the defect. Work that remains safe and authorized MAY continue within the contract's limits.

A correction already within authorized scope MAY proceed under the existing contract; a Mechanical Correction remains governed by Section 9. These distinctions do not require a separate work item for every discovery. Architectural classification and control-design review remain owned by Architectural Reasoning; this section determines the execution consequences of the finding.

## 9. Mechanical Corrections

A Mechanical Correction MAY be made within an already authorized implementation scope without separate escalation when it:

- does not materially change the intended outcome;
- does not alter normative or approved substantive meaning;
- does not cross a Protected Boundary;
- does not introduce a materially different operational consequence;
- remains within the ordinary implementation responsibility already authorized.

Examples may include:

- removing trailing whitespace;
- applying required formatting;
- correcting lint-safe syntax;
- regenerating a deterministic structure listing;
- normalizing line endings;
- making semantics-preserving packaging or serialization adjustments required by established tooling.

A change that appears mechanical but alters behavior, meaning, authority, security posture, data handling, or operational consequence is not a Mechanical Correction.

This section exists to preserve proportionate execution control. It MUST NOT be used to disguise substantive scope expansion as cleanup.

## 10. Protected Boundaries

An Execution Contract MUST identify Protected Boundaries when realistic adjacent actions could create material harm outside the intended scope.

Protected Boundaries SHOULD be expressed as denial rules where practical.

Examples may include:

- production data not involved in the change;
- secrets or credentials;
- unrelated provider resources;
- backup archives;
- customer-controlled content;
- protected configuration;
- unrelated runtime services;
- externally owned resources;
- state that must survive rollback or recovery.

An Executor MUST NOT cross a Protected Boundary unless separately authorized.

If the intended objective cannot be completed without crossing one, execution MUST stop before doing so.

### 10.1 Defective Controls and Continued Protection

Identifying a control as defective MUST NOT itself authorize bypassing, disabling, or weakening it, or accepting state that violates the condition it protects.

Where a control enforces a required acceptance or safety condition or a Protected Boundary, execution MUST preserve that protection while the defect is unresolved. If the affected action cannot proceed with that protection enforced, it MUST remain stopped until an authorized correction or authorized equivalent protection is in place and validated against the protected condition. Authorization to prepare a correction, or a proposal for substitute protection, does not establish that protection is already effective.

This is a fail-closed requirement for the protected action or state: a defective enforcement mechanism does not make otherwise prohibited state acceptable. It does not require shutting down unrelated safe activity, retaining a particular defective mechanism when equivalent protection is effective, or treating every advisory check as a mandatory gate.

Changes to execution authority or Protected Boundaries remain subject to Sections 8 and 10. An alternative validation disposition under Section 11 MUST NOT be used to silently waive the protection required here. The bounded emergency exception in Section 16 continues to apply when its conditions are met; defect discovery alone does not establish an emergency or expand that exception.

## 11. Validation

An Execution Contract MUST define validation proportionate to the authorized consequence.

Validation MAY include:

- repository checks;
- tests;
- dry-run or preview behavior;
- configuration validation;
- artifact verification;
- health checks;
- runtime smoke tests;
- integrity checks;
- recovery verification;
- human review;
- other evidence appropriate to the operation.

Validation success demonstrates only what the validation can actually establish.

It does not grant additional authority.

A validation failure that defeats a required acceptance or safety condition MUST block completion unless the contract or legitimate authority explicitly provides another disposition.

## 12. Completion and Stop Conditions

Every Execution Contract MUST define a Completion Boundary.

The Executor MUST stop when that boundary is reached unless additional work is already authorized.

Completion MUST NOT be claimed before the required conditions are satisfied.

A Completion Boundary MAY be, for example:

- a decision recorded;
- a repository candidate prepared;
- a change merged;
- an artifact published;
- a deployment completed;
- a service verified;
- a recovery rehearsal completed;
- a bounded administrative mutation confirmed.

This standard does not prescribe which boundary is appropriate for a particular workflow.

## 13. Rollback and Recovery

An Execution Contract MUST define rollback or recovery expectations when the work can create material state that is difficult to reverse, destructive, externally consequential, or operationally risky.

Where rollback is simple and obvious, a concise expectation MAY be sufficient.

Where no practical rollback exists, the contract MUST state that fact and SHOULD define any compensating recovery or containment strategy appropriate to the consequence.

The standard MUST NOT require fictional rollback plans for operations that cannot genuinely be reversed.

## 14. Publication, Deployment, and Live Operation

Repository implementation, merge, publication, validation, release preparation, or identification of a candidate artifact MUST NOT by themselves authorize live operational execution.

Where live operational action requires an artifact, version, release, image, package, configuration, or other input, the organization SHOULD identify that input with enough precision to prevent unintended substitution.

The appropriate identity mechanism is governed by the nature of the object and any applicable provenance standard.

This standard does not define publication or deployment lifecycle states.

It defines the authority required to perform the operational action.

## 15. Delegated and Automated Execution

Delegated or automated execution MUST remain bounded by the same Execution Contract that governs equivalent human execution.

Automation MUST NOT infer expanded authority from:

- successful prior runs;
- available credentials;
- nearby accessible systems;
- tool capability;
- repository state;
- publication state;
- previous conversations;
- implied workflow momentum.

Where an automated Executor cannot determine whether an action remains within scope, it SHOULD stop or request review rather than assume broader authority.

The adopting organization MAY define more specific automation authority where needed.

## 16. Emergency Actions

Emergency action MAY proceed without a complete pre-action Execution Contract when delay would create greater material harm than acting.

This exception MUST be limited to the scope reasonably necessary to stabilize, contain, recover, or preserve the affected system or interest.

Protected Boundaries continue to apply during emergency action except to the minimum extent that crossing one is itself necessary to stabilize, contain, recover, or preserve the affected system or interest.

An emergency action MUST NOT use the exception to broaden execution beyond what the emergency reasonably requires.

After the emergency action, the organization SHOULD retain enough information to determine:

- what action was taken;
- why pre-action review was impractical;
- what authority was exercised;
- what material state was affected;
- what validation or recovery occurred;
- what follow-up remains.

This standard does not require a universal incident-reporting format.

## 17. Evidence and Reviewability

Execution Contracts SHOULD be retained in a durable, reviewable location appropriate to the work.

The contract MAY exist in:

- a work item;
- implementation plan;
- change record;
- repository document;
- change request;
- deployment record;
- controlled operational system;
- another mechanism suited to the organization.

An ephemeral conversation MUST NOT be the only record of consequential execution authority when later review of that authority would materially matter.

The record need not become a permanent compliance artifact merely because an Execution Contract existed.

Retention SHOULD be proportionate to the consequence and the organization's legitimate records needs.

## 18. Boundaries with Related Standards

This standard governs authorized execution scope, protected boundaries, validation expectations, and completion or stop conditions for consequential work.

It also governs selection among established authorized execution paths, evidence for exceptional escalation, the scope consequences of separately discovered defects, and continued protection while a control is defective.

[`architectural-reasoning`](../architectural-reasoning/standard.md) owns system modeling, proportional architecture, control-design review, final-state reasoning, and architectural dependency impact. OEC applies execution authority to the accepted model without duplicating that design responsibility. This reference clarifies ownership and does not require adopting the sibling template.

It does not determine:

- whether work belongs in one repository or several;
- whether reusable standards become organizational authority;
- how shared assets establish provenance or immutable consumed identity;
- the complete lifecycle of publication or deployment artifacts;
- general work-management or task-continuity rules;
- incident-response procedure;
- organization-specific approval hierarchy.

A related standard may determine what artifact is valid, published, authoritative, or ready.

This standard determines whether execution is authorized to act on it.

## 19. Anti-Patterns

Avoid:

- treating implementation progress as authority to continue into live operation;
- assuming that successful validation expands scope;
- requiring heavyweight execution contracts for trivial work with no material consequence;
- allowing consequential work to proceed with only implied authority;
- using fixed role names where clear authority is sufficient;
- treating an available credential as permission;
- redefining success after execution begins to make an incomplete result appear complete;
- turning every nearby discovery into authorized additional work;
- requiring fictional rollback where recovery is the real control;
- stopping for harmless Mechanical Corrections that remain inside already authorized implementation scope;
- disguising substantive changes as Mechanical Corrections;
- making an agent or automation-specific execution model when the same boundary applies to human execution.

## 20. Default Standard

Unless concrete organizational requirements demonstrate otherwise:

> **Use an explicit Execution Contract for work whose execution can create material operational consequence.**
>
> **Define what may be changed, what must remain protected, how success will be validated, and where execution must stop.**
>
> **Do not let planning, implementation, publication, validation, or available capability silently expand execution authority.**
>
> **Require explicit review before Material Scope Expansion crosses the existing authority boundary.**
>
> **Allow harmless Mechanical Corrections inside already authorized implementation scope when they do not change meaning, consequence, or protected boundaries.**
>
> **Use rollback or recovery expectations where the consequence warrants them rather than as ceremonial fields.**
>
> **Keep delegated and automated execution bounded by the same authority limits that govern human execution.**
>
> **Apply execution-control overhead in proportion to the consequence it protects against.**
