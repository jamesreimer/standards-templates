# Project Repository Responsibility Standard

## 1. Purpose

This standard defines the default responsibility model for information, artifacts, and work state within a project.

It establishes the relationship between:

- project repositories;
- canonical project documentation;
- specifications, decisions, and other durable project artifacts;
- issues or equivalent work items;
- project-management systems;
- exploratory reasoning;
- multiple-repository topologies.

Its purpose is to keep durable project truth, actionable work, dynamic planning state, and exploratory reasoning in the systems that legitimately own them without allowing planning tools, work trackers, or repository convenience to replace canonical artifacts or prematurely dictate repository topology.

## 2. Scope

This standard applies to projects whose durable artifacts or responsibilities may warrant version control unless a concrete project need justifies an exception.

It governs the default placement and responsibility of:

- durable specifications;
- project documentation;
- consequential decisions;
- implementation, production, research, publication, delivery, or other project artifacts;
- issues or equivalent work items, such as GitHub Issues;
- planning systems, such as GitHub Projects;
- exploratory conversations and working reasoning;
- additional repositories.

It does not prescribe domain-specific artifact structure, working methods, release or distribution process, implementation model, or organizational standards-adoption semantics.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, RFC 2119 and RFC 8174. Lowercase forms retain their ordinary English meaning.

## 3. Core Principle

The default project model is:

```text
Exploratory reasoning
        ↓
Settled consequential result
        ↓
Canonical durable project artifact

Issues
    track work arising from the project

Designated planning system
    tracks status, priority, sequencing, and dependencies
```

These responsibilities MUST remain distinct even when one system performs more than one of them.

A planning tool is not a canonical project artifact.

An issue or equivalent work item is not a substitute for durable project truth.

A repository is not created merely to provide a container for management state.

## 4. Default Repository Model

A project SHOULD begin with one canonical project repository once it has durable artifacts that warrant source control.

The repository MAY initially contain only documentation or another early durable artifact.

No particular artifact type needs to exist before the repository is created.

As the project develops, the same repository MAY grow to contain production, research, publication, implementation, validation, delivery, or other project artifacts.

The existence of one repository at project inception does not require the project to remain a single-repository project permanently.

## 5. Canonical Durable Artifacts

Durable project artifacts SHOULD be stored in version control when their loss, mutation without history, or inability to review changes would materially impair the project.

Examples include:

- project specifications;
- production or design documents;
- research protocols or methods;
- publication or delivery specifications;
- consequential project decisions;
- interface, format, or contract specifications;
- evaluation specifications;
- durable project requirements;
- operational documentation;
- project-specific standards where legitimately applicable.

These materials are canonical artifacts rather than planning records.

Version-control history SHOULD preserve meaningful changes to them.

## 6. Issues and Equivalent Work Items

Issues or equivalent work items represent work.

Appropriate uses include:

- defects or corrections;
- implementation, production, research, publication, or delivery tasks;
- proposed capabilities or changes;
- investigations;
- concrete follow-up work;
- unresolved project questions requiring action;
- changes proposed to canonical documents;
- validation or evaluation work.

Issues or equivalent work items MUST NOT replace canonical specifications, standards, decisions, or other durable project artifacts.

For example:

```text
Canonical document:
Public deliverables require accessibility review before distribution.

Issue:
Complete the accessibility review for the release candidate.
```

Closing the issue does not retire or erase the canonical requirement.

Issue comments MAY preserve useful discussion, but consequential settled results SHOULD be promoted to the appropriate canonical artifact.

## 7. Dynamic Planning State

A project SHOULD designate one system of record for dynamic planning state such as:

- status;
- priority;
- sequencing;
- dependencies;
- milestones;
- iteration;
- assignment;
- roadmap placement.

The designated system MAY be an issue tracker, a project-management product, a repository document, or another mechanism proportionate to the project's needs.

Other systems and documents SHOULD NOT duplicate this state merely to create a competing planning system.

For example, avoid maintaining a Markdown backlog that duplicates state already owned by the active issue tracker, project board, or other designated system.

The designated system SHOULD be the source of truth for current work state.

## 8. Exploratory Reasoning

Chat threads, meetings, working conversations, whiteboards, notebooks, and similar environments MAY be used for exploratory reasoning.

They are working spaces rather than canonical project artifacts by default.

The normal promotion path is:

```text
exploration
    ↓
reasoning / review / pressure testing
    ↓
settled consequential result
    ↓
canonical version-controlled artifact
```

The complete conversational history does not need to be copied into the repository.

Preserve the resulting decision or specification rather than all of the intellectual archaeology that produced it.

## 9. Consequential Decisions

A consequential project decision that materially affects future work or interpretation SHOULD be preserved durably.

Depending on its nature, it may belong in:

- a project specification;
- a production, research, publication, implementation, or delivery document;
- a decision record;
- another appropriate canonical document.

Do not create decision records merely for ceremonial completeness.

A decision deserves durable preservation when forgetting it would materially impair future understanding or cause a rejected approach, constraint, or consequential choice to be incorrectly reconsidered as unsettled.

## 10. Additional Repositories

Projects SHOULD NOT create separate repositories merely because activities or artifact types are conceptually different.

Additional repositories SHOULD be created when materially independent responsibility or lifecycle consequences justify separation.

Examples include:

- independent release, publication, distribution, or versioning lifecycle;
- materially different ownership;
- materially different permissions;
- different maintenance responsibility;
- independent external consumption;
- substantially different cadence;
- one specification governing multiple independent realizations;
- repository coupling becoming operationally harmful.

Conceptual separation alone is insufficient justification.

## 11. Canonical-Artifact Repositories

A separate canonical-artifact repository MAY be appropriate when the governed material has a materially independent responsibility or lifecycle from other project artifacts or activities.

Examples include:

- one specification governing several independent realizations;
- specifications, publications, or production assets distributed independently;
- canonical material maintained under different permissions or ownership;
- working repositories that may change while a governing artifact remains stable.

Such a repository SHOULD exist because the artifacts themselves have earned independent version control, not because an issue tracker needs a repository.

This section addresses repository topology. The adoption, ownership, and independent lifecycle of standards derived from external or reusable source material are governed separately by the `standards-adoption-model` template.

## 12. Canonical Artifact Change Model

A change to a canonical project standard, specification, decision, or other governed artifact SHOULD follow a reviewable path such as:

```text
identified need
    ↓
issue or proposal
    ↓
discussion / analysis
    ↓
artifact change
    ↓
review
    ↓
canonical version update
```

The issue or proposal tracks the work.

The resulting canonical artifact contains the settled outcome.

Approval or closure of the work item does not itself substitute for updating the canonical artifact.

## 13. Repository Creation Timing

A project repository is justified when the project has something that legitimately deserves source control.

This may include:

- canonical project documentation;
- specifications;
- manuscripts or production source material;
- source code or schemas;
- validation or evaluation assets;
- automation or validation configuration;
- tooling;
- other durable project artifacts.

A repository does not need to wait for implementation or production artifacts.

Conversely, a repository SHOULD NOT be created solely because a management tool happens to require one if no repository-owned artifact or lifecycle has otherwise been earned.

## 14. Default Responsibility Model

The default responsibility model is:

```text
Exploratory discussions
    working reasoning

Canonical artifacts
    durable specifications, decisions, and project material

Version-control repository
    version history for durable project artifacts

Issues / work items
    actionable work

Designated planning system
    dynamic planning state; can be an issue tracker, project-management product,
    repository document, or another proportionate mechanism

Pull requests / change reviews
    reviewable changes to repository artifacts

Additional repositories
    SHOULD NOT be created merely because activities or artifact types
    are conceptually different
    SHOULD be created when materially independent responsibility or lifecycle consequences
    justify separation
```

## 15. Anti-Patterns

Avoid:

- using Issues or work items as the only canonical specification;
- copying issue status into Markdown planning documents;
- creating a `project-management` repository automatically for every project;
- separating artifact types solely because they are conceptually different;
- treating repository membership as evidence of authority;
- keeping consequential project decisions only in chat history;
- copying entire design conversations into the canonical repository;
- creating multiple repositories before independent responsibility or lifecycle consequences are demonstrated;
- treating repository membership as authority over material canonically owned elsewhere;
- maintaining multiple competing sources of truth for the same planning state.

## 16. Default Standard

Unless concrete project requirements demonstrate otherwise:

> **Start with one canonical project repository once durable project artifacts warrant source control.**
>
> **Store canonical project specifications, consequential decisions, and other durable project artifacts in version control when their loss or unreviewable mutation would materially impair the project.**
>
> **Use Issues or equivalent work items for actionable work, not as substitutes for canonical artifacts.**
>
> **Designate one proportionate system of record for dynamic status, priority, sequencing, and dependencies.**
>
> **Use exploratory discussions as working spaces and promote settled consequential results into canonical artifacts.**
>
> **Projects SHOULD NOT create separate repositories merely because activities or artifact types are conceptually different.**
>
> **Additional repositories SHOULD be created when materially independent responsibility or lifecycle consequences justify separation.**
>
> **Respect canonical ownership boundaries: local repository membership does not by itself transfer authority over material owned elsewhere.**
