#!/usr/bin/env python3
"""
check-candidate.py — deterministic pre-research gate for the canon drip.

Answers ONE question before any expensive work begins: is this album
eligible to be tonight's candidate? Exit 0 (PASS) or 1 (REFUSED — reason
printed). The nightly drip must run this for every prospective candidate
BEFORE researching, writing files, or convening the council (2026-07-17
incident: without this gate, the drip re-researched and re-judged albums
that stage-candidate.py was always going to refuse).

Checks, in order:
  1. Rubric year window (config/canon-rubric.md frontmatter).
  2. Database — any album row matching artist+title (any canon_status).
  3. Next-batch list — data/canon-draft.json entries with include=false.
  4. Existing artifacts — research/candidates-inbox/ and
     research/candidates-archive/ records matching artist+title.

Stdlib + psql only (read-only JAZZCANON_DB_URL) — no venv needed.

Usage:
  python3 scripts/check-candidate.py "Art Blakey & The Jazz Messengers" "Free for All" 1964
  python3 scripts/check-candidate.py "Booker Ervin" "The Freedom Book"     # year optional
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/john/dev/active/mccoy-tyner")
RUBRIC = REPO / "config" / "canon-rubric.md"


def rubric_frontmatter() -> dict:
    m = re.match(r"---\n(.*?)\n---", RUBRIC.read_text(), re.DOTALL)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            line = line.split("#", 1)[0].strip()
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def db_url() -> str:
    for line in (REPO / ".env.local").read_text().splitlines():
        if line.startswith("JAZZCANON_DB_URL="):
            return line.split("=", 1)[1].strip()
    sys.exit("JAZZCANON_DB_URL not found in .env.local")


def refuse(reason: str) -> None:
    print(f"REFUSED — {reason}")
    print("Pick a different album and run this check again before researching.")
    sys.exit(1)


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(f"usage: {sys.argv[0]} \"<Artist>\" \"<Title>\" [year]")
    artist, title = sys.argv[1].strip(), sys.argv[2].strip()
    year = None
    if len(sys.argv) > 3:
        try:
            year = int(sys.argv[3])
        except ValueError:
            sys.exit(f"year must be an integer, got {sys.argv[3]!r}")

    # 1. Year window
    fm = rubric_frontmatter()
    year_min, year_max = int(fm.get("year_min", 1940)), int(fm.get("year_max", 1972))
    if year is not None and not (year_min <= year <= year_max):
        refuse(f"year {year} outside rubric window {year_min}-{year_max}")

    # 2. Database (any status) — same key stage-candidate.py refuses on
    # NB: variables interpolate only for stdin scripts, never for -c
    out = subprocess.run(
        ["psql", db_url(), "-X", "-At", "-F", "\t", "-q",
         "-v", "ON_ERROR_STOP=1", "-v", f"a={artist}", "-v", f"t={title}"],
        input="SELECT id, canon_status, site_status FROM _jazzcanon.album "
              "WHERE lower(artist_name) = lower(:'a') AND lower(title) = lower(:'t');",
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    if out:
        aid, status, site = out.splitlines()[0].split("\t")
        refuse(f"already in the database: id={aid} canon_status={status} site_status={site}")

    # 3. Next-batch list
    draft = REPO / "data" / "canon-draft.json"
    if draft.exists():
        for a in json.loads(draft.read_text())["albums"]:
            if not a.get("include") and \
               str(a.get("artist", "")).lower() == artist.lower() and \
               str(a.get("album", "")).lower() == title.lower():
                refuse(f"on the identified next-batch list (id={a.get('id')}) — already under consideration")

    # 4. Existing candidate artifacts
    for d in ("candidates-inbox", "candidates-archive"):
        folder = REPO / "research" / d
        if not folder.exists():
            continue
        for f in sorted(folder.glob("*.json")):
            try:
                rec = json.loads(f.read_text())
            except (json.JSONDecodeError, OSError):
                continue
            if str(rec.get("artist", "")).lower() == artist.lower() and \
               str(rec.get("album") or rec.get("title") or "").lower() == title.lower():
                refuse(f"candidate artifact already exists: research/{d}/{f.name}")

    y = f" ({year})" if year else ""
    print(f"PASS — {artist} — {title}{y} is eligible: not in DB, next-batch, or prior artifacts"
          + (f"; inside window {year_min}-{year_max}" if year else
             f"; NOTE: no year given — confirm {year_min}-{year_max} window during research"))


if __name__ == "__main__":
    main()
