# Publication and Release Integrity Standard

## 1. Purpose

This standard defines the integrity requirements that apply when an
artifact transitions from a reviewed, validated, approved, or otherwise
authorized source state into a published artifact or release.

Its purpose is to ensure that publication preserves a demonstrable
relationship between the state authorized for publication and the state
actually made available, that publication identities accurately denote
their published states, that moving references remain distinguishable
from fixed identities, and that publication claims are supported by
evidence appropriate to what they assert.

The central principle is:

```text
a publication must identify what was published,
correspond to what was authorized for publication,
bind its identities to the states they are intended to denote,
and preserve the declared meaning of identities and references
on which consumers may rely
```

Publication is distinct from implementation, review, validation,
integration, deployment, activation, consumption, and downstream
adoption. Applicable authority and provenance models remain
independently governed.

## 2. Scope

This standard applies when an Artifact becomes available under a
Publication Identity for organizational, external, downstream, or other
durable consumption.

It also applies to unintended or premature exposure when an Artifact
becomes observable under an identity or reference on which consumers may
reasonably rely, even if the exposure was not authorized or intended as
Publication.

Artifacts may include, for example:

-   documents;
-   standards or policies;
-   software packages;
-   source distributions;
-   release bundles;
-   machine images;
-   configuration packages;
-   data products;
-   models;
-   media assets;
-   schemas;
-   reusable templates;
-   generated artifacts;
-   other versioned or identifiable deliverables.

This standard applies regardless of whether publication occurs through a
source repository, package registry, artifact store, document-management
system, release service, distribution platform, controlled records
system, file repository, or another publication mechanism.

This standard does not determine:

-   who may authorize Publication;
-   how review or validation must be performed;
-   how provenance is generally represented;
-   whether a downstream consumer adopts, consumes, deploys, activates,
    or accepts a Publication;
-   which versioning, tagging, signing, hashing, release, or
    distribution technology an organization must use.

## 2.1 Normative Language

Where `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY` appear in
uppercase, they are to be interpreted as described in BCP 14, [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html)
and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html). Lowercase forms retain their ordinary English meaning.

## 3. Definitions

**Artifact**

A document, package, bundle, image, file, data product, model, template,
generated output, or other identifiable deliverable capable of
Publication.

**Publication**

The state transition through which an Artifact becomes available under a
Publication Identity for organizational, external, downstream, or other
durable consumption.

A Publication MAY involve multiple technical or distribution stages.

Publication does not by itself establish deployment, activation,
downstream adoption, or other independently governed lifecycle state.

**Release**

A Publication that groups or identifies one or more Artifacts as a
coherent distribution state.

A Release is one form of Publication. This standard does not require
every Publication to be a Release.

**Publication Transition**

The transition from preparation toward a Published State. A Publication
Transition MAY span multiple observable stages, such as creation of an
identity, transfer of content, publication of metadata, indexing, or
availability through an authoritative publication surface.

Authority to initiate or complete a Publication Transition is governed
by the applicable authority model rather than by this standard.

**Authorized Source State**

The specific source state, content state, build input, candidate, or
equivalent artifact state that received the authorization applicable to
the intended Publication.

**Published State**

The Artifact or Release state made available through an Authoritative
Publication Surface under a Publication Identity.

**Authoritative Publication Surface**

A publication location, service, system, record, or distribution surface
that the publisher designates or uses as authoritative for a Published
State.

Mirrors, caches, replicas, indexes, or other copies outside the
publisher's control are not Authoritative Publication Surfaces merely
because they reproduce or reference the Publication.

**Publication Identity**

An identifier or combination of identifiers associated with a Published
State or Publication relationship.

A Publication Identity may be fixed or may participate in a declared
moving reference.

**Fixed Publication Identity**

A Publication Identity whose declared meaning binds it to one particular
Published State.

A Fixed Publication Identity does not become a Moving Publication
Reference merely because the publication technology permits its target
or content to be changed.

**Moving Publication Reference**

A Publication Identity whose declared meaning intentionally identifies a
changing designated state, such as the current, stable, recommended, or
otherwise selected Publication.

Movement is part of the reference's declared semantics.

**Identity Layer**

A distinct identity associated with an Artifact or Publication for a
particular purpose, such as an authorized-state identity, component
identity, edition identity, distribution identity, package identity, or
Content-Binding Identity.

**Content-Binding Identity**

An identity whose declared meaning binds it to the substantive content
of one particular Published State such that changing that content would
change what the identity denotes.

**Correspondence**

An evidence-supported relationship sufficient to establish that the
Published State represents the Authorized Source State as intended for
the Publication.

Where an applicable provenance model governs derivation or
correspondence semantics, that model governs how the relationship is
established. This standard determines when such Correspondence is
required across Publication and what publication claims it supports.

**Established Publication Identity**

A Fixed Publication Identity that has become available for durable
reference or on which consumers may reasonably rely.

Premature or unintended exposure does not prevent an identity from
becoming established.

**Successor Publication**

A distinguishable Publication that corrects, replaces, supersedes, or
otherwise follows an earlier Publication without changing the historical
meaning of the earlier Fixed Publication Identity.

**Withdrawal**

A state in which a Publication is intentionally made unavailable,
restricted, deprecated from use, or otherwise removed from ordinary
consumption while preserving the identity semantics necessary to
distinguish its historical Published State.

## 4. Publication Transition and Observable Exposure

The publisher MUST make the intended completion of a Publication
Transition determinable.

A Publication Transition MAY comprise multiple technical stages. An
organization need not treat every intermediate stage as a completed
Publication.

However, when an Artifact becomes observable under a Publication
Identity on an Authoritative Publication Surface, the publisher MUST account for that observable state before
replacing, retrying, withdrawing, correcting, or claiming completion of
the Publication.

Unintended or premature exposure MUST NOT be treated as though no
publication state existed merely because the exposure lacked
authorization or intent.

Where an applicable execution or authority standard governs permission
to publish, that standard determines authority to cross the Publication
Transition. This standard governs the integrity consequences of the
resulting publication state.

The publisher MUST NOT represent Publication as establishing downstream
adoption, deployment, activation, or another independently governed
lifecycle state.

## 5. Authorized Source State

A Publication MUST identify or make determinable the Authorized Source
State to which it is intended to correspond.

The Authorized Source State MUST be precise enough to determine what
content, inputs, or artifact state the publication authorization
actually covered.

If the state intended for Publication materially changes from the
Authorized Source State, the publisher MUST NOT claim that the changed
state carries the earlier publication authorization unless the
applicable authority model establishes that it does.

Whether authorization exists, how it is granted, and what changes remain
within it are governed by the applicable authority model.

## 6. Publication Correspondence

The Published State MUST correspond to the Authorized Source State.

At the time Publication is claimed complete, evidence sufficient to
establish that Correspondence MUST exist or be producible.

The evidence MAY include, as appropriate:

-   exact content comparison;
-   content or artifact digests;
-   equivalent source states;
-   deterministic build or transformation evidence;
-   provenance attestations;
-   reproducible outputs;
-   controlled packaging records;
-   system-established immutable relationships;
-   other evidence appropriate to the Artifact and publication
    mechanism.

No particular correspondence mechanism is required by this standard.

Where an applicable provenance model governs derivation or
correspondence, its rules determine whether a transformation or derived
Artifact preserves the required relationship. This standard does not
establish a competing derivation model.

Successful execution of a publication operation MUST NOT by itself be
represented as proof of Correspondence unless the operation's evidence
actually establishes the relationship between the Authorized Source
State and Published State.

If Correspondence cannot be established, the intended Publication MUST
NOT be claimed complete.

Ongoing evidence retention SHOULD be sufficient for as long as
maintainers or consumers materially need to verify publication
integrity, subject to applicable legal, security, privacy, or records
requirements.

## 7. Publication Identity and State Binding

Every Published State MUST have a Publication Identity sufficient to
distinguish it for its intended lifecycle and consumers.

The Publication Identity MUST denote, resolve to, or otherwise identify
the Published State whose Correspondence to the Authorized Source State
has been established.

Where a Release has a Fixed Publication Identity, the Artifacts included
in that Release and the identities by which those Artifacts are included
form part of what that Fixed Publication Identity denotes.

A Release designated through a Moving Publication Reference MAY
designate different Release states over time according to that
reference's declared movement semantics.

A Publication Identity MAY use, for example:

-   a release identifier;
-   revision identifier;
-   document edition;
-   package version;
-   component version;
-   artifact digest;
-   immutable object identifier;
-   publication record identifier;
-   another stable identification mechanism.

This standard does not prescribe the syntax, technology, numbering
system, or storage mechanism used for Publication Identity.

A human-readable label MAY participate in Publication Identity but MUST
NOT be represented as uniquely identifying a Published State when it is
ambiguous within the relevant publication context.

The publisher MUST make it determinable whether an identity intended for
durable reliance is a Fixed Publication Identity or a Moving Publication
Reference when confusing the two could cause consumers to identify the
wrong Published State.

## 8. Fixed Identities, Moving References, and Identity Layers

A Fixed Publication Identity MUST NOT be reassigned to materially
different substantive content after it becomes established.

This prohibition applies whether or not the reassignment is announced.

Technical mutability does not convert a Fixed Publication Identity into
a Moving Publication Reference.

When a Publication Identity has no declared movement semantics and
consumers may reasonably rely on it as denoting one Published State, it
MUST be treated as a Fixed Publication Identity.

The fixed-or-moving classification of an Established Publication
Identity MUST NOT be changed retroactively.

A Moving Publication Reference MAY resolve to different Published States
over time when such movement is part of its declared meaning.

A Moving Publication Reference MUST NOT be represented as a fixed or
content-immutable identity.

When consumers need to distinguish historical Published States, a Fixed
Publication Identity or another Content-Binding Identity sufficient to
make those states distinguishable MUST exist or be determinable
alongside the Moving Publication Reference.

A Publication MAY have multiple Identity Layers.

The publisher MUST make the meanings and relationships of materially
relevant Identity Layers sufficiently clear to prevent an identity from
being represented as establishing a state or relationship that it does
not establish.

A distribution identity MUST NOT be represented as establishing the
independent version, edition, or content state of each component unless
it actually does so.

A component identity likewise MUST NOT be represented as establishing a
particular distribution unless that relationship is part of its defined
meaning.

Where an identity permits in-place change, the publisher MUST NOT
represent that identity as content-immutable.

Publication-identity stability does not by itself establish that an
identity qualifies as an immutable consumed identity under an applicable
provenance model.

Where consumers materially require a content-immutable consumed
identity, an appropriate Content-Binding Identity MUST be provided or
determinable.

## 9. Publication Verification

When the resulting Published State is observable, the publisher MUST
verify Publication using evidence of the resulting state rather than
relying solely on the initiating publication operation's own success
report.

Verification MUST establish, in proportion to consequence, that:

-   the intended Publication Identity exists;
-   that identity denotes the intended Published State;
-   the Published State is available through the intended Authoritative
    Publication Surface;
-   the Published State corresponds to the Authorized Source State; and
-   material identity relationships, Release membership, and publication
    information required for correct consumption are consistent with the
    intended Publication.

Verification evidence is independent for purposes of this section when
it observes or establishes the resulting publication state rather than
merely repeating the initiating operation's assertion that the operation
succeeded. It need not originate from a different provider, system, or
organization.

Where an Authoritative Publication Surface is eventually consistent,
verification MUST observe the resulting state after the relevant state
has settled sufficiently to support the completion claim, or the
completion claim MUST remain bounded to the state actually established.

Where the resulting Published State cannot reasonably be observed, the
publisher MUST limit completion claims to what available evidence
establishes, such as successful transfer, receipt, acknowledgment, or
another applicable state.

A successful command, upload, push, workflow, API response, transfer, or
local operation MUST NOT be represented as stronger evidence than it
actually provides.

This standard does not require verification of uncontrolled mirrors,
caches, replicas, or third-party indexes as a condition of Publication
completion.

## 10. Published-Identity Stability and Change Classification

The historical meaning of an Established Publication Identity MUST be
preserved.

Whether a proposed in-place change to what a Publication Identity
denotes is substantive MUST be determined by its effect rather than by
whether it is described as metadata, presentation, indexing,
documentation, or another category.

A change to what a Publication Identity denotes MUST be treated as
substantive when it could cause a reasonable consumer to reach a
materially different conclusion about, as applicable:

-   the Artifact's meaning or requirements;
-   conformance;
-   compatibility;
-   dependency or resolution behavior;
-   installation or execution;
-   licensing or permitted use;
-   security or safety significance;
-   the content or components identified;
-   whether the Artifact is suitable for the consumer's intended
    reliance.

When it is materially uncertain whether an in-place change is
substantive, the change MUST be treated as substantive for
publication-identity purposes.

Changing Artifact content under a Fixed Publication Identity that is a
Content-Binding Identity is a substantive change even when the change
might otherwise be characterized as presentation or editorial
correction.

A non-substantive change MAY be made in place only when doing so
preserves the declared meaning of the affected identity and does not
cause the publisher to represent materially different substantive
content as the same fixed Published State.

Information about a Published State, such as defect, withdrawal,
deprecation, or supersession status; security or safety advisories;
evidence; signatures; or attestations, MAY be added or changed in place
without creating a Successor Publication when doing so does not change
or misrepresent what the affected Fixed Publication Identity denotes.

## 11. Corrections and Successor Publications

When correcting a Published State would substantively change the content
denoted by an Established Publication Identity, the publisher MUST
preserve the earlier identity's historical meaning.

The corrected Artifact MUST receive a distinguishable Successor
Publication or use another mechanism that preserves the earlier Fixed
Publication Identity without causing it to denote the corrected
substantive state.

Where consumer understanding materially depends on the relationship, the
Successor Publication MUST make its correction, replacement, or
supersession relationship to the earlier Publication determinable.

A Published State known to contain a material defect MUST be
identifiable as defective, withdrawn, superseded, or otherwise
unsuitable for continued reliance when failure to communicate that
condition could cause material harm, except while legal, security,
safety, privacy, contractual, or comparable legitimate constraints
require that disclosure to be limited or deferred.

When such constraints no longer prevent disclosure, the applicable
defect, withdrawal, or supersession status MUST be made determinable
when continued reliance could cause material harm.

This standard does not prescribe the notice mechanism, version
increment, release numbering, edition syntax, deprecation period,
changelog format, or release-note format used to communicate that state.

A non-substantive correction MAY occur in place when it satisfies
Section 10.

## 12. Withdrawal, Removal, and Identity Reservation

A publisher MAY withdraw, restrict, redact, or remove a Published State
when authorized or required to do so.

Withdrawal or removal does not release an Established Publication
Identity for reassignment to materially different substantive content.

Where the original content cannot remain available because of legal,
security, safety, privacy, contractual, or other legitimate constraints,
preserving historical identity meaning does not require continued
availability of that content.

The publisher MUST preserve enough information, where legally and
operationally permissible, to prevent the withdrawn Fixed Publication
Identity from being represented as a different Published State.

Withdrawal, restriction, redaction, or supersession MUST be determinable
by consumers when continued reliance on the earlier Publication could
cause material harm, except while legal, security, safety, privacy,
contractual, or comparable legitimate constraints require that
disclosure to be limited or deferred.

When such constraints no longer prevent disclosure, the applicable
status MUST be made determinable when continued reliance could cause
material harm.

While disclosure is constrained, the publisher MAY limit the retained or
exposed information to what applicable constraints permit, but MUST NOT
reuse the Fixed Publication Identity for materially different
substantive content.

## 13. Partial, Failed, and Premature Publication

A failed, interrupted, or premature publication operation MUST NOT be
assumed to have produced no observable publication state.

When a Publication Transition fails, is interrupted, or occurs
prematurely after any state may have become observable, the publisher
MUST assess the relevant Authoritative Publication Surface before
retrying, replacing, correcting, withdrawing, or claiming completion.

The assessment MUST be sufficient to avoid, as applicable:

-   conflicting Publication Identities;
-   unintended duplicate Publications;
-   reassignment of a Fixed Publication Identity;
-   publication of an unintended Artifact;
-   false completion claims;
-   loss of evidence needed to establish Correspondence;
-   incorrect movement of a Moving Publication Reference.

A retry MUST NOT overwrite, reinterpret, or release for reuse an
Established Publication Identity merely because the initiating
publication operation reported failure.

Where observable publication state remains materially ambiguous,
Publication MUST NOT be claimed complete until the ambiguity is resolved
or the completion claim is explicitly bounded to what the available
evidence establishes.

## 14. Evidence and Publication Claims

Publication evidence MUST be interpreted according to what it actually
establishes.

The publisher MUST NOT make or preserve a publication claim stronger
than the available evidence supports.

For example:

-   review evidence does not by itself establish Publication;
-   validation evidence does not by itself establish Publication;
-   publication authorization does not establish that Publication
    occurred;
-   successful initiation does not necessarily establish the resulting
    Published State;
-   Correspondence evidence does not grant publication authority;
-   a distribution identity does not necessarily establish independent
    component identities;
-   Publication does not establish downstream adoption, deployment,
    activation, or consumption.

Where another standard governs provenance, authority, adoption,
deployment, activation, or consumption, evidence created under this
standard MAY support that later determination but MUST NOT be
represented as satisfying independently governed requirements that it
does not establish.

## 15. Relationship to Provenance

Publication integrity depends on establishing the relationship between
an Authorized Source State and Published State.

Where an applicable provenance standard governs source identity,
derivation, correspondence, moving references, or immutable consumed
identities, this standard MUST be applied consistently with that
provenance model.

This standard does not redefine the competent source from which an
Artifact is legitimately obtained, nor does it establish a competing
derivation or authoritative-consumption model.

For publication-integrity purposes:

-   provenance determines origin, derivation, and correspondence
    semantics where applicable;
-   this standard determines when Correspondence must be established
    across Publication, how publication identities bind to resulting
    states, and what publication claims that evidence supports.

Neither provenance evidence nor publication integrity grants execution
authority governed elsewhere.

## 16. Relationship to Downstream Control

Publication does not by itself change independently controlled
downstream state.

Where a downstream authority deliberately adopts, installs, deploys,
activates, consumes, or updates a Publication, that action remains
governed by its applicable authority, adoption, provenance, dependency,
or operational model.

A publisher MUST NOT represent Publication, correction, supersession, or
movement of a Moving Publication Reference as independently changing
downstream state unless a declared relationship actually gives the
source authority to manage that state.

This requirement does not prohibit automatic or source-managed
propagation where the downstream relationship deliberately grants such
authority.

## 17. Proportionality

Publication controls SHOULD be proportionate to:

-   consequence of publishing unintended content;
-   consequence of incorrect or ambiguous identity;
-   number and independence of consumers;
-   difficulty of correcting an erroneous Publication;
-   durability of external references;
-   reversibility of publication effects;
-   transformation between Authorized Source State and Published State;
-   ability to observe and verify the resulting Published State.

Low-consequence Publication MAY use simple identity, Correspondence, and
verification mechanisms.

High-consequence or widely consumed Publication SHOULD use stronger
identity, Correspondence, verification, and historical-stability
controls.

Proportionality MUST NOT be used to justify:

-   unsupported Publication claims;
-   ambiguous identity where the ambiguity could cause consumers to
    identify the wrong Published State;
-   reassignment of an Established Publication Identity;
-   representing a Moving Publication Reference as fixed or
    content-immutable;
-   representing an identity as establishing more than it actually
    establishes;
-   bypassing required Correspondence between the Authorized Source
    State and Published State.

The strength or complexity of a control MAY vary with consequence. The
integrity property the control protects remains applicable wherever this
standard requires it.

## 18. Conformance

Conformance requires satisfaction of every applicable `MUST` and
`MUST NOT` in this standard. The following list summarizes the principal
conformance properties and does not replace or narrow the normative
requirements elsewhere in the standard.

A publication process conforms to this standard when, as applicable, it:

1.  makes the intended completion of the Publication Transition
    determinable and accounts for prematurely or unintentionally
    observable publication state;
2.  identifies or makes determinable the Authorized Source State;
3.  establishes Correspondence between the Authorized Source State and
    Published State before claiming the intended Publication complete;
4.  provides a Publication Identity that denotes the Published State
    whose Correspondence has been established;
5.  distinguishes Fixed Publication Identities from Moving Publication
    References where confusing them could cause incorrect
    identification;
6.  makes materially relevant Identity Layers and their relationships
    sufficiently clear for correct interpretation;
7.  verifies observable Published State using evidence of the resulting
    state rather than relying solely on the initiating operation's
    success report;
8.  bounds completion claims to available evidence when the resulting
    Published State cannot reasonably be observed;
9.  preserves the historical meaning of Established Publication
    Identities and does not reassign them to materially different
    substantive content;
10. treats changes to what an identity denotes according to their
    consequence while permitting accurate status, advisory, evidence,
    signature, and attestation information about the Published State;
11. uses a distinguishable Successor Publication or another
    identity-preserving mechanism when correcting substantive content
    under an Established Publication Identity;
12. preserves identity semantics through withdrawal, removal,
    restriction, or redaction without requiring continued availability
    where legitimate constraints prohibit it;
13. assesses observable state after failed, interrupted, or premature
    Publication before retrying or claiming completion;
14. limits Publication claims to what the available evidence actually
    establishes;
15. applies applicable provenance semantics without creating a competing
    source-identity, derivation, or authoritative-consumption model; and
16. preserves the independent authority of downstream adoption,
    consumption, deployment, activation, and other lifecycle decisions
    except where a declared relationship legitimately grants
    source-managed authority.

Conformance does not require any particular repository, versioning
scheme, release service, publication platform, cryptographic mechanism,
organizational role structure, or implementation technology.
