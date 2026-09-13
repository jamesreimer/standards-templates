# Repository Work Identification Standard

## 1. Purpose

This standard governs how branch names, pull request titles, and issue labels identify and classify repository work so that humans and automation can understand what the work represents.

These surfaces share a semantic responsibility but need not use identical vocabulary or encode every fact about the work. The standard leaves category vocabularies and syntax to the adopting organization.

## 2. Scope

This standard applies to the creation and material revision of implementation branch names, pull request titles, and issue-label classifications within the adopted scope. It also governs the meaning and maintenance of label sets used for that classification.

It does not require a particular repository host, version-control system, prefix vocabulary, title syntax, or label taxonomy. Repositories need not use labels where they provide no material value. It does not require every work item to have a branch or pull request, or every pull request to have an issue.

This standard does not govern repository or filesystem names, repository creation or separation, execution authority, organizational standards adoption, general task-management workflow, project status systems, assignment of people, prioritization methodology, release/version names, or commit-message format.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html). Lowercase forms retain their ordinary English meaning.

## 3. Terminology

**Work identity** describes the subject and substantive change, investigation, or other work represented by an artifact. It is distinct from workflow state, such as whether work is awaiting review or complete.

**Classification** places work in a defined category or dimension for interpretation, discovery, or automation. Type, area, state, priority, and risk are possible dimensions, not a required taxonomy.

**Implementation branch** means a named version-control line used to develop repository work. This standard does not prescribe long-lived integration, release, or version naming schemes.

**Pull request** includes an equivalent merge request or reviewable repository change proposal, regardless of host terminology.

**Issue** includes an equivalent work item. **Issue labels** are named classifications attached to work items; equivalent category mechanisms are covered when used for this purpose. This does not extend the standard to all work-item fields or tracking behavior.

## 4. Truthful and Proportionate Identification

Branch names, pull request titles, and applied issue classifications MUST NOT materially misrepresent the work they identify. Retained branch names and historical identification are subject to the explicit contextual treatment in Sections 5 and 9; retention does not make stale classification current truth. Classification MUST follow the substance of the work rather than an incidental tool, actor, file format, or implementation technique.

Identification SHOULD be concise, readable, and sufficiently specific to distinguish relevant concurrent work in its repository context. A reference number MAY aid traceability but SHOULD NOT replace meaningful subject information in a branch name or pull request title.

When structured prefixes, title categories, or labels are used, their meanings and applicability MUST be defined clearly enough for consistent use. Existing contributor guidance or label descriptions MAY provide those definitions; a separate registry or schema is not required.

The amount of classification SHOULD be proportionate to its value for understanding, discovery, or reliable automation. A naming or labeling system SHOULD NOT attempt to reproduce every fact in the work item or proposed change.

## 5. Branch Names

An implementation branch name SHOULD identify the work's subject and intended change or investigation. It SHOULD remain meaningful while implementation details evolve within that subject.

Where branch prefixes or categories are used, names MUST follow the applicable locally governed convention and its defined meanings. A prefix MUST NOT imply a change type that contradicts the work. This standard does not select the vocabulary for that convention.

Branch names MUST satisfy the constraints of the version-control system, repository host, and required tools that process them. The adopter SHOULD choose a readable syntax compatible with its intended operating environments and SHOULD avoid unnecessarily fragile punctuation, opaque abbreviations, and distinctions that intended consumers cannot reliably recognize.

The name SHOULD contain enough subject information to distinguish simultaneous branches with related work. A locally meaningful qualifier or work-item reference MAY supply that distinction without changing the substantive classification.

When a branch's purpose materially changes, its identification MUST be re-evaluated. A misleading name SHOULD be corrected with dependent references considered under Section 9. When a retained name cannot safely be changed immediately, its current purpose MUST be made explicit in associated work or review records, and consumers MUST NOT rely on the stale classification as current truth.

## 6. Pull Request Titles

A pull request title MUST truthfully identify the proposed change. When it states a change type, that type MUST reflect the substantive result, including when normative or behavioral changes are made through documentation files.

Titles SHOULD concisely name the result or question under review with enough specificity to distinguish it from other proposed changes. They SHOULD NOT describe only editing mechanics when the substantive change can be named clearly.

If an adopter chooses a structured title convention, titles MUST follow that convention and its meanings. This standard does not require Conventional Commits or any other universal title syntax.

The title MUST be re-evaluated when the proposed result materially changes and corrected if it becomes misleading. Changes to implementation technique alone do not require retitling while the title remains accurate. Review discussion and change descriptions can carry detail that would make a title unwieldy.

## 7. Issue Labels

### 7.1 Useful and Defined Semantics

Labels SHOULD be introduced or retained when they provide material classification value. Each label in use MUST have a defined meaning and application criteria accessible to the people and automation that use it.

Meanings SHOULD remain stable across ordinary use. A label MUST NOT silently acquire a materially different meaning while consumers continue to interpret it under its former meaning.

Labels SHOULD classify useful dimensions without proliferating synonyms, near-duplicates, or categories that are not used. Where several dimensions are represented, their meanings MUST remain distinguishable. A type label, for example, MUST NOT silently stand for a priority or approval decision.

Overlapping classifications SHOULD be minimized where they create ambiguity. Multiple labels MAY describe distinct facets of the same work. Labels that are mutually exclusive under the adopted definitions MUST NOT be applied together as a current classification. Uncertainty MAY be represented explicitly without making contradictory claims.

### 7.2 Relationship to Workflow and Authority

Work identity and workflow state MUST remain distinguishable. A label MAY represent state, priority, or risk under an existing governing model, but this standard does not establish that model or require those dimensions.

Where labels represent state governed elsewhere, their relationship to the designated source of truth MUST be explicit. They MUST NOT silently establish a competing workflow or authority system. Label presence alone MUST NOT be treated as approval or execution authority unless the applicable authority model explicitly assigns it that meaning.

### 7.3 Automation and Maintenance

Automation that interprets labels MUST rely on documented label semantics, including the meaning of combinations or absence where those affect its decisions. Automation MUST NOT assign undocumented authority or workflow meaning to a label merely because its name appears suggestive.

Label sets SHOULD be reviewed when unused, obsolete, ambiguous, or duplicate classifications become apparent. Such labels MAY be revised, consolidated, or removed after considering existing usage and dependent consumers. No fixed review cadence or universal label inventory is required.

Before changing or removing a label relied upon by automation, reporting, or active work, its dependent interpretations MUST be identified and addressed so that consumers do not silently apply obsolete semantics. Section 9 governs the identification-change implications, not authorization of the resulting operational actions.

## 8. Consistency Across Surfaces

When branches, pull requests, and issues refer to related work, their identification MUST be consistent with what each actually represents. A broader issue may contain several narrower changes; consistency does not require identical scope, identical wording, or a one-to-one relationship.

A branch prefix, pull request type, and issue label MAY express related concepts using different vocabularies. Where people or automation depend on a correspondence between them, the relationship MUST be defined rather than inferred from spelling alone.

Existing links, work-item references, or associated descriptions SHOULD make the relationship traceable when names alone leave material ambiguity. This does not require copying every classification onto every surface or creating an additional tracking system.

A change in implementation detail SHOULD NOT trigger renaming or reclassification of related artifacts whose substantive identity remains accurate. A workflow-state change does not by itself change work identity.

## 9. Identification Changes and Historical Material

Before materially renaming branches, changing title syntax, or revising label names or meanings, maintainers MUST assess affected references and interpretations where those changes could disrupt active work or dependent consumers. Relevant consumers may include scripts, filters, dashboards, links, and automation. Dependent consumers MUST remain able to identify or interpret the affected work correctly through the change.

The assessment SHOULD be proportionate to the actual impact; it does not require a migration project for an ordinary title correction without dependent consumers. This standard does not authorize a rename, classification mutation, or operational migration beyond existing authority.

Adoption does not require retroactive normalization of historical names, titles, or labels. Accurate historical identification SHOULD remain unchanged where alteration would add only cosmetic uniformity or obscure the record. If historical classification is retained after conventions change, its historical meaning MUST NOT be silently presented as a current classification under the new convention.

## 10. Boundaries with Related Standards

- [`repository-naming`](../repository-naming/standard.md) governs repository names.
- [`filesystem-naming`](../filesystem-naming/standard.md) governs file, directory, and path-component names.
- [`project-repository-model`](../project-repository-model/standard.md) governs repository responsibility, durable artifact placement, planning-state ownership, and repository separation.
- [`operational-execution-contract`](../operational-execution-contract/standard.md) governs execution authority, Protected Boundaries, Material Scope Expansion, stop conditions, and recovery. Work classification does not supply that authority.
- [`standards-adoption-model`](../standards-adoption-model/standard.md) governs deliberate organizational adoption and the authority of adopted material.

These references clarify responsibility and create no adoption dependency. This standard governs identification and classification, not general issue management, assignment, prioritization, status transitions, release/version naming, or commit-message syntax.

## 11. Informative Examples

An adopter could choose `feat/`, `fix/`, and `docs/` branch prefixes, titles of the form `<type>: <subject>`, and labels such as `kind:defect` or `area:search`. Another could use unprefixed descriptive branches, plain-language titles, and no labels. Neither scheme is prescribed here.

A branch named `fix/search-empty-results`, a pull request titled `Correct empty-result handling`, and an issue labeled `kind:defect` can describe consistent work without matching text. A broader issue about search usability can also include that correction without itself being classified solely as a defect.

A title such as `Edit standard.md` describes mechanics. `Clarify branch classification semantics` more directly identifies the proposed result. These examples illustrate semantic clarity, not required phrases, syntax, or categories.

## 12. Basis

The identification and classification rules are synthesized organization-neutral standards decisions. BCP 14 supplies the normative-keyword interpretation; it does not prescribe branch prefixes, pull request syntax, or issue-label vocabularies. Host and tool compatibility must be assessed in the adopter's actual environment rather than inferred from a universal character list in this template.

## 13. Default Standard

Unless concrete organizational requirements demonstrate otherwise:

> **Identify the substantive work accurately and concisely. Define the meanings of classifications that people or automation rely on.**
>
> **Keep related branch, pull request, and issue identification consistent without forcing identical vocabularies or scopes.**
>
> **Keep work identity distinct from workflow state and authority. Preserve reliable interpretation when conventions change.**
