# Repository Work Identification Template

Stable template ID: `repository-work-identification`

Human-facing title:

> **Repository Work Identification Standard**

## Purpose

This template governs the identification and classification of repository work through branch names, pull request titles, and issue labels. These surfaces answer a shared question: what work does this artifact represent?

It provides durable semantic requirements while leaving vocabulary and syntax to adopters. It does not prescribe universal prefixes, Conventional Commits, a label taxonomy, or a repository host.

The reusable template is [`standard.md`](standard.md).

## Adoption

Adopt this template through deliberate review into an organization-owned canonical artifact. The adopted local standard governs within its assigned scope; this repository remains provenance and a possible source of improvements, not continuing authority over that artifact.

See [ADOPTION.md](../../ADOPTION.md) for the universal adoption and relationship model. Adoption does not itself authorize renaming existing branches, retitling pull requests, changing labels, or changing automation. It does not require retroactive normalization of historical work.

## Subject-specific adoption review

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. For this standard specifically, determine:

- which existing contribution rules, branch conventions, title checks, label definitions, or externally governed naming constraints already apply;
- whether PR-title syntax is enforced by tooling or consumed for other purposes, and whether the proposed standard conflicts with those meanings;
- whether current labels represent type, area, state, priority, risk, or mixed dimensions, and which existing systems govern any state or authority they express;
- which scripts, filters, dashboards, links, and automation depend on existing prefixes, title syntax, label names, combinations, or absence;
- whether adoption would add meaningful clarity or merely duplicate adequate conventions;
- what migration, compatibility checks, and validation any proposed identification changes would require, including how historical names and classifications can remain intelligible without mass renaming.

## Agent integration

Route human or automated implementation work to the adopted local artifact when creating or materially renaming an implementation branch, proposing or materially retitling a pull request, or creating, applying, changing, or rationalizing issue labels or classification. After adoption, that artifact governs within its assigned scope; the upstream `standards-templates` copy remains source material.

Adapt this optional snippet for `AGENTS.md` or an equivalent contributor/automation entry point. Replace `<local-standard-path>` with the adopted artifact's location. This section is informative routing guidance and requires neither a particular agent product nor an `AGENTS.md` file.

```text
Before identifying or classifying repository work through branch names, pull request titles, or issue labels, read and apply the organization's adopted Repository Work Identification Standard at <local-standard-path>. Use the applicable local conventions; this route does not prescribe a host, prefix vocabulary, title syntax, or label taxonomy, or confer execution authority.
```

## Applicability

The template applies across repository subjects, including software, research, publishing, standards, and operational artifacts. “Pull request” includes an equivalent reviewable change proposal, and “issue” includes an equivalent work item. Label rules apply to equivalent named category mechanisms when used for classification, not to every field in a tracking system.

A repository can adopt the standard without introducing labels where they provide no material value. It need not create a branch, pull request, and issue for every activity solely to satisfy the standard.

## Likely organization-specific review points

An adopter may need to define or adapt:

- the repositories and work surfaces in scope;
- readable branch syntax and any category vocabulary;
- plain-language or structured PR-title conventions;
- useful label dimensions, definitions, and application criteria;
- mappings between related classifications that use different vocabulary;
- documented interpretations used by automation;
- treatment of retained historical identification and consumer-sensitive changes.

Use existing contribution guidance and classification descriptions where sufficient. No separate schema, registry, or automation system is required.

## Boundary with neighboring standards

- [`repository-naming`](../repository-naming/) owns repository names, while [`filesystem-naming`](../filesystem-naming/) owns file and directory names.
- [`project-repository-model`](../project-repository-model/) owns repository responsibility, durable artifact placement, planning-state ownership, and repository separation.
- [`operational-execution-contract`](../operational-execution-contract/) owns execution authority, protected boundaries, scope expansion, and recovery. Identification or classification does not grant that authority.
- [`standards-adoption-model`](../standards-adoption-model/) owns deliberate organizational standards adoption.

These references clarify conceptual ownership without requiring sibling adoption. This template does not establish general task-management workflow, project status systems, assignment of people, prioritization methodology, release/version naming, or commit-message format. Labels can represent dimensions governed elsewhere without making this template their governing workflow or authority system.
