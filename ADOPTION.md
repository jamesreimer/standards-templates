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

## Adoption review

The following review is informative operational guidance for every proposed adoption from this repository. It does not replace the candidate template's normative content or the adopting organization's legitimate approval process.

Applicability alone does not justify adoption. A template should not be adopted merely because it is generally sound, convenient to copy, or useful as a test. Adoption should add durable value within a deliberately assigned scope.

Before creating or changing an adopted artifact:

1. **Define the scope and adoption authority.** State what the proposed artifact would govern, what it would not govern, and which organization-controlled role or process may make the adoption decision.
2. **Inventory existing authority.** Identify current standards, policies, contracts, specifications, repository rules, canonical documents, external requirements, and established systems that already govern or constrain the proposed scope. Identify the systems of record and the owners of that authority.
3. **Compare the source requirements individually.** For each requirement, determine whether existing authority already provides the same outcome, uses conflicting terminology or ownership, imposes a stronger rule, or would be weakened or accidentally superseded by the candidate.
4. **Classify each difference.** Mark the candidate requirement as `accept`, `adapt`, `reject`, or `not applicable`, and retain enough reasoning to make material conflicts and departures reviewable.
5. **Test for durable value.** Determine whether adoption closes a real gap or improves clarity, consistency, or protection. Reject or defer an adoption that merely duplicates sufficient authority or adds disproportionate process, metadata, migration, or normative churn.
6. **Choose the canonical destination and resolve precedence.** Identify where the adopted result would be authoritative. Where authority overlaps, decide which artifact takes precedence and whether the source will be integrated, superseded, subordinated, or kept within a distinct boundary. Do not reclassify an existing canonical artifact without an authority and migration decision.
7. **Record provenance and lifecycle relationship.** Identify the immutable source revision reviewed and record whether the downstream artifact is independently governed or legitimately source-managed. For the normal independently adopted relationship, later upstream changes require downstream review.
8. **Identify protected effects.** Check protected or externally governed artifacts, consumers, integrations, links, automation, validation, permissions, delivery paths, and other systems that could be affected by the adopted rule or a related migration.
9. **Use a reviewable and reversible change path.** Prepare the proposal through the organization's normal review mechanism, define relevant validation, and preserve a practical way to withdraw or revise the proposal before it becomes authoritative. Plan staged migration or rollback where adoption changes existing behavior or artifacts.
10. **Make an explicit decision.** Record `adopt`, `adapt`, `reject`, or `defer`, together with the scope, decision authority, material overlap disposition, and any required migration or follow-up.
11. **Define later-source-change review.** Identify how a later upstream change may be surfaced and reviewed. Re-run the relevant comparison and decision steps; do not allow the upstream change to mutate the downstream artifact automatically.

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
source_template_edition: N.M # Optional human-facing label
```

The optional template edition is human-facing and does not satisfy an immutable-identity requirement, including `standards-adoption-model` §6. Exact SHA/path remains binding provenance. Prefer adopting from a repository release or a commit on `main`'s first-parent history, rather than an intermediate PR commit.

Use the full commit SHA as the immutable source revision. A content digest or organizational adoption record may also be retained when useful.

The provenance record identifies the source used for adoption. It does not make this repository authoritative for the organization, and it does not by itself determine intellectual-property ownership or replace applicable license obligations.

## Later source changes

A later change in this repository is a candidate for downstream review, not an automatic downstream update.

The adopting organization may accept, adapt, reject, or defer the change through its own legitimate process. Moving, renaming, or deleting a source template does not by itself alter the authority or lifecycle of an already adopted organizational artifact.

### Checking current upstream status

Open `templates/<id>/` and compare the recorded template edition with the current README:

- Same edition: no edition-tracked upstream `standard.md` change.
- Same edition number, higher editorial update number: editorial upstream changes.
- Higher edition number: meaning or citable identity changed, requiring substantive downstream review. An explicit edition correction may instead correct the classification of earlier content; consult the release notes and correction PR.

Use the exact diff to determine what changed. After fetching current upstream history, for an unchanged path:

```sh
git diff <source_revision> origin/main -- templates/<id>/standard.md
```

A newer upstream edition is a review candidate, not an automatic update. After a rename or move, release notes identify the current path; compare the old path at the recorded SHA with the current path at the target SHA. Historical `source_path` remains correct at its recorded SHA and must not be rewritten to the new path.

### Adoptions made before editions

The one-time equivalence mapping is:

- Adoption from `v1.0.0`, or a later pre-edition `main` state whose relevant `standard.md` is identical to `v1.0.0`: equivalent to `1.0`.
- Earlier adoption: equivalent to `1.0` only if the recorded source content equals the `v1.0.0` file.
- Otherwise: pre-`1.0`, requiring later-source-change review.

Compare source bytes at the recorded SHA/path with the corresponding file at `v1.0.0` (`76382fb84cb9d43340c508145b83c2c1dbdff8c4`). For a path unchanged between those revisions:

```sh
git diff --exit-code <source_revision> v1.0.0 -- templates/<id>/standard.md
```

An unreachable or otherwise unverifiable source SHA maps conservatively to pre-`1.0`, unless retained source bytes or a retained content digest establish equality with the `v1.0.0` content. This mapping supplements historical provenance; it does not rewrite it or reconstruct historical editions.

## General policy

Organizations that want a reusable policy for deliberate adoption, canonical governance, provenance, source-managed exceptions, and cross-organizational independence should review and adopt the [`standards-adoption-model`](templates/standards-adoption-model/) template.
