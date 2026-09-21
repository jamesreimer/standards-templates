# Filesystem Naming Template

Stable template ID: `filesystem-naming`

Human-facing title:

> **File and Directory Naming Standard**

## Purpose

This template defines organization-neutral defaults for naming files, directories, and path components so that version-controlled material remains readable, portable, automatable, and resilient across common operating systems and filesystems.

It can be adopted for software repositories, media-production repositories, research collections, standards libraries, publishing projects, operational repositories, archives, and other version-controlled work.

## Source document

The reusable template is [`standard.md`](standard.md).

## Adoption

Adopt this template into an organization-owned standards repository through deliberate review.

An adopting organization may strengthen the defaults or add domain-specific exceptions for programming languages, creative-production tooling, publishing systems, archival conventions, generated files, or other environments.

The adopted copy becomes the organization's canonical standard for the scope assigned to it. This repository remains provenance and a possible source of future improvements, not continuing authority over the adopted standard.

See the repository-level [ADOPTION.md](../../ADOPTION.md) for the recommended relationship model.

## Subject-specific adoption review

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. For this standard specifically, also determine:

- whether an existing filesystem convention, language or framework rule, external format, delivery contract, archive requirement, or tool-owned naming scheme already governs affected paths;
- whether the template's terminology, default syntax, or exception ownership conflicts with established authority;
- which system or owner is canonical for generated, externally supplied, synchronized, archival, or delivery-controlled artifacts;
- which links, imports, scripts, manifests, automation, synchronization systems, archives, delivery paths, or external consumers depend on existing names;
- whether the standard adds durable portability or clarity value or would cause only cosmetic churn;
- what migration and validation would be required across case-sensitive and case-insensitive filesystems and other affected environments.

Adopting this naming standard does not authorize any file or directory rename. Each proposed rename requires its own authority, migration, consumer-impact, and validation decision.

## Likely organization-specific review points

Before adoption, an organization should consider:

- whether non-ASCII filenames are intentionally required;
- language, framework, or tool conventions that require another case or separator style;
- conventional or deliberately established prominent root filenames such as `README.md`, `LICENSE`, `ADOPTION.md`, or `NAMING.md`, and tool-owned dotfiles;
- generated or externally supplied filenames that should remain untouched;
- whether dates, sequence numbers, or release identifiers are legitimate parts of filenames;
- stricter path-length limits imposed by target systems, storage, synchronization, or delivery tooling;
- archival or media-delivery systems with additional naming restrictions.

## Conceptual boundary

This template governs **file and directory names and path components**.

It does not define:

- repository names;
- branch or tag names;
- package or service names;
- product, project, production, or publication titles;
- template IDs inside this library.

Repository naming is governed separately by [`repository-naming`](../repository-naming/).

The repository-level [NAMING.md](../../NAMING.md) governs template IDs and human-facing titles inside `standards-templates` itself.
