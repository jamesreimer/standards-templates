# Organizational Standards Adoption and Ownership Policy

## 1. Purpose

This policy defines the default requirements for adopting standards, policies, templates, or other normative material from an external or reusable source into organizational authority.

Its purpose is to preserve legitimate organizational governance, provenance, and independent lifecycle while allowing organizations to reuse good source material without creating accidental continuing authority outside the organization.

## 2. Scope

This policy applies when an organization adopts normative source material that was created outside the organization's own authoritative standards source.

Examples include:

- public standards templates;
- personal or independently maintained templates;
- material from another organization;
- reusable internal templates maintained outside the adopting standards source;
- prior standards used as source material for a new organizational standard.

This policy governs adoption, canonical governance, provenance, and later upstream changes.

It does not prescribe the exact approval workflow, repository topology, synchronization tooling, or content of the adopted standard.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in uppercase, they are to be interpreted as described in BCP 14, RFC 2119 and RFC 8174. Lowercase forms retain their ordinary English meaning.

## 2.2 Organizational Ownership

In this policy, **organizational ownership** or **canonical ownership** means responsibility for the adopted artifact's organizational authority, scope, interpretation, and lifecycle.

It does not by itself mean that copyright or other intellectual-property rights in the source material transfer to the adopting organization. Those rights remain governed separately by applicable law, license terms, assignments, and other legal instruments.

## 3. Core Principle

Reusable source material does not become organizational authority merely because it is available, useful, copied, or historically followed.

The default relationship is:

```text
external or reusable source material
        ↓ deliberate organizational adoption
organizational canonical standard
        ↓ independent lifecycle
later upstream change
        ↓ review candidate
accept / adapt / reject
```

Adoption creates a normative artifact governed canonically by the adopting organization.

The upstream source remains provenance and a possible source of later improvements, not continuing authority over the adopted standard.

## 4. Deliberate Adoption

An organization MUST make an affirmative adoption decision before external or reusable source material is treated as an organization-owned standard.

Copying material into an organization repository, linking to it, or using it operationally does not by itself establish organizational authority.

The adoption decision SHOULD establish at minimum:

- which artifact is being adopted;
- the organizational scope for which it will govern;
- the organization-controlled canonical location of the adopted result;
- the organizational role or process authorized to adopt it.

Exact approval mechanics MAY vary by organization.

## 5. Canonical Governance After Adoption

Once adopted, the organizational artifact becomes canonical for the scope assigned by the organization.

The adopting organization controls:

- the standard's organizational authority within that scope;
- its lifecycle;
- later modifications;
- supersession or withdrawal decisions;
- any organization-specific interpretation legitimately assigned to the standards owner.

The adopting organization MUST NOT treat the external source as retaining continuing authority merely because the adopted artifact originated there.

An organization SHOULD NOT depend on a personal or unrelated external repository as the canonical source of its own governing standard unless the organization has deliberately established that source as legitimate authority.

## 6. Provenance

An adopted standard SHOULD retain enough provenance to identify the source material from which it was adopted.

Useful provenance may include:

- source repository or publication;
- source path or artifact identity;
- source revision or release;
- content digest where useful;
- adoption date or organizational adoption record where useful.

When the adopted source can change, the adoption record MUST identify an immutable source revision, release, edition, or content digest sufficient to determine what material was reviewed.

Provenance records origin.

Provenance does not confer continuing upstream authority.

Attribution required by an applicable license remains a separate legal obligation and is not replaced by this policy.

## 7. Independent Lifecycle

The adopting organization MUST govern an adopted standard under a lifecycle independent from its upstream source unless it has explicitly established a different authority relationship.

Therefore:

- the adopting organization MUST NOT treat an upstream modification as automatically changing the organizational standard;
- the adopting organization MUST NOT treat an upstream deletion as automatically withdrawing the organizational standard;
- the adopting organization MUST NOT treat an upstream rename or relocation as altering the organizational standard's authority;
- the adopting organization MUST NOT allow an upstream lifecycle label to silently replace its own lifecycle judgment for the adopted artifact.

The organization may deliberately review upstream changes, but the organizational standard changes only through an organizational decision.

## 8. Later Upstream Changes

A later upstream revision SHOULD be treated as a candidate for review rather than as an inherited update.

The organization may:

- accept the upstream change;
- adapt part of the upstream change;
- reject the upstream change;
- defer action;
- make an independent change instead.

A later upstream revision does not overwrite or mutate the existing organizational standard merely because the two artifacts retain a provenance relationship.

## 9. Relationship Metadata

Where relationship metadata is maintained, it SHOULD distinguish independent adoption from source-managed synchronization.

An independently adopted standard SHOULD be represented in a way that communicates:

- its upstream source and adopted revision;
- that downstream review is required for later upstream changes;
- that the adopting organization controls the downstream lifecycle.

The fact that an adopted copy is byte-identical to its source at the moment of adoption does not by itself make it a source-managed copy.

Exact content similarity and canonical governance are different facts.

## 10. Cross-Organizational Independence

An adopting organization MUST NOT treat another adopter's changes as automatically authoritative for its own standard unless the organizations have deliberately established shared authority.

Therefore:

```text
organization A changes its adopted standard
    != automatic change to organization B
```

and:

```text
upstream template changes
    != automatic change to any adopter
```

A common source may explain similarity and provenance without creating shared lifecycle ownership.

## 11. Changes to the Organization-Governed Standard

A change to an adopted organizational standard SHOULD follow the organization's normal review and canonical-document change process.

A typical relationship is:

```text
identified need or upstream change
        ↓
organizational review
        ↓
accept / adapt / reject
        ↓
organizational canonical update, if approved
```

The review item tracks the decision process.

The canonical organizational artifact contains the resulting normative outcome.

## 12. Relationship to Repository Topology

This policy addresses authority, adoption, provenance, and lifecycle.

It does not determine whether standards live in:

- one organization-wide standards repository;
- several scoped standards repositories;
- a broader governance system;
- another authoritative publication mechanism.

Repository topology is a separate design question.

For software-project responsibility among repositories, canonical documents, issues, project-management systems, and exploratory discussions, see the `project-repository-model` template.

## 13. Anti-Patterns

Avoid:

- treating availability or historical use as organizational adoption;
- relying on a personal repository as continuing company authority without deliberate organizational authorization;
- automatically synchronizing independently adopted standards from upstream templates;
- allowing an upstream change to silently rewrite an organization-governed standard;
- treating provenance as proof of continuing upstream authority;
- treating byte-identical content as proof of shared lifecycle ownership;
- mutating one organization's standard because another organization changed its copy;
- losing the source revision needed to understand what was originally adopted when that provenance matters;
- treating a relationship manifest as authority rather than as evidence of relationship and provenance.

## 14. Default Policy

Unless an organization deliberately establishes a different authority relationship:

> **External or reusable source material becomes organizational authority only through deliberate organizational adoption.**
>
> **The adopted result is governed canonically by the adopting organization for its assigned scope.**
>
> **Upstream provenance may be retained, but provenance does not create continuing upstream authority.**
>
> **The adopted organizational standard has an independent lifecycle.**
>
> **Later upstream changes are candidates for organizational review, not automatic downstream updates.**
>
> **Different organizations that adopt the same source material remain independently responsible for their own standards and later changes.**
