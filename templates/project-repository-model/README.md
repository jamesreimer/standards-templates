# Project Repository Model Template

Stable template ID: `project-repository-model`

Human-facing title:

> **Software Project Repository, Documentation, and Work Tracking Standard**

## Purpose

This template defines a default responsibility model for software project repositories, canonical project documentation, issue tracking, project-management systems, exploratory design discussions, and multi-repository topology.

It is intended for organizations that want a consistent rule for where durable project artifacts live and what planning tools are responsible for.

## Source document

The reusable template is [`standard.md`](standard.md).

## Adoption

Adopt this template into an organization-owned standards repository through deliberate review.

The adopted copy becomes the organization's canonical standard for whatever scope the organization assigns to it. This repository remains provenance and a possible source of future improvements, not continuing authority over the adopted standard.

See the repository-level [ADOPTION.md](../../ADOPTION.md) for the recommended relationship model.

## Likely organization-specific review points

Before adoption, an organization should consider whether it needs to adapt:

- references to GitHub Projects and GitHub Issues to another work-management platform;
- repository naming or ownership conventions;
- requirements for architecture decision records;
- review or approval requirements for canonical document changes;
- conditions that justify repository separation;
- documentation locations or repository layout conventions.

These are adoption considerations, not requirements to customize the template. If the default language already fits, the organization may adopt it unchanged.

## Conceptual boundary

This template governs **where durable project artifacts and dynamic work state belong**.

It does not define:

- application architecture;
- source-code layout;
- branching strategy;
- release process;
- deployment process;
- development workflow;
- company-specific security or compliance requirements.

Those subjects may be governed separately.
