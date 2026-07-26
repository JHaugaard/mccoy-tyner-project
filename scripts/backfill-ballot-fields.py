#!/usr/bin/env python3
"""
Backfill council ballot prose from research dossiers into the album table.

One-time companion to migrate-4a-ballot-fields.sql. Handoff:
docs/handoffs/2026-07-26-ballot-fields-into-db.md

Reads every dossier under research/candidates-archive/ and
research/candidates-inbox/ that carries a top-level "ballot" key, and writes
three fields to the matching album row (match on album.id == dossier id):

  album.case_for            <- ballot.case_for
  album.case_against        <- ballot.case_against
  album.inclusion_rationale <- dossier's top-level `rationale`

The third is a REPOINT, not a fill (John's decision, 2026-07-26). Before
migrate-4a, stage-candidate.py wrote the ballot's case_for into
inclusion_rationale, so on ballot-staged rows that column held the council's
argument while on the original 100 it held the dossier's source-tagged
description. Now it means one thing everywhere: what the album IS. What the
council ARGUED lives in case_for. The displaced values are recoverable from
edit_log.old_value.

Contract (config/edit-contract.md):
  - Writes as _jazzcanon_app (SELECT/INSERT/UPDATE, no DELETE).
  - One edit_log row per album per CHANGED field. Fields already holding the
    target value are skipped and logged nowhere — re-running writes nothing.
  - Never touches canon_status, site_status, embedding or search_document.
    Embeddings are pipeline-owned; run embed.py --only-ids afterwards.
  - No epistemic pairing: these are prose projections of an existing archival
    source, not new factual claims.

Usage:
  .venv/bin/python3 scripts/backfill-ballot-fields.py --dry-run
  .venv/bin/python3 scripts/backfill-ballot-fields.py
  .venv/bin/python3 scripts/backfill-ballot-fields.py --print-ids   # for embed.py

Exit 1 if any dossier's id has no matching album row — a missing row means the
candidate was never staged, and inventing one here would bypass the staging
guards. Stage it first.
"""

import argparse
import json
import os
import sys
from pathlib import Path

import psycopg2

REPO_ROOT = Path(__file__).resolve().parent.parent
DOSSIER_DIRS = ["research/candidates-archive", "research/candidates-inbox"]
EDITOR = "claude-code"
REASON = "ballot backfill 2026-07-26 (Claude Code handoff)"

# field -> (dossier accessor, human label)
FIELDS = [
    ("case_for", lambda rec: (rec.get("ballot") or {}).get("case_for")),
    ("case_against", lambda rec: (rec.get("ballot") or {}).get("case_against")),
    ("inclusion_rationale", lambda rec: rec.get("rationale")),
]


def load_env(path=".env.local"):
    """Shallow .env.local loader, environment wins. Mirrors stage-candidate.py.
    Parsed in Python, not shell — passwords may contain '#'."""
    p = REPO_ROOT / path
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())


def null(v):
    """Empty/whitespace-only strings are NULL, not ''."""
    if v is None:
        return None
    v = str(v).strip()
    return v or None


def collect_dossiers():
    """Every dossier with a ballot block, keyed by album id. Later dirs win on
    a duplicate id; none exist today, but the collision is reported."""
    found = {}
    for d in DOSSIER_DIRS:
        for path in sorted((REPO_ROOT / d).glob("*.json")):
            try:
                rec = json.loads(path.read_text())
            except json.JSONDecodeError as e:
                print(f"  ✗ {path.name}: unparseable JSON ({e})", file=sys.stderr)
                sys.exit(1)
            if not isinstance(rec, dict) or not rec.get("ballot"):
                continue
            aid = rec.get("id")
            if not aid:
                print(f"  ✗ {path.name}: ballot present but no top-level 'id'", file=sys.stderr)
                sys.exit(1)
            if aid in found:
                print(f"  ! duplicate dossier id {aid!r} — {path.name} wins over "
                      f"{found[aid][0].name}", file=sys.stderr)
            found[aid] = (path, rec)
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true",
                    help="show what would change; roll back without writing")
    ap.add_argument("--print-ids", action="store_true",
                    help="print the matched album ids, space-separated, and exit "
                         "(feed to embed.py --only-ids)")
    args = ap.parse_args()

    dossiers = collect_dossiers()
    if not dossiers:
        print("No dossiers with a ballot block found — nothing to do.")
        return

    if args.print_ids:
        print(" ".join(sorted(dossiers)))
        return

    load_env()
    db_url = os.environ.get("JAZZCANON_APP_DB_URL")
    if not db_url:
        print("✗ JAZZCANON_APP_DB_URL not set (check .env.local)", file=sys.stderr)
        sys.exit(1)

    print(f"Ballot dossiers found: {len(dossiers)}")
    if args.dry_run:
        print("DRY RUN — will roll back")

    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("SET search_path TO _jazzcanon, public")

    # ── Guard: every dossier id must already be an album row ─────────────────
    cur.execute(
        "SELECT id, case_for, case_against, inclusion_rationale FROM album WHERE id = ANY(%s)",
        (list(dossiers),),
    )
    rows = {r[0]: {"case_for": r[1], "case_against": r[2], "inclusion_rationale": r[3]}
            for r in cur.fetchall()}
    missing = sorted(set(dossiers) - set(rows))
    if missing:
        print(f"\n✗ REFUSED — {len(missing)} dossier(s) have no album row:", file=sys.stderr)
        for aid in missing:
            print(f"    {aid}", file=sys.stderr)
        print("Stage them with stage-candidate.py first. Nothing written.", file=sys.stderr)
        conn.close()
        sys.exit(1)

    changed_albums, updates, skipped, blank = set(), 0, 0, []

    try:
        for aid in sorted(dossiers):
            path, rec = dossiers[aid]
            current = rows[aid]
            for field, accessor in FIELDS:
                new_value = null(accessor(rec))
                old_value = current[field]

                if new_value is None:
                    blank.append(f"{aid}.{field}")
                    continue
                if old_value == new_value:
                    skipped += 1
                    continue

                if args.dry_run:
                    old_repr = "NULL" if old_value is None else f"{old_value[:48]!r}…"
                    print(f"  {aid}\n    {field}: {old_repr}\n      -> {new_value[:48]!r}…")

                # UPDATE and edit_log are one statement pair inside the same
                # transaction — a row never changes without its audit entry.
                cur.execute(
                    f"UPDATE album SET {field} = %s, updated_at = now() WHERE id = %s",
                    (new_value, aid),
                )
                cur.execute("""
                    INSERT INTO edit_log
                        (editor, table_name, record_id, field, old_value, new_value, reason)
                    VALUES (%s, 'album', %s, %s, %s, %s, %s)
                """, (EDITOR, aid, field, old_value, new_value, REASON))
                updates += 1
                changed_albums.add(aid)

    except Exception as e:
        conn.rollback()
        print(f"\n✗ ERROR — rolled back, nothing written: {e}", file=sys.stderr)
        conn.close()
        sys.exit(1)

    if args.dry_run:
        conn.rollback()
        print("\nDRY RUN — rolled back, nothing written to DB")
    else:
        conn.commit()
        print("\nBACKFILL COMMITTED")

    print("\n── Summary ──")
    print(f"  dossiers read     : {len(dossiers)}")
    print(f"  albums changed    : {len(changed_albums)}")
    print(f"  field updates     : {updates}  (= edit_log rows written)")
    print(f"  already correct   : {skipped}")
    if blank:
        print(f"  blank in dossier  : {len(blank)}  (left untouched, not nulled)")
        for b in blank:
            print(f"      {b}")

    if changed_albums and not args.dry_run:
        print("\nNext — regenerate embeddings for the changed rows:")
        print("  cp scripts/embed.py /tmp/ && chmod 644 /tmp/embed.py")
        print("  sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/embed.py --only-ids \\")
        print("    " + " ".join(sorted(changed_albums)))

    cur.close()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
