# Web Accessibility Template

Stable template ID: `web-accessibility`

Human-facing title:

> **Web Accessibility Standard**

## Purpose

The reusable template is [`standard.md`](standard.md). It defines a web-accessibility target and the assessment, evidence, and claim discipline needed to evaluate it. It is independently adoptable; no umbrella or other companion is required.

This README is informative adoption guidance for humans and AI agents, not a second normative layer. Adopting the template does not establish that a web experience conforms to WCAG or applicable law.

## Adoption

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. Organizational authority, conflicts, destination, provenance, protected effects, and relationship choices are handled there, not replaced by this subject-specific guidance.

The default technical target is WCAG 2.2 Level AA from the fixed W3C Recommendation dated 12 December 2024. The template incorporates the source's complete applicable conformance conditions rather than copying a checklist. Local `WEB-A11Y-NNN` requirements govern the additional assessment discipline; they do not rename WCAG success criteria.

An organization may select another target through its own authority. A stronger local target is not a new WCAG level; a different or weaker target does not support unchanged WCAG 2.2 AA claims. Each external claim depends on the actual edition, level, scope, and results. Upstream changes never update the adopted artifact automatically.

## Subject-specific adoption review

In addition to the universal review, determine:

- Do existing accessibility commitments, legal obligations, contracts, or platform constraints require a different edition, level, or additional scope? Who can resolve a conflict without treating this template as legal certification?
- Can the assessed experience, release, pages, states, responsive variations, and complete processes be identified without misleading exclusions? How will third-party content and alternate versions be assessed under the source's actual conditions?
- Can evidence cover every applicable success criterion and the conformance requirements beyond the criteria, including accessibility support and non-interference?
- Are automated, manual, assistive-technology, and specialist capabilities sufficient for the intended scope? Where would unavailable environments, unsupported languages, missing expertise, or sampling leave the result undetermined?
- Do existing claims or reporting systems distinguish external WCAG conformance, local-standard conformance, partial assessment, known failure, source-defined partial-conformance statements, and undetermined results?
- Would adoption require reassessing existing claims or evidence? What migration and validation consequences follow from a changed target, and what existing commitments remain protected?
- Does candidate wording prematurely assert approval or conformance, or contain provisional statements that would become false on publication? Are any historical statements clearly contextualized, and would finalization require renewed review under the organization's existing process?

These are pre-adoption safety questions, not a prescribed approval ceremony.

## Likely organization-specific adaptation choices

Review whether there is a justified need to adapt:

- the technical target or additional accessibility obligations, with explicit claim consequences;
- the governed web-experience scope and release identification conventions;
- relevant technologies, languages, environments, and the basis for selecting evaluation coverage;
- assignment of evaluation responsibilities using existing roles;
- evidence representation and integration with existing review or quality systems;
- reassessment triggers more specific to the organization's products or publishing activity.

Customization is not required when the defaults fit. Local waivers cannot rewrite WCAG's conformance conditions or turn an unverified result into a pass.

## Verification considerations

Automation is useful but does not replace knowledgeable human judgment. Manual evaluation, actual assistive-technology behavior, and specialist input address different evidence needs. An AI-generated test plan is not an executed test; a clean scan is not full conformance; a sample does not automatically establish unexamined scope. Evidence needs to remain tied to the actual assessed revision and context.

The template does not mandate a vendor, fixed browser matrix, audit service, badge, file format, or retention system. Its evidence requirements support reviewable conclusions rather than administrative machinery.

Inclusive-use research and participation by people with disabilities can inform improvements beyond the target. They remain informative here, not an independently verified inclusive-design conformance model.

## Boundaries

Accessibility consequences remain in scope even when they arise in design, layout, interaction, content, semantics, or media. This template does not own those subjects' broader conventions. It retains accessibility-specific verification without prescribing a general quality-management system. It neither determines legal obligations nor creates organizational approval competence.

No other proposed web standard is made a dependency by this template. Its adjacent guidance does not create a separate AI policy or authorize downstream mutation.

## Primary sources

- [WCAG 2.2, W3C Recommendation, 12 December 2024](https://www.w3.org/TR/2024/REC-WCAG22-20241212/) — fixed normative external dependency; the standard's source map identifies the incorporation boundary.
- [WCAG 2.2 errata](https://www.w3.org/WAI/WCAG22/errata/) — reviewed as of 2 September 2026; acknowledged without silently replacing the dated dependency.
- [W3C Evaluating Web Accessibility Overview](https://www.w3.org/WAI/test-evaluate/) — informative evaluation guidance.
- [Understanding Conformance](https://www.w3.org/WAI/WCAG22/Understanding/conformance.html) — informative explanation, not replacement normative text.
- [ARIA Authoring Practices Guide introduction](https://www.w3.org/WAI/ARIA/apg/about/introduction/) — informative implementation guidance, not an additional conformance target.
