# Agent Guidance

## Before editing

- Read [MAINTAINING.md](MAINTAINING.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
- Read [NAMING.md](NAMING.md) when template identity or naming is involved.
- Read the [`standards-authoring`](templates/standards-authoring/standard.md) standard before changing normative templates.
- Inspect the current branch and worktree, and preserve unrelated user changes.
- Identify whether the request changes template scope, evidence, or repository structure.

## Adoption assistance

Before assisting an adoption, read root [ADOPTION.md](ADOPTION.md), the candidate template's adjacent `README.md`, the candidate `standard.md`, and the adopting source's existing authority.

Do not create or modify an adopted artifact until the proposed scope and adoption authority, existing authority and conflicts, canonical destination, provenance, protected effects, and proposed `adopt`, `adapt`, `reject`, or `defer` disposition have been reviewed.

Humans and agents use the same canonical adoption guidance; do not create a separate agent-only adoption policy.

## Before completion

- Run `python3 -m unittest discover -s tests` and `python3 scripts/validate.py`.
- Manually reverify affected external claims when citations change.
- Update `repository-structure.txt` only for an intentional structural change by running `python3 scripts/update_repository_structure.py`.
- Do not create templates, metadata, taxonomies, automation, or tooling merely because they are conventional.
