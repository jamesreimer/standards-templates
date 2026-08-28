# Repository Naming Standard

## 1. Purpose

This standard defines default rules for naming version-control repositories so that repository identities remain clear, durable, portable, and appropriately scoped over time.

It is intentionally domain-neutral. A repository may contain software, media-production material, research, standards, publishing content, infrastructure, documentation, automation, operational artifacts, or other version-controlled work.

The standard governs repository identity. It does not prescribe how files, directories, branches, packages, products, productions, services, or other neighboring entities are named except where those identities must be distinguished from the repository name.

## 2. Scope

This standard applies when creating or renaming repositories unless an organization has a documented reason to adopt a different convention.

It governs:

- repository-name syntax;
- repository identity and scope;
- use of organizational namespaces;
- topology or responsibility qualifiers;
- provisional names;
- lifecycle-state naming;
- repository-family naming;
- public-name collision considerations;
- rename criteria and migration considerations.

It does not determine whether a repository should exist. Repository creation and separation are separate responsibility and topology decisions.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, RFC 2119 and RFC 8174. Lowercase forms retain their ordinary English meaning.

## 3. Repository Identity Is Distinct from Neighboring Identities

A repository name identifies the repository's durable responsibility or coherent unit of work.

Do not assume that any of the following must use the same name:

```text
organization
project or initiative
product or brand
production or publication title
repository
package or library
service or deployment
artifact
```

These identities may align when that is useful, but one SHOULD NOT silently dictate another.

A repository may retain a stable descriptive identity while a project uses a working title, a product later acquires a brand, or an implementation topology changes.

## 4. Name for the Durable Subject

Repository names SHOULD describe the durable subject, responsibility, or coherent unit the repository exists to serve.

Do not name a repository for an incidental implementation detail, temporary workflow, current storage mix, or short-lived phase unless that characteristic is itself the repository's durable purpose.

Prefer:

```text
standards-templates
customer-portal
feature-film-title
research-archive
```

over names that enumerate today's contents or transient implementation details.

When a repository intentionally contains several responsibilities, name it for the coherent organizational, project, product, production, operational, or archival unit those responsibilities collectively serve rather than enumerating the contents.

## 5. Organizational Namespace

The repository owner or organization namespace ordinarily communicates organizational ownership.

Repository names SHOULD NOT repeat the organization name merely to restate information already present in the namespace.

Prefer:

```text
organization/documentary-archive
organization/standards
```

over:

```text
organization/organization-documentary-archive
organization/organization-standards
```

An organization MAY include its name in a repository identity when the repository is intentionally expected to retain that identity outside the owner namespace, such as through mirroring, distribution, transfer, or another demonstrated requirement.

## 6. Technical Syntax and Portability

Repository names SHOULD use a conservative syntax that remains readable in URLs, shells, automation, and common repository hosts.

Unless an adopting organization defines a stricter rule, repository names SHOULD:

- use lowercase ASCII letters `a-z` and digits `0-9`;
- use a single hyphen `-` to separate words;
- begin and end with an ASCII letter or digit;
- avoid spaces, underscores, periods, and other punctuation;
- avoid consecutive separators;
- contain no more than 64 characters;
- avoid names reserved by likely repository hosts or operating environments.

Examples of widely reserved system names include:

```text
con
prn
aux
nul
com1 ... com9
lpt1 ... lpt9
```

Repository names MUST also satisfy the requirements of the repository host actually in use.

The 64-character recommendation is a conservative portability baseline, not a universal platform law. An organization MAY impose a stricter limit.

Lowercase is a consistency and ambiguity-reduction convention. It is not presented as a requirement imposed by every repository host.

## 7. Responsibility and Topology Qualifiers

A suffix or qualifier SHOULD appear only when it expresses a real, durable repository distinction.

Examples that require justification include:

```text
-api
-web
-service
-infrastructure
-docs
-architecture
-management
-archive
-monorepo
```

Do not encode speculative topology into repository identity.

For example, do not create `project-api` merely because an API is currently expected if the repository's durable responsibility is actually the broader project or product.

`-monorepo` is discouraged by default because it describes current repository topology rather than the subject the repository serves. Use it only when monorepo topology itself is a durable identity needed to distinguish the repository from legitimate siblings.

Whether an additional repository is justified is separate from what that repository should be named and is outside this standard's scope. Software projects MAY use the `project-repository-model` standard for that software-specific responsibility question. Other domains SHOULD apply criteria appropriate to their own artifacts, ownership, distribution, and lifecycles.

## 8. Lifecycle State and Provisional Names

Transient lifecycle state SHOULD NOT be encoded in a durable repository name.

Avoid suffixes or qualifiers such as:

```text
-wip
-new
-old
-legacy
-deprecated
-archived
-obsolete
```

Lifecycle state belongs in repository-host metadata, archive controls, topics, status fields, documentation banners, or another mechanism designed to change without renaming the repository.

Version-like repository suffixes such as `-v2` SHOULD also be avoided when they merely indicate a temporary generation of the same durable repository responsibility. They MAY be used when the versions are intentionally distinct long-lived repositories with independent identities and lifecycles.

A descriptive working or provisional repository name is acceptable when a final project, product, production, or brand name has not yet been earned.

A provisional name SHOULD:

- accurately describe the repository's current durable subject;
- avoid pretending to be final branding;
- avoid unexplained acronyms or codenames unless the codename itself is the legitimate working identity;
- be marked as provisional in repository documentation when that status could otherwise be misleading.

Do not block useful work merely to invent final branding for a repository.

## 9. Repository Families

Related repositories MAY share a common prefix or subject name when that relationship is real and useful for discovery.

For example:

```text
publication
publication-assets
publication-archive
```

or:

```text
platform
platform-infrastructure
```

Each member of a repository family MUST still have an independently intelligible responsibility.

Do not manufacture a common prefix merely to make unrelated repositories appear coordinated.

Do not use numbering alone as the primary distinction between sibling repositories when a responsibility-based distinction exists.

## 10. Public Identity and Collision Review

Before establishing a public repository name intended to become recognizable outside the organization, an organization SHOULD review whether the name:

- creates substantial ambiguity with a prominent existing project, product, organization, or repository;
- could imply an affiliation that does not exist;
- conflicts with an established public identity the organization needs to distinguish from;
- raises trademark or naming concerns appropriate to the intended use.

This review SHOULD be proportionate to the repository's public significance. An internal operational repository does not require the same naming diligence as a public project intended for broad distribution.

## 11. Rename Criteria and Migration

A repository SHOULD be renamed when its existing name has become materially misleading about its durable subject, responsibility, or legitimate identity.

A repository SHOULD NOT be renamed merely for stylistic preference once the existing name remains accurate and understandable.

Before renaming an established repository:

1. verify the current host's redirect and rename behavior;
2. audit hardcoded repository references in automation, CI, documentation, packages, dependencies, integrations, mirrors, and external systems;
3. identify references that do not follow host-level redirects;
4. update repository relationships and canonical documentation as needed;
5. avoid reusing the prior repository name where doing so would invalidate redirects or create ambiguity.

Renaming cost is environment-dependent. Do not assume that a rename is either free or catastrophic.

For example, GitHub redirects most web and Git traffic after a repository rename, but actions referenced from a renamed repository are not redirected, and reusing the old repository name breaks the redirect relationship.

## 12. Boundary with Other Naming Standards

This standard governs repository names only.

File and directory names and path components are governed separately by the `filesystem-naming` standard.

It does not automatically govern:

- file and directory names;
- branch or tag names;
- package names;
- service names;
- product or brand names;
- project or production titles;
- template IDs inside a template library.

Related naming standards SHOULD remain separate when their constraints and consequences differ materially.

## 13. Anti-Patterns

Avoid:

- using a temporary lifecycle state as part of permanent repository identity;
- repeating the organization name without a demonstrated need;
- encoding speculative implementation topology in the name;
- naming a broad repository by enumerating its current contents;
- using unexplained abbreviations solely to shorten a name;
- using `-management`, `-architecture`, `-docs`, `-api`, `-service`, or similar qualifiers without an earned repository responsibility;
- using `-monorepo` merely to describe current topology;
- forcing project, product, brand, package, and repository identities to use one string;
- using a public name that misleadingly implies affiliation;
- renaming stable repositories for cosmetic preference alone;
- relying on host redirects without auditing integrations that may not follow them.

## 14. Basis and External Constraints

This standard combines external platform constraints with organization-neutral naming decisions.

The external sources establish compatibility facts; they do not by themselves define the semantic naming rules in this standard.

### GitHub

GitHub currently permits repository names of up to 100 characters using ASCII letters, digits, `.`, `-`, and `_`.

Source: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository

GitHub documents rename redirects for most repository traffic, while noting that calls to GitHub Actions hosted in a renamed repository are not redirected and that reusing the old repository name breaks existing redirects.

Source: https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository

### Azure DevOps

Azure DevOps currently limits Git repository names to 64 Unicode characters, requires uniqueness within the Azure DevOps project, disallows several special characters and system-reserved names, and discourages spaces.

Source: https://learn.microsoft.com/en-us/azure/devops/organizations/settings/naming-restrictions?view=azure-devops

### Windows reserved names

Windows reserves device-like names including `CON`, `PRN`, `AUX`, `NUL`, `COM1` through `COM9`, and `LPT1` through `LPT9`, including some related variants.

Source: https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file

### Synthesized conventions

The following are standards decisions rather than claims that every host requires them:

- lowercase naming;
- kebab-case with single hyphens;
- a 64-character portability default;
- durable-subject naming;
- avoiding transient lifecycle state;
- avoiding speculative topology;
- organizational namespace discipline;
- repository-family semantics;
- rename criteria.

An adopting organization MAY strengthen these conventions but SHOULD NOT weaken them accidentally merely because its current repository host permits a broader syntax.

## 15. Default Standard

Unless concrete organizational requirements demonstrate otherwise:

> **Name repositories for their durable subject, responsibility, or coherent unit of work rather than transient implementation detail or lifecycle state.**
>
> **Use lowercase ASCII alphanumerics with single hyphens as the default syntax, and prefer names of 64 characters or fewer.**
>
> **Do not repeat organizational identity already expressed by the repository-owner namespace without a demonstrated reason.**
>
> **Add topology or responsibility qualifiers only when they describe an earned and durable repository distinction.**
>
> **Keep lifecycle state out of repository names and express it through mutable host or documentation metadata instead.**
>
> **Allow descriptive provisional names when final branding or titles are unresolved rather than blocking useful work or inventing premature identity.**
>
> **Treat repository identity as distinct from project, product, brand, production, package, service, and artifact identity.**
>
> **Review public repository names for material ambiguity, misleading affiliation, and appropriate trademark concerns.**
>
> **Rename only when the existing identity becomes materially misleading, and audit host redirects and external references before relying on the rename.**
