# Web Quality and Verification Template

Stable template ID: `web-quality-verification`

Human-facing title:

> **Web Quality and Verification Standard**

## Purpose

Use this template when an organization needs a reusable standard for credible performance, compatibility, resilience, regression, and verification claims across web experiences.

The reusable template is [standard.md](standard.md).

This template is independently adoptable. It does not require a Web Standards Suite umbrella, any sibling Web Standard, an analytics platform, monitoring vendor, test framework, browser-automation system, performance tool, service worker, or evidence repository.

## Adoption

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. Organizational authority, existing protections, conflicts, destination, provenance, migration, protected effects, and later-source review are handled there, not replaced by this subject-specific guidance.

The questions below are informative review aids. They do not create a prescribed approval ceremony.

## Subject-specific adoption review

In addition to the universal review, determine:

1. Which performance budgets, service targets, compatibility matrices, browser-support policies, or quality gates already govern the proposed scope?
2. Which performance claims are field claims, lab claims, synthetic claims, pre-release targets, or regression comparisons?
3. Which metrics, thresholds, percentiles, populations, devices, network conditions, or environments materially affect those claims?
4. Which browser engines, versions, embedded user agents, operating systems, or device classes are actually important to the declared audience and distribution?
5. Which Web platform features are material to the experience, and where do compatibility databases or standards maturity indicate elevated verification risk?
6. Which fallbacks, progressive enhancements, polyfills, alternate resources, or degraded treatments are expected to preserve capability?
7. Which third-party resources, CDNs, APIs, payment/authentication surfaces, fonts, media hosts, or other dependencies can materially affect delivered quality?
8. Which network degradation, dependency failure, resource failure, or offline scenarios are genuinely part of the required resilience profile?
9. Which field environments or browsers are unavailable for testing, and how will those verification gaps affect claims?
10. Which existing CI, monitoring, analytics, synthetic-testing, browser-automation, or regression systems can supply evidence without becoming mandatory dependencies?
11. Which sibling standards own the substantive accessibility, content, design, layout, or interaction results that may share this evidence?
12. Which infrastructure SLOs, deployment controls, security/privacy obligations, backend durability requirements, and incident practices must remain outside this Standard?

## Likely adaptation choices

An adopter may need to define:

- performance metrics, thresholds, budgets, and percentiles;
- field-versus-lab evidence policies;
- browser/runtime compatibility coverage;
- representative devices and network conditions;
- synthetic or browser-automation environments;
- compatibility fallback expectations;
- resilience conditions and degraded capability profiles;
- dependency-failure scenarios;
- regression tolerances and comparison methods;
- field-data availability/minimum-sample conventions;
- evidence storage or reporting formats;
- stronger requirements for high-risk or high-volume experiences.

These choices are not requirements of the unchanged upstream template. Record adaptations and provenance through the adopter's existing standards system.

## Important boundaries

This template:

- governs credible performance, compatibility, resilience, and verification claims;
- may provide shared evidence context without taking over sibling standards' substantive results;
- permits field measurement, lab tests, synthetic tests, direct observation, browser automation, feature detection, progressive enhancement, caching, service workers, fallbacks, or other suitable mechanisms;
- does not prescribe universal Core Web Vitals thresholds, browser/device matrices, analytics, Lighthouse, WPT, service workers, monitoring, or test infrastructure;
- does not establish accessibility, content-semantic, design-foundation, responsive-layout, interaction, security, infrastructure-availability, legal, brand-approval, or whole-suite conformance;
- does not make upstream changes automatically authoritative downstream.

## Verification considerations

Plan evidence around the claim being made, not around whichever tool is easiest to run.

Useful coverage commonly includes:

- field versus lab versus synthetic evidence;
- repeated measurements and distribution where relevant;
- performance metric definitions and thresholds;
- mobile/desktop or other population segmentation where adopted;
- browser/runtime environments in the declared compatibility profile;
- materially used platform features;
- partial-support and fallback conditions;
- low-bandwidth, interrupted, or failed dependency conditions selected by the resilience profile;
- third-party resource failure;
- regression comparisons across revisions;
- inaccessible or untested environments recorded as gaps;
- shared evidence reused across sibling assessments without merging their conclusions.

Automated tools can measure timing, execute browser tests, compare revisions, inspect resource behavior, and detect regressions. Human review remains necessary for representativeness, materiality, profile applicability, degraded-capability sufficiency, and claim scope. Do not claim populations, browsers, devices, field conditions, resilience cases, or sibling conclusions that were not actually established.

## Related templates

- [Web Accessibility](../web-accessibility/README.md) retains accessibility-specific requirements and conclusions.
- [Web Content and Semantics](../web-content-semantics/README.md) retains content meaning and semantic conclusions.
- [Web Design Foundations](../web-design-foundations/README.md) retains visual-foundation conclusions.
- [Responsive Web Layout](../responsive-web-layout/README.md) retains layout and responsive-composition conclusions.
- [Web Interface and Interaction](../web-interface-interaction/README.md) retains task-state and interaction conclusions.
- A future Styling Architecture template may govern style ownership and change containment if independently justified.
- A future Web Experience Baseline may compose declared companion results into suite-level claims without changing this template's independent adoption.

Future references describe boundaries only. They neither require those templates nor claim that unpublished companions already exist.
