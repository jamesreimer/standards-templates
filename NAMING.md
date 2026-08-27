# Template Naming Standard

## Purpose

This document defines how templates in this repository are named.

Each template has two names with different responsibilities:

```text
stable template ID
    identifies the durable subject

human-facing title
    describes the document clearly, including its form and authority
```

A stable folder ID does not need to repeat the document type or encode the full human-facing title.

## Priority order

When naming principles conflict, apply them in the following order.

### 1. Match the register to what the name is responsible for communicating

The human-facing title should accurately express the document's form and authority.

Terms carry implications:

- `standard`, `policy`, and similar terms imply normative or binding force;
- `practices`, `guide`, and similar terms imply advisory or optional content;
- `workflow`, `process`, and similar terms imply prescribed procedure.

Do not let a title claim more or less authority than the document is intended to have.

The short stable template ID primarily identifies the durable subject. It does not need to repeat words such as `standard`, `policy`, or `guide` when the human-facing title already communicates the document type.

Neither the title nor the template ID should positively misrepresent the document's authority or nature.

A template may be a template **for a standard or policy** without this repository itself conferring organizational authority. Organizational adoption is what gives a particular downstream artifact governing force within that organization's legitimate scope.

### 2. Do not annex a neighboring concept's future territory

Do not broaden a name merely to make it sound future-proof when that breadth reaches into a concept that should remain distinct.

The relevant test is not:

> Is this name broad enough?

It is:

> Does this name reach into territory that belongs to a different concept, even if that concept does not yet have its own document?

Related concepts may remain related without sharing one name.

If two subjects are intended to remain conceptually distinct, their identifiers should preserve that boundary.

### 3. Name for the durable subject, not today's incomplete slice

Once neighboring conceptual territory has been protected, prefer a name that can survive legitimate growth within the same subject.

If a template currently covers only part of a durable subject but is expected to grow into fuller coverage of that same subject, name the template for the durable subject rather than today's narrower draft.

This principle never overrides Principle 2.

Broadening within the legitimate territory of the same concept is useful.

Broadening into another concept is not.

### 4. Treat established-term collisions as a lower-priority tiebreaker

Some word combinations carry strong established meanings in software or other domains.

Avoid accidental collisions when a costless alternative exists, but do not let a minor naming collision override a name that is otherwise semantically correct under Principles 1 through 3.

Repository context and the adjacent template README can resolve mild ambiguity.

## Stable template IDs

Template IDs should be:

- short enough to use comfortably in paths and relationship metadata;
- descriptive enough to identify the durable subject;
- stable across ordinary expansion of the template within its existing conceptual territory;
- lowercase and hyphen-separated;
- free of organization-specific names unless the template itself is intentionally organization-specific, which is ordinarily outside this repository's purpose.

Do not optimize IDs for marketing language.

Do not encode transient status, version numbers, organizational adoption state, or implementation technology into the ID unless those concepts are genuinely part of the durable subject.

## Human-facing titles

Human-facing titles may be substantially more descriptive than the folder ID.

A title should communicate what the document actually is and what territory it covers without requiring the stable ID to carry that entire burden.

For example:

```text
template ID:
project-repository-model

human-facing title:
Software Project Repository Responsibility Standard
```

## Worked example

The first template uses the stable ID:

> `project-repository-model`

and the human-facing title:

> **Software Project Repository Responsibility Standard**

The ID was chosen to name the durable project-repository subject without forcing the path to enumerate every system the standard discusses.

Candidates were evaluated as follows.

### `project-repository-practices`

Rejected because `practices` sounds advisory while the document is intended to be a normative standard after organizational adoption.

### `project-repository-governance`

Rejected because `governance` claims broader territory and a stronger governance subject than the document actually defines.

### `project-repo-workflow`

Rejected because `workflow` implies prescribed procedural steps, while the standard deliberately separates required conditions from specific procedures.

### `project-workspace-model`

Rejected because `workspace` was reserved for a distinct neighboring concept. Broadening into it would annex conceptual territory rather than future-proof the existing subject.

### `project-repository-model`

Accepted because it:

- identifies the durable subject without overstating the document's form;
- leaves neighboring concepts distinct;
- can accommodate legitimate future growth within the same project-repository subject;
- has only a minor potential echo of the software Repository pattern, which repository context resolves easily.

The human-facing title was later narrowed from an enumerative title after review showed that one section actually belonged to the separate `standards-adoption-model` subject. That refinement illustrates the same naming rule: a title should name the document's actual center rather than preserve breadth that belongs to a neighboring concept.

## Evaluation procedure

When evaluating a proposed template name:

1. determine what the template ID is responsible for identifying and what the human-facing title is responsible for communicating;
2. check authority and procedural register;
3. check for annexation of neighboring conceptual territory;
4. check whether the name can survive legitimate growth within the same subject;
5. only then consider accidental collisions with established terminology.

If a candidate survives these checks, keep it.

Do not manufacture alternatives merely to appear thorough.

## Change discipline

Template IDs are intended to be stable because downstream organizations may retain them in provenance and relationship metadata.

Renaming an existing template should therefore require a substantive naming defect, such as semantic misrepresentation or conceptual collision, rather than stylistic preference.
