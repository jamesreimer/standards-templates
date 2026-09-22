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

These roles describe responsibilities rather than required tools or a fixed number of participants. Independent review is not universally required. It is required when an applicable governing standard, an explicit handoff, or a project-specific instruction imposes it, and where it is required the implementor's own checks do not substitute for it. Review should produce information about the work, not an additional confirmation that checks already report.

When preparing or returning from an implementation handoff, reference settled authoritative results rather than replaying their reasoning, and carry forward only the context, constraints, and unresolved questions the next decision needs, keeping detail proportionate to remaining uncertainty and consequence; `architectural-reasoning` §2 governs that proportionality, and `operational-execution-contract` §5 and §12.1 govern what each direction carries. Bound the authorized problem, permitted consequences, and protected interests without unnecessarily prescribing the form of the solution, and let `architectural-reasoning` §8 determine whether the conforming result is additive, modifying, consolidating, replacing, or removing. Where exact-change discipline is materially required, state that restriction deliberately and name the consequence it protects rather than letting it arise implicitly from substantive scope limits or non-goals; `operational-execution-contract` §9 and §5 own that distinction.

## Adoption assistance

Before assisting an adoption, read root [ADOPTION.md](ADOPTION.md), the candidate template's adjacent `README.md`, the candidate `standard.md`, and the adopting source's existing authority.

Do not create or modify an adopted artifact until the proposed scope and adoption authority, existing authority and conflicts, canonical destination, provenance, protected effects, and proposed `adopt`, `adapt`, `reject`, or `defer` disposition have been reviewed.

Humans and agents use the same canonical adoption guidance; do not create a separate agent-only adoption policy.

## Tooling

Locally authored standards-specific repository tooling is Python using only the standard library, targeting the version floor stated in [CONTRIBUTING.md](CONTRIBUTING.md#validation). Use shell only where the shell is itself the interface, such as a Git hook shim.

Generic repository mechanics inherited from an approved `repo-template` baseline may use the runtimes, package managers, and maintained dependencies owned by that baseline. Their use does not transfer ownership of those mechanics to this repository.

Do not add a package manager, dependency, or runtime solely to implement local standards-specific repository tooling unless a separately justified need requires it.

## Implementation lifecycle

1. Create or use a bounded implementation branch, following applicable contribution naming conventions. Keep unrelated work out of its commits and PR.
2. Run the validation below and open a reviewable PR stating scope, applicable standards, validation evidence, and any unresolved review questions.
3. Merge only when it is within authorized scope, the PR is non-draft, any required review gate is complete, and the applicable required checks and repository protections are satisfied. Auto-merge may be used where available, including before those prerequisites complete, but it is not required; merging manually once the same prerequisites are satisfied is equally permitted. Do not bypass a required protection, and do not treat either merge mechanism as authority to ignore an independently applicable publication or deployment rule.
4. Confirm the merge before cleanup. Fetch and prune as appropriate, verify remote branch cleanup, and delete merged local implementation branches only after confirming their work is present on `main` and no unique or unmerged work would be lost. Preserve unrelated branches, worktrees, and uncommitted work.
5. Return to `main`, update it safely from `origin/main` without overwriting local work, and verify final local/remote state. Report merge identity, branch cleanup, and any preserved changes or unresolved cleanup conditions.

## Validation and completion

- Follow setup in [CONTRIBUTING.md](CONTRIBUTING.md#validation), stage intended new files, then run `.venv/bin/pre-commit run --all-files --show-diff-on-failure` and `git diff --check`. This is the authoritative local/CI composition.
- Standards-domain validation remains independently executable: `python3 scripts/validate_local.py` and `python3 -m unittest discover -s tests`.
- Preserve exact-copy correspondence with the immutable upstream revision recorded in [PROVENANCE.md](PROVENANCE.md). Standards-domain checks belong in the Python validator; generic defects belong at their owning upstream source. The bounded temporary generic policy/selection controls have explicit preservation and retirement obligations in PROVENANCE.
- Do not retain or recreate the retired generic Python validator, dynamic loader, hook installer, or arbitrary configuration schema as hidden glue.
- Run representative positive and injected-defect cases when changing validation. Fail-closed behavior, source preservation, whole-repository coverage, and protected policies remain required outcomes.
- Manually reverify affected external claims when citations change.
- Update `repository-structure.txt` only for an intentional structural change with `node tools/check-repository-policy.mjs --write-snapshot`; ordinary validation must not rewrite it.
- Do not create templates, metadata, taxonomies, automation, or tooling merely because they are conventional.
