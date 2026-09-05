# Operational Execution Contract Template

Stable template ID: `operational-execution-contract`

Human-facing title:

> **Operational Execution Contract Standard**

## Purpose

This template defines a proportionate contract model for consequential execution.

Its central question is:

> **Before consequential work proceeds, what is authorized, what is protected, how will success be verified, and where must execution stop?**

It is intended for organizations that perform infrastructure, deployment, data, security, administrative, publishing, migration, recovery, delegated, automated, or other work where execution can materially affect protected systems or state.

## Source document

The reusable template is [`standard.md`](standard.md).

## Adoption

Use the repository-level [ADOPTION.md](../../ADOPTION.md) review before adopting this template.

The standard is intentionally consequence-based. It does not require every repository edit or routine action to receive a formal execution contract.

An organization should adopt it where explicit execution boundaries close a real operational gap rather than merely adding another approval artifact.

## Subject-specific adoption review

Before adoption, determine:

- which kinds of work actually create material operational consequence;
- which existing approval, change, deployment, administrative, recovery, or automation systems already define execution authority;
- whether planning, repository implementation, publication, and live operation are currently distinguished clearly enough;
- which protected systems or state are at realistic risk from scope creep;
- how the organization currently handles rollback, recovery, validation, and emergency action;
- whether delegated tools or automation can exercise authority beyond what humans intended;
- whether existing workflows already allow harmless mechanical implementation corrections without unnecessary escalation;
- whether adoption would duplicate or conflict with stronger domain-specific operational controls.

Do not adopt this template merely to make ordinary low-risk work more formal.

## Likely organization-specific review points

An adopting organization may need to adapt:

- which work categories require an Execution Contract;
- how execution scope is expressed;
- who may authorize higher-consequence execution;
- how approval is recorded;
- which Protected Boundaries commonly matter;
- what validation is required for different operational classes;
- what counts as a Mechanical Correction;
- when rollback or recovery planning is required;
- how emergency authority is handled;
- how delegated or automated execution requests review when scope is uncertain;
- how long execution-contract evidence should be retained.

These are adaptation choices, not requirements to create a new work-management or approval platform.

## Conceptual boundary

This template governs:

- execution authority;
- Execution Scope;
- Protected Boundaries;
- Completion Boundaries;
- validation expectations;
- Material Scope Expansion;
- proportionate rollback or recovery expectations;
- bounded delegated and automated execution.

It does not define:

- repository topology;
- standards adoption;
- shared-asset provenance;
- publication/deployment lifecycle states;
- general task management;
- incident-response procedure;
- one approval hierarchy;
- one deployment or automation platform.

For repository responsibility, see [`project-repository-model`](../project-repository-model/).

For standards adoption and organizational authority, see [`standards-adoption-model`](../standards-adoption-model/).

For source provenance and immutable consumed identity, see [`shared-asset-provenance`](../shared-asset-provenance/).

The standard may be implemented through existing work items, plans, change records, deployment systems, operational tools, or other durable mechanisms. It does not require a dedicated execution-contract platform.
