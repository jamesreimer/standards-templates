# Template Adoption Model

## Purpose

This document defines how a template from this repository should become an organization-owned standard without transferring ongoing authority to the template source.

## Core rule

> **Adoption transfers responsibility for the adopted artifact, not authority back to the template source.**

A template in this repository is reusable source material. It becomes authoritative for an organization only through that organization's own legitimate adoption process and within the scope the organization assigns to it.

## Adoption lifecycle

```text
source template
    ↓ review
organization adoption decision
    ↓
organization-owned canonical standard
    ↓
independent organizational lifecycle
```

After adoption:

- the organization owns the canonical standard;
- the organization controls its scope and lifecycle;
- the organization may modify it independently;
- upstream template changes do not automatically alter the organization-owned standard;
- the upstream relationship may be retained for provenance and future comparison.

## Default relationship type

The default relationship for adopted templates is conceptually:

```text
relationship: adapted-copy
sync_policy: manual-review
```

This remains the preferred relationship even when the initial adopted copy is byte-for-byte identical to the source template.

The reason is semantic rather than technical: the downstream organization owns its future lifecycle. Exact equality at adoption time must not imply automatic external control later.

## Recommended provenance

Where an organization maintains repository relationship metadata, an adopted standard should retain enough provenance to identify the source template used for adoption.

A downstream relationship may record information equivalent to:

```yaml
relationship: adapted-copy
sync_policy: manual-review
source_repo: jamesreimer/standards-templates
source_path: templates/<template-id>/standard.md
source_revision: <adopted-source-commit>
```

A content digest may also be recorded when useful, but this repository does not require a particular downstream relationship schema.

## Upstream changes

A later change to a source template is a **candidate for downstream review**, not a downstream change.

The healthy path is:

```text
upstream template changes
    ↓
relationship or comparison reports difference
    ↓
downstream organization reviews
    ↓
accept / adapt / reject
    ↓
organization updates its own canonical standard if approved
```

Never:

```text
upstream template changes
    ↓
automatic rewrite of organization-owned standards
```

## Divergence

Divergence is normal.

An organization may:

- adopt the template unchanged;
- adapt wording to organizational terminology;
- add organization-specific requirements;
- remove provisions that do not apply;
- decline later upstream changes;
- independently evolve the standard over time.

The upstream source remains useful provenance even when the downstream artifact no longer matches it exactly.

## Authority boundary

This repository does not determine whether an adopted standard is active, superseded, withdrawn, or otherwise authoritative inside an organization.

Those judgments belong to the adopting organization and whatever governance process legitimately owns that organization's standards.

## Cross-organization reuse

Two organizations may adopt the same source template while producing different standards.

Neither organization's copy governs the other, and neither should rely on this personal repository as its ongoing authoritative source.

Reusable origin may be shared.

Organizational authority and lifecycle are not.
