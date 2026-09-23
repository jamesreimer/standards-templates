"""Real-Git transition and injected-defect tests for template editions."""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import check_template_editions as editions  # noqa: E402
from validate_local import DomainInput, StandardsChecks, template_edition  # noqa: E402


def readme(template_id="example", edition="1.0"):
    label = "" if edition is None else f"\nTemplate edition: `{edition}`\n"
    return f"# Example\n\nStable template ID: `{template_id}`\n{label}\nHuman-facing title:\n\n> **Example**\n"


class EditionFormatTests(unittest.TestCase):
    def test_valid(self):
        for value, expected in [("1.0", (1, 0)), ("12.34", (12, 34))]:
            with self.subTest(value=value):
                self.assertEqual(template_edition(readme(edition=value)), expected)

    def test_snapshot_validator_reports_edition_defects(self):
        for content in [
            readme(edition=None),
            readme(edition="01.0"),
            readme() + "\nTemplate edition: `1.0`\n",
        ]:
            files = {
                "templates/example/README.md": content,
                "templates/example/standard.md": "# Example\n",
            }
            findings = StandardsChecks(DomainInput(tuple(files), files)).run()
            self.assertTrue(any("edition" in reason for _, _, reason in findings))

    def test_multiple_blank_lines_are_paragraph_separators(self):
        self.assertEqual(template_edition(readme().replace("\n\n", "\n\n\n")), (1, 0))

    def test_invalid_numbers(self):
        for value in ["0.0", "01.0", "1.00", "1.-1", "-1.0", "1", "1.2.3", "1.a", "１.0"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                template_edition(readme(edition=value))

    def test_missing_duplicate_malformed_and_fenced(self):
        for content in [
            readme(edition=None),
            readme() + "\nTemplate edition: `1.0`\n",
            readme() + "\nTemplate edition: broken\n",
            readme().replace("Template edition: `1.0`", "Template edition: 1.0"),
            readme().replace("Template edition: `1.0`", "```\nTemplate edition: `1.0`\n```"),
            readme().replace("Template edition: `1.0`", "> Template edition: `1.0`"),
        ]:
            with self.subTest(content=content), self.assertRaises(ValueError):
                template_edition(content)
        self.assertEqual(
            template_edition(readme() + "\n```\nTemplate edition: `5.0`\n```\n"), (1, 0)
        )

    def test_paragraph_placement(self):
        for content in [
            readme().replace("`example`\n\n", "`example`\n"),
            readme().replace("\n\nHuman-facing", "\nHuman-facing"),
            readme().replace("Template edition:", "Intervening prose\n\nTemplate edition:"),
            readme().replace("Template edition:", "```\nexample\n```\n\nTemplate edition:"),
        ]:
            with self.subTest(content=content), self.assertRaises(ValueError):
                template_edition(content)

    def test_missing_only_allowed_for_historical_bootstrap(self):
        self.assertIsNone(template_edition(readme(edition=None), allow_missing=True))
        with self.assertRaises(ValueError):
            template_edition(readme(edition="bad"), allow_missing=True)


class GitEditionTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Edition Test")
        self.git("config", "user.email", "edition@example.invalid")
        self.git("config", "core.hooksPath", str(self.root / "no-hooks"))
        self.write()
        self.initial = self.commit("Initial template")
        self.git("update-ref", "refs/remotes/origin/main", self.initial)
        self.git("switch", "-q", "-c", "candidate")

    def git(self, *args):
        return (
            subprocess.check_output(["git", *args], cwd=self.root, stderr=subprocess.PIPE)
            .decode()
            .strip()
        )

    def write(self, template_id="example", edition="1.0", content=b"# Example\n"):
        directory = self.root / "templates" / template_id
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "README.md").write_text(readme(template_id, edition))
        (directory / "standard.md").write_bytes(content)

    def commit(self, message):
        self.git("add", ".")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def check(self, env=None, base=None):
        return editions.validate(self.root, env or {}, base)

    def event(self, name, payload, sha=None):
        # Event outside inventory, just as GITHUB_EVENT_PATH is on the runner.
        event_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
        self.addCleanup(Path(event_file.name).unlink)
        json.dump(payload, event_file)
        event_file.close()
        return {
            "GITHUB_ACTIONS": "true",
            "GITHUB_EVENT_NAME": name,
            "GITHUB_EVENT_PATH": event_file.name,
            "GITHUB_SHA": sha or self.git("rev-parse", "HEAD"),
        }

    def test_unchanged_and_readme_only(self):
        self.assertEqual(self.check(), [])
        path = self.root / "templates/example/README.md"
        path.write_text(path.read_text() + "\nGuidance only.\n")
        self.assertEqual(self.check(), [])

    def test_exact_content_transitions(self):
        for label in ["1.1", "2.0"]:
            with self.subTest(label=label):
                self.write(edition=label, content=b"# Changed\n")
                self.assertEqual(self.check(), [])

    def test_missing_skipped_decreased_and_invalid_bumps(self):
        for label in ["1.0", "1.2", "2.1", "3.0"]:
            with self.subTest(label=label):
                self.write(edition=label, content=b"# Changed\n")
                self.assertTrue(self.check())
        self.write(edition="2.2")
        base = self.commit("Later base")
        self.write(edition="1.0", content=b"# Changed\n")
        self.assertTrue(self.check(base=base))

    def test_byte_changes_not_newline_normalized(self):
        self.write(content=b"# Example\r\n")
        self.assertTrue(self.check())

    def test_edition_only_mutations_fail(self):
        for label in ["1.1", "2.0", "3.0"]:
            with self.subTest(label=label):
                self.write(edition=label)
                self.assertTrue(self.check())

    def test_untracked_new_template_and_ignored_inventory(self):
        self.write("new-template")
        self.assertEqual(self.check(), [])
        self.write("new-template", "2.0")
        self.assertTrue(self.check())
        (self.root / ".gitignore").write_text("templates/new-template/\n")
        self.assertEqual(self.check(), [])

    def test_missing_tracked_file_fails_closed(self):
        (self.root / "templates/example/standard.md").unlink()
        with self.assertRaises(OSError):
            self.check()

    def test_symlink_input_fails_closed(self):
        (self.root / "templates/example/standard.md").unlink()
        (self.root / "templates/example/standard.md").symlink_to("/dev/zero")
        with self.assertRaises(OSError):
            self.check()

    def test_missing_pair_and_malformed_edition_fail_closed(self):
        (self.root / "templates/new").mkdir()
        (self.root / "templates/new/README.md").write_text(readme("new"))
        with self.assertRaises(ValueError):
            self.check()
        shutil.rmtree(self.root / "templates/new")
        self.write(edition="bad")
        with self.assertRaises(ValueError):
            self.check()

    def move(self, old="example", new="renamed"):
        self.git("mv", f"templates/{old}", f"templates/{new}")
        path = self.root / f"templates/{new}/README.md"
        path.write_text(path.read_text().replace(f"`{old}`", f"`{new}`"))

    def test_exact_move_carries_edition_with_other_content_changes(self):
        self.write("referrer", content=b"# References example\n")
        base = self.commit("Add referrer")
        self.move()
        self.write("referrer", "1.1", b"# References renamed\n")
        self.assertEqual(self.check(base=base), [])
        self.write("renamed", "1.1")
        self.assertTrue(self.check(base=base))

    def test_changed_move_cannot_reset_lineage(self):
        self.move()
        self.write("renamed", content=b"# Changed while moving\n")
        self.assertTrue(self.check())

    def test_ambiguous_moves_fail(self):
        self.write("duplicate")
        base = self.commit("Duplicate content")
        self.git("rm", "-qr", "templates/example", "templates/duplicate")
        self.write("renamed")
        self.assertTrue(self.check(base=base))

    def test_deletion_and_historical_id_reuse(self):
        self.git("rm", "-qr", "templates/example")
        self.assertEqual(self.check(), [])
        base = self.commit("Remove template")
        self.write(content=b"# Different lineage\n")
        self.assertTrue(self.check(base=base))

    def test_bootstrap_requires_approved_unchanged_baseline(self):
        self.write(edition=None)
        base = self.commit("Pre-edition baseline")
        with patch.object(editions, "BASELINE", base):
            self.write()
            self.assertEqual(self.check(base=base), [])
            for label, content in [("1.1", b"# Example\n"), ("1.0", b"# Changed\n")]:
                self.write(edition=label, content=content)
                self.assertTrue(self.check(base=base))
            self.write(edition=None, content=b"# Changed\n")
            intervening = self.commit("Intervening content change")
            self.write()
            self.assertTrue(self.check(base=intervening))

    def test_missing_bootstrap_revision_fails_closed(self):
        self.write(edition=None)
        base = self.commit("Pre-edition baseline")
        self.write()
        with (
            patch.object(editions, "BASELINE", "0" * 40),
            self.assertRaises(subprocess.CalledProcessError),
        ):
            self.check(base=base)

    def editorial_base(self):
        self.write(edition="1.1", content=b"# Editorial change\n")
        return self.commit("Editorial transition")

    def declaration(self, source):
        return f"Edition correction: `example` at `{source}`"

    def test_bounded_correction_and_required_evidence(self):
        base = self.editorial_base()
        self.write(edition="2.0", content=b"# Editorial change\n")
        self.assertTrue(self.check(base=base))
        env = {"TEMPLATE_EDITION_CORRECTIONS": self.declaration(base)}
        self.assertEqual(self.check(env, base), [])
        for label in ["1.2", "2.1", "3.0", "1.0"]:
            self.write(edition=label, content=b"# Editorial change\n")
            self.assertTrue(self.check(env, base))
        self.write(edition="2.0", content=b"# Editorial change\n")
        self.commit(self.declaration(base))
        self.assertEqual(self.check(base=base), [])

    def test_correction_rejects_nontransition_or_unreachable_source(self):
        base = self.editorial_base()
        self.write(edition="2.0", content=b"# Editorial change\n")
        for source in [self.initial, "a" * 40]:
            with self.subTest(source=source), self.assertRaises(ValueError):
                self.check({"TEMPLATE_EDITION_CORRECTIONS": self.declaration(source)}, base)

    def test_correction_follows_exact_rename_lineage(self):
        source = self.editorial_base()
        self.move()
        base = self.commit("Exact rename")
        self.write("renamed", "2.0", b"# Editorial change\n")
        declaration = self.declaration(source).replace("`example`", "`renamed`")
        self.assertEqual(self.check({"TEMPLATE_EDITION_CORRECTIONS": declaration}, base), [])

    def test_local_merge_base_and_missing_remote(self):
        self.editorial_base()
        self.assertEqual(self.check(), [])
        self.git("update-ref", "-d", "refs/remotes/origin/main")
        with self.assertRaises(subprocess.CalledProcessError):
            self.check()

    def test_ci_context_cannot_fall_back(self):
        with self.assertRaises(ValueError):
            self.check({"GITHUB_ACTIONS": "true"})
        env = self.event("workflow_dispatch", {})
        with self.assertRaises(ValueError):
            self.check(env)
        with self.assertRaises(ValueError):
            self.check(env, self.initial)

    def test_pr_head_context_and_wrong_head(self):
        head = self.editorial_base()
        payload = {"pull_request": {"base": {"sha": self.initial}, "head": {"sha": head}}}
        env = self.event("pull_request", payload)
        self.assertEqual(self.check(env), [])
        env["GITHUB_SHA"] = self.initial
        with self.assertRaises(ValueError):
            self.check(env)

    def merge_candidate(self):
        head = self.editorial_base()
        self.git("switch", "-q", "main")
        (self.root / "unrelated.txt").write_text("Base advances\n")
        base = self.commit("Base advances")
        self.git("merge", "-q", "--no-ff", "candidate", "-m", "Synthetic PR merge")
        return base, head

    def test_head_checkout_rejects_stale_ancestor_metadata(self):
        actual_base = self.editorial_base()
        self.git("update-ref", "refs/remotes/origin/main", actual_base)
        self.write(edition="1.1", content=b"# Missing next bump\n")
        head = self.commit("Candidate misses bump after base advanced")
        payload = {"pull_request": {"base": {"sha": self.initial}, "head": {"sha": head}}}
        with self.assertRaisesRegex(ValueError, "not constructed"):
            self.check(self.event("pull_request", payload))

    def test_pr_merge_context_verifies_actual_parents(self):
        base, head = self.merge_candidate()
        payload = {"pull_request": {"base": {"sha": base}, "head": {"sha": head}}}
        self.assertEqual(self.check(self.event("pull_request", payload)), [])
        payload["pull_request"]["base"]["sha"] = self.initial
        with self.assertRaisesRegex(ValueError, "parents disagree"):
            self.check(self.event("pull_request", payload))
        payload["pull_request"]["base"]["sha"] = base
        payload["pull_request"]["head"]["sha"] = self.initial
        with self.assertRaises(ValueError):
            self.check(self.event("pull_request", payload))

    def test_stale_head_checkout_is_rejected(self):
        base, head = self.merge_candidate()
        self.git("checkout", "-q", head)
        payload = {"pull_request": {"base": {"sha": base}, "head": {"sha": head}}}
        with self.assertRaisesRegex(ValueError, "not constructed"):
            self.check(self.event("pull_request", payload))

    def test_pr_correction_reads_body(self):
        base = self.editorial_base()
        self.git("update-ref", "refs/remotes/origin/main", base)
        self.write(edition="2.0", content=b"# Editorial change\n")
        head = self.commit("Correction")
        payload = {
            "pull_request": {
                "base": {"sha": base},
                "head": {"sha": head},
                "body": self.declaration(base),
            }
        }
        self.assertEqual(self.check(self.event("pull_request", payload)), [])
        payload["pull_request"]["body"] = ""
        self.assertTrue(self.check(self.event("pull_request", payload)))

    def test_push_checks_each_authoritative_state(self):
        self.editorial_base()
        self.write(edition="1.2", content=b"# Another editorial change\n")
        head = self.commit("Second editorial transition")
        self.assertEqual(
            self.check(self.event("push", {"before": self.initial, "after": head})), []
        )

    def test_push_rejects_bad_intermediate_state_even_when_net_transition_valid(self):
        self.write(content=b"# Missing bump\n")
        self.commit("Bad intermediate state")
        self.write(edition="1.1", content=b"# Final state\n")
        head = self.commit("Bump only final state")
        self.assertTrue(self.check(self.event("push", {"before": self.initial, "after": head})))

    def test_push_correction_uses_commit_evidence(self):
        base = self.editorial_base()
        self.write(edition="2.0", content=b"# Editorial change\n")
        head = self.commit(self.declaration(base))
        self.assertEqual(self.check(self.event("push", {"before": base, "after": head})), [])

    def test_push_invalid_before_after_or_merge_fails_closed(self):
        head = self.editorial_base()
        for payload in [
            {"before": "0" * 40, "after": head},
            {"before": head, "after": head},
            {"before": self.initial, "after": self.initial},
        ]:
            with (
                self.subTest(payload=payload),
                self.assertRaises((ValueError, subprocess.CalledProcessError)),
            ):
                self.check(self.event("push", payload))
        self.git("switch", "-q", "main")
        self.git("merge", "-q", "--no-ff", "candidate", "-m", "Disallowed merge")
        head = self.git("rev-parse", "HEAD")
        with self.assertRaises(ValueError):
            self.check(self.event("push", {"before": self.initial, "after": head}))

    def test_cli_and_shallow_history_fail_closed(self):
        env = {key: value for key, value in os.environ.items() if not key.startswith("GITHUB_")}
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "check_template_editions.py"), "--root", str(self.root)],
            env=env,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        (self.root / ".git/shallow").write_text(self.initial + "\n")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "check_template_editions.py"), "--root", str(self.root)],
            env=env,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn(b"full history", result.stderr)


if __name__ == "__main__":
    unittest.main()
