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
8. add the completed template to [CATALOG.md](CATALOG.md) only when it exists.

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
9. inspect the complete diff for unintended scope, authority, naming, licensing, or lifecycle changes.

## Repository releases

A repository release labels a coherent published library state. Stable template IDs identify subjects; the exact source commit and template path remain the binding adoption provenance described in [ADOPTION.md](ADOPTION.md). A release label does not replace that provenance, assign individual template versions, or govern the authority, versions, or lifecycle of independently adopted downstream standards.

### Version meaning

Use `vMAJOR.MINOR.PATCH` release tags with these repository-level meanings:

| Increment | Meaning |
| --- | --- |
| **MAJOR** | An incompatible change to the published library contract, such as removing or renaming a published template or materially changing the adoption/source-path contract. |
| **MINOR** | A backward-compatible library expansion or normative template change, including adding a template or changing normative meaning within an existing `standard.md`. |
| **PATCH** | Editorial, documentary, tooling, maintenance, or other changes that alter neither normative template meaning nor the published library contract. |

Use the highest applicable increment across the release's changes.

### Tag preparation and publication

For each future release:

1. identify the full commit SHA of the exact reviewed and merged revision being released, and verify it against current canonical `main` and the merge/review evidence;
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

Provide release notes for every future release, whether or not GitHub Release metadata is used. For every template changed since the previous release, identify its stable template ID and classify its change:

| Class | Meaning |
| --- | --- |
| `normative` | A `standard.md` change that can alter requirement meaning, scope, strength, dependency, interpretation, or a conformance/adoption conclusion. |
| `editorial` | A `standard.md` change with unchanged normative meaning, such as a typo, link, citation, or wording correction with unchanged effect. |
| `README-only` | A change to the adjacent template guidance with no `standard.md` change. |

Classify a template as `normative` if any of its changes are normative; use `editorial` only when all `standard.md` changes leave normative meaning unchanged. Unchanged templates need not be listed. Classification is a maintainer review judgment, not an inference delegated to validation. When uncertain, treat the change as normative.

Notes support later-source-change review under [ADOPTION.md](ADOPTION.md); they do not authorize downstream updates. They may include the exact release SHA or other useful provenance, without duplicating identity already supplied by the release revision and template path. Do not require per-template tags, changelogs, or digest tables solely for release classification.

### Per-template versioning

Do not maintain per-template versions or add version metadata to template READMEs, `standard.md`, or [CATALOG.md](CATALOG.md). Stable IDs, exact source revisions/paths, and repository releases serve the current identity and provenance needs, consistent with [PROVENANCE.md](PROVENANCE.md)'s distinction between a binding commit identity and a human-facing release label.

Reconsider per-template versioning only through separate architectural review of a concrete forcing function, such as independent distribution without repository revision provenance, demonstrated failure of downstream later-source-change review without a human-readable template revision label, or a cross-template dependency requiring independent revision identity that a coherent repository revision cannot express. Do not infer a template version from the repository release version.

## Contribution relationship

[CONTRIBUTING.md](CONTRIBUTING.md) describes how to prepare new templates and revisions for review. Maintainers apply the principles and review criteria in this document when evaluating those contributions.
