# Web Experience Baseline Standard

## 1. Purpose and Scope

This standard defines how a declared web experience composes the required core Web Standards into a truthful Baseline assessment and conformance conclusion.

The operative question is whether the claimed Baseline scope has been evaluated against the exact required companion versions, with every applicable mandatory obligation resolved under its owning standard and with failures, exclusions, adaptations, and uncertainty preserved rather than averaged, omitted, or relabeled.

This standard owns suite composition and Baseline claim integrity. It does not restate or replace the substantive requirements of its companion standards.

Adoption of this standard does not establish organizational authority, approve a release, certify legal compliance, require a public claim, or make later upstream revisions automatically authoritative downstream. Adoption, adaptation, exceptions to local organizational rules, publication, and approval remain subject to the adopting organization's existing authority.

## 2. Interpretation and Baseline Dependencies

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html)) when, and only when, they appear in this uppercase form. Lowercase uses have their ordinary meaning.

`WEB-BASE-NNN` identifies a local requirement synthesized by this template, independently of section numbers. Numbered local requirements are normative. Sections explicitly marked informative are not.

**Baseline assessment** means an assessment that evaluates this standard together with the required companion set identified below for one declared scope and artifact revision.

**Required companion set** means the exact six independently adoptable standards incorporated into the unchanged Baseline dependency model:

- [Web Accessibility Standard](../web-accessibility/standard.md), stable ID `web-accessibility`;
- [Web Content and Semantics Standard](../web-content-semantics/standard.md), stable ID `web-content-semantics`;
- [Web Design Foundations Standard](../web-design-foundations/standard.md), stable ID `web-design-foundations`;
- [Responsive Web Layout Standard](../responsive-web-layout/standard.md), stable ID `responsive-web-layout`;
- [Web Interface and Interaction Standard](../web-interface-interaction/standard.md), stable ID `web-interface-interaction`;
- [Web Quality and Verification Standard](../web-quality-verification/standard.md), stable ID `web-quality-verification`.

Each companion retains its own requirement identifiers, definitions, conditions, evidence rules, adaptations, external dependencies, and results. This standard composes those results; it does not redefine them.

Web Styling Architecture is not a required dependency of this Baseline. Separately adopting another standard does not change this dependency set unless a deliberately adopted later Baseline revision expressly does so.

**Material** means capable of changing dependency applicability, a required companion result, the declared assessment scope, a Baseline conclusion, or a reasonable decision based on a Baseline claim.

## 3. Declared Baseline Composition

**WEB-BASE-001 — Declared Baseline assessment scope.** A Baseline assessment MUST identify the evaluated web experience, artifact or release revision, covered pages, views, processes and material states, declared audience or audiences where relevant, material environments or conditions inherited from applicable companion assessments, and material exclusions. Any difference between assessed coverage and a claimed Baseline scope MUST be explicit.

**WEB-BASE-002 — Required companion set.** A claim to conformance with the unchanged Baseline MUST include all six standards in the required companion set. Omission of a required companion MUST NOT be treated as a passing Baseline result, even when the omitted subject appears inapplicable in whole or in part; applicability MUST be resolved under that companion's own requirements and conditions.

**WEB-BASE-003 — Exact dependency identity and version.** The Baseline assessment MUST identify the adopted version or immutable revision of this standard and of every required companion used for the conclusion. A later upstream revision MUST NOT be treated as automatically incorporated. Results from materially different dependency versions MUST NOT be represented as interchangeable without an explicit affected-obligation review.

**WEB-BASE-004 — Companion applicability resolution.** Applicability MUST be determined using the owning companion's own scope, definitions, conditions, exceptions, external dependencies, and assessment rules. This standard MUST NOT create a local shortcut that converts an applicable companion obligation into not-applicable, satisfied, excepted, or out of scope.

**WEB-BASE-005 — Preservation of companion requirement ownership.** Each substantive obligation MUST remain owned and decided by the standard that defines it. Shared scenarios, tools, environments, evidence, or execution MAY support multiple obligations when they actually address each one, but a Baseline assessment MUST NOT merge distinct requirement identities or replace one companion's substantive pass/fail conclusion with another standard's result.

**WEB-BASE-006 — Preservation of companion conformance models.** The Baseline assessment MUST preserve each required companion's own result and conformance model, including any incorporated external model. The Baseline MUST NOT redefine external WCAG conformance, convert an organizational exception into a source-defined exception, rename a sibling result, or represent Baseline conformance as legal, accessibility, security, brand, or other certification beyond what the owning authority establishes.

## 4. Coverage, Evidence, and Conflict Handling

**WEB-BASE-007 — Complete mandatory coverage.** A Baseline conformance conclusion MUST have a resolved result for every applicable mandatory obligation of this standard and every required companion under the identified adopted versions and declared scope. A legitimately inapplicable obligation MUST be supported by its owning standard's applicability basis. Unperformed, inaccessible, missing, stale, conflicting, or otherwise insufficient evidence MUST remain unresolved or undetermined as required by the owning standard and MUST NOT be converted into a pass.

**WEB-BASE-008 — Shared evidence without merged conclusions.** Evidence context MAY be deduplicated across companion assessments, including artifact revision, environment, execution records, screenshots, traces, reviewer identity, or tool output. Evidence reuse MUST preserve traceability to each supported requirement and MUST NOT imply that shared storage, orchestration, or execution transfers substantive result ownership to the Baseline or to Web Quality and Verification.

**WEB-BASE-009 — Conflict and incompatibility handling.** When required companion obligations, adopted adaptations, dependency versions, external conformance conditions, or assessment results materially conflict, the Baseline assessment MUST preserve the conflict and MUST NOT assert Baseline conformance until a reviewable resolution establishes a configuration in which every applicable mandatory Baseline dependency can be satisfied. Organizational authority MAY select or adopt a changed configuration, but the changed configuration MUST be identified and its claim consequences made explicit.

**WEB-BASE-010 — No averaging or substitution.** A known failure of an applicable mandatory Baseline or companion obligation MUST remain a failure regardless of successful results elsewhere. Aggregate scores, percentages, grades, recommendation counts, tool summaries, or strong results in another companion MUST NOT substitute for the unsatisfied obligation or convert it into a passing Baseline result.

## 5. Baseline Results and Claims

**WEB-BASE-011 — Baseline conformance condition.** Baseline conformance requires the declared scope to satisfy every applicable mandatory requirement of this standard and every required companion under the exact identified adopted versions, with each required result supported according to its owning evidence model. A known applicable mandatory failure prevents Baseline conformance. An unresolved required result prevents a Baseline conformance conclusion until resolved.

**WEB-BASE-012 — Distinct suite and individual results.** Results MUST distinguish Baseline conformance, individual-standard conformance, partial Baseline assessment, Baseline nonconformance, and undetermined Baseline status. An individual companion result MUST NOT be represented as Baseline conformance, and a Baseline result MUST NOT erase or replace the more specific companion result from which it is composed.

Any Baseline conformance claim MUST identify the adopted Baseline version or immutable revision, all required companion versions or immutable revisions, evaluated artifact revision, assessed scope, material exclusions, and conclusion. A public badge, registry, dashboard, or claim is not required.

**WEB-BASE-013 — Partial, excluded, not-applicable, and undetermined treatment.** Partial coverage is not a reduced Baseline conformance level. A material exclusion MUST remain visible and MUST NOT imply assessment of excluded scope. A legitimately not-applicable companion obligation MUST retain the applicability basis required by its owning standard. A required obligation that cannot be decided because evidence is missing, inaccessible, conflicting, stale, or otherwise insufficient MUST remain undetermined rather than being treated as passed or not applicable. Known failures MUST remain visible even when other obligations are undetermined.

**WEB-BASE-014 — Adaptations, exceptions, and unchanged claims.** An adopter MAY adapt this standard or a companion through its existing authority. The assessment MUST identify any material adaptation or exception and its effect on dependency identity, obligation meaning, and claims. An adaptation or organizational exception that leaves an applicable mandatory obligation of the unchanged Baseline unsatisfied MUST NOT be represented as conformance to the unchanged Baseline. A separately governed adapted Baseline MAY define its own claim only when the changed dependency model and requirements are explicit.

## 6. Changes and Reassessment

**WEB-BASE-015 — Change and reassessment.** A material change to the assessed experience, artifact revision, declared scope, required companion version, adopted adaptation, applicable external dependency, companion result, or relevant evidence MUST trigger reassessment of the Baseline obligations and companion obligations whose results may be affected before a current Baseline conclusion is asserted. Unaffected evidence and companion results MAY be reused when their continued applicability to the current versions, revision, scope, and obligations is justified; reuse MUST NOT conceal stale or invalidated results.

## 7. Informative Composition Guidance

This section is informative.

The Baseline is a composition contract, not another subject checklist. A single browser session, test execution, review record, or evidence repository can support several companion assessments, but each requirement still needs the conclusion defined by its owner.

A complete Baseline assessment can legitimately contain not-applicable obligations where the owning requirement's conditions are absent. For example, absence of a particular interaction pattern can make a conditional requirement inapplicable without making the entire Interaction Standard optional. The required companion itself remains part of the Baseline dependency set.

Missing evidence differs from non-applicability. If an environment cannot be accessed, a manual check was not performed, or conflicting evidence remains unresolved, the owning standard's undetermined or incomplete result carries into the Baseline rather than disappearing at composition time.

A companion's external conformance model also remains intact. In particular, the Web Accessibility Standard distinguishes its local result from WCAG conformance and source-defined partial-conformance statements. The Baseline consumes those distinctions without creating a new WCAG level or legal meaning.

Web Styling Architecture can be adopted independently when useful. Its presence or absence does not alter the unchanged Baseline dependency set. A Styling failure can still reveal or cause a failure in a required Design, Layout, Interaction, Accessibility, Content, or Quality outcome, but the Styling result itself is not a Baseline dependency unless a later Baseline revision deliberately changes that architecture.

## 8. Adaptation and Boundaries

An adopting organization MAY define reporting formats, assessment coordination, review routing, evidence storage, additional optional standards, stronger local requirements, or an adapted dependency set through its existing authority. Such adaptations MUST identify their scope and consequences and MUST NOT be represented as requirements of an unchanged upstream Baseline.

This standard does not create organizational approval authority, an adoption ceremony, a release gate, a public registry, a dashboard, a machine-readable schema, a badge, a mandatory evidence repository, or automatic synchronization. It does not define Enhanced conformance or domain profiles.

The six required companions remain independently adoptable outside a Baseline assessment. Their cross-references and their participation in this Baseline do not create a dependency on this umbrella for standalone use.

### Strength and ownership rationale — informative

The mandatory rules protect the meaning of a Baseline conclusion: exact dependency identity, complete required coverage, preserved ownership, preserved conformance models, truthful aggregation, and reassessment after material change. Permissions preserve legitimate variation in evidence orchestration, reporting, organization-specific adaptations, optional standards, and implementation technology.
