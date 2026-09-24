# Publication and Release Integrity Template

Stable template ID: `publication-release-integrity`

Template edition: `1.0`

Human-facing title:

> **Publication and Release Integrity Standard**

## Purpose

This template defines publisher-side integrity across and after publication: correspondence to the authorized source state, identity-to-state binding, fixed identities and moving references, verification, corrections, withdrawal, and partial or premature publication.

It applies to documents, software, data, media, and other identifiable deliverables without prescribing a publication platform or versioning scheme. A release is one form of publication, not a required distribution model.

## Source document

The reusable template is [`standard.md`](standard.md).

## Adoption

Use the repository-level [ADOPTION.md](../../ADOPTION.md) review before adopting this template into an organization-controlled standards source.

Adoption assigns organizational authority only within the adopter's chosen scope. This repository remains provenance and a possible source of later improvements, not continuing authority over the adopted result.

The publication-integrity rules are synthesized standards decisions. BCP 14 supplies the normative-keyword interpretation, not the publication model.

## Subject-specific adoption review

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. For this subject, also determine:

- which existing publication, release, controlled-document, artifact, or records controls already govern identity stability, corrections, withdrawal, and completion claims, and whether their authority or terminology conflicts with this template;
- which systems own publication authorization, source provenance, authoritative publication surfaces, and downstream adoption or activation, so that integration preserves each responsibility;
- whether existing identities have declared movement semantics or are reasonably relied on as identifying one state, and whether current correction or deletion practices would reassign established fixed identities;
- whether distribution and component identities, release membership, and consumption-relevant metadata have meanings that current consumers or automation rely on;
- whether legal, security, safety, privacy, contractual, or records constraints affect content availability, status disclosure, or evidence retention;
- what migration is needed to preserve established identity meanings and consumer reliance when introducing these controls, without retroactively reclassifying identities;
- whether current verification observes the resulting authoritative state, including eventual consistency, unobservable results, and state left by failed or premature publication;
- what validation would demonstrate that existing publication mechanisms preserve correspondence, identity reservation, truthful completion claims, and independent downstream authority.

These questions assess adoption safety and overlap. Adoption does not itself authorize publication, identity migration, withdrawal, or changes to downstream state.

## Likely organization-specific review points

An adopting organization may need to adapt:

- terminology and scope for its artifacts, releases, identity layers, and publication surfaces;
- how authorized source states and publication completion are identified;
- the identity and correspondence mechanisms appropriate to each artifact type;
- where verification evidence is retained and for how long;
- how verification accommodates propagation delays or limited observability;
- how correction, successor, withdrawal, and advisory information is communicated;
- how existing systems represent release membership and component relationships.

These are adaptation choices, not requirements to create a new publication ledger, metadata schema, tool, or approval workflow. Existing systems may satisfy the standard's outcomes.

## Conceptual boundary

This template owns publisher-side integrity across and after the publication transition. It preserves the following neighboring responsibilities:

- [`operational-execution-contract`](../operational-execution-contract/standard.md) owns authority to perform publication or other consequential execution;
- [`shared-asset-provenance`](../shared-asset-provenance/standard.md) owns source identity, derivation, provenance, and general correspondence and authoritative-consumption semantics where applicable;
- [`standards-adoption-model`](../standards-adoption-model/standard.md) owns deliberate organizational adoption and the independent authority and lifecycle of adopted normative material;
- deployment and activation remain separately governed lifecycle decisions.

These references clarify ownership without requiring adoption of the sibling templates. Publication evidence can support another governed determination without conferring that determination or its authority.

The template does not prescribe Git, a release service, Semantic Versioning, template editions, cryptographic mechanisms, permanent ledgers, or mandatory separation of human roles.
