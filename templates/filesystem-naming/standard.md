# File and Directory Naming Standard

## 1. Purpose

This standard defines default rules for naming files, directories, and path components so that version-controlled material remains readable, portable, automatable, and resilient across common operating systems and filesystems.

The same principles may apply to software, media production, research, standards, publishing, infrastructure, documentation, archives, operations, and other version-controlled work.

The standard governs filesystem-visible names. It does not prescribe the naming of repositories, branches, tags, packages, services, products, productions, publications, or other neighboring identities except where those identities must remain distinct from filenames or directory names.

## 2. Scope

This standard applies to human-managed files and directories unless a language, framework, operating system, tool, external format, or generated artifact imposes a legitimate conflicting convention.

It governs:

- file and directory name syntax;
- case and separators;
- filename extensions;
- path-component portability;
- reserved names and characters;
- transient-state naming;
- dates, sequence numbers, and version-like suffixes;
- case-only and normalization-sensitive collisions;
- conventional and tool-owned exceptions;
- rename considerations.

It does not require an organization to rename externally supplied, generated, or tool-managed material merely to make it stylistically uniform.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, RFC 2119 and RFC 8174. Lowercase forms retain their ordinary English meaning.

## 3. Name for the Durable Subject

A file or directory SHOULD be named for the durable artifact, subject, grouping, or responsibility it represents.

Do not name material primarily for transient workflow state, a temporary location in a process, or incidental content that is likely to change while the artifact remains the same thing.

Prefer names such as:

```text
semantic-architecture.md
contract-architecture.md
production-notes/
release-assets/
research-sources/
```

over names such as:

```text
new-notes.md
final-final.md
old-assets/
working-stuff/
misc/
```

Names SHOULD remain useful after ordinary edits, review, promotion, archival, or movement through a workflow.

## 4. Default Syntax

For ordinary human-managed files and directories, the default naming form SHOULD be:

```text
lowercase ASCII words separated by single hyphens
```

Examples:

```text
project-overview.md
camera-notes.md
source-material/
client-deliverables/
```

Unless a legitimate convention requires otherwise, names SHOULD:

- use lowercase ASCII letters `a-z` and digits `0-9`;
- use a single hyphen `-` to separate words;
- avoid spaces;
- avoid underscores and other punctuation in ordinary prose-like names;
- avoid consecutive separators;
- avoid leading or trailing separators;
- remain concise enough that full paths stay readable and portable.

This is a synthesized portability and consistency convention, not a claim that all filesystems require lowercase or hyphen-separated names.

## 5. Legitimate Exceptions to the Default Syntax

The default syntax MUST NOT override a stronger technical or ecosystem requirement.

Legitimate exceptions include:

- language or framework conventions, such as source files that conventionally use `snake_case`, `PascalCase`, or another required form;
- conventional repository files such as `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, or `SECURITY.md`;
- intentionally prominent root-level repository governance or guidance documents such as `ADOPTION.md`, `CATALOG.md`, `NAMING.md`, or `MAINTAINING.md` when the repository has deliberately established that convention;
- tool-owned paths such as `.gitignore`, `.github/`, or other dotfiles and metadata directories;
- files whose names are defined by an external specification or delivery system;
- generated files whose names are controlled by the generating system;
- externally supplied assets whose original names MUST be preserved for provenance, compatibility, or contractual reasons.

An exception SHOULD exist because another legitimate owner or convention requires it, not because individual contributors prefer inconsistent styling.

## 6. Files and Directories Share a Baseline but Not an Identity

Files and directories use the same portability baseline, but they name different things.

A directory SHOULD name a durable grouping, boundary, collection, or responsibility.

A file SHOULD name the durable artifact or content unit it represents.

Do not force directory context into every filename when the path already supplies it clearly.

For example, prefer:

```text
contracts/
    reference.md
    context.md
```

when those names are unambiguous in context, rather than mechanically repeating:

```text
contracts/
    reference-contract.md
    context-contract.md
```

Conversely, include enough context in a filename when the file is likely to be copied, exported, attached, or encountered outside its parent directory and would otherwise become ambiguous.

## 7. Filename Extensions

A file SHOULD use a filename extension when the extension materially communicates the file's format or is required by the platform or toolchain.

Extensions SHOULD ordinarily be lowercase unless an external convention requires otherwise.

Prefer one meaningful extension:

```text
project-brief.md
source-data.csv
production-still.jpg
```

Multiple extensions MAY be used when they represent a real layered format or established convention, such as:

```text
archive.tar.gz
```

Do not use extension-like suffixes merely to encode workflow state.

## 8. Portability and Reserved Names

Names MUST satisfy the requirements of the operating systems, filesystems, synchronization systems, archive formats, repository hosts, and delivery environments that legitimately need to process them.

For conservative cross-platform use, avoid the Windows-reserved characters:

```text
< > : " / \ | ? *
```

Avoid ASCII control characters and path-separator characters.

Do not use `.` or `..` as ordinary path-component names.

Do not end a file or directory name with a space or period.

Avoid widely reserved Windows device names, including these names even when followed by an extension:

```text
con
prn
aux
nul
com1 ... com9
lpt1 ... lpt9
```

Organizations MAY impose additional reserved-name rules for their target platforms.

## 9. Case and Collision Safety

Do not rely on case alone to distinguish sibling files or directories.

Avoid structures such as:

```text
Report.md
report.md
```

or:

```text
Assets/
assets/
```

Some filesystems are case-sensitive while others are case-insensitive by default. A repository that depends on case-only distinctions can therefore behave differently across environments.

Lowercase-by-default naming reduces this ambiguity but does not eliminate the need to treat paths consistently.

When performing a case-only rename in version control, verify that the rename is recorded correctly on case-insensitive systems and use an intermediate name where necessary.

## 10. Unicode and Normalization

ASCII SHOULD be the default for portable machine-facing paths when non-ASCII characters do not carry necessary meaning.

An organization MAY permit Unicode filenames when language, culture, publishing, media, archival, or domain requirements justify them.

Where Unicode is permitted:

- use one documented normalization convention where tooling permits;
- avoid visually confusable names in the same directory;
- do not rely on Unicode normalization variants to distinguish files;
- verify compatibility with synchronization, archive, build, delivery, and downstream systems.

ASCII is a portability default, not a statement that non-English or non-ASCII names are inherently improper.

## 11. Dates, Sequence Numbers, and Ordering Prefixes

Dates, sequence numbers, and ordering prefixes SHOULD appear in a name only when they are part of the durable identity or required ordering of the artifact.

When a calendar date legitimately belongs in a filename, prefer ISO-style ordering:

```text
YYYY-MM-DD
```

Example:

```text
2026-08-27-production-log.md
```

Avoid locale-dependent forms such as:

```text
08-27-26
27-08-26
August-27-2026
```

unless a domain-specific convention legitimately requires them.

Numeric ordering prefixes MAY be used when order is meaningful and stable. Use consistent zero-padding when lexical sorting must preserve numerical order:

```text
01-introduction.md
02-method.md
10-appendix.md
```

Do not add sequence numbers merely to impose cosmetic order on material whose ordering is not semantically meaningful.

## 12. Versions and Lifecycle State

Transient lifecycle state SHOULD NOT be encoded into durable file or directory names.

Avoid names such as:

```text
final.md
final-final.md
new.md
old.md
latest.md
approved-copy.md
archive-old/
```

Use version control, document metadata, workflow state, issue tracking, approval systems, or archival metadata for mutable state whenever those systems legitimately own it.

Version identifiers MAY appear in filenames when multiple independently meaningful versions must coexist as distinct artifacts outside ordinary version-control history or when an external delivery convention requires them.

Do not use `v2`, `v3`, or similar suffixes merely as a substitute for version control.

## 13. Hidden Files and Special Prefixes

A leading period SHOULD be used only when a hidden or tool-recognized path is intentionally required.

Do not use dot-prefixed names merely to make ordinary project material visually disappear.

Avoid leading hyphens for ordinary filenames because command-line tools may interpret them as options.

Other special prefixes SHOULD be reserved for documented conventions with real semantic or tooling value.

## 14. Path Depth and Redundant Context

Names SHOULD be evaluated as parts of full paths, not in isolation.

Avoid unnecessary repetition between parent directories and child names.

Avoid deep hierarchies created solely to encode categories that are not useful boundaries.

However, do not optimize for the shortest possible path at the cost of ambiguity or loss of meaningful structure.

The goal is a path whose components each contribute useful identity or organization.

## 15. Rename Criteria

A file or directory SHOULD be renamed when its existing name has become materially misleading, violates an adopted naming rule in a way that creates real operational cost, or no longer identifies the durable artifact or grouping accurately.

A file or directory SHOULD NOT be renamed solely for cosmetic consistency when the rename would create disproportionate migration cost and the existing name remains clear and safe.

Before renaming a path that may be referenced elsewhere:

1. audit links, imports, scripts, automation, manifests, media references, documentation, and external integrations;
2. identify consumers that do not automatically follow version-control history;
3. perform the rename through version control so history remains traceable;
4. update canonical references and relationship metadata where applicable.

Rename cost depends on how broadly the path has escaped the repository boundary.

## 16. Boundary with Other Naming Standards

This standard governs files, directories, and path components.

Repository naming is governed separately by the `repository-naming` standard.

It does not automatically govern:

- repository names;
- branch or tag names;
- package or service names;
- database identifiers;
- product or brand names;
- project, production, or publication titles;
- template IDs inside a template library.

Related naming standards SHOULD remain separate when their constraints and consequences differ materially.

## 17. Anti-Patterns

Avoid:

- spaces and gratuitous punctuation in portable machine-facing paths;
- relying on case alone to distinguish siblings;
- Windows-reserved names or characters in cross-platform material;
- trailing spaces or periods;
- names such as `misc`, `stuff`, `new`, `old`, `latest`, or `final-final` as substitutes for meaningful identity or lifecycle metadata;
- version-number suffixes used merely to avoid version control;
- unnecessary repetition of parent-directory context;
- unexplained abbreviations used only to shorten names;
- hidden-file prefixes without a real hidden/tooling requirement;
- renaming widely referenced paths for cosmetic preference alone;
- forcing externally defined or tool-owned filenames into a house style that breaks interoperability.

## 18. Basis and External Constraints

This standard combines external filesystem constraints with organization-neutral naming decisions.

The external sources establish compatibility facts; they do not by themselves define every naming convention in this standard.

### POSIX

POSIX defines a portable filename character set and notes that applications should avoid filenames beginning with a hyphen because of command-line ambiguity.

Source: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html

POSIX also requires portable filenames to use the portable filename character set.

Source: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html

### Windows

Microsoft documents reserved filename characters, reserved device names, case-insensitivity concerns, trailing-space/period behavior, and path-length variability across Windows filesystems and APIs.

Source: https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file

### Apple filesystems

Apple recommends treating paths as case-sensitive in code and including filename extensions. Its archived APFS FAQ documents that APFS preserves case and normalization on disk, may be case-sensitive or case-insensitive, and provided normalization-insensitive lookup behavior in the specified macOS and iOS versions.

Sources:

- https://developer.apple.com/documentation/technologyoverviews/files-and-directories
- https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html

### Synthesized conventions

The following are standards decisions rather than claims that every filesystem requires them:

- lowercase as the ordinary default;
- single-hyphen word separation;
- ASCII as the ordinary portable baseline;
- durable-subject naming;
- avoiding transient lifecycle state;
- ISO-style dates when dates belong in names;
- minimizing redundant path context;
- treating tool, language, ecosystem, generated, and external names as legitimate exceptions.

An adopting organization MAY strengthen these conventions or define domain-specific exceptions where concrete requirements justify them.

## 19. Default Standard

Unless concrete organizational or domain requirements demonstrate otherwise:

> **Name files and directories for the durable artifact, subject, grouping, or responsibility they represent rather than transient workflow state.**
>
> **Use lowercase ASCII alphanumerics with single hyphens as the ordinary default for human-managed names, while preserving legitimate tool, language, ecosystem, generated, and external conventions.**
>
> **Avoid spaces, reserved characters, reserved device names, trailing spaces or periods, and case-only sibling distinctions in material expected to work across platforms.**
>
> **Use meaningful filename extensions and keep extension casing consistent unless another legitimate convention requires otherwise.**
>
> **Use dates, sequence numbers, and version identifiers only when they are part of the artifact's durable identity or required ordering, not as substitutes for version control or workflow state.**
>
> **Treat Unicode as a legitimate option when the domain requires it, but verify normalization and downstream compatibility rather than assuming all filesystems behave identically.**
>
> **Evaluate names in the context of their full path, avoiding both redundant repetition and unnecessary hierarchy.**
>
> **Rename when a path becomes materially misleading or operationally harmful, and audit references before changing widely consumed paths.**
