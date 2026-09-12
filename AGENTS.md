# Agent Guidance

## Before planning or editing

- Inspect the current branch and worktree first, and preserve unrelated user changes.
- Read [MAINTAINING.md](MAINTAINING.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
- Read [NAMING.md](NAMING.md) when template identity or naming is involved.
- Identify whether the request changes template scope, evidence, or repository structure.
- Identify and read the applicable standards below before planning or implementing substantive changes.

## Governing standards

For work in this repository, agents MUST apply the relevant standards as governing constraints, not merely contextual documentation. Do not invent a parallel rule, workflow, taxonomy, repository responsibility, or authority model where an existing standard governs. Preserve each standard's documented conceptual boundary when several apply. Surface substantive governance questions without a clear existing owner for planning rather than silently creating policy.

### Default architectural reasoning

For substantive repository work, read and apply [`architectural-reasoning`](templates/architectural-reasoning/standard.md) before committing to an implementation model. Use it to determine, as applicable, the Architectural Unit, responsible system or owner, existing-system versus new-system treatment, evidence that changes assumed boundaries or ownership, proportional architecture, final state versus transition mechanisms, adjacent and dependent-system effects, and whether a discovered defect is a separate Architectural Unit.

Keep reasoning proportionate to consequence and uncertainty. Trivial mechanical edits do not require a heavyweight architecture exercise.

### Additional subject routing

Read and apply each standard whose subject the work implicates:

| Subject | Governing standard |
| --- | --- |
| Consequential execution; execution authority and protected boundaries; material scope expansion; established paths and escalation; stop conditions; recovery or exceptional execution | [`operational-execution-contract`](templates/operational-execution-contract/standard.md) |
| Shared, external, propagated, copied, generated, installed, or otherwise source-related governed artifacts; source identity, immutable consumed state, correspondence, or required governed targets | [`shared-asset-provenance`](templates/shared-asset-provenance/standard.md) |
| Creation or modification of normative templates | [`standards-authoring`](templates/standards-authoring/standard.md) |
| Organizational adoption of reusable or external normative material | [`standards-adoption-model`](templates/standards-adoption-model/standard.md) |
| Repository responsibility, canonical durable artifact placement, planning/work-item versus durable-record questions, or justification for another repository | [`project-repository-model`](templates/project-repository-model/standard.md) |

Consult [CATALOG.md](CATALOG.md) for other applicable subjects and their boundaries. This routing governs repository work; it does not itself confer downstream organizational authority on templates.

## Workflow roles

- **Planner / coordinator:** establishes scope, boundaries, intended outcome, review gates, and the implementation handoff.
- **Implementor:** performs repository mutations, branch and PR work, validation, and cleanup within authorized scope.
- **Independent reviewer:** evaluates proposed or completed results for conceptual defects, omissions, duplication, misclassification, and boundary drift. Independent review does not itself grant implementation authority.

These roles describe responsibilities rather than required tools or a fixed number of participants. Honor the planned review gates; the implementor's own checks do not substitute for a required independent review.

## Adoption assistance

Before assisting an adoption, read root [ADOPTION.md](ADOPTION.md), the candidate template's adjacent `README.md`, the candidate `standard.md`, and the adopting source's existing authority.

Do not create or modify an adopted artifact until the proposed scope and adoption authority, existing authority and conflicts, canonical destination, provenance, protected effects, and proposed `adopt`, `adapt`, `reject`, or `defer` disposition have been reviewed.

Humans and agents use the same canonical adoption guidance; do not create a separate agent-only adoption policy.

## Implementation lifecycle

1. Create or use a bounded implementation branch, following applicable contribution naming conventions. Keep unrelated work out of its commits and PR.
2. Run the validation below and open a reviewable PR stating scope, applicable standards, validation evidence, and any unresolved review questions.
3. When merge is within authorized scope, the PR is non-draft, the intended review gate is complete, and required checks are present and satisfied, enable auto-merge on that PR. Repository-level auto-merge availability does not enable it for an individual PR. Do not manually merge merely because checks are green when auto-merge is the intended path.
4. Confirm the merge before cleanup. Fetch and prune as appropriate, verify remote branch cleanup, and delete merged local implementation branches only after confirming their work is present on `main` and no unique or unmerged work would be lost. Preserve unrelated branches, worktrees, and uncommitted work.
5. Return to `main`, update it safely from `origin/main` without overwriting local work, and verify final local/remote state. Report merge identity, branch cleanup, and any preserved changes or unresolved cleanup conditions.

## Validation and completion

- Run `python3 -m unittest discover -s tests` and `python3 scripts/validate.py`.
- Run applicable supplemental checks from [CONTRIBUTING.md](CONTRIBUTING.md), including Markdown lint for Markdown changes, and `git diff --check`.
- Manually reverify affected external claims when citations change.
- Update `repository-structure.txt` only for an intentional structural change by running `python3 scripts/update_repository_structure.py`.
- Do not create templates, metadata, taxonomies, automation, or tooling merely because they are conventional.
