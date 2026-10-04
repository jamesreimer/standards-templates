# Purpose-Specific Review Guidance

This guidance is non-normative. It helps reviewers apply Review Integrity to common review purposes. It does not create conformance requirements, require a particular review purpose, establish review authority, require independent review, prescribe a report format, or replace more specific applicable standards.

## 1. Status and purpose

The two suggested review shapes help frame questions about an existing state or a proposed change. Organizations and projects may adapt, combine, narrow, omit, or replace them. Selecting this guidance does not itself adopt Review Integrity or another standard. This document introduces no new BCP 14 requirements.

## 2. Relationship to Review Integrity and specific standards

The current normative reference for this guidance is [Review Integrity](templates/review-integrity/standard.md), stable ID `review-integrity`, [template edition `1.0`](templates/review-integrity/README.md). Where adopted or applicable, it remains the general normative owner of Review integrity. More specific applicable requirements govern their own matters as described in [Review Integrity §2.2](templates/review-integrity/standard.md#22-more-specific-applicable-requirements); Review Integrity continues to govern matters they do not address.

Relevant subject owners include:

- [Architectural Reasoning](templates/architectural-reasoning/standard.md): architectural conclusion sufficiency, architecture-specific findings, and architectural completion.
- [Operational Execution Contract](templates/operational-execution-contract/standard.md): execution authority and execution validation.
- [Publication and Release Integrity](templates/publication-release-integrity/standard.md): publication identity, correspondence, resulting-state verification, and publication claims.
- [Web Quality and Verification](templates/web-quality-verification/standard.md) and the [Web Standards Suite](CATALOG.md#web-standards-suite): domain-specific Web assessment semantics and substantive requirements.
- [Standards Authoring](templates/standards-authoring/standard.md): authoring-specific review obligations and publication-text review.

These links clarify ownership; they do not create adoption dependencies. If the Review Integrity reference changes materially, this guidance can be reassessed through ordinary maintenance.

[Review Integrity §15](templates/review-integrity/standard.md#15-review-completion) describes information that a Review result should retain for later reliance. This guidance does not create another report schema; existing records may provide that information by reference. Reusing those records can avoid duplication. Identifying the next authority or later action can also help readers interpret what the Review result supports.

## 3. Selecting, combining, narrowing, or omitting review purposes

Select either purpose independently, or combine them when one Review legitimately addresses both an existing state and a change. Scope can be narrowed to the question that needs an answer, with irrelevant prompts omitted and material coverage limitations visible. Organizations may replace these shapes with their own procedures. The two purposes do not form a mandatory lifecycle, and adapting the guidance does not alter applicable requirements.

## 4. Existing-State Review

Use this shape when evaluating the current identified state of an existing subject rather than primarily evaluating one proposed change. The subject might be a repository, service, publication, document set, maintained system, or another identifiable existing state.

The central question is:

> What is true of this identified state within the declared review dimensions and coverage?

Where relevant, consider:

- identifying the state being reviewed and the dimensions or subject areas being evaluated;
- making partial, bounded, sampled, or non-exhaustive coverage visible where it affects interpretation;
- identifying strengths or satisfactory conditions worth preserving;
- identifying Material Findings and limitations that affect the conclusion;
- retaining justified no-change or no-finding conclusions where omission would make the record misleading;
- keeping findings distinct from authority to perform later remediation.

For a repository, possible dimensions include architecture and responsibility structure, implementation and tooling, tests, CI and security, documentation and contributor experience, and domain-specific content. These are informative examples, not mandatory coverage for every repository or other subject. Reviewing selected dimensions supports a conclusion about that coverage; it does not imply certification of the whole subject.

The [Standards Templates #56 repository audit](https://github.com/jamesreimer/standards-templates/issues/56) and Web pilots [#36](https://github.com/jamesreimer/standards-templates/issues/36), [#37](https://github.com/jamesreimer/standards-templates/issues/37), and [#38](https://github.com/jamesreimer/standards-templates/issues/38) provide examples of this reusable shape across different subjects. Their particular review methods and workflow choices are contextual evidence, not general requirements. For Web assessment, consult [Web Standards Suite Assessment Guidance](web-standards-assessment-guidance.md); the pilots do not override domain-specific Web rules.

## 5. Change / Implementation Review

Use this shape when evaluating a changed or proposed state relative to a comparison baseline, governing intent or accepted requirements, and materially relevant adjacent or dependent surfaces.

As applicable, consider:

- identifying the changed state, comparison baseline, and governing intent or requirements;
- reviewing the actual result and effects rather than conformity to a predicted implementation technique;
- inspecting adjacent or dependent surfaces capable of invalidating the conclusion;
- examining validation evidence and its relationship to the reviewed state;
- distinguishing pre-existing, change-introduced, and interaction-exposed conditions only where evidence supports the distinction and it matters;
- identifying Material Findings and their effect on the conclusion;
- reassessing affected dimensions after material state change before relying on an earlier conclusion.

Possible dimensions include local correctness, integration with adjacent definitions and dependencies, authority and responsibility boundaries, lifecycle and completion relationships, cross-references, generated or propagated effects, regressions, validation evidence, and documentation, catalog, or consumer effects. These remain prompts, not mandatory coverage.

Variance from an approach anticipated in a plan, design, work item, or other nonbinding implementation forecast is not itself a defect. It becomes review-relevant when the actual result materially changes or violates governing intent, requirements, responsibility, architecture, dependencies, protected behavior, authority, or required evidence. Where applicable, [Architectural Reasoning §4](templates/architectural-reasoning/standard.md#4-applicable-authority) distinguishes governing requirements from implementation choices and their revision authority.

## 6. Relying on a completed Review for a later action

Before relying on a completed Review for an action such as publication, merge, deployment, adoption, or activation, confirm that the reviewed subject and state have not materially changed. If they have, [Review Integrity §13](templates/review-integrity/standard.md#13-change-and-reassessment) governs reassessment and continued applicability. Under [§10](templates/review-integrity/standard.md#10-material-findings-and-later-reliance), Material Findings affecting the reliance need accurate disclosure or a valid disposition under applicable authority. Review completion does not itself grant authority for the later action; the more specific standard governing that action remains applicable.

Where [Publication and Release Integrity](templates/publication-release-integrity/standard.md) applies, it governs Publication Transition, source/published correspondence, publication identity, resulting-state verification, partial/failed/premature publication, correction, withdrawal, and publication claims. A Review may support a readiness decision, but it does not establish that Publication occurred or that the resulting Published State is correct.

## 7. Human and agent usage boundary

These review shapes are usable by a human-only organization through its ordinary review practices and records. Agent-oriented workflows may operationalize them with stricter mechanics, but those mechanics do not become requirements of this guidance. Agent-specific mechanics belong in systems such as `jamesreimer/agent-workflows`, repository-local agent guidance such as `AGENTS.md`, or consuming-project workflow authority.
