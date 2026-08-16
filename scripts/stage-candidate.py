#!/usr/bin/env python3
"""
stage-candidate.py — ingest.py for one record, as the app role, at candidate status.

Takes ONE specialist candidate record (the shape defined in
research/candidate-schema.md, with a nested `personnel_record` per
docs/personnel-contract.md) and inserts it into `_jazzcanon` as a
CANDIDATE — never `included`. This is McCoy's staging path for a single
album surfaced by a specialist or the nightly drip; John's own
`candidate → included` / `candidate → excluded` verdicts happen later,
by hand, per config/edit-contract.md.

Reuses ingest.py's mapping logic and house style: same vocabulary
dicts (CANONICAL_INSTRUMENTS, INSTRUMENT_NORMALIZE, STYLES,
PRIORITY_MAP), same get_or_create_person/find_leader helpers. Reuses
citation-backfill.py's source dedup keys (normalize_url/
normalize_title/source_key) for the source registry.

Recording places are NOT shared with ingest.py: parse_studio and
get_or_create_studio were retired 2026-08-16 in favour of a per-session
resolver over the canonical place set. See the "Recording places" block
below and docs/personnel-contract.md §Recording sites.

Differences from ingest.py (see team-lead brief for the full contract):
  - One record in, not a whole canon-draft.json.
  - Writes as `_jazzcanon_app` (SELECT/INSERT/UPDATE, no DELETE) via
    JAZZCANON_APP_DB_URL, not the superuser bulk-load path.
  - album.canon_status is hard-coded 'candidate', site_status 'found'.
  - canon_tier/priority come from a ballot (jazz-canon-orchestrator's
    tier/priority) when one is available, else from the record's own
    fields, and the ballot's case_for/case_against prose is written to
    the album columns of the same names. inclusion_rationale always
    comes from the record's own top-level `rationale` on BOTH paths —
    what the album IS, as opposed to what the council ARGUED (migrate-4a,
    John's decision 2026-07-26). Before 4a the ballot path wrote case_for
    into inclusion_rationale, which made the column mean two different
    things depending on which era a row came from. A ballot can arrive
    two ways: a top-level "ballot": {tier,priority,case_for,case_against}
    key embedded directly in the record, or a separate --ballot file
    (looked up by album id — see load_ballot_entry). The inline key
    always wins when both are present. --ballot-inline is a pure
    assertion flag: it requires the inline "ballot" key to exist and
    errors out before touching the DB if it doesn't; it changes no
    behavior beyond that check (inline already wins on its own).
  - Recording sites resolve per session against the canonical place set
    (`studio.name_slug`), never by blind insert of a free-text string.
    A place is created complete — name, city, kind, lat, lon,
    location_epistemic, location_source — or not created at all, because
    an incomplete row passes every DB constraint and then aborts
    export.sh's places.json validator for the entire canon. Unknown
    slug, tombstoned slug, incomplete site_new, invented precision, or
    more than NEW_PLACE_CAP new places in one run are all REFUSALS.
  - Dedup guard (id OR (artist,title) match) and the rubric's
    year_min/year_max window are hard refusals — exit 1, nothing
    written — rather than an ON CONFLICT upsert.
  - Unknown instrument strings are a validation error (list the valid
    taxonomy), not a silent skip — ingest.py's bulk load can afford to
    warn and move on; staging one record by hand cannot.
  - Citations are album-level only (v1, matches citation-backfill.py):
    a `source_map` key (token -> {title,type,url,notes}) or `sources`
    entries that are already {title,type,url} objects become `source`
    + `citation` rows. Bare S-token strings with no map are warned and
    skipped — never fabricated.
  - embedding/search_document are left NULL; the embed pipeline fills
    them later.

Usage:
  .venv/bin/python3 scripts/stage-candidate.py <candidate.json> [--dry-run] [--ballot <ballot.json>] [--ballot-inline]

The nightly drip calls this as:
  python3 scripts/stage-candidate.py --ballot-inline research/candidates-inbox/<id>.json

--dry-run runs the full transaction (so FK ids resolve exactly as a
real run would) and rolls back at the end instead of committing —
same convention as ingest.py/citation-backfill.py's dry-run mode.

Idempotent-ish: re-running against the same file after a successful
insert hits the dedup guard (id match) and exits 1. That's the desired
behavior — staging is a one-shot action per candidate, not an upsert.
"""

import argparse
import json
import os
import re
import sys
import uuid
from pathlib import Path

import psycopg2

REPO_ROOT = Path(__file__).resolve().parent.parent
RUBRIC_PATH = REPO_ROOT / "config" / "canon-rubric.md"

# ── Vocabulary (mirrors scripts/ingest.py verbatim — keep in sync) ───────────

CANONICAL_INSTRUMENTS = {
    "trumpet":            "brass",
    "cornet":             "brass",
    "flugelhorn":         "brass",
    "trombone":           "brass",
    "valve trombone":     "brass",
    "bass trombone":      "brass",
    "French horn":        "brass",
    "tuba":               "brass",
    "euphonium":          "brass",
    "tenor saxophone":    "woodwinds",
    "alto saxophone":     "woodwinds",
    "soprano saxophone":  "woodwinds",
    "baritone saxophone": "woodwinds",
    "clarinet":           "woodwinds",
    "bass clarinet":      "woodwinds",
    "flute":              "woodwinds",
    "piccolo":            "woodwinds",
    "bassoon":            "woodwinds",
    "oboe":               "woodwinds",
    "piano":              "keyboards",
    "electric piano":     "keyboards",
    "organ (hammond)":    "keyboards",
    "guitar":             "strings",
    "electric guitar":    "strings",
    "double bass":        "strings",
    "electric bass":      "strings",
    "violin":             "strings",
    "viola":              "strings",
    "cello":              "strings",
    "harp":               "strings",
    "drums":              "percussion",
    "vibraphone":         "percussion",
    "congas":             "percussion",
    "percussion":         "percussion",
    "marimba":            "percussion",
    "voice":              "other",
    "conductor":          "other",
    "arranger":           "other",
}

NON_INSTRUMENTS = {"liner notes", "liner-notes", "notes"}

INSTRUMENT_NORMALIZE = {
    "bass":               "double bass",
    "upright bass":       "double bass",
    "contrabass":         "double bass",
    "string bass":        "double bass",
    "acoustic bass":      "double bass",
    "bass guitar":        "electric bass",
    "electric bass guitar": "electric bass",
    "organ":              "organ (hammond)",
    "hammond organ":      "organ (hammond)",
    "hammond b3":         "organ (hammond)",
    "b3":                 "organ (hammond)",
    "fender rhodes":      "electric piano",
    "rhodes":             "electric piano",
    "tenor sax":          "tenor saxophone",
    "alto sax":           "alto saxophone",
    "soprano sax":        "soprano saxophone",
    "baritone sax":       "baritone saxophone",
    "bari sax":           "baritone saxophone",
    "vocals":             "voice",
    "vocal":              "voice",
    "horn":               "French horn",
    "french horn":        "French horn",
}

STYLES = {
    "hard-bop":   ("Hard Bop",   "Hard-driving post-bebop with blues and gospel roots"),
    "soul-jazz":  ("Soul Jazz",  "Blues and gospel inflected hard bop variant"),
    "cool-jazz":  ("Cool Jazz",  "Relaxed, lyrical post-bebop from the late 1940s–50s"),
    "modal-jazz": ("Modal Jazz", "Improvisation over modal scales rather than chord changes"),
    "post-bop":   ("Post-Bop",   "Eclectic post-1960 jazz drawing from multiple traditions"),
    # Opened genre gates, 2026-07-28 (docs/handoffs/2026-07-28-style-vocabulary-
    # opened-gates.md). Emitted by the fusion / free-jazz / ECM specialist agents.
    "fusion":             ("Fusion",             "Jazz improvisation fused with rock and funk rhythm and electric instruments"),
    "jazz-rock":          ("Jazz-Rock",          "Rock-weighted fusion variant driven by backbeat and amplified guitar"),
    "jazz-funk":          ("Jazz-Funk",          "Groove-first fusion built on funk vamps and electric bass"),
    "free-jazz":          ("Free Jazz",          "Collective improvisation released from fixed changes, meter, or key"),
    "avant-garde-jazz":   ("Avant-Garde Jazz",   "Composition-minded experimentalism in the AACM lineage"),
    "free-improvisation": ("Free Improvisation", "Non-idiomatic improvisation of the European wing, without jazz form"),
    "european-jazz":      ("European Jazz",      "Postwar European jazz with folk and chamber-music centre of gravity"),
    "spiritual-jazz":     ("Spiritual Jazz",     "Modal and free playing in a devotional, often non-Western frame"),
    "loft-jazz":          ("Loft Jazz",          "New York loft-era scene of the 1970s, free playing outside the club circuit"),
    "aacm":               ("AACM",               "Association for the Advancement of Creative Musicians and its lineage"),
    "ecm":                ("ECM",                "ECM Records label tag — never a primary style"),
}

# Label tags that describe an imprint, not a musical style: valid in `style_tags`,
# refused as `style_primary` (John, 2026-07-29 — keeps the tag from taking
# outsized emphasis; ECM records earn their place on musical continuity).
LABEL_ONLY_STYLES = {"ecm"}

PRIORITY_MAP = {
    "must_have": "must_have",
    "strong":    "strong",
    "consider":  "consider",
    "standard":  "strong",   # 'standard' not in ENUM; map to closest
}

CANON_TIERS = {"consensus_core", "contested", "scope_call", "exclude_suggested"}
EPISTEMIC_VALUES = {"obs", "inf", "unk"}
SOURCE_TYPE_ENUM = {"book", "web", "liner-notes", "discography", "other"}


# ── Helpers shared with ingest.py ────────────────────────────────────────────

def slugify(s):
    if not s:
        return ""
    s = s.lower().strip()
    s = re.sub(r"['\"\.,!?&/]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]

def null(v):
    """Return None for absent/FILL-REQUIRED values, else v."""
    return None if v in (None, "", "FILL-REQUIRED", "null", "NULL") else v

def ep(v, default="obs"):
    """Coerce epistemic value to ENUM string or default."""
    return v if v in EPISTEMIC_VALUES else default

def safe_date(v):
    """Return ISO date string (YYYY-MM-DD) or None if unparseable."""
    if not v:
        return None
    s = str(v).strip()[:10]
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return s
    return None

def normalize_instruments(raw):
    """Return list of canonical instrument names, splitting on '/' and ','.
    Skips non-instruments silently. Returns [] if nothing maps — the caller
    treats an empty result on a real instrument string as a validation error,
    unlike ingest.py's bulk-load warn-and-skip."""
    if not raw:
        return []
    parts = re.split(r"[/,]", raw)
    results = []
    for part in parts:
        n = part.strip()
        if not n:
            continue
        if n.lower() in NON_INSTRUMENTS:
            continue
        canonical = INSTRUMENT_NORMALIZE.get(n.lower(), n.lower())
        if canonical not in CANONICAL_INSTRUMENTS:
            canonical = INSTRUMENT_NORMALIZE.get(n, n)
        if canonical in CANONICAL_INSTRUMENTS:
            if canonical not in results:
                results.append(canonical)
    return results

# ── Recording places ────────────────────────────────────────────────────────
#
# Replaces parse_studio/get_or_create_studio (retired 2026-08-16). Those split
# a free-text string on its first comma and blind-inserted the halves as
# name/city with kind, address, lat, lon, location_epistemic and
# location_source all NULL. Two failure modes followed:
#
#   1. A compound string ("X, city (tracks 1-2); Y, city (tracks 3-5)") became
#      one row with garbage in `city`. Nine such rows are tombstoned in the DB.
#   2. The row it wrote could not satisfy export.sh's places.json validator,
#      which requires kind/city/lat/lon on every exported place and aborts the
#      WHOLE export on a miss. The bad row stayed invisible while the album sat
#      at candidate/found and broke the next ship.sh the moment John promoted it.
#
# Hence the completeness invariant: a place is created complete or not created.

STUDIO_KINDS = ("studio", "club", "hall", "festival", "home", "other")

# At most this many brand-new canonical places per run. A night wanting more
# has almost certainly misparsed a compound string rather than discovered three
# genuinely unknown venues.
NEW_PLACE_CAP = 2

# Tombstoned rows (name_slug rewritten to 'merged-<id>') encode identity
# decisions John ruled on in the 2026-08-14 studios cleanup. A slug landing on
# one is not an error to re-mint as a duplicate:
#   * MERGED — one surviving target, the ruling already answers it ⇒ redirect.
#   * SPLIT  — the raw described two venues; picking either silently drops one
#              ⇒ refuse and flag.
#
# Provenance: _jazzcanon.edit_log field='place_merged_away', 2026-08-14.
# Deliberately a reviewed constant, NOT a runtime query — that column is
# free-text convention, and a resolver mining prose at runtime is a liability.
# Regenerate by hand if the canonical place set is ever re-ruled.
TOMBSTONE_REDIRECT = {
    "merged-120": "contemporary-records-studio",         # Contemporary Records
    "merged-160": "a-r-recording-112-west-48th-street",   # A & R Recording
    "merged-179": "cbs-30th-street-studio",               # CBS 30th Street Studio
    "merged-196": "cbs-30th-street-studio",               # Columbia Recording Studio B
    "merged-198": "studio-bauer-ludwigsburg",             # Tonstudio Bauer
}
TOMBSTONE_SPLIT = {
    "merged-123": "Capitol Melrose + Forum Theatre",
    "merged-128": "WOR Studios + Van Gelder Hackensack",
    "merged-151": "RCA Hollywood + RCA New York",
    "merged-207": "Columbia Square + CBS 30th Street",
}


class SiteRefusal(Exception):
    """A recording-site problem that must stop staging outright.

    Distinct from the generic exception path so the operator (and the drip)
    sees REFUSED with a reason they can act on, rather than a stack trace.
    """


# ── Helpers shared with citation-backfill.py (source dedup) ─────────────────

PLACEHOLDER_URLS = {"https://example.com", "https://example.com/"}

def normalize_url(url):
    if not url or url.strip() in ("—", "-", ""):
        return None
    u = url.strip().lower().rstrip("/")
    if u in PLACEHOLDER_URLS:
        return None
    return u

def normalize_title(title):
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()

def source_key(title, url):
    u = normalize_url(url)
    return ("url", u) if u else ("title", normalize_title(title))

def resolve_source_type(raw_type):
    """Accept either an exact source_type ENUM string or a loose
    markdown 'Type' column value (Book/Website/API/Project doc/...)."""
    t = (raw_type or "").strip().lower()
    if t in SOURCE_TYPE_ENUM:
        return t
    if "book" in t:
        return "book"
    if "liner" in t:
        return "liner-notes"
    if "discog" in t:
        return "discography"
    return "web"


# ── Env / config ──────────────────────────────────────────────────────────────

def load_env(path=".env.local"):
    """Mirror citation-backfill.py: shallow .env.local loader, environment wins."""
    p = REPO_ROOT / path
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

def load_rubric_window():
    """Parse year_min/year_max from canon-rubric.md's YAML frontmatter."""
    text = RUBRIC_PATH.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None
    fm = m.group(1)
    ymin = re.search(r"^year_min:\s*(\d+)", fm, re.M)
    ymax = re.search(r"^year_max:\s*(\d+)", fm, re.M)
    return (int(ymin.group(1)) if ymin else None,
            int(ymax.group(1)) if ymax else None)


# ── Ballot resolution ─────────────────────────────────────────────────────────

def load_ballot_entry(ballot_path, album_id):
    """A ballot (jazz-canon-orchestrator output) may be a flat {tier,
    priority, case_for} object, a dict keyed by album id, {"albums":
    {...}} / {"albums": [...]}, or a bare list of entries with "id".
    Return the entry for this album, or None if not found."""
    data = json.loads(Path(ballot_path).read_text())

    if isinstance(data, dict):
        if album_id in data and isinstance(data[album_id], dict):
            return data[album_id]
        albums = data.get("albums")
        if isinstance(albums, dict):
            return albums.get(album_id)
        if isinstance(albums, list):
            return next((e for e in albums if e.get("id") == album_id), None)
        if {"tier", "priority", "case_for"} & set(data.keys()):
            return data
        return None

    if isinstance(data, list):
        return next((e for e in data if e.get("id") == album_id), None)

    return None


# ── Citation source resolution (album-level, v1 — matches citation-backfill.py) ──

def resolve_citation_sources(record, warnings):
    """Return [(title, source_type, url, notes, locator), ...] for
    album-level citations. Two supported shapes:
      1. record['source_map']: {token: {title,type,url,notes}} keyed by
         the tokens in record['sources'].
      2. record['sources']: [{title,type,url,notes}, ...] — objects
         embedded directly, no token layer.
      3. record['sources'] as a DICT: {token: {title,type,url,notes}} —
         the map and the token list in one object. Drip dossiers arrive
         this way, and before 2026-08-16 this shape fell through to the
         bare-token warning below and silently dropped complete
         provenance: iterating a dict yields its KEYS, so the
         all-dicts test in shape 2 sees strings and fails. Both inbox
         candidates (Lateef, Russell) staged with zero citations for
         exactly this reason.
    Bare string tokens with no source_map are warned and skipped —
    never fabricated, per the brief."""
    raw_sources = record.get("sources") or []
    source_map = record.get("source_map")

    if not source_map and isinstance(raw_sources, dict):
        source_map = raw_sources
        raw_sources = list(raw_sources.keys())

    if source_map:
        out = []
        for token in raw_sources:
            entry = source_map.get(token)
            if not entry:
                warnings.append(f"source token {token!r} not found in source_map — citation skipped")
                continue
            out.append((
                # Some dossiers name the source `label` rather than `title`
                # ("AllMusic", "JazzDisco"). Both are in use across the corpus
                # — 253 title, 22 label, none with neither — and falling back
                # to the bare token would write a source row called "S1",
                # which is provenance in name only.
                entry.get("title") or entry.get("label") or token,
                resolve_source_type(entry.get("type")),
                null(entry.get("url")),
                entry.get("notes"),
                token,
            ))
        return out

    if raw_sources and all(isinstance(s, dict) for s in raw_sources):
        out = []
        for i, entry in enumerate(raw_sources, start=1):
            title = entry.get("title") or entry.get("label") or f"untitled source {i}"
            out.append((
                title,
                resolve_source_type(entry.get("type")),
                null(entry.get("url")),
                entry.get("notes"),
                title,
            ))
        return out

    if raw_sources:
        warnings.append(
            f"sources are bare tokens with no source_map ({raw_sources!r}) — "
            "citations skipped, nothing fabricated"
        )
    return []


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("record_file", help="Path to a single candidate-album JSON file")
    parser.add_argument("--dry-run", action="store_true", help="Run the full transaction and roll back (default: commit)")
    parser.add_argument("--ballot", help="Optional decision-ballot JSON (jazz-canon-orchestrator output), looked up by album id")
    parser.add_argument("--ballot-inline", action="store_true",
                         help="Assert the record has a top-level 'ballot' key (tier/priority/case_for); "
                              "error out before touching the DB if it's missing. The inline key wins over "
                              "--ballot whether or not this flag is given — this only adds the assertion.")
    args = parser.parse_args()

    record = json.loads(Path(args.record_file).read_text())
    aid    = record["id"]
    pr     = record.get("personnel_record") or {}
    personnel = pr.get("personnel") or []

    warnings = []

    inline_ballot = record.get("ballot")
    if args.ballot_inline and not inline_ballot:
        print(f"✗ --ballot-inline given but {args.record_file} has no top-level 'ballot' key", file=sys.stderr)
        sys.exit(1)

    ballot_entry = None
    if inline_ballot:
        ballot_entry = inline_ballot
        if args.ballot:
            warnings.append("both inline 'ballot' key and --ballot file given — inline wins")
    elif args.ballot:
        ballot_entry = load_ballot_entry(args.ballot, aid)
        if ballot_entry is None:
            warnings.append(f"--ballot given but no entry found for {aid!r} — falling back to record's own fields")

    load_env()
    db_url = os.environ.get("JAZZCANON_APP_DB_URL")
    if not db_url:
        print("✗ JAZZCANON_APP_DB_URL not set (check .env.local)", file=sys.stderr)
        sys.exit(1)

    dry_run = args.dry_run
    print(f"Staging candidate: {aid}")
    if dry_run:
        print("DRY RUN — will roll back")

    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("SET search_path TO _jazzcanon, public")

    # ── Guard 1: dedup — id OR (artist, title) match ─────────────────────────
    cur.execute("""
        SELECT id, canon_status, site_status FROM album
        WHERE id = %s OR (lower(artist_name) = lower(%s) AND lower(title) = lower(%s))
    """, (aid, record.get("artist", ""), record.get("album", "")))
    existing = cur.fetchone()
    if existing:
        ex_id, ex_status, ex_site = existing
        print(f"REFUSED — already in album: id={ex_id!r} canon_status={ex_status} site_status={ex_site}")
        print("No rows written.")
        conn.close()
        sys.exit(1)

    # ── Guard 2: rubric year window ──────────────────────────────────────────
    year_min, year_max = load_rubric_window()
    year = record.get("year")
    if year_min is not None and year_max is not None and not (year_min <= year <= year_max):
        print(f"REFUSED — year {year} outside rubric window {year_min}-{year_max} "
              f"({RUBRIC_PATH.relative_to(REPO_ROOT)})")
        print("No rows written.")
        conn.close()
        sys.exit(1)

    # ── Guard 3: style vocabulary ────────────────────────────────────────────
    # A label tag (ecm) must never headline a record — the fix is always "pick
    # the real musical style, keep the tag in style_tags". Unknown codes are
    # warned rather than refused: style_id() would otherwise drop them to NULL
    # in silence, which is how the opened gates would have lost data.
    style_primary = (record.get("style_primary") or "").strip()
    if style_primary in LABEL_ONLY_STYLES:
        print(f"REFUSED — style_primary={style_primary!r} is a label tag, not a musical style.")
        print(f"  Fix: set style_primary to the record's real musical style and keep "
              f"{style_primary!r} in style_tags.")
        print("No rows written.")
        conn.close()
        sys.exit(1)
    if style_primary and style_primary not in STYLES:
        warnings.append(f"unknown style_primary {style_primary!r} — style_primary_id will be "
                        f"NULL. Known codes: {', '.join(sorted(STYLES))}")

    try:
        # ── Guard 4: instrument taxonomy — hard fail, list valid names ───────
        cur.execute("SELECT name FROM instrument")
        valid_instruments = {row[0] for row in cur.fetchall()}
        unknown = []
        for p in personnel:
            raw_inst = p.get("instrument", "")
            if not raw_inst or raw_inst.strip().lower() in NON_INSTRUMENTS:
                continue
            canonicals = normalize_instruments(raw_inst)
            if not canonicals or any(c not in valid_instruments for c in canonicals):
                unknown.append((p.get("name", "?"), raw_inst))
        if unknown:
            print("VALIDATION ERROR — unmapped instrument(s):")
            for name, raw in unknown:
                print(f"  {name}: {raw!r}")
            print("\nValid instrument names:")
            for name in sorted(valid_instruments):
                print(f"  {name}")
            raise ValueError("unmapped instrument(s) — see above")

        # ── Vocabulary: style, label, studio (create-if-missing, ingest.py style) ──
        for code, (name, desc) in STYLES.items():
            cur.execute("""
                INSERT INTO style (code, display_name, description) VALUES (%s,%s,%s)
                ON CONFLICT (code) DO NOTHING
            """, (code, name, desc))

        def style_id(code):
            if not code:
                return None
            cur.execute("SELECT id FROM style WHERE code = %s", (code,))
            row = cur.fetchone()
            return row[0] if row else None

        def get_or_create_label(name):
            name = null(name)
            if not name:
                return None
            cur.execute("""
                INSERT INTO label (name, name_slug) VALUES (%s,%s)
                ON CONFLICT (name) DO NOTHING
            """, (name, slugify(name)))
            cur.execute("SELECT id FROM label WHERE name = %s", (name,))
            row = cur.fetchone()
            return row[0] if row else None

        # ── Recording-place resolver (replaces get_or_create_studio) ──────────
        new_places = []      # slugs minted this run — feeds the cap and summary
        site_assignments = []  # (session date, slug|None) — printed in the summary
        site_cache = {}      # entry index -> studio_id, so a broadcast entry
                             # resolves (and counts) exactly once

        COMPLETENESS = ("name", "city", "kind", "lat", "lon",
                        "location_epistemic", "location_source")

        def _num(v):
            """JSON numbers only. bool is an int subclass — exclude it explicitly."""
            return isinstance(v, (int, float)) and not isinstance(v, bool)

        def resolve_existing(slug, idx):
            """Match a slug against the canonical place set. Never creates."""
            if slug in TOMBSTONE_SPLIT:
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_slug {slug!r} is a SPLIT tombstone "
                    f"({TOMBSTONE_SPLIT[slug]}). That raw string described two venues, "
                    f"so no single slug is the right answer — split the entry in two "
                    f"and name each place explicitly.")
            if slug in TOMBSTONE_REDIRECT:
                target = TOMBSTONE_REDIRECT[slug]
                warnings.append(
                    f"recording_sites[{idx}]: {slug!r} was merged away on 2026-08-14 "
                    f"— redirected to {target!r} per John's ruling")
                slug = target

            cur.execute("""
                SELECT id, name_slug, city, kind, lat, lon, location_epistemic
                FROM studio WHERE name_slug = %s
            """, (slug,))
            row = cur.fetchone()
            if not row:
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_slug {slug!r} is not in the canonical "
                    f"place set. Slugs are chosen from the list injected at dispatch, "
                    f"never invented — if this place is genuinely new, supply a complete "
                    f"site_new instead.")
            if row[1].startswith("merged-"):
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_slug {slug!r} is a tombstoned row. "
                    f"Tombstones are never matched or resurrected.")

            incomplete = [c for c, v in zip(("city", "kind", "lat", "lon",
                                             "location_epistemic"), row[2:7])
                          if v is None]
            if incomplete:
                raise SiteRefusal(
                    f"recording_sites[{idx}] matched existing place {slug!r}, but that "
                    f"row is incomplete (missing {', '.join(incomplete)}) and would fail "
                    f"export.sh's places.json validator the moment this album is "
                    f"promoted. Staging refuses rather than build on a broken place; "
                    f"fix the place first.")
            return row[0]

        def create_place(new, idx):
            """Create a genuinely new canonical place — complete, or not at all."""
            missing = [k for k in COMPLETENESS if new.get(k) in (None, "")]
            if missing:
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_new is incomplete — missing "
                    f"{', '.join(missing)}. A place is created complete or not at all: "
                    f"a partial row satisfies every database constraint and then aborts "
                    f"export.sh's places.json validator, taking the whole canon's export "
                    f"down weeks later and far from the mistake.")

            name = str(new["name"]).strip()
            city = str(new["city"]).strip()
            kind = new["kind"]
            if kind not in STUDIO_KINDS:
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_new.kind {kind!r} is not in the "
                    f"vocabulary — one of {', '.join(STUDIO_KINDS)}.")
            if not (_num(new["lat"]) and -90 <= new["lat"] <= 90):
                raise SiteRefusal(f"recording_sites[{idx}] site_new.lat {new['lat']!r} "
                                  f"is not a number in -90..90.")
            if not (_num(new["lon"]) and -180 <= new["lon"] <= 180):
                raise SiteRefusal(f"recording_sites[{idx}] site_new.lon {new['lon']!r} "
                                  f"is not a number in -180..180.")

            loc_ep = new["location_epistemic"]
            if loc_ep not in ("obs", "inf"):
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_new.location_epistemic {loc_ep!r} must "
                    f"be 'obs' (street-level documentation cited in location_source) or "
                    f"'inf' (city-level only).")
            address = null(new.get("address"))
            if address is None and loc_ep != "inf":
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_new has no address but claims "
                    f"location_epistemic={loc_ep!r}. No documented address means city "
                    f"precision — use a 3-decimal centroid and 'inf'. Never invent "
                    f"street-level precision.")

            slug = slugify(name)
            if slug.startswith("merged-") or slug in TOMBSTONE_REDIRECT or slug in TOMBSTONE_SPLIT:
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_new.name {name!r} slugifies to {slug!r}, "
                    f"a tombstoned row. Tombstones are never resurrected.")

            # Already present? Enrich rather than duplicate — name_slug is UNIQUE,
            # so a blind insert would fail anyway, and a row that exists but is
            # incomplete is exactly what this pipeline used to leave behind.
            cur.execute("""
                SELECT id, city, kind, lat, lon, location_epistemic
                FROM studio WHERE name_slug = %s
            """, (slug,))
            row = cur.fetchone()
            if row:
                gaps = [c for c, v in zip(("city", "kind", "lat", "lon",
                                           "location_epistemic"), row[1:6]) if v is None]
                if not gaps:
                    warnings.append(
                        f"recording_sites[{idx}]: site_new {name!r} already exists and is "
                        f"complete ({slug!r}) — matched instead of created; prefer "
                        f"site_slug next time")
                    return row[0]
                cur.execute("""
                    UPDATE studio SET city=%s, kind=%s, address=%s, lat=%s, lon=%s,
                           location_epistemic=%s::epistemic_label, location_source=%s
                    WHERE id=%s
                """, (city, kind, address, new["lat"], new["lon"], loc_ep,
                      new["location_source"], row[0]))
                cur.execute("""
                    INSERT INTO edit_log (editor, table_name, record_id, field,
                                          old_value, new_value, reason)
                    VALUES ('mccoy','studio',%s,'place_enriched',%s,%s,%s)
                """, (str(row[0]), f"incomplete: missing {', '.join(gaps)}",
                      f"{name} / {city} / {kind} / {new['lat']},{new['lon']} / {loc_ep}",
                      f"enriched by stage-candidate.py while staging {aid}"))
                warnings.append(f"recording_sites[{idx}]: enriched incomplete place {slug!r} "
                                f"(was missing {', '.join(gaps)})")
                return row[0]

            # UNIQUE (name, city) — a different slug holding this identity means the
            # place is already known under another name. That is a merge question,
            # and merges are John's ruling, not the pipeline's.
            cur.execute("SELECT name_slug FROM studio WHERE name = %s AND city = %s",
                        (name, city))
            clash = cur.fetchone()
            if clash:
                raise SiteRefusal(
                    f"recording_sites[{idx}] site_new ({name!r}, {city!r}) already exists "
                    f"as {clash[0]!r}. Use that slug, or — if you believe they are "
                    f"different rooms — say so; consolidating places is John's ruling.")

            if len(new_places) >= NEW_PLACE_CAP:
                raise SiteRefusal(
                    f"recording_sites[{idx}] would be new place #{len(new_places) + 1} this "
                    f"run; the cap is {NEW_PLACE_CAP}. A run wanting more has usually "
                    f"misparsed a compound string rather than found that many unknown "
                    f"venues. Already created: {', '.join(new_places)}.")

            cur.execute("""
                INSERT INTO studio (name, city, name_slug, kind, address, lat, lon,
                                    location_epistemic, location_source)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s::epistemic_label,%s)
                RETURNING id
            """, (name, city, slug, kind, address, new["lat"], new["lon"],
                  loc_ep, new["location_source"]))
            place_id = cur.fetchone()[0]
            cur.execute("""
                INSERT INTO edit_log (editor, table_name, record_id, field,
                                      old_value, new_value, reason)
                VALUES ('mccoy','studio',%s,'place_created',NULL,%s,%s)
            """, (str(place_id), f"{name} / {city} / {kind} / {new['lat']},{new['lon']} / {loc_ep}",
                  f"created by stage-candidate.py while staging {aid}"))
            new_places.append(slug)
            counts["places_created"] += 1
            return place_id

        def resolve_site(idx, entry):
            """One recording_sites entry -> studio_id or None. Memoised by index."""
            if idx in site_cache:
                return site_cache[idx]
            slug = null(entry.get("site_slug"))
            new  = entry.get("site_new") or None
            if slug and new:
                raise SiteRefusal(
                    f"recording_sites[{idx}] sets both site_slug ({slug!r}) and site_new — "
                    f"they are mutually exclusive. A place is either already canonical or "
                    f"it is not.")
            if slug:
                result = resolve_existing(slug, idx)
            elif new:
                result = create_place(new, idx)
            else:
                result = None            # unk — an honest, supported absence
            site_cache[idx] = result
            return result

        def instr_ids(raw):
            canonicals = normalize_instruments(raw)
            result = []
            for canonical in canonicals:
                cur.execute("SELECT id FROM instrument WHERE name = %s", (canonical,))
                row = cur.fetchone()
                if row:
                    result.append((row[0], canonical))
            return result

        # ── Person registry (dedup by canonical name, same as ingest.py) ────
        person_reg = {}

        def get_or_create_person(name, variants=None):
            if not name:
                return None
            name = name.strip()
            if name in person_reg:
                return person_reg[name]
            pid = str(uuid.uuid4())
            slug = slugify(name)
            cur.execute("""
                INSERT INTO person (id, canonical_name, sort_name, name_slug)
                VALUES (%s,%s,%s,%s)
                ON CONFLICT (canonical_name) DO UPDATE SET name_slug = person.name_slug
                RETURNING id
            """, (pid, name, name, slug))
            actual_id = str(cur.fetchone()[0])
            person_reg[name] = actual_id
            for v in (variants or []):
                v = v.strip() if v else ""
                if v and v != name:
                    cur.execute("""
                        INSERT INTO person_name_variant (person_id, variant_name)
                        VALUES (%s,%s) ON CONFLICT (person_id, variant_name) DO NOTHING
                    """, (actual_id, v))
            return actual_id

        for p in personnel:
            get_or_create_person(p.get("name"), p.get("name_variants") or [])
        for field in ("producer", "engineer"):
            get_or_create_person(null(pr.get(field)))
        for t in pr.get("tracks") or []:
            for c in t.get("composers") or []:
                get_or_create_person(null(c))

        def find_leader(artist_str):
            if not artist_str:
                return None
            artist_lower = artist_str.lower()
            for p in personnel:
                name = (p.get("name") or "").strip()
                if name and name.lower() in artist_lower:
                    return person_reg.get(name)
            return None

        # ── Resolve tier/priority: ballot > record's own fields ─────────────
        # inclusion_rationale is NOT part of this fallback — it is the record's
        # own `rationale` on both paths (migrate-4a). The ballot's prose goes to
        # case_for/case_against, its own columns since 4a.
        if ballot_entry:
            canon_tier = ballot_entry.get("tier") if ballot_entry.get("tier") in CANON_TIERS else None
            priority = PRIORITY_MAP.get(ballot_entry.get("priority"))
            case_for = null(ballot_entry.get("case_for"))
            case_against = null(ballot_entry.get("case_against"))
        else:
            canon_tier = None
            priority = PRIORITY_MAP.get(record.get("priority"))
            case_for = None
            case_against = None

        inclusion_rationale = null(record.get("rationale"))
        if ballot_entry and inclusion_rationale is None:
            warnings.append("ballot present but record has no top-level 'rationale' — "
                            "inclusion_rationale left NULL (case_for is not a substitute)")

        leader_id = find_leader(record.get("artist", ""))
        mbid      = null(pr.get("musicbrainz_release_group_mbid"))
        apple_id  = null(pr.get("apple_album_id"))
        if apple_id is not None:
            apple_id = str(apple_id)
        catalog   = null(record.get("catalog_number")) or ""
        rec_dates = pr.get("recording_dates") or []
        dates_text = ", ".join(str(d) for d in rec_dates if d) or None

        # ── Album row: canon_status='candidate', site_status='found' — hard-coded ──
        cur.execute("""
            INSERT INTO album (
                id, title, artist_name, leader_person_id, year, label_id,
                catalog_number, consensus, style_primary_id,
                recording_dates_text, multi_session,
                musicbrainz_release_group_mbid, apple_album_id,
                canon_status, site_status, canon_tier, priority, inclusion_rationale,
                epistemic, notes, case_for, case_against
            ) VALUES (
                %s,%s,%s,%s,%s,%s,
                %s,%s,%s,
                %s,%s,
                %s,%s,
                'candidate'::canon_status, 'found', %s::canon_tier, %s::priority_label, %s,
                %s::epistemic_label, %s, %s, %s
            )
        """, (
            aid,
            record.get("album", ""),
            record.get("artist", ""),
            leader_id,
            year,
            get_or_create_label(record.get("label")),
            catalog,
            null(record.get("consensus")),
            style_id(record.get("style_primary", "")),
            dates_text,
            pr.get("multi_session", False),
            mbid,
            apple_id,
            canon_tier,
            priority,
            inclusion_rationale,
            ep(record.get("epistemic")),
            null(pr.get("notes")),
            case_for,
            case_against,
        ))

        counts = dict(sessions=0, tracks=0, track_composers=0, performances=0,
                      perf_tracks=0, prod_credits=0, art_rows=0,
                      sources_created=0, citations_created=0, places_created=0)

        # ── Secondary styles ──────────────────────────────────────────────────
        for tag in record.get("style_tags") or []:
            sid = style_id(tag)
            if sid:
                cur.execute("""
                    INSERT INTO album_style (album_id, style_id, is_primary)
                    VALUES (%s,%s,false) ON CONFLICT (album_id, style_id) DO NOTHING
                """, (aid, sid))
            else:
                # unknown tags stay non-fatal (a tag is not load-bearing), but
                # they no longer vanish without trace
                warnings.append(f"unknown style_tag {tag!r} — skipped")

        # ── Sessions ──────────────────────────────────────────────────────────
        # Each session gets its OWN place. The retired code resolved one studio
        # per album and applied it to every session row, so a two-venue album
        # could not be staged correctly no matter how good the research was.
        sites = pr.get("recording_sites")
        if sites is None:
            raise SiteRefusal(
                "personnel_record has no `recording_sites`. Required since "
                "personnel-contract v1.1 — one entry per session. If sources do not "
                "say where the album was recorded, that is an entry with epistemic "
                "'unk' and null site fields, not a missing array: silence is "
                "indistinguishable from an oversight.")
        if not isinstance(sites, list) or not sites:
            raise SiteRefusal(
                "`recording_sites` is empty. Unknown is a value — emit one entry with "
                "epistemic 'unk' and null site fields rather than an empty array.")

        site_by_date = {}
        undated = None
        for idx, entry in enumerate(sites):
            if not isinstance(entry, dict):
                raise SiteRefusal(f"recording_sites[{idx}] is not an object")
            d = safe_date(entry.get("session_date"))
            if d:
                if d in site_by_date:
                    raise SiteRefusal(
                        f"recording_sites has two entries for session_date {d} — one "
                        f"entry per session. If the album really used two venues that "
                        f"day, the sessions need distinguishing first.")
                site_by_date[d] = (idx, entry)
            elif undated is None:
                undated = (idx, entry)
            else:
                raise SiteRefusal(
                    "recording_sites has more than one entry without a session_date, so "
                    "they cannot be matched to sessions. Date the entries, or record the "
                    "ambiguity as a single 'unk' entry and explain it in notes.")

        # Sessions come from recording_dates, plus any dated site entry that
        # recording_dates omitted — so a place is never silently dropped for
        # want of a matching date.
        session_dates = list(rec_dates)
        known = {safe_date(d) for d in session_dates}
        for d in site_by_date:
            if d not in known:
                session_dates.append(d)
                warnings.append(f"recording_sites names session_date {d}, absent from "
                                f"recording_dates — session row added for it")
        if not session_dates:
            session_dates = [None]
        if undated and len(session_dates) > 1 and not site_by_date:
            warnings.append(
                f"one undated recording_sites entry applied to all {len(session_dates)} "
                f"sessions — date the entries if the venues differed")

        date_to_session = {}
        primary_session_id = None
        for seq, date_val in enumerate(session_dates, start=1):
            sid_uuid = str(uuid.uuid4())
            date_str = safe_date(date_val)
            date_text = str(date_val) if date_val else None

            hit = site_by_date.get(date_str) or undated
            if hit is None:
                stid = None
                warnings.append(f"session {date_str or '(undated)'} has no recording_sites "
                                f"entry — staged without a place")
            else:
                stid = resolve_site(hit[0], hit[1])
            if stid is None:
                site_assignments.append((date_str or "(undated)", None))
            else:
                cur.execute("SELECT name_slug FROM studio WHERE id = %s", (stid,))
                site_assignments.append((date_str or "(undated)", cur.fetchone()[0]))

            cur.execute("""
                INSERT INTO session (id, album_id, session_date, session_date_text, studio_id, sequence, epistemic)
                VALUES (%s,%s,%s,%s,%s,%s,'obs'::epistemic_label)
            """, (sid_uuid, aid, date_str, date_text, stid, seq))
            if date_str:
                date_to_session[date_str] = sid_uuid
                date_to_session[date_text] = sid_uuid
            if seq == 1:
                primary_session_id = sid_uuid
            counts["sessions"] += 1

        # ── Tracks ────────────────────────────────────────────────────────────
        track_key_to_id = {}
        for t in pr.get("tracks") or []:
            tnum  = t.get("track_number")
            title = t.get("title", "")
            tdate = safe_date(t.get("session_date"))
            sess  = date_to_session.get(tdate, primary_session_id)
            dur   = t.get("duration") or t.get("duration_text")

            cur.execute("""
                INSERT INTO track (id, album_id, session_id, title, track_number, side,
                                   duration_text, bonus_track, alternate_take, epistemic_track)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::epistemic_label)
                RETURNING id
            """, (
                str(uuid.uuid4()), aid, sess, title, tnum,
                t.get("side"), dur,
                t.get("bonus_track", False),
                t.get("alternate_take", False),
                ep(t.get("epistemic_track")),
            ))
            actual_tid = str(cur.fetchone()[0])
            track_key_to_id[(tnum, title)] = actual_tid
            counts["tracks"] += 1

            for composer in t.get("composers") or []:
                cid = person_reg.get(composer) if composer else None
                if cid:
                    cur.execute("""
                        INSERT INTO track_composer (track_id, person_id)
                        VALUES (%s,%s) ON CONFLICT (track_id, person_id) DO NOTHING
                    """, (actual_tid, cid))
                    counts["track_composers"] += 1

        track_name_set = {title: tid for (_, title), tid in track_key_to_id.items()}

        # ── Performances ──────────────────────────────────────────────────────
        for p in personnel:
            pname = (p.get("name") or "").strip()
            pid   = person_reg.get(pname)
            if not pid:
                warnings.append(f"person not in registry: {pname!r}")
                continue

            instrument_list = instr_ids(p.get("instrument"))
            if not instrument_list:
                continue  # already validated above; NON_INSTRUMENTS entries land here

            scope = p.get("scope", "all-tracks")
            if scope not in ("all-tracks", "selected-tracks", "unknown"):
                scope = "unknown"

            for iid, _ in instrument_list:
                cur.execute("""
                    INSERT INTO performance (id, album_id, person_id, instrument_id, scope, epistemic)
                    VALUES (%s,%s,%s,%s,%s::performance_scope,%s::epistemic_label)
                    RETURNING id
                """, (str(uuid.uuid4()), aid, pid, iid, scope, ep(p.get("epistemic"))))
                perf_id = str(cur.fetchone()[0])
                counts["performances"] += 1

                if scope == "selected-tracks" and p.get("tracks"):
                    for track_ref in (p["tracks"] or []):
                        tid = track_name_set.get(track_ref) or track_key_to_id.get((None, track_ref))
                        if tid:
                            cur.execute("""
                                INSERT INTO performance_track (performance_id, track_id)
                                VALUES (%s,%s) ON CONFLICT (performance_id, track_id) DO NOTHING
                            """, (perf_id, tid))
                            counts["perf_tracks"] += 1

        # ── Production credits ────────────────────────────────────────────────
        for field, role in (("producer", "producer"), ("engineer", "engineer")):
            val = null(pr.get(field))
            if not val:
                continue
            cred_person_id = person_reg.get(val)
            if not cred_person_id:
                continue
            ep_prod = ep(null(pr.get("epistemic_production")))
            cur.execute("""
                INSERT INTO production_credit (id, album_id, person_id, role, epistemic)
                VALUES (%s,%s,%s,%s::production_role,%s::epistemic_label)
            """, (str(uuid.uuid4()), aid, cred_person_id, role, ep_prod))
            counts["prod_credits"] += 1

        # ── Cover art ─────────────────────────────────────────────────────────
        cover = pr.get("cover_art")
        if isinstance(cover, list):
            for ca in cover:
                url = null(ca.get("url") or ca.get("source_url"))
                if not url:
                    continue
                src = ca.get("source", "cover-art-archive")
                if src not in ("cover-art-archive", "itunes", "discogs", "wikimedia", "manual", "other"):
                    src = "other"
                cur.execute("""
                    INSERT INTO album_art (id, album_id, role, source, source_url, is_primary, epistemic)
                    VALUES (%s,%s,'front'::art_role,%s::art_source,%s,true,%s::epistemic_label)
                """, (str(uuid.uuid4()), aid, src, url, ep(ca.get("epistemic"), "inf")))
                counts["art_rows"] += 1

        # ── Citations (album-level, v1) ───────────────────────────────────────
        cur.execute("SELECT id, title, url FROM source")
        source_registry = {source_key(title, url): sid for sid, title, url in cur.fetchall()}

        for title, source_type, url, notes, locator in resolve_citation_sources(record, warnings):
            key = source_key(title, url)
            sid = source_registry.get(key)
            if sid is None:
                cur.execute("""
                    INSERT INTO source (title, source_type, url, notes)
                    VALUES (%s, %s::source_type, %s, %s)
                    RETURNING id
                """, (title, source_type, url, notes))
                sid = cur.fetchone()[0]
                source_registry[key] = sid
                counts["sources_created"] += 1
            cur.execute("""
                INSERT INTO citation (source_id, album_id, locator)
                VALUES (%s, %s, %s)
            """, (sid, aid, locator))
            counts["citations_created"] += 1

        # ── Audit ─────────────────────────────────────────────────────────────
        cur.execute("""
            INSERT INTO edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
            VALUES ('mccoy', 'album', %s, 'staged', NULL, 'candidate/found', 'staged by stage-candidate.py')
        """, (aid,))

    except SiteRefusal as e:
        conn.rollback()
        print(f"\nREFUSED — {e}")
        print("Nothing written. Fix the record's recording_sites block and re-run.")
        conn.close()
        sys.exit(1)

    except Exception as e:
        conn.rollback()
        print(f"\n✗ ERROR — rolled back, nothing written: {e}", file=sys.stderr)
        conn.close()
        sys.exit(1)

    if dry_run:
        conn.rollback()
        print("\nDRY RUN — rolled back, nothing written to DB")
    else:
        conn.commit()
        print("\nCANDIDATE STAGED — awaiting John's review")

    print("\n── Summary ──")
    print(f"  album id       : {aid}")
    print(f"  persons        : {len(person_reg)}")
    for k, v in counts.items():
        print(f"  {k:15s}: {v}")

    if site_assignments:
        print("\n── Recording places ──")
        for when, slug in site_assignments:
            print(f"  {when:12s} -> {slug or '(none — unk)'}")
        for slug in new_places:
            print(f"  + new place: {slug}")

    if warnings:
        print(f"\n── Warnings ({len(warnings)}) ──")
        for w in warnings:
            print(f"  {w}")

    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
