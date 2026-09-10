"""
Focused tests for stage-candidate.py's council-ballot gate.

The rule being pinned: a ballot carrying a `_council` block must show at least
MIN_COUNCIL_REFERENCES references answered, or staging REFUSES before the DB is
touched. canon-council.py tolerates a single live reference (it prints COUNCIL
DEGRADED and synthesizes anyway); a one-voice ballot is degraded output, not the
two-family disagreement the council exists to produce. This matters most on the
recovery lane, which by definition retries nights when the aggregator was flaky.

Ballots with no `_council` block (jazz-canon-orchestrator output) are not
council ballots and must pass through untouched.

Run (from /home/john/dev/active/mccoy-tyner):
  scripts/.venv/bin/python3 -m unittest scripts/tests/test_stage_candidate_ballot.py

Each test names the wrong implementation it would catch (see docstrings).
"""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "scripts" / "stage-candidate.py"
spec = importlib.util.spec_from_file_location("stage_candidate", SCRIPT)
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)


def council(answered, **extra):
    b = {"tier": "contested", "priority": "consider", "case_for": "x",
         "case_against": "y"}
    c = {"references": ["a", "b"], "aggregator": "z", "preset": "canon-council"}
    if answered is not None:
        c["references_answered"] = answered
    c.update(extra)
    b["_council"] = c
    return b


class CouncilReferenceGate(unittest.TestCase):
    def test_two_references_passes(self):
        """Catches an off-by-one that refuses the normal, healthy 2/2 ballot —
        which would take the whole nightly drip offline rather than one album."""
        self.assertIsNone(sc.council_reference_shortfall(council(2)))

    def test_more_than_two_references_passes(self):
        """Catches a gate written as `== 2`; a three-reference preset is a
        config change John can make without this refusing every ballot."""
        self.assertIsNone(sc.council_reference_shortfall(council(3)))

    def test_one_reference_is_refused(self):
        """Catches the shipped behavior: canon-council.py prints COUNCIL
        DEGRADED for a single live reference and synthesizes a ballot anyway,
        and nothing downstream stopped that ballot from being staged."""
        reason = sc.council_reference_shortfall(council(1))
        self.assertIsNotNone(reason)
        self.assertIn("1 reference", reason)

    def test_zero_references_is_refused(self):
        """Catches a truthiness test (`if answered:`) that would let 0 through
        the same way it lets None through."""
        self.assertIsNotNone(sc.council_reference_shortfall(council(0)))

    def test_council_block_without_the_count_is_refused(self):
        """Catches a gate that reads the count with `.get(..., 2)`. A council
        block that lost its count is unverifiable, and unverifiable fails
        closed — the drip's whole guardrail posture."""
        b = council(None)
        self.assertNotIn("references_answered", b["_council"])
        self.assertIsNotNone(sc.council_reference_shortfall(b))

    def test_non_integer_count_is_refused(self):
        """Catches `answered < 2` on a str, which raises TypeError in py3 and
        would crash staging instead of refusing it."""
        self.assertIsNotNone(sc.council_reference_shortfall(council("2")))

    def test_ballot_without_council_block_passes(self):
        """Catches a gate that demands `_council` on every ballot. The
        jazz-canon-orchestrator emits flat tier/priority ballots with no
        council metadata; refusing those breaks the other staging path."""
        self.assertIsNone(sc.council_reference_shortfall(
            {"tier": "consensus_core", "priority": "must_have"}))

    def test_no_ballot_at_all_passes(self):
        """Catches a gate that fires on the record's-own-fields path, where
        there is no ballot to judge."""
        self.assertIsNone(sc.council_reference_shortfall(None))


class RefusesBeforeTouchingTheDatabase(unittest.TestCase):
    """The gate's value is that it fails BEFORE the database is reached. These
    run the real script the way the drip does, but with JAZZCANON_APP_DB_URL
    pointed at a dead port — load_env() uses setdefault, so the environment
    wins. A gate in the right place never notices; a gate placed after
    psycopg2.connect() dies on the connection instead of refusing."""

    DEAD_DB = "postgresql://nobody@127.0.0.1:1/nowhere?connect_timeout=1"

    def stage(self, ballot):
        rec = {"id": "test-album-1965", "artist": "Test", "album": "Test",
               "year": 1965, "ballot": ballot}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(rec, f)
            path = f.name
        env = dict(os.environ, JAZZCANON_APP_DB_URL=self.DEAD_DB)
        return subprocess.run(
            [str(REPO / "scripts" / ".venv" / "bin" / "python3"), str(SCRIPT),
             "--ballot-inline", path, "--dry-run"],
            capture_output=True, text=True, cwd=REPO, env=env)

    def test_degraded_ballot_refuses_without_reaching_the_database(self):
        """Catches a gate placed after load_env()/psycopg2.connect(): with the
        database unreachable, that version raises OperationalError instead of
        refusing, so a degraded ballot's fate would depend on whether the DB
        happened to be up."""
        p = self.stage(council(1))
        self.assertEqual(p.returncode, 1)
        self.assertIn("REFUSED", p.stderr)
        self.assertIn("council ballot answered by 1 reference", p.stderr)
        self.assertNotIn("Traceback", p.stderr)
        self.assertNotIn("OperationalError", p.stderr)

    def test_healthy_ballot_gets_past_the_gate_to_the_database(self):
        """Catches a gate that refuses everything: a 2/2 ballot must reach the
        connection attempt — the dead port failing is the proof it got past."""
        p = self.stage(council(2))
        self.assertNotIn("council ballot answered by", p.stderr)
        self.assertIn("OperationalError", p.stderr)


if __name__ == "__main__":
    unittest.main()
