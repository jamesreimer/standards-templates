# Web Quality and Verification Standard

## 1. Purpose and Scope

This standard defines baseline requirements for credible performance, compatibility, resilience, and verification conclusions for a declared web experience.

The operative question is whether quality claims are tied to explicit targets, environments, methods, populations, revisions, and limitations, and whether the delivered experience demonstrates the claimed behavior under the conditions actually represented as covered.

It applies to performance targets and measurements, field/lab/synthetic evidence distinctions, compatibility coverage, material feature support, fallbacks, declared resilience conditions, degraded delivery, dependency-failure containment, regression-sensitive evidence, and shared verification context within the declared scope.

It is independently adoptable. It does not depend on a web-suite umbrella, analytics platform, monitoring vendor, performance tool, browser-automation system, test framework, service worker, or another companion standard. Field measurement, lab measurement, synthetic testing, browser automation, direct observation, platform APIs, feature detection, progressive enhancement, fallbacks, caching, and other mechanisms can satisfy it when the evidence and delivered result meet the applicable requirements.

This standard does not prescribe a universal performance threshold, browser list, device matrix, analytics product, RUM system, Lighthouse score, Web Vitals profile, service worker, cache strategy, polyfill, compatibility database, test runner, or evidence repository.

Accessibility conformance, content semantics, visual-foundation calibration, responsive-layout correctness, interaction correctness, CSS architecture, security, privacy, infrastructure operations, deployment, and legal duties remain subject to separately selected authorities where applicable. Adoption, exceptions to local organizational rules, publication, and approval remain subject to the adopting organization's existing authority. Publication of this source does not adopt or update any downstream artifact.

## 2. Interpretation and Definitions

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html)) when, and only when, they appear in this uppercase form. Lowercase uses have their ordinary meaning.

`WEB-QUA-NNN` identifies a local requirement synthesized by this template, independently of section numbers. Numbered local requirements are normative. Sections explicitly marked informative are not.

**Quality profile** means the declared set of performance, compatibility, resilience, and verification conditions against which a result or claim is evaluated. A profile can select only the dimensions applicable to its declared purpose.

**Field evidence** means measurement produced from actual use in the declared population or distribution context. **Lab evidence** means measurement produced under a controlled test environment. **Synthetic evidence** means evidence produced through scripted or simulated execution. One execution can be both lab and synthetic.

**Compatibility environment** means a declared browser, runtime, embedded user agent, device class, operating-system context, or materially relevant combination in which a claimed result is expected to hold.

**Resilience condition** means a declared degraded, unavailable, slow, interrupted, or failed dependency/network/resource condition under which a bounded delivered result is expected.

**Material** means capable of changing a claimed quality result, availability of necessary delivered capability, a reasonable decision or action by the declared audience, an assessment result, or a conformance claim.

The [Web Accessibility Standard](../web-accessibility/standard.md), [Web Content and Semantics Standard](../web-content-semantics/standard.md), [Web Design Foundations Standard](../web-design-foundations/standard.md), [Responsive Web Layout Standard](../responsive-web-layout/standard.md), and [Web Interface and Interaction Standard](../web-interface-interaction/standard.md) retain their own substantive requirements, evidence conditions, and results. Shared evidence MAY be reused when it actually supports each obligation, but this Standard MUST NOT reclassify a sibling's substantive result as its own.

## 3. Declared Quality Context and Performance

**WEB-QUA-001 — Declared assessment scope.** An assessment MUST identify the evaluated web experience, artifact or release revision, covered pages/views/processes/resources, selected quality dimensions, declared audience or population where relevant, material environments and conditions, material exclusions, and the quality claims being evaluated. Any difference between assessed coverage and a claimed scope MUST be explicit.

**WEB-QUA-002 — Declared quality profile.** Each assessment MUST identify the quality profile used for its conclusions, including the applicable performance targets, compatibility environments, resilience conditions, and verification expectations that materially affect the result. A profile MAY select only the dimensions applicable to the declared purpose. The absence of an inapplicable dimension MUST NOT be represented as evidence that the omitted dimension was assessed.

**WEB-QUA-003 — Measurement-context integrity.** A measured result MUST identify the material context needed to interpret it, including the evaluated revision, measurement method, environment, relevant tool or implementation version, sampling or execution basis, and limitations. A measurement MUST NOT be represented as applying to materially different conditions without evidence supporting that extension.

**WEB-QUA-004 — Performance-target integrity.** A performance claim MUST identify the metric or observable outcome, target or comparison basis, applicable population or execution set, aggregation or percentile where relevant, measurement method, and material environment. A score, grade, or aggregate tool result MUST NOT substitute for the underlying target definition when the claim depends on specific performance outcomes.

**WEB-QUA-005 — Field, lab, synthetic, and observed result distinction.** Evidence MUST distinguish field, lab, synthetic, and directly observed results where that distinction materially affects interpretation. Lab or synthetic evidence MUST NOT be represented as field evidence, and field evidence MUST NOT be represented as proof of a controlled condition it did not establish.

**WEB-QUA-006 — Representative performance evidence.** Evidence used for a performance conclusion MUST be representative of the claim actually made. Sampling, repeated execution, population selection, or controlled conditions MUST be sufficient to avoid materially misleading conclusions from an isolated or unrepresentative result. This requirement does not mandate field measurement where no field claim is made or where the declared experience does not yet have a meaningful field population.

## 4. Compatibility

**WEB-QUA-007 — Declared compatibility coverage.** A compatibility claim MUST identify the compatibility environments to which it applies and any material exclusions or limitations. A generic claim such as “cross-browser compatible” MUST NOT imply unbounded browser, version, runtime, or device coverage.

**WEB-QUA-008 — Material feature compatibility.** Material capabilities required to understand or use the declared scope MUST operate as represented in each claimed compatibility environment or have a declared alternative that preserves the applicable bounded capability. Compatibility documentation, specification status, feature databases, or vendor claims MAY inform coverage decisions but MUST NOT alone establish the delivered result.

**WEB-QUA-009 — Compatibility fallback integrity.** When a fallback, alternate implementation, progressive enhancement, polyfill, or other compatibility treatment is relied upon to satisfy the declared profile, the delivered treatment MUST be verified under the condition that requires it and MUST NOT be represented as available solely because it is documented or present in source.

## 5. Resilience and Regression

**WEB-QUA-010 — Declared resilience conditions.** A resilience conclusion MUST identify the material degraded or failure conditions it covers. Offline operation, low-bandwidth behavior, third-party failure, cache availability, or other resilience scenarios are not automatically required unless selected by the quality profile or otherwise applicable to the declared claim.

**WEB-QUA-011 — Degraded-delivery integrity.** Under a declared resilience condition, the delivered experience MUST preserve the bounded capability represented by that profile or explicitly establish that the capability is unavailable. A degraded state MUST NOT be represented as equivalent to the normal state when material capability is absent. Content meaning, interaction recovery, and accessibility of the degraded state remain separately owned by their applicable authorities.

**WEB-QUA-012 — Dependency-failure containment.** Where a declared resilience profile requires continued bounded use despite failure of a material dependency, resource, or service, the failure MUST NOT unnecessarily prevent unrelated capability that the profile represents as remaining available. This requirement does not mandate offline operation, duplicate infrastructure, a service worker, a specific fallback architecture, or backend availability guarantees.

**WEB-QUA-013 — Regression-sensitive evidence.** For material performance, compatibility, or resilience risks, verification SHOULD include a repeatable comparison or regression-sensitive method when such a method is reasonably available and proportionate. A departure is legitimate when repeatability is impractical or would not materially improve confidence, but the resulting evidence limitations SHOULD remain explicit.

## 6. Verification and Results

**WEB-QUA-014 — Shared and reviewable evidence.** Evidence MUST be proportionate to the obligation and sufficient to trace a result to the assessed scope and revision, applicable requirement, quality profile, method and environment, expected and observed result, reviewer or tool, date, limitations, and unresolved findings. Shared context MAY be referenced rather than repeated. Tool output, compatibility data, screenshots, traces, monitoring data, test results, or sibling-standard evidence MUST NOT be treated as proof of conclusions they cannot establish.

Automated tools MAY establish detectable measurements, browser behavior, resource outcomes, or regression differences. Human review is required where deciding materiality, representativeness, applicability, resilience sufficiency, or claim scope exceeds the method's capability. No vendor, analytics service, browser list, test framework, evidence format, storage system, or universal review ceremony is prescribed.

**WEB-QUA-015 — Distinct and truthful results.** Results MUST distinguish local-standard conformance, partial assessment, nonconformance, and undetermined obligations. An obligation is undetermined when it is applicable but evidence is missing, inaccessible, incomplete, conflicting, stale, or otherwise insufficient; this differs from an obligation outside the declared scope. Local-standard conformance requires the declared scope to satisfy every applicable mandatory requirement of the identified adopted version. Partial coverage is not a reduced conformance level, and missing environment access or missing evidence MUST NOT be converted into a pass.

Any conformance claim MUST identify the adopted standard version, evaluated artifact revision, assessed scope, selected quality profile, material exclusions, and conclusion. A quality-and-verification result MUST NOT be represented as accessibility conformance, content-semantic conformance, design-foundation conformance, responsive-layout conformance, interaction conformance, security approval, infrastructure availability certification, legal compliance, brand approval, or whole-suite conformance.

**WEB-QUA-016 — Change and reassessment.** A material change to implementation, content or resource composition, dependencies, browser/runtime support, selected compatibility environments, performance metric definition or target, measurement method, population, resilience condition, quality profile, assessed scope, or relevant evidence MUST trigger reassessment of the obligations whose results may be affected before a current conclusion is asserted. Unaffected evidence MAY be reused when its applicability to the current revision and obligation is justified; reuse MUST NOT conceal stale or invalidated results.

## 7. Informative Verification Guidance

This section is informative.

Performance evidence should match the claim. Field data describes actual observed populations; controlled lab and synthetic tests provide repeatability and can detect regressions before release. Neither should be silently substituted for the other. A pre-release experience can make a bounded lab-performance claim without pretending that real-user data exists.

Core Web Vitals are useful externally defined performance signals, but they are not the only valid quality profile. Their definitions and recommended thresholds are maintained externally and can change. An adopter that selects them should record the selected definitions, thresholds, aggregation, and data source rather than relying on a generic “good performance” label.

Compatibility evidence should combine source knowledge with delivered verification. Standards maturity and browser-compatibility databases can help select environments, but a support table cannot establish that a particular application correctly integrates the feature. Conversely, a browser-specific implementation need not be rejected merely because another technique is more fashionable if the declared compatibility outcomes are satisfied.

Resilience is conditional rather than synonymous with offline support. An informational site, transactional flow, embedded widget, and highly connected application can have very different justified resilience profiles. Service workers, caches, static fallbacks, server rendering, feature detection, dependency isolation, or explicit unavailability can each be appropriate mechanisms.

Shared verification infrastructure can reduce duplicate work. The same environment description, artifact revision, or execution record can support several sibling assessments. This Standard does not take over the sibling requirement's meaning or conclusion merely because the evidence is stored or orchestrated centrally.

## 8. Adaptation and Boundaries

An adopting organization MAY define performance budgets, Core Web Vitals profiles, browser-support matrices, device classes, field-data policies, synthetic-test environments, resilience scenarios, compatibility baselines, regression tolerances, evidence forms, or stronger quality requirements through its existing authority. Such adaptations MUST identify their scope and consequences and MUST NOT be represented as requirements of an unchanged upstream template.

Accessibility, content-semantic, design-foundation, responsive-layout, and interaction obligations remain with their selected authorities. This Standard can govern shared evidence context or a separate quality claim without changing those substantive requirements or converting their results into Quality results. CSS architecture, application security/privacy, infrastructure SLOs, deployment, disaster recovery, backend durability, and organizational incident response remain outside this standard.

This standard does not require an adopter to use any published sibling standard. Cross-references clarify ownership and evidence reuse; they do not create a whole-standard adoption dependency.

### Strength and ownership rationale — informative

Mandatory requirements protect the integrity of performance, compatibility, resilience, evidence, and claims. The recommendation for regression-sensitive evidence remains a `SHOULD` because repeatability can be impractical for some field conditions or low-volume experiences even when the underlying quality conclusion can still be responsibly supported. Permissions preserve legitimate variation in tools, metrics, browsers, environments, measurement systems, resilience strategies, and evidence infrastructure.
