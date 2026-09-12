# Architectural Reasoning Template

Stable template ID: `architectural-reasoning`

Human-facing title:

> **Architectural Reasoning Standard**

## Purpose

This template defines a reusable model for reasoning about authority, responsibility, system identity, proportionate architecture, final state, and dependent systems before committing to an implementation model.

Its central question is:

> **What system model correctly explains the responsibility, applicable authority, intended durable result, and effects on other systems?**

It applies across technical, operational, production, research, publishing, and governance work where choosing the wrong model could produce a materially incorrect result.

## Source document

The reusable template is [`standard.md`](standard.md).

## Adoption

Use the repository-level [ADOPTION.md](../../ADOPTION.md) review before adopting this template. Adoption assigns organizational authority; this template and its source material do not supply that authority by themselves.

Reasoning and evidence can be brief for a bounded decision. The template does not require a separate architecture board, graphing tool, decision-record format, or review workflow.

## Subject-specific adoption review

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. For this standard specifically, also determine:

- whether existing architecture or design governance already defines authority classification, system ownership, proportionality, and final-state review;
- whether the authority categories or system-identity criteria conflict with existing delegated authority or responsibility assignments;
- which current plans, compatibility commitments, controls, and dependent systems rely on boundaries that adoption might cause reviewers to reconsider;
- how any changed ownership or durable-state interpretation would be reviewed and validated without silently authorizing migration, control bypass, or operational changes;
- whether existing review evidence can demonstrate the required reasoning without duplicating an adequate design-review process.

## Agent integration

Route human or automated implementation work to the adopted local artifact when substantive work will commit to an implementation model involving system identity, responsibility, authority, ownership, boundaries, proportionality, durable state, controls, or dependent-system effects. After adoption, that artifact governs within its assigned scope; the upstream `standards-templates` copy remains source material.

Adapt this optional snippet for `AGENTS.md` or an equivalent contributor/automation entry point. Replace `<local-standard-path>` with the adopted artifact's location. Neither `AGENTS.md` nor a particular agent product is required; this snippet is informative routing guidance, not independent authority.

```text
Before committing to an implementation model, read and apply the organization's adopted Architectural Reasoning Standard at <local-standard-path> to determine the applicable Architectural Unit and model. Keep reasoning proportionate; trivial mechanical edits do not require heavyweight analysis. Execution authorization remains a separate question.
```

## Likely organization-specific review points

An adopting organization may need to adapt:

- terminology for systems, capabilities, authority, and responsibility;
- how consequential architectural reasoning is retained in existing review records;
- what evidence supports reasonably anticipated evolution and lifecycle cost;
- how compatibility commitments and transition-retirement conditions are represented;
- which existing review mechanism resolves conflicting authority or revisits a defective control design.

These are adaptation choices, not a requirement to introduce new roles, metadata, or tooling.

## Conceptual boundary

This template determines the system model. It is independently adoptable; the following references identify neighboring responsibilities without requiring adoption of those templates:

- [`operational-execution-contract`](../operational-execution-contract/) governs consequential execution authority, scope, protected boundaries, and completion or stop conditions. Execution-path selection, escalation, and the authorized disposition of separately discovered defects belong to that subject.
- [`shared-asset-provenance`](../shared-asset-provenance/) governs shared-material source identity, consumed state, relationship meaning, and correspondence. Shared-target resolution and propagation mechanics belong to that subject where applicable. This template considers what depends on a target and what breaks if it changes.
- [`standards-adoption-model`](../standards-adoption-model/) governs how reusable normative material becomes organizational authority and follows an independent lifecycle.
- [`project-repository-model`](../project-repository-model/) governs repository responsibility, artifact and work-state placement, and repository separation. A distinct Architectural Unit does not by itself require a separate repository.
- [`standards-authoring`](../standards-authoring/) governs normative drafting and requirement calibration.

This template does not prescribe publication lifecycle, distribution topology, administrative mutation classes, or an organization-specific governance hierarchy.
