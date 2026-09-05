# Shared Asset Provenance Template

Stable template ID: `shared-asset-provenance`

Human-facing title:

> **Shared Asset Provenance Standard**

## Purpose

This template defines how an organization can govern provenance, maintenance meaning, and exact consumed state when shared material crosses repository, package, artifact, generation, installation, publication, adaptation, or similar boundaries.

Its central question is:

> **When a consumer relies on externally sourced governed material, how does it prove where the material came from, which immutable state it consumed, and that the content actually used corresponds to that state?**

The template is intended for organizations that use shared tooling, copied or adapted assets, internal packages, generated material, schemas, published contracts, artifact bundles, installed tooling, or other source/consumer relationships where incorrect provenance or ambiguous consumed state could affect a governed result.

## Source document

The reusable template is [`standard.md`](standard.md).

## Adoption

Adopt this template through the organization's normal standards-adoption process.

This template does not make `standards-templates`, another repository, package publisher, registry, or source system authoritative for the adopting organization merely because provenance is retained.

See repository-level [ADOPTION.md](../../ADOPTION.md) for the universal review applicable to templates from this repository.

## Subject-specific adoption review

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first.

For this standard specifically, also determine:

- which cross-boundary relationships materially affect governed decisions or maintenance;
- which relationships are Authoritative Consumption and which are only impact, discovery, or maintenance information;
- which Source Identities are competent to supply each governed asset, package, contract, or artifact;
- what Immutable Consumed Identity mechanism is appropriate for each consumed object type;
- how the organization will verify that content actually used corresponds to the declared source and immutable state;
- whether existing lockfiles, package metadata, artifact registries, release records, attestations, signatures, provenance systems, or relationship manifests already provide required evidence;
- which local copies are exact, adapted, generated, installed, bootstrap-owned, contract-based, or otherwise intentionally distinct;
- where ownership intentionally transfers to the consumer;
- whether any current automation assumes that all copies or dependencies follow the same update model;
- whether local working-state changes can silently alter material represented as immutable authoritative input;
- whether adoption would duplicate or conflict with existing source-management, software-supply-chain, package, release, artifact, or governance controls.

Do not replace an existing competent provenance or artifact-control system merely to conform to an example representation from this template.

## Likely organization-specific review points

An adopting organization may need to adapt:

- terminology for source and consumer relationships;
- local relationship classifications;
- which relationships require durable records;
- what provenance or immutable-identity systems are authoritative for each object type;
- whether exact copies are checked automatically or manually;
- how adapted copies are surfaced for review;
- how bootstrap ownership transfer is represented;
- what generator identity or configuration must be retained for generated material;
- which package, artifact, schema, image, or release identities count as immutable;
- what evidence must be retained and for how long;
- where relationship records live;
- which automation may verify or synchronize relationships;
- what equivalent controls are acceptable when the default verification mechanism does not fit.

These are adaptation choices, not requirements to create a new manifest schema or tooling platform.

If existing organization-owned systems already satisfy the standard's outcomes, they may be retained.

## Conceptual boundary

This template governs:

- shared-asset relationship meaning;
- source provenance;
- source-versus-local authority distinction;
- Immutable Consumed Identity;
- correspondence between declared identity and content actually consumed;
- maintenance distinctions between exact, adapted, generated, installed, bootstrap-owned, contractual, and impact-only relationships.

It does not determine:

- whether a separate repository should exist;
- how repositories should be named;
- whether externally sourced standards become organizational authority;
- publication or deployment lifecycle;
- live operational execution authority;
- exact package-manager or version-control behavior;
- one required Relationship Record;
- one required provenance or attestation system.

For repository-responsibility decisions, see [`project-repository-model`](../project-repository-model/).

For adoption, canonical organizational authority, provenance of adopted standards, and independent downstream lifecycle, see [`standards-adoption-model`](../standards-adoption-model/).

Organizations may implement this standard using existing mechanisms such as version-control revisions, lockfiles, package resolution records, release manifests, checksums, content or image digests, signatures, attestations, generated-output records, relationship metadata, or ordinary controlled documentation.

Those mechanisms are examples, not a required implementation set.

A conforming adoption does not need to create new metadata merely because another organization uses it.
