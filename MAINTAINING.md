# Maintaining the Template Library

## Purpose

This document describes how this repository is maintained. It records the maintainer review path for new templates and material changes. [CONTRIBUTING.md](CONTRIBUTING.md) defines the contributor path and refers here for maintenance standards.

## Maintenance principles

Maintain the smallest coherent library that can meet its current responsibilities without speculative growth.

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
2. run the unit tests and repository validator documented in [README.md](README.md);
3. review requirement strength using the A/B/C calibration test in `standards-authoring`;
4. confirm that examples remain informative and do not silently change the rule;
5. check documents for unintended domain-specific assumptions or universalized handoffs;
6. update `README.md`, `ADOPTION.md`, `NAMING.md`, or `CATALOG.md` only when their repository-level responsibilities are affected;
7. verify internal links and manually re-check affected external claims;
8. inspect the complete diff for unintended scope, authority, naming, licensing, or lifecycle changes.

## Contribution relationship

[CONTRIBUTING.md](CONTRIBUTING.md) describes how to prepare new templates and revisions for review. Maintainers apply the principles and review criteria in this document when evaluating those contributions.
