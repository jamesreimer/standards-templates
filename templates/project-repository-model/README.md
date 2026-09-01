# Project Repository Model Template

Stable template ID: `project-repository-model`

Human-facing title:

> **Project Repository Responsibility Standard**

## Purpose

This template defines a default responsibility model for durable project artifacts, canonical project documentation, issues or equivalent work items, dynamic planning state, exploratory reasoning, and multi-repository topology.

Its central question is:

> **Which project system legitimately owns which kind of information, artifact, or work state?**

It is intended for organizations that want a consistent rule across project domains for where durable project truth lives and what planning and collaboration tools are responsible for.

## Source document

The reusable template is [`standard.md`](standard.md).

## Adoption

Adopt this template into an organization-owned standards repository through deliberate review.

The adopted copy becomes the organization's canonical standard for whatever scope the organization assigns to it. This repository remains provenance and a possible source of future improvements, not continuing authority over the adopted standard.

See the repository-level [ADOPTION.md](../../ADOPTION.md) for the recommended relationship model.

## Subject-specific adoption review

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. For this standard specifically, also determine:

- whether existing project governance already assigns ownership among canonical artifacts, repositories, issues or work items, planning systems, and exploratory spaces;
- whether terms such as `canonical artifact`, `system of record`, `issue`, or `planning system` conflict with established terminology or ownership;
- which systems are authoritative for durable project truth and dynamic planning state, and whether adoption would create a competing source of truth;
- whether protected repositories, locked or externally governed artifacts, permission boundaries, integrations, reports, or consumers depend on the existing responsibility model;
- whether repository separation, artifact movement, or planning-state migration would be required and how those effects would be reviewed and validated;
- whether adoption resolves real ownership ambiguity or only relabels established systems and creates normative churn.

Do not reclassify an existing canonical artifact or system of record without an explicit authority and migration decision.

## Likely organization-specific review points

Before adoption, an organization should consider whether it needs to adapt:

- the system designated to own dynamic planning state, which may be an issue tracker, project-management product, repository document, or another proportionate mechanism;
- repository naming or ownership conventions;
- requirements for durable decision records;
- review or approval requirements for canonical document changes;
- conditions that justify repository separation;
- documentation locations or repository layout conventions.

These are adoption considerations, not requirements to customize the template. If the default language already fits, the organization may adopt it unchanged.

## Conceptual boundary

This template governs **where durable project artifacts and dynamic work state belong, and when repository separation is justified**.

It does not define:

- organizational standards-adoption and ownership semantics;
- domain-specific artifact structure;
- branching strategy;
- release, publication, distribution, or deployment process;
- project workflow;
- company-specific security or compliance requirements.

For the distinct problem of adopting external or reusable standards into organization-owned authority, see [`standards-adoption-model`](../standards-adoption-model/).
