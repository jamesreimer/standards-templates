# Pull Request

## Summary

What changed and why?

## Scope / Boundary Impact

Did this change alter template scope, conceptual boundaries, applicability, or repository structure?

## Template Editions

For each changed `standard.md`, declare `template-id: old → new` and explain the meaning/citable-identity or editorial classification. For new templates declare `1.0`; for renames/moves identify old/current paths and the carried edition. Otherwise confirm editions are unchanged (or identify the initial baseline labeling).

For an edition-only correction, identify the earlier misclassified transition and explain why it was misclassified. Use ``Edition correction: `template-id` at `<full-transition-commit-sha>` `` on its own line and retain it in the squash commit message; see [CONTRIBUTING.md](../CONTRIBUTING.md#edition-validation).

## External Evidence

Did any cited external claim change? If yes, confirm that the source was reverified.

## Adoption Impact

Adoption impact:

- No
- Yes
- Unclear

If yes or unclear, briefly explain what organizations that adopted an earlier revision should review. This repository does not push or synchronize changes downstream.

## Validation

Confirm that the full pre-commit composition and `git diff --check` passed, that changed validation includes positive and injected-defect evidence, and that any required manual evidence review was completed. For adoption changes, identify the immutable upstream baseline and verify each claimed exact-copy relationship.
