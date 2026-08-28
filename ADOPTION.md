# Adopting Templates from This Repository

## Purpose

This document describes how to adopt a template specifically from `jamesreimer/standards-templates` while preserving the source relationship without giving this repository continuing authority over the adopted result.

For the general reusable policy governing organizational adoption, authority, provenance, and independent lifecycle, see the [`standards-adoption-model`](templates/standards-adoption-model/) template.

## Source material

Reusable source documents are stored at:

```text
templates/<template-id>/standard.md
```

The adjacent template `README.md` describes the subject, adoption considerations, and important boundaries.

## Independent adoption

Templates in this repository may be adopted independently. References to sibling templates generally describe conceptual boundaries, related subjects, or optional companions. A sibling reference does not by itself require the adopting organization to adopt that sibling standard.

If a future template genuinely depends on another adopted standard, that dependency should be stated explicitly rather than inferred from an ordinary cross-reference.

## Illustrative relationship information

The YAML-shaped examples below illustrate semantic information an adopting organization may choose to record. They do not define a required schema, companion YAML file, Markdown frontmatter format, or mandatory storage mechanism. An adopting organization may represent the same facts in frontmatter, a prose header, repository relationship metadata, a records system, or another legitimate organization-owned control mechanism.

## Recommended relationship

The recommended downstream relationship is:

```yaml
relationship: adapted-copy
sync_policy: manual-review
```

Use this relationship even when the initial adopted copy is byte-for-byte identical to the source. Exact equality at adoption time does not transfer control of the downstream artifact's future authority or lifecycle to this repository.

## Recommended provenance

Record enough provenance to identify exactly what source material was reviewed. For this repository, that normally means:

```yaml
relationship: adapted-copy
sync_policy: manual-review
source_repo: https://github.com/jamesreimer/standards-templates
source_path: templates/<template-id>/standard.md
source_revision: <full-source-commit-sha>
```

Use the full commit SHA as the immutable source revision. A content digest or organizational adoption record may also be retained when useful.

The provenance record identifies the source used for adoption. It does not make this repository authoritative for the organization, and it does not by itself determine intellectual-property ownership or replace applicable license obligations.

## Later source changes

A later change in this repository is a candidate for downstream review, not an automatic downstream update.

The adopting organization may accept, adapt, reject, or defer the change through its own legitimate process. Moving, renaming, or deleting a source template does not by itself alter the authority or lifecycle of an already adopted organizational artifact.

## General policy

Organizations that want a reusable policy for deliberate adoption, canonical governance, provenance, source-managed exceptions, and cross-organizational independence should review and adopt the [`standards-adoption-model`](templates/standards-adoption-model/) template.
