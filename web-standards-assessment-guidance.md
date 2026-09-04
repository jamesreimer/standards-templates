# Web Standards Suite Assessment Guidance

This guidance is non-normative. It assists assessment and evidence recording; it does not create new conformance requirements, alter existing requirement identifiers or owner boundaries, override normative text, change Web Experience Baseline dependencies, or change the optional status of Web Styling Architecture.

## 1. Evidence layering and reuse

Assessment evidence should be recorded by evidence class so that its strength and limitations remain reviewable. A practical evidence classification is:

1. **Direct observation** — behavior or output actually observed in the assessed delivered artifact or declared environment during the assessment.
2. **Exact-revision automated or regression evidence** — repeatable automated evidence demonstrably bound to the exact assessed source or build revision.
3. **Prior revision-bound manual or production-acceptance evidence** — previously recorded human/manual evidence that is demonstrably bound to the same assessed artifact or to an artifact whose equivalence is established for the relevant behavior.
4. **Inference** — a conclusion drawn from source, configuration, implementation structure, or other indirect evidence without directly observing the claimed delivered behavior.
5. **Unperformed evidence** — an assessment method or observation that would be relevant but was not performed and cannot be represented as observed evidence.

Evidence from one class may support an obligation only to the extent that the method is capable of establishing the relevant fact. Evidence reuse does not convert one method into another. For example:

- semantic source does not become assistive-technology observation;
- an automated accessibility scan result does not become complete WCAG conformance;
- a media query does not become delivered responsive behavior;
- a green CI run does not become a universal quality claim;
- a mocked transactional test does not become proof of live provider completion;
- prior manual evidence may be reused only where artifact/revision identity and relevant behavioral equivalence are adequately established.

When a consequential or production-unsafe scenario cannot be executed without creating state, invoking external effects, or risking harm to a live system, the assessor may use safe exact-revision evidence where it is relevant and sufficient. Any aspect that the reused evidence cannot establish remains unresolved rather than being inferred as conforming or nonconforming.

Assessment records should identify the method, environment or tool version when material, artifact/revision binding, date or evidence age when relevant, limitations, and whether the evidence was directly observed, reused, inferred, or unperformed.

## 2. Live artifact and source-revision identity binding

A live observation should not be silently attributed to a repository revision merely because that revision is believed to be current.

Where conformance or assessment conclusions depend on associating a delivered artifact with an immutable source/build identity, the assessment should record the strongest available binding evidence. Examples include:

- a deployment record identifying the exact source commit or build digest activated in the environment;
- a signed or provenance-bearing build artifact tied to the source revision;
- a cryptographic relationship between tested and deployed trees or artifacts;
- a release manifest, deployment ledger, image digest, immutable preview identity, or comparable repository-owned record;
- a delivered build identifier exposed by the application where that identifier is itself trustworthy and revision-bound.

If the public response does not expose a source revision, repository-owned deployment evidence may be used to bind the observation to a revision when that evidence is sufficiently specific and credible for the assessment claim.

The assessment should distinguish:

- **directly bound** observations, where the delivered artifact itself exposes or cryptographically proves the relevant identity;
- **indirectly bound** observations, where a trustworthy deployment/release record establishes the association;
- **unbound or uncertain** observations, where the relationship cannot be established strongly enough for the intended conclusion.

An indirect binding is not automatically defective. Its limitation should simply remain visible. If the identity relationship is insufficient for a claim, that claim remains unresolved rather than being silently associated with a convenient commit.

## 3. Proportionate Quality/Verification profile scoping

A bounded Quality/Verification profile should reflect the material risks, user tasks, dependencies, and environments of the assessed web experience. It need not become a universal certification program merely because compatibility, performance, resilience, and regression quality are relevant dimensions.

For a small informational site, a proportionate profile might declare only the materially relevant dimensions, for example:

- representative modern-browser delivery for the declared audience/environment;
- basic responsive rendering across selected representative width ranges;
- static asset and font loading behavior;
- a bounded lab performance check for the primary public route;
- a small number of meaningful dependency or degraded-resource cases;
- repeatable build or smoke verification appropriate to the site's complexity.

For a transactional or stateful application, a proportionate profile may need broader coverage, such as:

- material task paths and state transitions;
- consequential-action and recovery behavior;
- representative compatibility environments;
- performance around critical user journeys;
- external-provider or dependency degradation behavior;
- repeatable regression suites and evidence provenance.

The profile should state what it covers and what it does not cover. A narrow declared claim is preferable to an implied universal claim that the evidence cannot support.

The absence of field-performance data, a universal browser matrix, or every imaginable resilience scenario does not by itself establish nonconformance when those claims were not made and the applicable requirement permits a bounded declared profile. Conversely, an assessor must not describe a narrow profile as evidence for broader compatibility, performance, resilience, or quality claims than were actually evaluated.

Proportionality changes assessment scope, not the truthfulness requirement. Every claim still needs evidence adequate for the claim actually made.

## 4. Integration recommendation

Use one organization-neutral assessment-guidance document or guidance section that is explicitly non-normative and referenced from the Web Standards Suite documentation.

Avoid scattering duplicate guidance into each normative standard unless a genuinely standard-specific clarification is later identified.

The guidance should make clear that it assists assessment and evidence recording; it does not create new conformance requirements or override normative text.
