# Maintaining the Template Library

## Purpose

This document describes how this repository is maintained. It records the maintainer review path for new templates and material changes. [CONTRIBUTING.md](CONTRIBUTING.md) defines the contributor path and refers here for maintenance standards.

## Maintenance principles

Maintain a coherent library whose growth is justified by demonstrated need rather than constrained by size or driven by speculative expansion.

Apply the repository-wide [addition-decision model](README.md#design-principle) when considering templates, repository structure, metadata, validation, automation, taxonomy, or related machinery.

Reusable documents may acknowledge domain-specific implementations or sibling standards, but do not present one domain's answer as the universal answer.

Repository work state belongs in Issues. Settled repository guidance belongs in the appropriate canonical document. Reusable normative requirements belong in a template only after the subject and its boundary have been justified.

## Evaluating a proposed template

Before creating a template:

1. identify the concrete problem and the consequence a normative document would protect against;
2. determine whether the problem belongs in an existing template or repository-level guidance;
3. test whether the proposed subject has a coherent center of consequence;
4. check whether the proposal would split one subject by noun or annex a neighboring subject;
5. confirm that the need is concrete or imminent, confidence is high, and a reusable template is a proportionate response rather than an Issue, example, named trigger, or deferred question.

Do not create a template merely because an external framework has a standard on the subject, a mature project commonly has one, or prior practice makes expansion convenient.

## Naming and authoring

For a justified template:

1. choose the stable template ID and human-facing title using [NAMING.md](NAMING.md);
2. author and calibrate the normative document against [`standards-authoring`](templates/standards-authoring/);
3. distinguish external facts from conventions synthesized by the template;
4. preserve boundaries with sibling templates and use cross-references without duplicating their requirements;
5. keep the adjacent template `README.md` focused on purpose, adoption considerations, and boundaries;
6. retain a bounded subject-specific adoption review in the adjacent `README.md` that defers to root [ADOPTION.md](ADOPTION.md) for the universal review and adds only authority, conflict, migration, and validation questions peculiar to the subject;
7. keep that subject-specific review distinct from likely organization-specific review points, which identify legitimate adaptation choices rather than pre-adoption safety checks;
8. initialize its README template edition at `1.0`, following the edition rules below;
9. add the completed template to [CATALOG.md](CATALOG.md) only when it exists.

## External claims

For each load-bearing external claim:

1. prefer a current primary or authoritative source;
2. verify that the source establishes the fact actually stated;
3. distinguish the external fact from the template's standards decision;
4. avoid presenting platform-specific behavior as universal;
5. re-check facts that are likely to change when materially revising the template.

Do not add citations merely for appearance or copy external text when a precise paraphrase and source link are sufficient.

## Review before merging

Before merging a material change:

1. regenerate `repository-structure.txt` when repository paths changed intentionally;
2. run the authoritative pre-commit composition, including the independent standards-domain tests and validator, documented in [CONTRIBUTING.md](CONTRIBUTING.md#validation);
3. when a change adds or alters validation behavior, confirm the check is owned by the appropriate layer: generic repository mechanics belong upstream in `repo-template`, standards-domain checks remain local, and explicitly temporary generic preservation controls retain the ownership and retirement obligations recorded in PROVENANCE. [CONTRIBUTING.md](CONTRIBUTING.md) states the ownership rule and [PROVENANCE.md](PROVENANCE.md) covers adoption verification;
4. review requirement strength using the A/B/C calibration test in `standards-authoring`;
5. confirm that examples remain informative and do not silently change the rule;
6. check documents for unintended domain-specific assumptions or unnecessary workflow prescriptions;
7. update `README.md`, `ADOPTION.md`, `NAMING.md`, or `CATALOG.md` only when their repository-level responsibilities are affected;
8. verify internal links and manually re-check affected external claims;
9. review each proposed template edition transition against the content diff, including correction evidence and rename lineage;
10. confirm squash-only repository merge settings and the default-branch ruleset remain in force;
11. inspect the complete diff for unintended scope, authority, naming, licensing, or lifecycle changes.

## Repository releases

A repository release labels a coherent published library state. Stable template IDs identify subjects; the exact source commit and template path remain the binding adoption provenance described in [ADOPTION.md](ADOPTION.md). A release label does not replace that provenance, imply a template edition, or govern the authority, versions, or lifecycle of independently adopted downstream standards.

### Version meaning

Use `vMAJOR.MINOR.PATCH` release tags with these repository-level meanings:

| Increment | Meaning |
| --- | --- |
| **MAJOR** | An incompatible change to the published library contract, such as removing or renaming a published template or materially changing the adoption/source-path contract. |
| **MINOR** | A library expansion or any template edition-number increase, including an edition correction or citable-identity change; adding a template also requires at least MINOR. |
| **PATCH** | Editorial-update-only template changes, README-only, tooling, maintenance, or other changes that alter neither normative meaning nor the published library contract. |

The published library contract means template identity, template paths, and the adoption/source-path contract. Normative content changes are MINOR even when they can change downstream conformance or adoption conclusions. The release-note `normative` classification signals the need for downstream review; the repository version increment does not substitute for that classification. Use the highest applicable increment across the release's changes.

### Tag preparation and publication

For each future release:

1. identify the full commit SHA of the exact merged revision intended for release, and verify it against current canonical `main` and the merge/review evidence; when the merge method produces a different commit from the reviewed candidate, verify that the merged commit and reviewed candidate have identical tree object IDs before release;
2. confirm that applicable repository validation in [CONTRIBUTING.md](CONTRIBUTING.md#validation) passed for that revision; validation of a different revision or altered working tree is insufficient;
3. select an unused release version and prepare the release notes described below;
4. create an annotated Git tag targeting that exact commit;
5. before pushing, verify that the tag ref identifies a tag object, inspect its annotation, and confirm that its target resolves to the intended full commit SHA;
6. publish only the verified release tag through the authorized release path.

For example, after the target and validation checks, replace the placeholder with the verified full SHA:

```sh
git tag -a v1.2.0 <verified-full-commit-sha> -m "Release v1.2.0"
git cat-file -t refs/tags/v1.2.0
git show refs/tags/v1.2.0
git rev-parse 'refs/tags/v1.2.0^{commit}'
```

The object-type check must report `tag`, and the resolved commit must match the verified release target. These commands illustrate the checks; they do not confer publication authority.

Published release tags are immutable: do not move, delete, or recreate them to identify different content. Correct a published release through a new release version. Preserving published tags provides durable reachability for their revisions; this does not prohibit legitimate repository-history maintenance that preserves that boundary.

The Git tag identifies the release. Optional GitHub Release metadata may present notes and other release information for that tag; it does not replace the tag or its target verification.

The existing published `v1.0.0` and `v1.0.1` tags are lightweight tags and must remain unchanged. The annotated-tag and release-note requirements apply prospectively beginning with the next release; do not rewrite the existing tags to satisfy them retroactively.

### Release notes

Provide release notes for every future release, whether or not GitHub Release metadata is used. For every changed template, identify its stable ID and compare the README editions at the previous release and the release candidate. The reviewed edition transition is the source of truth for semantic classification; do not independently reclassify the content at release time.

| Transition or change | Release-note entry |
| --- | --- |
| Edition number increased | Start → end editions, `normative`, for example `1.0 → 3.0`. |
| Only editorial update number increased | Start → end editions, `editorial`, for example `2.0 → 2.2`. |
| README-only | `README-only (edition unchanged)`. |
| Added template | `added at 1.0`. |
| Removed template | Last edition and last path. |
| Renamed/moved template | Previous/current ID and path, with the carried edition. |
| Edition-only correction | Start → end editions, `edition correction, content unchanged`, identifying the earlier misclassified transition. |

When multiple transitions occur between releases, report the start and end editions. Consult intermediate history for corrections and structural changes; a correction must not be presented as new normative content in its correction PR. Combine rename/move information with any content transitions in the same release. Unchanged templates need not be listed. Initializing the existing library at `1.0` labels unchanged baseline content; it does not introduce normative changes.

Use the highest applicable repository release class: an edition-number increase (including a correction) or added template requires at least MINOR; an identity/path-contract removal, rename, or move requires MAJOR; editorial-update-only, README-only, and other non-normative/non-library-contract changes require PATCH. Repository release numbering remains separate and never implies a template edition.

Notes support later-source-change review under [ADOPTION.md](ADOPTION.md); they do not authorize downstream updates. Exact SHA/path remains binding provenance. Do not create per-template tags, changelogs, or digest tables for this purpose.

## Template editions

Every template README contains exactly one declaration as the next metadata paragraph after its stable template ID, separated by blank lines:

```text
Stable template ID: `example-template`

Template edition: `1.0`
```

The whole `N.M` is the **template edition**; `N` is the **edition number** and `M` is the **editorial update number**, not a revision. Use decimal integers with `N >= 1`, `M >= 0`, and no leading zeros. The edition covers only the adjacent `standard.md`. Do not add it to `standard.md` or [CATALOG.md](CATALOG.md), or treat it as a repository release version or downstream standard version.

### Content transitions

Increment the edition number when a `standard.md` change could cause a reasonable reader to reach a different requirement, applicability determination, conformance conclusion, adoption comparison, or citable identity. When uncertain, increment the edition number. This includes:

- tightening, loosening, adding, or removing requirements;
- changing BCP 14 strength, including correcting lowercase or misspelled keywords when normative force changes;
- changing scope, definitions, or dependencies;
- materially changing the external authority or source relied on;
- changing examples in a way that affects interpretation;
- adding, removing, renumbering, or changing requirement IDs;
- changing section numbers where sections are the citable anchors.

Increment only the editorial update number for content changes that preserve meaning, applicability, conformance/adoption conclusions, and citable identity. Examples include citation URL/title corrections with unchanged fact and authority, true typo/wording corrections with unchanged defined terms and normative strength, and restructuring that preserves meaning and every citable ID or section number.

Only exact next steps are allowed:

```text
N.M → N.(M+1)
N.M → (N+1).0
```

A mixed change uses only the edition-number increase, resetting the editorial update number to zero. README-only, catalog, tooling, test, and other non-`standard.md` changes do not change the edition, except for the bounded correction below. Semantic classification remains a human review judgment; validation checks the transition, not its meaning.

### Cadence and initialization

Every authoritative `standard.md` state merged to `main` receives its edition in the same PR. Authoritative states are on `main`'s first-parent history. Do not batch edition changes at release time: adoptions can occur between releases.

An edition label never identifies more than one `standard.md` content state within its template lineage.

The 17 templates existing at migration initialize at `1.0`, corresponding to their byte-identical `v1.0.0` content at `76382fb84cb9d43340c508145b83c2c1dbdff8c4`. Bootstrap validation requires base and candidate content to equal that immutable baseline. Earlier history stays unassigned. New templates start at `1.0`.

Standards Templates permits squash merging only, both in repository settings and the protected default-branch ruleset. Each reviewed PR therefore produces one authoritative state and at most one transition per affected template. Rebase merging can introduce intermediate unlabeled states; merge commits expose branch states adopters might mistake for authoritative revisions. The loss of individual PR commits on `main` is accepted. This repository-specific edition requirement is not a universal merge-method preference.

### Renames and moves

The edition follows the template lineage. Automatic carry-over requires the moved template's own `standard.md` to remain byte-identical. Pair removed and added paths by exact content identity, never Git similarity scoring. Ambiguous pairings require review rather than arbitrary selection. Other templates referencing the moved template may change in the same PR, with their own appropriate transitions.

A move requiring changes inside the moved `standard.md` is outside automatic carry-over and requires ordinary edition treatment and appropriate review. The validator fails closed for unmatched simultaneous removals/additions rather than silently treating a changed move as a new lineage. Such a restructure needs reviewed lineage handling before proceeding.

Never reuse a removed template ID for a new lineage. A legitimate return must continue its existing lineage or receive separate architectural review; the validator rejects historical ID reuse for that review. Historical `source_path` remains correct at its recorded SHA. Identity/path-contract changes still require a repository MAJOR release.

### Edition corrections

An edition-only upward correction is allowed only when `standard.md` is unchanged, the current editorial update number is at least `1`, and the target is exactly `(N+1).0`. The PR must explicitly identify the earlier transition that was misclassified. No other edition-only mutation is permitted.

Place the correction declaration on its own line in a commit message body as described in [CONTRIBUTING.md](CONTRIBUTING.md#edition-validation). Reviewers assess the claimed misclassification; automation verifies its historical editorial transition and the numerical/content bounds. The PR body may explain the correction but is not machine-authoritative evidence. Retain the declaration in the resulting squash commit message so push validation has the same evidence; do not remove it during manual squash-message editing. Release notes identify unchanged-content corrections explicitly.

## Contribution relationship

[CONTRIBUTING.md](CONTRIBUTING.md) describes how to prepare new templates and revisions for review. Maintainers apply the principles and review criteria in this document when evaluating those contributions.
