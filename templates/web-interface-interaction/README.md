# Web Interface and Interaction Template

Stable template ID: `web-interface-interaction`

Human-facing title:

> **Web Interface and Interaction Standard**

## Purpose

Use this template when an organization needs a reusable standard for reliable task states, action outcomes, asynchronous progress, failure recovery, user-work preservation, consequential actions, interruptions, and interaction continuity across web experiences.

The reusable template is [standard.md](standard.md).

This template is independently adoptable. It does not require a Web Standards Suite umbrella, the Web Accessibility Standard, the Web Content and Semantics Standard, the Web Design Foundations Standard, the Responsive Web Layout Standard, a component library, a JavaScript framework, or another companion template.

## Adoption

Use the universal review in [ADOPTION.md](../../ADOPTION.md) first. Organizational authority, existing protections, conflicts, destination, provenance, migration, protected effects, and later-source review are handled there, not replaced by this subject-specific guidance.

The questions below are informative review aids. They do not create a prescribed approval ceremony.

## Subject-specific adoption review

In addition to the universal review, determine:

1. Which existing interaction patterns, component libraries, state-management systems, platform conventions, or legacy workflows already govern the proposed scope?
2. Which material task paths include pending, loading, completion, failure, retry, cancellation, unavailable, interrupted, or indeterminate states?
3. Which actions can be destructive, costly, difficult to reverse, legally consequential, or otherwise high consequence?
4. Which tasks contain user-entered work or selections whose loss would materially increase recovery burden?
5. Which operations can complete asynchronously, out of order, ambiguously, or after navigation?
6. Which interactions permit repeated activation, retry, refresh, back/forward navigation, or resubmission that can create duplicate effects?
7. Which disclosures, accordions, tabs, menus, dialogs, modals, interstitials, or conditional interfaces materially alter task state?
8. Which third-party widgets, hosted flows, payment surfaces, authentication steps, or embedded interactions are within the adopter's control and assessment scope?
9. Which accessibility authority governs keyboard and pointer operability, focus, accessible names/states, status announcements, timing, and assistive-technology exposure?
10. Which content-semantic authority governs labels, instructions, error-message meaning, factual state descriptions, and semantic structure?
11. Which visual and responsive-layout authorities govern state styling, hierarchy, clipping, overlay fitting, and spatial continuity?
12. Which security, backend transaction, authorization, performance, compatibility, and legal responsibilities must remain outside this Standard?

## Likely adaptation choices

An adopter may need to define:

- interaction-state vocabularies;
- task-risk or consequence tiers;
- confirmation, review, undo, or staged-commitment policies;
- autosave and user-work preservation rules;
- retry, cancellation, resumption, and timeout conventions;
- duplicate-action or resubmission handling;
- asynchronous/pending-state conventions;
- interruption and modal policies;
- third-party interaction boundaries;
- representative failure and recovery scenarios;
- stronger evidence requirements for high-consequence workflows;
- ownership and review routing for security- or transaction-specific decisions.

These choices are not requirements of the unchanged upstream template. Record adaptations and provenance through the adopter's existing standards system.

## Important boundaries

This template:

- governs delivered task behavior, state continuity, recovery, and action-result integrity;
- permits native controls, navigation, server-driven interaction, client-side applications, dialogs, disclosures, inline updates, optimistic or pessimistic updates, and other mechanisms;
- does not prescribe a component API, ARIA pattern, keyboard model, focus algorithm, JavaScript framework, state-management architecture, modal, confirmation dialog, undo system, or client-side validation strategy;
- does not establish WCAG or legal accessibility conformance;
- does not establish content-semantic, design-foundation, responsive-layout, performance, compatibility, security, backend-correctness, brand-approval, or whole-suite conformance;
- does not make upstream changes automatically authoritative downstream.

## Verification considerations

Plan complete task-path review rather than checking individual controls or screenshots alone.

Useful coverage commonly includes:

- action initiation and known/unknown results;
- pending and asynchronous operations;
- successful completion and post-completion state;
- transient and persistent failure;
- retry, cancellation, resumption, and deliberate exit;
- user-entered work before and after failure;
- destructive or difficult-to-reverse actions;
- disclosure and conditional state changes;
- modals, dialogs, overlays, interstitials, and replaced content;
- repeated activation and duplicate-effect scenarios;
- unavailable or disabled actions;
- navigation and context changes during multi-step tasks;
- representative third-party interactions;
- differences between documented component behavior and shipped implementation.

Automated tools can exercise actions, capture events, compare state, inspect network activity, and detect repeated requests. Human review remains necessary for task continuity, consequence, recovery sufficiency, deliberate action, and contextual correctness. Do not claim states, failures, retries, recovery paths, users, environments, or third-party behavior that were not actually evaluated.

## Related templates

- [Web Accessibility](../web-accessibility/README.md) owns its selected accessibility target and accessibility-specific keyboard, focus, accessible-state, status, timing, and assistive-technology evidence and claims.
- [Web Content and Semantics](../web-content-semantics/README.md) owns intended message meaning, labels, instructions, error content, and semantic structure.
- [Web Design Foundations](../web-design-foundations/README.md) owns visual hierarchy and visual-role calibration for interaction states.
- [Responsive Web Layout](../responsive-web-layout/README.md) owns spatial adaptation, clipping, overflow, overlay fitting, and responsive composition.
- A future Quality and Verification template may govern performance, compatibility, resilience, and shared evidence-system requirements without taking over this template's interaction-specific findings.
- A future Styling Architecture template may govern style ownership and change containment if independently justified.

Future references describe boundaries only. They neither require those templates nor claim that unpublished companions already exist.
