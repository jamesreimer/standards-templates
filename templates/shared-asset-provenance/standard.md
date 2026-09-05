# Shared Asset Provenance Standard

## 1. Purpose

This standard defines how relationships involving shared assets preserve source identity, provenance, maintenance meaning, and verifiable consumed state across repository, package, artifact, generation, installation, publication, adaptation, and similar boundaries.

Its purpose is to prevent:

- copied, generated, installed, adapted, or published material from becoming an accidental source of truth;
- mutable or ambiguous references from being mistaken for immutable consumed state;
- a valid immutable identifier from being mistaken for proof of source authority;
- local working-state changes from silently altering authoritative consumption;
- different relationship types from being maintained as though they had identical ownership or synchronization semantics;
- package or artifact consumers from being forced into repository-specific identity models when the consumed object already provides an equivalent immutable identity.

The central distinction is:

```text
source identity and authority
        ≠
Immutable Consumed Identity
        ≠
verification of the content actually consumed
```

Where Authoritative Consumption depends on all three, none substitutes for another.

## 2. Scope

This standard applies when an organization relies on material whose source, ownership, provenance, maintenance model, or exact consumed state crosses a repository, package, artifact, publication, generation, installation, adaptation, or comparable boundary.

Such material may include:

- shared repository tooling;
- reusable templates;
- copied or synchronized files;
- adapted configuration or policy material;
- generated files or artifacts;
- installed internal tooling;
- packages;
- schemas;
- container or image artifacts;
- release bundles;
- published contracts;
- reusable automation;
- other governed inputs whose source or consumed state materially affects a decision or result.

This standard does not require every repository, package, artifact, or dependency to maintain relationship metadata.

It does not determine:

- whether work should be separated into multiple repositories;
- whether reusable normative material becomes organizational authority;
- release or deployment lifecycle;
- authority to perform live operations;
- package-manager behavior;
- repository-host behavior;
- a universal manifest schema;
- one required provenance, attestation, lockfile, registry, or automation system.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, RFC 2119 and RFC 8174. Lowercase forms retain their ordinary English meaning.

## 3. Definitions

**Shared Asset**
A file, package, artifact, schema, template, contract, generated output, installed component, or other governed material whose source, maintenance, or use involves more than one ownership or lifecycle boundary.

**Source Identity**
The repository, registry, publisher, package source, artifact source, organization-controlled system, or equivalent source from which a Shared Asset is legitimately obtained.

**Consumer**
A repository, system, workflow, process, package, environment, or other controlled context that uses a Shared Asset.

**Authoritative Consumption**
Use of externally sourced material as governed input to validation, synchronization, generation, execution, approval, publication, decision-making, or another result whose correctness materially depends on the material consumed.

**Immutable Consumed Identity**
An identifier that uniquely binds the consumed object or state and cannot silently resolve to different content while retaining the same identity.

Examples may include:

- an exact repository revision;
- an immutable package version;
- a cryptographic digest;
- a checksum;
- a signed provenance record;
- an attestation;
- an immutable release identity;
- an image digest;
- an equivalent content-addressed or otherwise immutable object identifier.

**Moving Reference**
A locator whose resolved contents may change without the reference itself changing.

Examples may include:

- a branch;
- a mutable tag;
- a symbolic reference;
- an unpinned package constraint;
- a local path;
- a sibling directory;
- a nearby checkout;
- a mutable release alias;
- another locator that does not itself uniquely bind immutable content.

**Consumption Evidence**
Reviewable evidence establishing the relevant Source Identity, Immutable Consumed Identity, and correspondence between those identities and the content actually used.

**Exact Copy**
A downstream copy expected to remain materially identical to a declared source within its governed scope.

**Adapted Copy**
Material derived from a source but intentionally modified and owned or maintained according to local requirements.

**Bootstrap-Owned Copy**
Material copied from a source during initialization or setup whose continuing ownership transfers to the consumer after that event.

**Generated Material**
Material produced by a generator from one or more source inputs.

**Installed Material**
Material installed through a package, tool, distribution, synchronization, or similar mechanism.

**Contract Dependency**
Reliance on a published interface, schema, standard, API, package contract, artifact contract, or equivalent governed agreement rather than reliance on a copied source file.

**Relationship Record**
A human-readable or machine-readable record that describes a material source, provenance, maintenance, or consumption relationship.

## 4. Source and Consumer Responsibility

A Shared Asset whose authority or maintenance depends on an external source SHOULD have a clearly identifiable Source Identity.

A consumer MUST NOT treat an Exact Copy, Generated Material, Installed Material, or Bootstrap-Owned Copy as the authoritative upstream source merely because that material exists locally.

A consumer MAY become authoritative for locally owned material when ownership has legitimately transferred or the relationship explicitly establishes local authority.

Where ownership or maintenance responsibility differs from source provenance, the distinction SHOULD remain reviewable.

The existence of provenance does not require continuing upstream authority.

## 5. Authoritative Consumption

Authoritative Consumption MUST bind the governed input to:

1. an explicit Source Identity;
2. an appropriate Immutable Consumed Identity;
3. verification that the content actually consumed corresponds to the identified source and Immutable Consumed Identity.

The evidence mechanism MAY vary by object type and implementation.

A valid Immutable Consumed Identity establishes consumed state only.

It MUST NOT, by itself, establish:

- source authority;
- organizational adoption;
- acceptance;
- publication status;
- release status;
- deployment status;
- approval;
- trust;
- permission to execute or operate.

Any authority or lifecycle condition required for the governed use MUST be established separately.

## 6. Object-Appropriate Immutable Identity

The Immutable Consumed Identity used for Authoritative Consumption MUST be appropriate to the governed object.

Direct repository-source consumption MUST use an exact immutable repository revision or an equivalent repository-native identity that uniquely binds the consumed state.

A package, image, release, signed bundle, schema artifact, or other published object MAY use an immutable version, digest, checksum, attestation, signed provenance record, release identity, or another stable object identifier where that mechanism uniquely identifies the consumed object.

A consumer MUST NOT require a repository revision merely because the object originated from a repository when an equivalent immutable identity already uniquely binds the governed published object.

A version or label that may later resolve to different content MUST NOT be treated as immutable merely because it appears precise.

## 7. Moving References

A Moving Reference MAY be used to discover or locate a candidate source.

Before the resulting content is accepted for Authoritative Consumption, the Moving Reference MUST resolve to and be verified against an appropriate Immutable Consumed Identity.

The following MUST NOT, by themselves, be treated as proof of Source Identity or Immutable Consumed Identity:

- repository name;
- directory name;
- filesystem location;
- branch name;
- mutable tag;
- package range;
- local checkout presence;
- nearby copy;
- another locator whose contents may change without changing the locator.

Discovery and authority are separate concerns.

## 8. Working-State Integrity

When Authoritative Consumption reads directly from a working checkout, workspace, staging area, generated directory, or comparable mutable local context, Consumption Evidence MUST establish that the content used corresponds to the declared Immutable Consumed Identity.

Uncommitted, staged, untracked, regenerated, substituted, patched, or otherwise locally altered content that can affect the governed result MUST either:

- be excluded from Authoritative Consumption; or
- be explicitly identified and governed as non-authoritative working state.

A workflow MUST NOT silently claim immutable-source consumption while materially relying on local content that differs from the content identified by the declared Immutable Consumed Identity.

This requirement does not prohibit working-state testing, development, or experimentation. It requires that such state not masquerade as immutable authoritative input.

## 9. Relationship Semantics

A material relationship SHOULD be classified clearly enough that a maintainer or consuming system can determine:

- who owns the current material;
- whether exact correspondence with a source is expected;
- whether local adaptation is intentional;
- whether the material is generated;
- whether it is installed or package-managed;
- whether ownership transferred after bootstrap;
- whether the dependency is contractual rather than copy-based;
- whether the relationship is Authoritative Consumption or impact/discovery information only.

An organization MAY use local names or machine-readable values for these relationship classes.

This standard does not require one universal enumeration.

Where different relationship classes would produce materially different update or validation behavior, they MUST NOT be treated as interchangeable.

## 10. Exact Copies

An Exact Copy SHOULD identify the source material from which exact correspondence is expected.

When exact correspondence is a required condition, verification MUST compare the governed downstream content against content uniquely bound by the declared Immutable Consumed Identity.

An Exact Copy MUST NOT be silently modified and still represented as exact.

If intentional local divergence becomes legitimate and durable, the relationship SHOULD be reclassified to reflect that changed ownership or maintenance model.

## 11. Adapted Copies

An Adapted Copy SHOULD preserve sufficient provenance to identify its source where that history remains materially useful.

An Adapted Copy MUST NOT be automatically overwritten as though it were an Exact Copy unless the adaptation has been intentionally discarded through a legitimate change decision.

An Adapted Copy does not require continuous byte-level correspondence with its source.

Where a review or adaptation decision depends on an exact upstream state, that source state SHOULD be bound to an Immutable Consumed Identity.

## 12. Bootstrap-Owned Material

Bootstrap-Owned Copy relationships SHOULD distinguish:

- historical source provenance; from
- continuing ownership after bootstrap.

After ownership has legitimately transferred, the consumer MAY maintain the material independently.

The historical source MUST NOT be treated as continuing maintenance authority merely because the material originated there.

Where a bootstrap decision depends on an exact source state, that state SHOULD be bound to an appropriate Immutable Consumed Identity.

## 13. Generated Material

Generated Material MUST have enough relationship information to prevent generated output from being mistaken for an authoritative source when its meaning depends on upstream inputs or generator behavior.

When Generated Material participates in Authoritative Consumption, Consumption Evidence MUST identify whichever of the following materially affect the governed result:

- authoritative source inputs;
- the generator or generator version;
- relevant generator configuration;
- the Immutable Consumed Identity of generated output when the output is independently consumed as an immutable artifact.

Not every generated file requires all of these identities.

The required evidence depends on which elements can materially change the governed result.

## 14. Installed Material

Installed Material SHOULD preserve enough source and identity information to determine what was installed and from where when that distinction affects maintenance, verification, security, or governed use.

Package-manager lockfiles, artifact manifests, release records, image digests, checksums, attestations, or equivalent mechanisms MAY provide some or all of this evidence.

Installed Material MUST NOT be treated as though its local installation path proves its Source Identity or Immutable Consumed Identity.

When Installed Material participates in Authoritative Consumption, the Source Identity, Immutable Consumed Identity, and content-verification requirements of this standard apply regardless of how the material was installed.

## 15. Contract and Published-Artifact Dependencies

A Contract Dependency SHOULD identify the governed contract or artifact precisely enough that the consumer can determine what compatibility or obligation it relies upon.

A Contract Dependency does not become a copied-source relationship merely because the contract or artifact originated from another repository.

Where Authoritative Consumption depends on an exact published contract or artifact, the consumer MUST identify that object through an appropriate Immutable Consumed Identity.

Repository revision identity is unnecessary when the governed published object already exposes an equivalent immutable identity.

## 16. Impact-Only Relationships

A relationship MAY be recorded solely to identify:

- downstream impact;
- maintenance follow-up;
- review candidates;
- possible synchronization work;
- dependency awareness.

Such a relationship is not Authoritative Consumption unless its contents are themselves accepted as governed input to a consequential result.

Impact discovery MAY therefore use weaker locator information than Authoritative Consumption, provided the weaker information is not misrepresented as proof of exact consumed state.

## 17. Relationship Records

An organization SHOULD maintain a Relationship Record when the relationship's meaning materially affects maintenance, verification, ownership, synchronization, or Authoritative Consumption and that meaning would otherwise be ambiguous.

A Relationship Record MAY be:

- prose documentation;
- a machine-readable manifest;
- a lockfile;
- an attestation;
- a release or deployment record;
- package metadata;
- an artifact manifest;
- a generation record;
- a standards or governance record;
- another durable mechanism appropriate to the relationship.

No particular filename, directory, schema, field name, serialization format, or storage system is required.

Where automation depends on a Relationship Record, the record SHOULD be machine-readable to the extent necessary for that automation.

A Relationship Record SHOULD identify only information needed to preserve the governed relationship and SHOULD NOT become a speculative metadata system.

Where a relationship participates in Authoritative Consumption, use of a separately designated Relationship Record remains optional, but required Consumption Evidence MUST still be reviewable through an appropriate durable mechanism.

## 18. Automation

Automation MAY use relationship information to:

- identify affected consumers;
- verify exact copies;
- surface adapted copies for review;
- regenerate generated material;
- verify installed or package-managed state;
- check contract dependencies;
- validate Immutable Consumed Identity;
- verify source/content correspondence.

Automation MUST respect the declared maintenance semantics of the relationship.

It MUST NOT:

- overwrite Adapted Copies as though they were Exact Copies;
- overwrite Bootstrap-Owned material merely because an upstream source still exists;
- treat Contract Dependencies as copied files;
- treat a Moving Reference as immutable proof;
- accept unverified content as authoritative merely because relationship metadata exists.

Automation performing Authoritative Consumption MUST fail closed when it cannot verify a required Source Identity, Immutable Consumed Identity, or content correspondence.

Failing closed does not require destructive rollback. It requires withholding the governed success, approval, synchronization, generation, execution, or other authoritative conclusion that depended on the unverified input.

## 19. Exceptions

An exception MAY alter ordinary relationship-recording, maintenance, or verification mechanisms when the adopting organization has a legitimate reason to use an equivalent control.

An exception MUST NOT silently remove a Source Identity, Immutable Consumed Identity, or content-verification requirement when Authoritative Consumption depends on that requirement for correctness.

Where a mandatory protection cannot be met and no equivalent protection exists, the affected consumption MUST remain non-authoritative or unresolved.

An exception SHOULD identify:

- the affected relationship;
- the normal rule being departed from;
- the reason for the departure;
- the equivalent protection, if any;
- the scope and duration where relevant.

## 20. Evidence and Verification

Verification SHOULD be proportionate to the consequence of the governed relationship.

Depending on the relationship, useful evidence may include:

- exact revision verification;
- content digest comparison;
- package lock or resolution evidence;
- signature or attestation verification;
- generated-output reproducibility;
- source and downstream comparison;
- artifact digest verification;
- relationship-record review;
- checks that local working state cannot silently alter authoritative input;
- manual provenance review where automation is not justified.

Evidence MUST support the claim actually being made.

For example:

- a matching repository name is not proof of Source Identity;
- a branch name is not proof of Immutable Consumed Identity;
- a recorded digest is not proof that the consumed content was actually verified against that digest;
- a source revision is not proof of organizational authority;
- a Relationship Record is not proof that its declared relationship is true.

## 21. Boundaries with Related Standards

This standard governs relationship meaning, provenance, and verifiable consumed state.

It does not determine organizational standards adoption. A reusable source may remain provenance without retaining authority after adoption.

Where adopted normative material is also governed by an organizational adoption standard, this standard's provenance and consumed-state requirements complement rather than replace adoption-specific authority and provenance requirements.

It does not determine repository topology. Repository separation may create relationships governed here, but this standard does not decide whether separation is justified.

It does not define publication or deployment lifecycle. Published artifacts may participate in governed relationships without making publication state part of this standard.

It does not grant authority for live operational execution. An execution process may consume provenance evidence without deriving execution authority from that evidence.

## 22. Anti-Patterns

Avoid:

- treating a local copy as authoritative merely because it is convenient;
- treating provenance as continuing upstream authority;
- treating a branch, mutable tag, path, or nearby checkout as Immutable Consumed Identity;
- treating an immutable identifier as proof of authority or approval;
- verifying an expected revision while consuming different local content;
- forcing package or artifact consumers to prove an unrelated repository revision;
- applying exact-copy synchronization to adapted material;
- treating bootstrap provenance as continuing upstream ownership;
- treating generated output as its own source when generator inputs materially determine meaning;
- treating every dependency as a file-copy relationship;
- creating mandatory relationship metadata where no meaningful relationship consequence exists;
- creating a universal manifest schema merely to standardize representation;
- allowing metadata presence to substitute for verification;
- using impact-discovery relationships as Authoritative Consumption evidence without the required identity and content proof.

## 23. Default Standard

Unless concrete organizational requirements demonstrate otherwise:

> **Identify the competent source for governed shared material.**
>
> **When externally sourced material participates in Authoritative Consumption, bind it to an appropriate Immutable Consumed Identity and verify that the content actually used corresponds to the declared Source Identity and Immutable Consumed Identity.**
>
> **Do not treat source authority, Immutable Consumed Identity, and physical content verification as interchangeable evidence.**
>
> **Use object-appropriate immutable identity rather than forcing repository-specific identity onto packages or artifacts that already expose an equivalent immutable identity.**
>
> **Treat Moving References as discovery mechanisms until they resolve to verified immutable state.**
>
> **Keep exact, adapted, generated, installed, bootstrap-owned, contractual, and impact-only relationships distinct when their maintenance or authority consequences differ.**
>
> **Do not let local working state silently masquerade as immutable authoritative input.**
>
> **Use Relationship Records and automation only where they protect a demonstrated relationship consequence, and do not require one universal representation.**
>
> **Fail closed when Authoritative Consumption cannot verify the identity or content evidence on which the governed result depends.**
