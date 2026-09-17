# Provenance

This repository consumes reusable repository mechanics from another repository.
This record identifies that source, the exact state consumed, and what each
copied file's relationship actually is.

It exists because [`shared-asset-provenance`](templates/shared-asset-provenance/)
requires it. Using an externally sourced validator as the mechanism that decides
whether this repository passes validation is Authoritative Consumption under
§3, so §5 requires binding that input to an explicit Source Identity, an
appropriate Immutable Consumed Identity, and verification that the content used
corresponds to both.

## Source

| | |
| --- | --- |
| Source Identity | [`jamesreimer/repo-template`](https://github.com/jamesreimer/repo-template) |
| Immutable Consumed Identity | `4318faa00cd6d02c78247ed799fbcae61210a43c` |
| Consumed | 2026-09-16 |

§6 requires an exact repository revision for direct repository-source
consumption, so the commit hash above is the binding identity. A branch name, a
tag, a sibling checkout, or a local path is a Moving Reference under §7 and is
not sufficient. A nearby working copy of `repo-template` may be used to discover
a candidate revision, but the content adopted must be verified against the hash
above before it is relied upon.

## History of ownership

The mechanics in this repository did not originate upstream.

They were written here first. `repo-template` was created afterwards, by
generalizing them out of this repository into a reusable foundation, and this
repository was its first consumer. Adoption therefore transferred ownership
upstream rather than recording a dependency that always existed.

That transfer is legitimate and deliberate: ownership follows system
responsibility rather than file history, and a repository whose purpose is
publishing standards templates was never the right long-term owner of generic
repository mechanics. But §4.1 forbids silently redefining a source or
reversing a declared maintenance relationship, and §12 requires distinguishing
historical provenance from continuing ownership. Both directions are recorded
here so neither is mistaken for the other.

Adoption also pushed capability upstream rather than only pulling it down. Nine
generic checks that existed only here were contributed to `repo-template`
across two reconciliation rounds, so that they would be owned once rather than
duplicated: committed symlinks, reference-label resolution, heading-level
skips, per-scope path naming, a single leading H1, fenced code block balance,
reference-definition validity and uniqueness, and correct loading of a local
check module.

## Relationship classes

| Class | Files | Expectation |
| --- | --- | --- |
| **Exact Copy** | `scripts/validate.py`, `scripts/update_repository_structure.py`, `scripts/setup_git_hooks.py`, `tests/test_validate.py`, `.editorconfig`, `.githooks/pre-commit`, `.vscode/settings.json`, `.github/dependabot.yml` | Byte-identical to the consumed revision. Never edited here. |
| **Adapted Copy** | `AGENTS.md`, `CONTRIBUTING.md`, `README.md`, `SECURITY.md`, `ruff.toml`, `.gitignore`, `.gitattributes`, `.markdownlint-cli2.jsonc`, `.github/workflows/validate.yml`, `.github/pull_request_template.md` | Seeded upstream, then intentionally diverged. Not overwritten wholesale. |
| **Local** | `validate.json`, `scripts/validate_local.py`, `tests/test_validate_local.py`, `LICENSE`, all standards content | Authored here. No upstream equivalent. |
| **Generated** | `repository-structure.txt` | Produced by the generator. Never copied from upstream. |

§10 requires that an Exact Copy not be silently modified while still being
represented as exact. Verify correspondence with:

```bash
diff -r --brief <path-to-repo-template>/scripts/validate.py scripts/validate.py
```

If an Exact Copy needs to change, the change belongs upstream. If local
divergence ever becomes legitimate and durable, reclassify the file here rather
than leaving the claim of exactness false.

## Updating

There is no synchronization mechanism, and none is wanted. Upstream changes are
review candidates, never automatic downstream updates, which is also upstream's
own stated position.

To adopt a newer revision:

1. Review what changed upstream since the revision recorded above.
2. Copy the Exact Copy files from the new revision.
3. Run the full validation set and confirm no defect class this repository
   detects has stopped being detected.
4. Update the Immutable Consumed Identity in this file in the same change.

Step 3 is the one that matters. Adoption can narrow coverage without any
failure signal: validation still passes, continuous integration still reports
green, and the loss is visible only by testing the defect classes directly.
Both reconciliation rounds during the initial adoption were found that way.

Resolution of any future divergence belongs to this repository. Recording
provenance does not give `repo-template` continuing authority here.
