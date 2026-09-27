import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest



SCRIPT = Path(__file__).parents[1] / "recently-added.py"
SPEC = importlib.util.spec_from_file_location("recently_added", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"could not import {SCRIPT}")
recently_added = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(recently_added)


class RecentlyAddedTests(unittest.TestCase):
    def fixture(self, content):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        path = Path(temporary.name) / "recently-added.json"
        path.write_text(content, encoding="utf-8")
        return path

    def test_cli_prepends_exact_batch_and_preserves_existing_entries(self):
        path = self.fixture(
            json.dumps(
                [
                    {"id": "older-a", "added": "2026-09-25"},
                    {"id": "older-b", "added": "2026-09-24"},
                ],
                indent=2,
            )
        )
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--file",
                str(path),
                "--ship-date",
                "2026-09-27",
                "--batch-id",
                "new-a",
                "--batch-id",
                "new-b",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual([entry["id"] for entry in result], ["new-a", "new-b", "older-a", "older-b"])
        self.assertEqual([entry["added"] for entry in result[:2]], ["2026-09-27", "2026-09-27"])

    def test_existing_batch_is_idempotent(self):
        document = [
            {"id": "new-a", "added": "2026-09-27"},
            {"id": "older", "added": "2026-09-25"},
        ]
        result, changed = recently_added.updated_document(document, ["new-a"], "2026-09-27")
        self.assertFalse(changed)
        self.assertEqual(result, document)

    def test_reapproved_album_moves_to_current_batch_date(self):
        document = [
            {"id": "newer", "added": "2026-09-26"},
            {"id": "returning", "added": "2026-09-24"},
        ]
        result, changed = recently_added.updated_document(
            document, ["returning"], "2026-09-27"
        )
        self.assertTrue(changed)
        self.assertEqual(result[0], {"id": "returning", "added": "2026-09-27"})
        self.assertEqual(result[1], document[0])

    def test_export_gate_requires_every_batch_id(self):
        albums = self.fixture(json.dumps([{"id": "present"}]))
        with self.assertRaisesRegex(RuntimeError, "rerun the ship"):
            recently_added.validate_exported_albums(albums, ["present", "missing"])

    def test_cli_writes_exact_batch_output(self):
        path = self.fixture("[]\n")
        batch_path = path.parent / "batch.txt"
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--file",
                str(path),
                "--ship-date",
                "2026-09-27",
                "--batch-id",
                "new-a",
                "--batch-id",
                "new-b",
                "--batch-output",
                str(batch_path),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(batch_path.read_text(encoding="utf-8"), "new-a\nnew-b\n")

    def test_cli_refuses_unexpected_shape_without_touching_file(self):
        malformed = '[\n  {"id": "album", "added": "2026-09-27", "title": "drift"}\n]\n'
        path = self.fixture(malformed)
        before = path.read_bytes()
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--file",
                str(path),
                "--ship-date",
                "2026-09-27",
                "--batch-id",
                "must-not-land",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("REFUSED", completed.stderr)
        self.assertEqual(path.read_bytes(), before)

    def test_non_recent_first_order_is_refused(self):
        path = self.fixture(
            json.dumps(
                [
                    {"id": "older", "added": "2026-09-24"},
                    {"id": "newer", "added": "2026-09-25"},
                ]
            )
        )
        with self.assertRaisesRegex(recently_added.SchemaError, "most-recent-first"):
            recently_added.load_document(path)

    def test_atomic_write_round_trips_format_and_preserves_mode(self):
        path = self.fixture("[]\n")
        path.chmod(0o664)
        document = [{"id": "album", "added": "2026-09-27"}]
        recently_added.atomic_write_json(path, document, expected_source=b"[]\n")
        self.assertEqual(recently_added.load_document(path), document)
        self.assertTrue(path.read_bytes().endswith(b"\n"))
        self.assertEqual(path.stat().st_mode & 0o777, 0o664)

    def test_atomic_write_refuses_if_gallery_file_changed_after_validation(self):
        path = self.fixture("[]\n")
        with self.assertRaisesRegex(RuntimeError, "changed after validation"):
            recently_added.atomic_write_json(
                path,
                [{"id": "album", "added": "2026-09-27"}],
                expected_source=b"[ ]\n",
            )
        self.assertEqual(path.read_bytes(), b"[]\n")

    def test_git_commit_only_preserves_unrelated_staged_and_dirty_work(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repo = Path(temporary.name)

        def git(*arguments):
            return subprocess.run(
                ["git", *arguments],
                cwd=repo,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

        git("init", "-q")
        git("config", "user.name", "Ship Test")
        git("config", "user.email", "ship-test@example.invalid")
        for name in ("intended", "unrelated-staged", "unrelated-dirty"):
            (repo / name).write_text("base\n", encoding="utf-8")
        git("add", ".")
        git("commit", "-q", "-m", "base")

        (repo / "intended").write_text("ship\n", encoding="utf-8")
        (repo / "unrelated-staged").write_text("held staged\n", encoding="utf-8")
        git("add", "unrelated-staged")
        (repo / "unrelated-dirty").write_text("held dirty\n", encoding="utf-8")

        git("commit", "--only", "-q", "-m", "ship", "--", "intended")
        self.assertEqual(git("show", "--pretty=", "--name-only", "HEAD"), "intended")
        self.assertEqual(git("diff", "--cached", "--name-only"), "unrelated-staged")
        self.assertEqual(git("diff", "--name-only"), "unrelated-dirty")


if __name__ == "__main__":
    unittest.main()
