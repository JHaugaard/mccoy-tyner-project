"""
Focused tests for stage-candidate.py's plan_album_art().

The rule being pinned: album_art.is_primary was hardcoded true for every
cover_art entry, so a dossier documenting two fronts aborted on
uq_album_art_primary (partial unique index on album_id WHERE is_primary) and
alternates had to live in prose notes. Now a declared is_primary is honoured;
when none is declared the first role='front' entry is primary; and a set that
would not yield exactly one primary is refused by name rather than left to the
index.

Absence is not failure: a dossier with no cover_art yields no rows, no error.

Run (from /home/john/dev/active/mccoy-tyner):
  scripts/.venv/bin/python3 -m unittest scripts/tests/test_stage_candidate_album_art.py

Each test names the wrong implementation it would catch (see docstrings).
"""

import importlib.util
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "scripts" / "stage-candidate.py"
spec = importlib.util.spec_from_file_location("stage_candidate", SCRIPT)
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)


def art(url, **kw):
    return dict(url=url, **kw)


def primaries(rows):
    return [r for r in rows if r["is_primary"]]


class DefaultsWhenNothingIsDeclared(unittest.TestCase):
    def test_single_front_becomes_primary(self):
        """Catches a default that marks nothing primary, which would leave the
        album with no cover for the site to render."""
        rows, err = sc.plan_album_art([art("https://a", role="front")])
        self.assertIsNone(err)
        self.assertEqual(len(primaries(rows)), 1)

    def test_two_fronts_yield_exactly_one_primary(self):
        """Catches the shipped implementation, which hardcoded is_primary=true
        and aborted the transaction on uq_album_art_primary — the whole reason
        a 78-era original plus a reissue front had to go in notes instead."""
        rows, err = sc.plan_album_art([
            art("https://original", role="front", source="discogs"),
            art("https://reissue", role="front", source="itunes"),
        ])
        self.assertIsNone(err)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(primaries(rows)), 1)
        self.assertEqual(primaries(rows)[0]["url"], "https://original")

    def test_first_front_wins_even_when_a_back_comes_first(self):
        """Catches a default that marks the first entry of ANY role primary.
        The rule is the first role='front', and a back cover is not a cover."""
        rows, err = sc.plan_album_art([
            art("https://back", role="back"),
            art("https://front", role="front"),
        ])
        self.assertIsNone(err)
        self.assertEqual(primaries(rows)[0]["url"], "https://front")

    def test_missing_role_is_treated_as_front(self):
        """Catches dropping the column default. Existing dossiers omit `role`
        entirely and their single cover must still come out primary."""
        rows, err = sc.plan_album_art([art("https://a")])
        self.assertIsNone(err)
        self.assertEqual(rows[0]["role"], "front")
        self.assertEqual(len(primaries(rows)), 1)

    def test_no_front_at_all_is_refused(self):
        """Catches an implementation that silently stages art with no primary —
        which the site would render as an album with no cover, quietly."""
        rows, err = sc.plan_album_art([art("https://back", role="back")])
        self.assertIsNotNone(err)
        self.assertIn("no entry is primary", err)


class DeclaredValuesAreHonoured(unittest.TestCase):
    def test_declared_primary_overrides_position(self):
        """Catches an implementation that ignores the dossier and always picks
        the first front — the researcher's explicit ruling must win."""
        rows, err = sc.plan_album_art([
            art("https://first", role="front", is_primary=False),
            art("https://second", role="front", is_primary=True),
        ])
        self.assertIsNone(err)
        self.assertEqual(primaries(rows)[0]["url"], "https://second")

    def test_undeclared_entries_are_false_when_another_declares(self):
        """Catches a mixed-case implementation that also applies the first-front
        default, producing two primaries and reintroducing the constraint abort."""
        rows, err = sc.plan_album_art([
            art("https://front-a", role="front"),
            art("https://front-b", role="front", is_primary=True),
        ])
        self.assertIsNone(err)
        self.assertEqual(len(primaries(rows)), 1)
        self.assertEqual(primaries(rows)[0]["url"], "https://front-b")

    def test_two_declared_primaries_are_refused_by_name(self):
        """Catches an implementation that trusts the dossier blindly. Two
        declared primaries must fail with an explanation, not with
        `uq_album_art_primary` from the database."""
        rows, err = sc.plan_album_art([
            art("https://a", role="front", is_primary=True),
            art("https://b", role="alternate", is_primary=True),
        ])
        self.assertIsNotNone(err)
        self.assertIn("2 entries are primary", err)
        self.assertIn("front", err)
        self.assertIn("alternate", err)

    def test_all_declared_false_is_refused(self):
        """Catches a fallback that quietly re-promotes the first front when the
        dossier deliberately said false everywhere — an explicit statement that
        leaves no primary is an error to surface, not one to paper over."""
        rows, err = sc.plan_album_art([
            art("https://a", role="front", is_primary=False),
            art("https://b", role="front", is_primary=False),
        ])
        self.assertIsNotNone(err)
        self.assertIn("no entry is primary", err)


class AbsenceIsNotFailure(unittest.TestCase):
    def test_no_cover_art_key_yields_nothing(self):
        """Catches a guard that fires on every record. Most dossiers carry no
        cover_art; refusing them would break routine staging."""
        self.assertEqual(sc.plan_album_art(None), ([], None))

    def test_empty_list_yields_nothing(self):
        """Same guard, the empty-list shape."""
        self.assertEqual(sc.plan_album_art([]), ([], None))

    def test_entries_without_a_url_are_dropped_not_refused(self):
        """Catches an implementation that counts url-less stubs toward the
        primary tally; the pre-existing behaviour skipped them and must stay."""
        rows, err = sc.plan_album_art([
            art(None, role="front"),
            art("https://real", role="front"),
        ])
        self.assertIsNone(err)
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(primaries(rows)), 1)

    def test_url_less_entries_alone_yield_nothing(self):
        """Catches a guard that refuses a list whose entries all lack urls —
        that is the same as having no art, not a broken primary set."""
        self.assertEqual(sc.plan_album_art([art(None), art(None)]), ([], None))


class VocabularyIsClamped(unittest.TestCase):
    def test_unknown_source_falls_back_to_other(self):
        """Pre-existing behaviour that must survive the rewrite: an unknown
        source string is clamped, never passed through to the enum cast."""
        rows, _ = sc.plan_album_art([art("https://a", source="bandcamp")])
        self.assertEqual(rows[0]["source"], "other")

    def test_known_source_is_preserved(self):
        """Catches a clamp that rewrites everything to 'other'."""
        rows, _ = sc.plan_album_art([art("https://a", source="discogs")])
        self.assertEqual(rows[0]["source"], "discogs")

    def test_unknown_role_falls_back_to_other(self):
        """Catches passing an arbitrary role string to the art_role cast, which
        would abort the transaction with an enum error."""
        rows, err = sc.plan_album_art([
            art("https://a", role="obi-strip"),
            art("https://b", role="front"),
        ])
        self.assertIsNone(err)
        self.assertEqual(rows[0]["role"], "other")


if __name__ == "__main__":
    unittest.main()
