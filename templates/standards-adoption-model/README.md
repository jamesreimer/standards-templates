# Standards Adoption Model Template

Stable template ID: `standards-adoption-model`

Human-facing title:

> **Organizational Standards Adoption and Ownership Policy**

## Purpose

This template defines how an organization should adopt standards, policies, or other normative material from an external or reusable source without creating a continuing upstream authority dependency.

Its central question is:

> **How does reusable source material become organizational authority and then evolve under an independent organizational lifecycle?**

It is intended for organizations that want a clear rule for deliberate adoption, canonical governance, provenance, later upstream changes, and cross-organizational independence.

## Source document

The reusable template is [`standard.md`](standard.md).

## Adoption

Adopt this template into an organization-owned standards repository through deliberate review.

Once adopted, the organization's copy becomes canonical for the scope the organization assigns to it. This repository remains source provenance and a possible source of future improvements, not continuing authority over the adopted policy.

See the repository-level [ADOPTION.md](../../ADOPTION.md) for guidance specific to adopting templates from this repository.

## Subject-specific adoption review

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. For this policy specifically, also determine:

- whether existing standards governance already defines adoption authority, canonical ownership, provenance, source-managed relationships, or controlled-document lifecycle;
- whether this policy's terminology or ownership model conflicts with established governance roles, lifecycle states, or systems of record;
- whether adopting the policy would clarify a real gap or duplicate an already sufficient adoption policy;
- how any material overlap will be integrated, superseded, subordinated, or retained within distinct boundaries;
- whether standards indexes, relationship records, lifecycle tooling, validators, or other consumers would require migration or validation.

Do not reclassify an existing canonical artifact as independently adopted, source-managed, superseded, or subordinate without an explicit authority and migration decision.

## Workflow integration

Route implementation and review work to the adopted local artifact when assisting adoption, adaptation, replacement, provenance, authority-conflict resolution, or lifecycle decisions involving reusable or external normative material. After adoption, that artifact governs within its assigned scope; the upstream `standards-templates` copy remains source material.

Adapt this optional snippet for the contributor guidance used by planners, implementors, and reviewers. Replace `<local-standard-path>` with the adopted artifact's location. No particular tool or instruction filename is required; this snippet is informative routing guidance, not independent authority.

```text
Read and apply the organization's adopted Organizational Standards Adoption and Ownership Policy at <local-standard-path> before making adoption, provenance, authority, or lifecycle decisions about reusable or external normative material. Treat upstream material as a review candidate, not automatically authoritative organizational policy.
```

## Likely organization-specific review points

Before adoption, an organization should consider whether it needs to adapt:

- which organizational role or process may adopt a standard;
- how canonical standards sources are identified;
- what provenance metadata is retained;
- how upstream changes are detected or surfaced;
- what review or approval is required before adopting later upstream revisions;
- whether any standards are intentionally source-managed rather than independently governed;
- how supersession, withdrawal, or deprecation is represented in the organization's own standards lifecycle.

These are adoption considerations, not requirements to customize the template. If the default policy already fits, the organization may adopt it unchanged.

## Conceptual boundary

This template governs **standards adoption, canonical governance, provenance, and independent downstream lifecycle**.

Canonical governance means organizational responsibility for authority, scope, interpretation, and lifecycle. It does not by itself transfer copyright or other intellectual-property rights in source material.

It does not define:

- project repository topology;
- where project documentation, issues, or planning state belong;
- the content of any particular engineering standard;
- exact approval workflows;
- repository synchronization tooling;
- organization-specific permissions or legal review procedures.

For the distinct problem of assigning responsibility among project repositories, canonical artifacts, issues or equivalent work items, planning systems, and exploratory reasoning, see [`project-repository-model`](../project-repository-model/).
