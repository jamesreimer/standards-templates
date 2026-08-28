# Maintaining the Template Library

## Purpose

This document describes how this repository is maintained. It records the review path for new templates and material changes without establishing an external contribution program.

## Maintenance principles

Maintain the smallest coherent library justified by concrete use.

Reusable documents may acknowledge domain-specific implementations or sibling standards, but do not present one domain's answer as the universal answer.

Repository work state belongs in Issues. Settled repository guidance belongs in the appropriate canonical document. Reusable normative requirements belong in a template only after the subject and its boundary have been justified.

## Evaluating a proposed template

Before creating a template:

1. identify the concrete problem and the consequence a normative document would protect against;
2. determine whether the problem belongs in an existing template or repository-level guidance;
3. test whether the proposed subject has a coherent center of consequence;
4. check whether the proposal would split one subject by noun or annex a neighboring subject;
5. confirm that current use has earned a reusable template rather than an Issue, example, or deferred question.

Do not create a template merely because an external framework has a standard on the subject or because a mature project commonly has one.

## Naming and authoring

For a justified template:

1. choose the stable template ID and human-facing title using [NAMING.md](NAMING.md);
2. author and calibrate the normative document against [`standards-authoring`](templates/standards-authoring/);
3. distinguish external facts from conventions synthesized by the template;
4. preserve boundaries with sibling templates and use cross-references without duplicating their requirements;
5. keep the adjacent template `README.md` focused on purpose, adoption considerations, and boundaries;
6. add the completed template to [CATALOG.md](CATALOG.md) only when it exists.

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

1. review requirement strength using the A/B/C calibration test in `standards-authoring`;
2. confirm that examples remain informative and do not silently change the rule;
3. check documents for unintended domain-specific assumptions or universalized handoffs;
4. update `README.md`, `ADOPTION.md`, `NAMING.md`, or `CATALOG.md` only when their repository-level responsibilities are affected;
5. verify internal links and re-check affected external claims;
6. inspect the complete diff for unintended scope, authority, naming, licensing, or lifecycle changes.

## External contributions

This document does not by itself invite or define an external contribution program. If the repository later accepts external contributions under a documented process, a separate `CONTRIBUTING.md` may define that public collaboration relationship and refer here for maintenance standards.
