# Web Interface and Interaction Standard

## 1. Purpose and Scope

This standard defines baseline requirements for reliable, understandable, and reviewable interaction behavior within a declared web experience.

The operative question is whether a person can initiate an action, understand the material task state and resulting outcome, recover from recoverable failure, and continue or deliberately end the task without the interaction materially contradicting what the experience represented would happen.

It applies to actions, state transitions, pending and completion states, failures and recovery, preservation of user work, consequential actions, conditional and disclosed interaction, interruptions, overlays, action availability, repeated activation, and other material task behavior within the declared scope.

It is independently adoptable. It does not depend on a web-suite umbrella, component library, JavaScript framework, state-management architecture, accessibility pattern library, or another companion standard. Native behavior, navigation, server-driven interactions, client-side applications, progressive enhancement, dialogs, disclosures, inline updates, optimistic or pessimistic updates, and other mechanisms can satisfy it when the delivered behavior and evidence meet the applicable requirements.

This standard does not prescribe a component API, widget taxonomy, event API, focus algorithm, keyboard binding, confirmation dialog, modal, undo system, optimistic-update architecture, client-side validation strategy, state-management library, routing model, or framework.

Accessibility conformance, content semantics and wording, visual-foundation calibration, responsive layout, performance, security policy, transaction authority, editorial authority, and legal duties remain subject to separately selected authorities where applicable. Adoption, exceptions to local organizational rules, publication, and approval remain subject to the adopting organization's existing authority. Publication of this source does not adopt or update any downstream artifact.

## 2. Interpretation and Definitions

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html)) when, and only when, they appear in this uppercase form. Lowercase uses have their ordinary meaning.

`WEB-INT-NNN` identifies a local requirement synthesized by this template, independently of section numbers. Numbered local requirements are normative. Sections explicitly marked informative are not.

**Interaction state** means a material condition of an interactive task or control that can affect what action can be taken, what result is pending or complete, or how the task can continue. Examples can include idle, pending, completed, failed, unavailable, disclosed, selected, or interrupted states; this list does not require those names or states.

**Interaction transition** means a material change from one interaction state or task context to another caused by user action, system response, navigation, dynamic update, interruption, or another declared condition.

**Recoverable failure** means a failure after which the declared task can reasonably continue, be retried, revised, resumed, or safely exited without requiring the failure itself to be reclassified as success.

**Material** means capable of changing the task state, availability of an action, preservation of user work, a reasonable decision or action by the declared audience, an assessment result, or a conformance claim.

The [Web Accessibility Standard](../web-accessibility/standard.md), [Web Content and Semantics Standard](../web-content-semantics/standard.md), [Web Design Foundations Standard](../web-design-foundations/standard.md), and [Responsive Web Layout Standard](../responsive-web-layout/standard.md) retain their own identifiers, conditions, evidence, and results. Evidence MAY support more than one assessment when it actually addresses each obligation, but one result MUST NOT be represented as another.

## 3. Declared Interaction Context and Action Outcomes

**WEB-INT-001 — Declared assessment scope.** An assessment MUST identify the evaluated web experience, artifact or release revision, covered pages, views, components, material actions and task paths, relevant interaction states and transitions, material failure and interruption conditions, material third-party or embedded interactions, declared audience or audiences, and material exclusions. Any difference between assessed coverage and a claimed scope MUST be explicit.

**WEB-INT-002 — Reviewable interaction states and transitions.** Material interaction states and transitions MUST have reviewable intended behavior sufficient to evaluate what initiates them, what they represent, and how the task is expected to continue or end. They MAY be expressed through rendered examples, source behavior, state diagrams, component guidance, test cases, requirements, assessment records, or another suitable mechanism. A particular state machine, component model, or documentation format is not required.

**WEB-INT-003 — Action-result integrity.** A delivered interaction MUST NOT materially misrepresent the relationship between an initiated action and its actual known result. An action represented as completed, failed, cancelled, unavailable, or still pending MUST correspond to the state established by the delivered interaction evidence. When the underlying result is genuinely unknown or indeterminate, the interaction MUST NOT represent certainty that the evidence does not support. This requirement does not certify backend correctness, factual content, transaction authority, or legal effect beyond the assessed evidence.

**WEB-INT-004 — Pending and processing continuity.** When a material action does not complete within the interaction's immediate response, the delivered interaction MUST preserve a reviewable distinction between an action that is still pending and one that is idle, completed, failed, or ready for a materially conflicting action. The mechanism MAY be visual, textual, navigational, control-state-based, or otherwise appropriate. This requirement does not establish a performance threshold or accessibility-specific status-announcement requirement.

**WEB-INT-005 — Completion and outcome continuity.** When a material task or action reaches a known completion state, the delivered interaction MUST make that state available to the continuing task context and MUST NOT require the user to proceed on a materially false assumption about whether the action completed. Completion MAY lead to replacement content, navigation, in-place state change, a confirmation view, or another appropriate treatment. Content wording and accessible exposure remain separately owned.

## 4. Failure, Recovery, and User Work

**WEB-INT-006 — Recoverable failure.** A recoverable failure MUST provide a viable path to continue, retry, revise, resume, or deliberately exit the affected task where continued use is within the declared scope. The recovery path MUST correspond to the actual state of the task and MUST NOT require the failure to be treated as success. This requirement does not prescribe error-message wording, focus placement, or a specific retry mechanism.

**WEB-INT-007 — Preservation of user work and task state.** A recoverable failure, temporary interruption, or ordinary interaction transition MUST NOT unnecessarily discard material user-entered work or task state needed to continue the declared task. Non-preservation is permitted when it is necessary for security, privacy, data integrity, the action's stated purpose, a deliberate user choice, or another documented material constraint. This requirement does not require preservation of secrets, credentials, transient security values, or data whose retention would itself create a material risk.

**WEB-INT-008 — Consequential and difficult-to-reverse actions.** An action with materially destructive, costly, difficult-to-reverse, or otherwise high-consequence effects MUST require a deliberate interaction sufficient to distinguish the intended action from incidental or materially ambiguous input. Proportionate safeguards MAY include confirmation, review, undo, delay, staged commitment, explicit labeling, or another suitable mechanism. This requirement does not mandate a confirmation dialog or universal undo capability.

**WEB-INT-009 — Task-context continuity.** A material transition MUST preserve or deliberately resolve the task context necessary for the user to understand what happened and how to continue. Replacement content, navigation, refreshed data, changed selection, or another transition MUST NOT silently place the task into a materially contradictory state. This requirement addresses interaction continuity; semantic meaning, focus management, and layout position remain separately owned.

## 5. Conditional Interaction, Interruptions, and Availability

**WEB-INT-010 — Conditional and disclosed interaction.** When controls, content, or task options become available, unavailable, expanded, collapsed, selected, filtered, or otherwise conditionally presented through interaction, the delivered behavior MUST preserve a coherent relationship between the controlling action, resulting interaction state, and subsequent available task path. A disclosure or conditional change MUST NOT silently reset or contradict material task state unless that reset is inherent in the represented action or explicitly established by the interaction. Accessible state exposure and visual-role calibration remain separately owned. Spatial fitting and overflow behavior of the disclosed or conditionally presented content remain separately owned.

**WEB-INT-011 — Interruptions and overlays.** A modal, dialog, overlay, interstitial, interruption, or replacement interaction that suspends or diverts an in-progress task MUST preserve, deliberately complete, or deliberately abandon the material interrupted task state. Closing or resolving the interruption MUST NOT silently leave the underlying task in a materially contradictory or unknowable state. This requirement governs task continuity, not focus behavior, accessibility semantics, or overlay geometry.

**WEB-INT-012 — Action availability integrity.** A control or interaction represented as materially available or unavailable MUST behave consistently with that represented availability within the assessed task context. Preventing an action, permitting an action, queueing it, or deferring it MAY all be valid when consistent with what the interaction represents. This requirement does not prescribe disabled-control semantics, styling, or authorization policy.

**WEB-INT-013 — Repeated activation and duplicate effects.** An interaction MUST NOT cause materially unintended repeated effects solely because the same action is reactivated while its prior result is pending, unknown, or already represented as complete. The interaction MAY prevent repeated activation, make repeated effects intentional and explicit, safely deduplicate, provide reviewable retry semantics, or use another suitable mechanism. This requirement governs the delivered interaction result and does not prescribe backend idempotency architecture.

## 6. Verification and Results

**WEB-INT-014 — Reviewable evidence.** Evidence MUST be proportionate to the obligation and sufficient to trace a result to the assessed scope and revision, applicable requirement, relevant action/state/transition, method and environment, expected and observed result, reviewer or tool, date, limitations, and unresolved findings. Shared context MAY be referenced rather than repeated. A component-library example, state diagram, automated test, source inspection, screenshot, event log, or network trace MUST NOT be treated as proof of a delivered conclusion it cannot establish.

Automated inspection or scripted interaction MAY establish detectable state transitions, duplicate requests, control-state changes, navigation, or recorded outcomes. Human review is required where deciding task continuity, material consequence, recovery sufficiency, deliberate action, or contradiction exceeds the method's capability. Representative-user or specialist review MAY support difficult conclusions. No vendor, test framework, evidence format, storage system, or universal review ceremony is prescribed.

**WEB-INT-015 — Distinct and truthful results.** Results MUST distinguish local-standard conformance, partial assessment, nonconformance, and undetermined obligations. An obligation is undetermined when it is applicable but the available evidence is missing, incomplete, conflicting, or otherwise insufficient; this differs from an obligation outside the declared scope. Local-standard conformance requires the declared scope to satisfy every applicable mandatory requirement of the identified adopted version. Partial coverage is not a reduced conformance level, and missing evidence MUST NOT be converted into a pass.

Any conformance claim MUST identify the adopted standard version, evaluated artifact revision, assessed scope, material exclusions, and conclusion. An interface-and-interaction result MUST NOT be represented as accessibility conformance, content-semantic conformance, design-foundation conformance, responsive-layout conformance, performance or compatibility certification, backend correctness, security approval, legal compliance, brand approval, or whole-suite conformance.

**WEB-INT-016 — Change and reassessment.** A material change to actions, interaction states, task transitions, asynchronous behavior, completion or failure handling, recovery, user-work preservation, consequential actions, disclosure/conditional behavior, interruptions, action availability, repeated-activation handling, assessed scope, or relevant evidence MUST trigger reassessment of the obligations whose results may be affected before a current conclusion is asserted. Unaffected evidence MAY be reused when its applicability to the current revision and obligation is justified; reuse MUST NOT conceal stale or invalidated results.

## 7. Informative Verification Guidance

This section is informative.

Useful verification follows complete material task paths, including failure and retry conditions, rather than checking only individual controls in isolation. A control can behave correctly on its own while the surrounding task loses state or misrepresents completion.

Asynchronous interaction deserves observation before, during, and after the action. A long operation can be interaction-correct when its pending state is clear, even if a separately selected performance standard finds the duration unacceptable.

Recovery testing should include failures that occur after the user has invested material effort. Ordinary form values or selections often need to survive a retry, while credentials, security tokens, or other sensitive values can legitimately be cleared.

High-consequence actions do not require one universal confirmation pattern. An undo mechanism, staged commitment, explicit review step, or another safeguard can provide stronger continuity than a modal confirmation in some contexts.

APG and design-system patterns can help identify established interaction conventions, but using the documented pattern does not prove the shipped behavior is correct. Accessibility-specific keyboard, focus, state, and assistive-technology behavior requires its own assessment.

## 8. Adaptation and Boundaries

An adopting organization MAY define interaction-state vocabularies, risk tiers, confirmation or undo policies, autosave practices, retry conventions, timeout handling, preservation rules, evidence forms, or stronger requirements through its existing authority. Such adaptations MUST identify their scope and consequences and MUST NOT be represented as requirements of an unchanged upstream template.

Accessibility requirements for keyboard/pointer operability, focus behavior, accessible names and states, status announcements, timing accessibility, and assistive-technology exposure remain with the adopter's selected accessibility authority. Intended message meaning, instructions, labels, error content, and semantic structure remain with the selected content-semantic authority. Visual state treatment remains with the selected design-foundation authority. Spatial behavior remains with the selected responsive-layout authority. Performance, compatibility, resilience engineering, security policy, transaction authorization, backend consistency, and organizational approval remain outside this standard.

This standard does not require an adopter to use any published sibling standard. Cross-references clarify boundaries and do not create a whole-standard adoption dependency.

### Strength and ownership rationale — informative

Mandatory requirements protect task-state truthfulness, action-result integrity, recovery, preservation of user work, deliberate consequential actions, task continuity, coherent conditional interaction, interruption handling, availability integrity, duplicate-effect handling, and truthful claims. Permissions preserve legitimate variation in architecture, interaction patterns, controls, navigation, confirmation, undo, retry, state management, and implementation technology.
