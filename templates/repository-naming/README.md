# Repository Naming Template

Stable template ID: `repository-naming`

Human-facing title:

> **Repository Naming Standard**

## Purpose

This template provides a baseline for naming version-control repositories across organizations and types of work.

It is intended for organizations that want repository names to remain clear, durable, portable, and appropriately scoped without encoding temporary status, speculative topology, or unnecessary organizational repetition.

The reusable template is [`standard.md`](standard.md).

## Adoption

Adopt this template into an organization-owned standards repository through deliberate review.

The adopted copy becomes the organization's canonical repository-naming standard for the scope assigned to it. This repository remains provenance and a possible source of future improvements, not continuing authority over the adopted standard.

See the repository-level [ADOPTION.md](../../ADOPTION.md) for the recommended adoption and relationship model.

## Subject-specific adoption review

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. For this standard specifically, also determine:

- whether an existing repository-naming policy, canonical registry, host rule, contractual requirement, or externally governed identity already controls repository names;
- whether the template's terms for durable responsibility, namespace, topology, lifecycle, and repository families conflict with established terminology or ownership;
- which system of record owns repository identity and whether protected, public, transferred, mirrored, or externally consumed repositories have stronger naming authority;
- whether automation, package references, hosted actions, deployment configuration, documentation, redirects, integrations, or other consumers depend on existing names;
- whether the standard adds durable naming value or would cause only cosmetic churn;
- what migration, compatibility review, redirect handling, and validation would be required for any later rename proposal.

Adopting this naming standard does not authorize any repository rename. Each proposed rename requires its own authority, migration, consumer-impact, and validation decision.

## Applicability

This template is not limited to software-development repositories.

It may be applied to repositories containing, for example:

- software and automation;
- media-production material;
- research;
- standards and policies;
- publishing or editorial work;
- infrastructure configuration;
- documentation;
- archival or operational material.

Organization-specific vocabulary may be added during adoption when a domain genuinely requires it.

## Boundary with neighboring standards

This template answers:

> **What should a repository be named once the repository has a legitimate responsibility?**

It does not answer:

> **Should this responsibility have its own repository?**

Repository creation and separation criteria are outside this naming template's scope. The sibling [`project-repository-model`](../project-repository-model/) template determines project repository responsibility and when repository separation is justified.

This template also does not govern file/directory naming, branch naming, product naming, or other neighboring naming subjects merely because they are related.

The repository-level [NAMING.md](../../NAMING.md) governs stable template IDs and human-facing titles **inside this template library**. It is not the repository-naming standard itself.

## Likely organization-specific review points

Before adoption, an organization should consider whether it needs to adapt:

- maximum repository-name length;
- permitted character set;
- organization-specific reserved names;
- public naming/trademark review requirements;
- conventions for repository families;
- domain-specific responsibility qualifiers;
- rename approval or migration requirements;
- host-specific constraints beyond the portability baseline.

These are adoption considerations, not requirements to customize the template. If the defaults fit, the organization may adopt them unchanged.

## External basis

The standard's compatibility baseline is informed by current GitHub and Azure DevOps repository naming constraints and Windows reserved-name behavior. Those sources establish technical facts; the semantic naming principles in the template are synthesized standards decisions rather than claims that a particular platform mandates them.
