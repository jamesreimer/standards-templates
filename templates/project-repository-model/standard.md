# Software Project Repository, Documentation, and Work Tracking Standard

## 1. Purpose

This standard defines the default relationship between:

- software project repositories;
- canonical project documentation;
- architecture and design artifacts;
- issue tracking;
- project-management systems;
- exploratory design discussions;
- multiple-repository topologies.

Its purpose is to provide a consistent, durable project-management and repository model without allowing planning tools, issue trackers, or repository convenience to replace canonical specifications or prematurely dictate implementation topology.

## 2. Scope

This standard applies to software projects unless a concrete project need justifies an exception.

It governs the default placement and responsibility of:

- durable specifications;
- architecture documents;
- design decisions;
- source code;
- implementation artifacts;
- GitHub Issues or equivalent work items;
- GitHub Projects or equivalent planning systems;
- exploratory design conversations;
- additional repositories.

It does not prescribe programming language, framework, deployment model, or application architecture.

## 3. Core Principle

The default project model is:

```text
Design discussions
        ↓
Canonical project artifacts
        ↓
Implementation and validation

Issues
    track work arising from the project

Project-management views
    track status, priority, sequencing, and dependencies
```

These responsibilities must remain distinct.

A planning tool is not a canonical specification.

An issue is not a substitute for durable architecture.

A repository is not created merely to provide a container for management state.

## 4. Default Repository Model

A software project SHOULD begin with one canonical project repository once the project has durable artifacts that warrant source control.

The repository MAY initially contain only documentation.

Implementation code does not need to exist before the repository is created.

A typical early structure may be:

```text
project/
├── README.md
└── docs/
    ├── architecture/
    ├── decisions/
    └── specifications/
```

As implementation begins, the same repository MAY grow to contain:

```text
project/
├── README.md
├── docs/
├── src/
├── tests/
└── ...
```

The existence of one repository at project inception does not require the project to remain a single-repository implementation permanently.

## 5. Canonical Durable Documents

Durable project artifacts SHOULD be stored in version control when their loss, mutation without history, or inability to review changes would materially impair the project.

Examples include:

- architecture specifications;
- contract specifications;
- system design documents;
- consequential architectural decisions;
- interface specifications;
- evaluation specifications;
- durable engineering requirements;
- operational documentation;
- project-specific standards where legitimately applicable.

These documents are canonical artifacts rather than planning records.

Git history SHOULD preserve meaningful changes to them.

## 6. Issues

Issues represent work.

Appropriate uses include:

- bugs;
- implementation tasks;
- features;
- investigations;
- concrete follow-up work;
- unresolved engineering questions requiring action;
- changes proposed to canonical documents;
- validation or evaluation work.

Issues MUST NOT replace canonical architecture, specifications, standards, or durable design documents.

For example:

```text
Canonical document:
Persistence proposals require Context adjudication.

Issue:
Implement persistence-proposal adjudication according to the canonical contract.
```

Closing the issue does not retire or erase the canonical requirement.

Issue comments MAY preserve useful discussion, but consequential settled results SHOULD be promoted to the appropriate canonical artifact.

## 7. Project-Management Systems

GitHub Projects or an equivalent project-management system SHOULD own dynamic planning state such as:

- status;
- priority;
- sequencing;
- dependencies;
- milestones;
- iteration;
- assignment;
- roadmap placement.

Repository documents SHOULD NOT duplicate this state merely to create a second planning system.

For example, avoid maintaining a Markdown backlog that duplicates the active issue tracker and project board.

The project-management system should be the source of truth for current work state.

## 8. Exploratory Design Discussions

Chat threads, meetings, design conversations, whiteboards, notebooks, and similar environments MAY be used for exploratory reasoning.

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

A consequential project decision that materially affects future implementation or interpretation SHOULD be preserved durably.

Depending on its nature, it may belong in:

- an architecture specification;
- a contract specification;
- a design document;
- an architecture decision record;
- another appropriate canonical document.

Do not create decision records merely for ceremonial completeness.

A decision deserves durable preservation when forgetting it would materially impair future understanding or cause a rejected approach, constraint, or architectural choice to be incorrectly reconsidered as unsettled.

## 10. Additional Repositories

Projects MUST NOT default to separate management and implementation repositories merely because planning and implementation are conceptually different activities.

Additional repositories SHOULD be created only when a concrete difference in lifecycle justifies separation.

Examples include:

- independent release or versioning lifecycle;
- materially different ownership;
- materially different permissions;
- independent deployment;
- different maintenance teams;
- independent external consumption;
- substantially different release cadence;
- one specification governing multiple independent implementations;
- repository coupling becoming operationally harmful.

Conceptual separation alone is insufficient justification.

## 11. Architecture or Standards Repositories

A separate architecture or specification repository MAY be appropriate when canonical architectural material genuinely has an independent lifecycle from any particular implementation.

Examples include:

- one architecture governing several implementation repositories;
- specifications distributed independently;
- standards consumed by multiple projects;
- architecture maintained under different permissions or ownership;
- implementation repositories that may change while the governing specification remains stable.

Such a repository should exist because the artifacts themselves have earned independent version control, not because an issue tracker needs a repository.

## 12. Cross-Project Standards

A standard intended to govern multiple projects SHOULD NOT be canonically owned by one of the projects it governs.

Cross-project standards SHOULD live in an organization-owned standards repository or equivalent authoritative source.

Reusable external or personal templates MAY be used as source material, but an organization SHOULD deliberately adopt its own canonical copy rather than depend on an external personal source for continuing authority.

Once adopted, the organization-owned copy governs according to the organization's own scope and lifecycle.

Subsequent changes to the external template MUST NOT automatically alter the organization-owned standard.

## 13. Standard Change Workflow

A change to a canonical standard or specification SHOULD follow a reviewable path such as:

```text
identified need
    ↓
issue or proposal
    ↓
discussion / analysis
    ↓
document change
    ↓
review
    ↓
canonical version update
```

The issue or proposal tracks the work.

The resulting document contains the normative outcome.

Approval of the work item does not itself substitute for updating the canonical artifact.

## 14. Repository Creation Timing

A project repository is justified when the project has something that legitimately deserves source control.

This may include:

- canonical architecture;
- specifications;
- source code;
- schemas;
- tests;
- executable evaluations;
- CI configuration;
- tooling;
- other durable project artifacts.

A repository does not need to wait for application code.

Conversely, a repository SHOULD NOT be created solely because a management tool happens to require one if no repository-owned artifact or lifecycle has otherwise been earned.

## 15. Default Responsibility Model

The default responsibility model is:

```text
Exploratory discussions
    working reasoning and design

Canonical documents
    durable specifications and decisions

Git repository
    version history for durable project artifacts

Issues
    actionable work

Project-management system
    dynamic planning state

Pull requests
    reviewable changes to repository artifacts

Additional repositories
    only when independent lifecycle justifies separation
```

## 16. Anti-Patterns

Avoid:

- using Issues as the only architecture specification;
- copying issue status into Markdown planning documents;
- creating a `project-management` repository automatically for every project;
- separating documentation from implementation solely because they are different kinds of content;
- treating repository membership as evidence of authority;
- keeping consequential architecture only in chat history;
- copying entire design conversations into the canonical repository;
- creating multiple repositories before their lifecycle differences are demonstrated;
- allowing an implementation repository to silently redefine a cross-project standard;
- maintaining multiple competing sources of truth for the same planning state.

## 17. Default Standard

Unless concrete project requirements demonstrate otherwise:

> **Start with one canonical project repository once durable project artifacts warrant source control.**
>
> **Store canonical project specifications, architecture, consequential design decisions, and implementation artifacts in version control.**
>
> **Use Issues for actionable work, not as substitutes for canonical documents.**
>
> **Use the project-management system for dynamic status, priority, sequencing, and dependencies.**
>
> **Use exploratory discussions as working spaces and promote settled consequential results into canonical artifacts.**
>
> **Create additional repositories only when lifecycle, ownership, permissions, distribution, release cadence, or implementation topology genuinely requires separation.**
>
> **Store standards that govern multiple projects in an organization-owned authoritative standards source. External templates may inform adoption but do not remain authoritative after adoption.**
