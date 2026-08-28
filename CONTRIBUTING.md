# Contributing

Keep contributions bounded to a concrete reusable need or defect. Use [MAINTAINING.md](MAINTAINING.md) for the maintainer review criteria, [NAMING.md](NAMING.md) for template identity and titles, and [CATALOG.md](CATALOG.md) to check current ownership and boundaries.

## New template

```text
identify a concrete reusable need
    ↓
check whether an existing template already owns the subject
    ↓
apply NAMING.md
    ↓
author against standards-authoring
    ↓
separate external facts from synthesized rules
    ↓
update CATALOG.md
    ↓
update repository structure snapshot if needed
    ↓
run tests and validation
    ↓
submit a reviewable change
```

A subject does not earn a template merely because an external standards body covers it. General applicability is the default unless the protected consequence genuinely depends on a narrower domain. Do not annex neighboring conceptual territory for completeness. New metadata, taxonomy, automation, or tooling needs a concrete consumer or failure mode.

Author normative documents against the [`standards-authoring`](templates/standards-authoring/) template and follow the repository structure in [README.md](README.md).

## Existing template revision

```text
identify concrete defect or need
    ↓
open or reference an issue/proposal when warranted
    ↓
modify the canonical template
    ↓
review scope, boundaries, and normative calibration
    ↓
reverify affected external claims
    ↓
run tests and validation
    ↓
submit for review
```

Keep the change within the template's established responsibility unless the proposal explicitly justifies a scope correction. Reverify any external claim or citation affected by the revision.

## Validation

Run both checks before submitting a change:

```bash
python3 -m unittest discover -s tests
python3 scripts/validate.py
```

When an intentional change adds, removes, or moves repository paths, regenerate the reviewed structure snapshot before validation:

```bash
python3 scripts/update_repository_structure.py
```

Automated validation checks mechanical repository invariants. Human review remains responsible for normative calibration, applicability, conceptual boundaries, external evidence, and prose quality as described in [MAINTAINING.md](MAINTAINING.md).
