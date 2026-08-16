#!/usr/bin/env python3
"""
seed-studio-name-variants.py — populate _jazzcanon.studio_name_variant once.

Seeds the recording-place alias table from the audit trail of the 2026-08-14
studios cleanup, plus hand-written variants for places that have no trail.

WHY A ONE-TIME SEED, NOT A RUNTIME LOOKUP
    The cleanup recorded its rulings in three `edit_log` fields whose targets
    live in FREE TEXT with no structured column ("merged into #121 (item B3)").
    That is fine to read once, under review, and a liability to parse every
    night. Nothing in the pipeline queries edit_log at runtime, and nothing
    should.

WHAT IS DELIBERATELY EXCLUDED — the whole point of the exercise
    1. COMPOUND raws (5) name two venues each. Mapping one to a single
       surviving slug silently drops the other, which is the exact failure the
       2026-08-14 cleanup existed to undo. Note that edit_log 191 is compound
       WITHOUT a semicolon ("Wally Heider Studios and Different Fur Trading
       Co.") — it does not look compound, and Different Fur was split out to
       its own row (#219).
    2. SPLIT tombstones (4) have TWO surviving targets, so no single slug is
       the right answer. Only the 5 MERGED tombstones — one target each — are
       valid aliases.
    3. AMBIGUOUS BARE NAMES (5). The cleanup ruled what a given ROW's raw
       string meant; that is not the same as ruling what the bare wording means
       going forward. "Van Gelder Studio" was ruled to Englewood Cliffs for row
       137, but the bare name is genuinely ambiguous with Hackensack and the
       session date is what decides. Seeding it would mis-file every Hackensack
       session that arrives phrased that way. These are handled by the
       precheck's [E] DISAMBIGUATION section, which teaches the rule instead of
       guessing the answer. A missing alias costs a match; a wrong one silently
       mis-files a session.

IDEMPOTENT. Inserts are ON CONFLICT DO NOTHING against UNIQUE (studio_id,
variant_name), so a re-run adds only what is genuinely new and reports zero
inserted otherwise. The brief assumed a one-shot script; making it re-runnable
cost one clause and removes the footgun of a half-applied seed that can only be
retried by hand.

Usage:
  .venv/bin/python3 scripts/seed-studio-name-variants.py [--dry-run]
"""

import argparse
import os
import re
import sys
from pathlib import Path

import psycopg2

REPO_ROOT = Path(__file__).resolve().parent.parent

# ── edit_log rows that must never become a flat alias ────────────────────────

# Compound raws: two venues in one string (191 has no semicolon and so does not
# look compound — it is the one that would slip through a naive filter).
COMPOUND_IDS = {
    "124": "Lennie Tristano's home studio + The Sing-Song Room",
    "134": "The Strollers + Radio Recorders",
    "161": "Half Note Club + Van Gelder Englewood Cliffs",
    "180": "Coltrane home Dix Hills + Village Gate",
    "191": "Wally Heider Studios + Different Fur Trading Co. (no semicolon!)",
}

# Bare wordings the cleanup resolved for ONE ROW but which are ambiguous as
# forward-looking aliases. Each is taught by the precheck's [E] section instead.
AMBIGUOUS_BARE = {
    "Van Gelder Studio":
        "Hackensack vs Englewood Cliffs — the session date decides (moved July 1959)",
    "Capitol Studios":
        "Melrose Avenue vs Capitol Tower — the session date decides (Tower opened Apr 1956)",
    "CBS Studios":
        "Paris vs New York vs CBS 30th Street — the city decides, then whether "
        "30th Street is actually documented",
    "Columbia Studios":
        "Columbia Square Hollywood vs CBS 30th Street New York — the city decides",
    "RCA Victor Studios":
        "New York vs Hollywood — the city decides",
}

# Variants with no cleanup trail, or the disambiguated forms of the five above.
# (variant_name, slug, note)
#
# The nine places born from SPLITS have no `place_canonicalization` row at all —
# they were created during the cleanup, so nothing records what a source called
# them. They are also the ones researchers phrase loosest, which is why they get
# the most generous coverage here.
HAND_VARIANTS = [
    # ── the 9 place_created places (no alias trail whatsoever) ──
    ("Van Gelder Studio, Hackensack",      "van-gelder-studio-hackensack",        "split-created; date-qualified"),
    ("Van Gelder Studio (Hackensack)",     "van-gelder-studio-hackensack",        "split-created; date-qualified"),
    ("Manhattan Towers",                   "manhattan-towers-hotel-ballroom",     "split-created"),
    ("Manhattan Towers Hotel",             "manhattan-towers-hotel-ballroom",     "split-created"),
    ("Manhattan Towers Ballroom",          "manhattan-towers-hotel-ballroom",     "split-created"),
    ("CBS Studios, New York",              "cbs-studios-new-york",                "split-created; city-qualified"),
    ("CBS Studios, New York City",         "cbs-studios-new-york",                "split-created; city-qualified"),
    ("A & R Recording (room undetermined)", "a-r-recording-room-undetermined",    "split-created; honest fallback, never the default"),
    ("The Sing-Song Room",                 "sing-song-room-confucius-restaurant", "split-created"),
    ("Confucius Restaurant",               "sing-song-room-confucius-restaurant", "split-created"),
    ("Capitol Tower",                      "capitol-records-studio-capitol-tower", "split-created; date-qualified"),
    ("Capitol Records Tower",              "capitol-records-studio-capitol-tower", "split-created; date-qualified"),
    ("Capitol Studios, Capitol Tower",     "capitol-records-studio-capitol-tower", "split-created; date-qualified"),
    ("Gold Star",                          "gold-star-recording-studios",         "split-created"),
    ("Gold Star Studios",                  "gold-star-recording-studios",         "split-created"),
    ("Village Gate",                       "village-gate",                        "split-created"),
    ("The Village Gate",                   "village-gate",                        "split-created"),
    ("Different Fur",                      "different-fur-trading-co",            "split-created"),
    ("Different Fur Studios",              "different-fur-trading-co",            "split-created"),

    # ── disambiguated forms of the five ambiguous bare names ──
    ("Van Gelder Studio, Englewood Cliffs", "van-gelder-studio-englewood-cliffs", "date/city-qualified form of an ambiguous bare name"),
    ("Van Gelder Studio (Englewood Cliffs)", "van-gelder-studio-englewood-cliffs", "date/city-qualified form of an ambiguous bare name"),
    ("Capitol Studios, Hollywood",         "capitol-records-studio-melrose-avenue", "pre-Apr-1956 form; the Tower has its own row"),
    ("Capitol Records Studio, Melrose Avenue", "capitol-records-studio-melrose-avenue", "date-qualified"),
    ("CBS Studios, Paris",                 "cbs-studios-paris",                   "city-qualified form of an ambiguous bare name"),
    ("Columbia Studios, Hollywood",        "columbia-records-hollywood-studio-columbia-square", "city-qualified"),
    ("Columbia Square",                    "columbia-records-hollywood-studio-columbia-square", "building name"),
    ("RCA Victor Studios, New York",       "rca-victor-studios-new-york",         "city-qualified form of an ambiguous bare name"),
    ("RCA Victor Studios, Hollywood",      "rca-victor-studios-hollywood",        "city-qualified form of an ambiguous bare name"),

    # ── wordings the cleanup did not record but sources do use ──
    ("A & R Recording",                    "a-r-recording-112-west-48th-street",  "merged tombstone raw; ruled 2026-08-14"),
    ("Columbia Recording Studio B",        "cbs-30th-street-studio",              "merged tombstone raw; ruling D1"),
    ("Columbia 30th Street",               "cbs-30th-street-studio",              "common short form"),
    ("30th Street Studio",                 "cbs-30th-street-studio",              "common short form"),
    ("Tonstudio Bauer",                    "studio-bauer-ludwigsburg",            "merged tombstone raw; ruling B4"),
    ("Pershing Lounge",                    "pershing-lounge-pershing-hotel",      "short form"),
    ("Pershing Hotel",                     "pershing-lounge-pershing-hotel",      "short form"),
    ("Wally Heider Studios",               "wally-heider-studios",                "first venue of compound edit_log 191"),
    # The four places whose ONLY trail was a compound raw keep no auto alias.
    # Three of them (Half Note Club, The Strollers, Lennie Tristano's home
    # studio) have a raw name identical to their canonical name, so an alias
    # would only duplicate what [C] already prints. This one genuinely differs
    # — a source writing "Coltrane home studios" would not match "Coltrane Home
    # (Dix Hills)" — so its first-venue name is recovered by hand. Taking the
    # FIRST VENUE's name from a compound raw is safe; taking the whole string
    # is what drops the second venue.
    ("Coltrane home studios",              "coltrane-home-dix-hills",             "first venue of compound edit_log 180"),
    ("Coltrane Home Studio, Dix Hills",    "coltrane-home-dix-hills",             "hand-written; common phrasing"),
    ("Wally Heider",                       "wally-heider-studios",                "short form"),
    ("Phil Turetsky's home",               "phil-turetskys-home",                 "name portion of a ' / '-ambiguous raw (edit_log 129)"),
    ("Los Angeles",                        "los-angeles-venue-unidentified",      "bare city = venue unidentified, not a venue name"),
    ("New York City",                      "new-york-city-venue-unidentified",    "bare city = venue unidentified, not a venue name"),
    ("Universal Recording",                "universal-recording-corporation",     "short form"),
    ("Olmsted Sound Studios",              "olmstead-sound-studios",              "source spelling; the DB row spells it Olmstead"),
    ("Forum Theater",                      "forum-theatre",                       "US spelling; the DB row uses Theatre"),
]


def load_env(path=REPO_ROOT / ".env.local"):
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v.strip())


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true",
                    help="Run the full transaction and roll back")
    args = ap.parse_args()

    load_env()
    url = os.environ.get("JAZZCANON_APP_DB_URL")
    if not url:
        sys.exit("✗ JAZZCANON_APP_DB_URL not set (check .env.local)")

    conn = psycopg2.connect(url)
    cur = conn.cursor()
    cur.execute("SET search_path TO _jazzcanon, public")

    slug_of, id_of = {}, {}
    cur.execute("SELECT id, name_slug FROM studio")
    for sid, slug in cur.fetchall():
        slug_of[sid] = slug
        id_of[slug] = sid
    canonical = {s for s in id_of if not s.startswith("merged-")}

    pending = {}          # (studio_id, variant) -> note
    excluded = {"compound": [], "split": [], "ambiguous": [], "unknown_slug": []}

    def offer(variant, studio_id, note):
        variant = variant.strip()
        if not variant:
            return
        pending.setdefault((studio_id, variant), note)

    def offer_raw(raw_name, studio_id, note):
        """Offer a raw name AND its bare form.

        Cleanup raws often carry a trailing qualifier the cataloguer added —
        "Birdland (live)", "Tsubo (live)", "The Jazz Workshop (live)". A source
        writes the bare name, so seeding only the annotated form would lose the
        match that the hand-built hint list had. Offer both: the annotated form
        costs one row and still matches if a researcher copies it verbatim.
        """
        offer(raw_name, studio_id, note)
        bare = re.sub(r"\s*\((?:live|studio|studios)\)\s*$", "", raw_name,
                      flags=re.I).strip()
        if bare and bare != raw_name.strip():
            offer(bare, studio_id, f"{note} — bare form")

    # ── source 1: place_canonicalization (38) ────────────────────────────────
    cur.execute("""
        SELECT record_id, old_value FROM edit_log
        WHERE table_name='studio' AND field='place_canonicalization'
        ORDER BY record_id::int
    """)
    canon_rows = cur.fetchall()
    for rid, raw in canon_rows:
        if rid in COMPOUND_IDS:
            excluded["compound"].append((rid, raw, COMPOUND_IDS[rid]))
            continue
        # `old_value` is "<name> / <city>". The delimiter is NOT safe: edit_log
        # 129 is "Phil Turetsky's home / Pacific Jazz sessions / Los Angeles",
        # so split from the RIGHT and take the city off the end.
        name = raw.rsplit(" / ", 1)[0] if " / " in raw else raw
        name = name.strip()
        if name in AMBIGUOUS_BARE:
            excluded["ambiguous"].append((rid, name, AMBIGUOUS_BARE[name]))
            continue
        sid = int(rid)
        if slug_of.get(sid, "").startswith("merged-"):
            excluded["unknown_slug"].append((rid, name, "target is a tombstone"))
            continue
        offer_raw(name, sid, "edit_log place_canonicalization (2026-08-14 cleanup)")

    # ── source 2: place_merged_away (9) — MERGED only, never SPLIT ───────────
    cur.execute("""
        SELECT record_id, old_value, new_value FROM edit_log
        WHERE table_name='studio' AND field='place_merged_away'
        ORDER BY record_id::int
    """)
    merged_rows = cur.fetchall()
    for rid, raw, target in merged_rows:
        if not target.startswith("merged into"):
            # SPLIT: two targets, so no single slug is correct. Note one row
            # names its second target by NAME not id, so a `#(\d+)` sweep
            # under-counts — which is why this branches on the verb, not a regex.
            excluded["split"].append((rid, raw, target))
            continue
        m = re.search(r"merged into #(\d+)", target)
        if not m:
            excluded["split"].append((rid, raw, f"unparseable target: {target}"))
            continue
        sid = int(m.group(1))
        if slug_of.get(sid, "").startswith("merged-"):
            excluded["unknown_slug"].append((rid, raw, "target is itself a tombstone"))
            continue
        name = raw.rsplit(" / ", 1)[0] if " / " in raw else raw
        offer_raw(name.strip(), sid, f"edit_log place_merged_away — {target}")

    # ── source 3: hand-written ───────────────────────────────────────────────
    for variant, slug, note in HAND_VARIANTS:
        if slug not in id_of:
            excluded["unknown_slug"].append(("hand", variant, f"no such slug: {slug}"))
            continue
        if slug.startswith("merged-"):
            excluded["unknown_slug"].append(("hand", variant, f"tombstone slug: {slug}"))
            continue
        offer(variant, id_of[slug], f"hand-written — {note}")

    # ── write ────────────────────────────────────────────────────────────────
    inserted = 0
    for (sid, variant), note in sorted(pending.items(), key=lambda kv: (slug_of[kv[0][0]], kv[0][1])):
        cur.execute("""
            INSERT INTO studio_name_variant (studio_id, variant_name, source_note)
            VALUES (%s,%s,%s) ON CONFLICT (studio_id, variant_name) DO NOTHING
        """, (sid, variant, note))
        inserted += cur.rowcount

    # ── the arithmetic, out loud ─────────────────────────────────────────────
    print("── Sources ──")
    print(f"  place_canonicalization rows : {len(canon_rows)}")
    print(f"  place_merged_away rows      : {len(merged_rows)}")
    print(f"  hand-written variants       : {len(HAND_VARIANTS)}")
    print(f"  canonical places in DB      : {len(canonical)}")

    print("\n── Excluded (named, never silently dropped) ──")
    print(f"  COMPOUND — two venues in one string ({len(excluded['compound'])}):")
    for rid, raw, why in excluded["compound"]:
        print(f"    [{rid}] {raw[:64]!r}\n          = {why}")
    print(f"  SPLIT tombstones — two surviving targets ({len(excluded['split'])}):")
    for rid, raw, target in excluded["split"]:
        print(f"    [{rid}] {raw[:56]!r}  ({target})")
    print(f"  AMBIGUOUS bare names — taught in [E], not guessed ({len(excluded['ambiguous'])}):")
    for rid, name, why in excluded["ambiguous"]:
        print(f"    [{rid}] {name!r}\n          {why}")
    if excluded["unknown_slug"]:
        print(f"  UNRESOLVABLE ({len(excluded['unknown_slug'])}):")
        for rid, name, why in excluded["unknown_slug"]:
            print(f"    [{rid}] {name!r} — {why}")

    used_canon = len(canon_rows) - len(excluded["compound"]) - len(excluded["ambiguous"])
    used_merged = len(merged_rows) - len(excluded["split"])
    print("\n── Arithmetic ──")
    print(f"  {len(canon_rows)} canonicalization - {len(excluded['compound'])} compound "
          f"- {len(excluded['ambiguous'])} ambiguous = {used_canon} used")
    print(f"  {len(merged_rows)} merged_away - {len(excluded['split'])} SPLIT = {used_merged} used")
    print(f"  + {len(HAND_VARIANTS)} hand-written")
    print(f"  = {len(pending)} distinct (studio, variant) pairs offered")
    print(f"  {inserted} inserted, {len(pending) - inserted} already present")

    cur.execute("SELECT count(*) FROM studio_name_variant")
    total = cur.fetchone()[0]
    cur.execute("SELECT count(DISTINCT studio_id) FROM studio_name_variant")
    covered = cur.fetchone()[0]
    print(f"\n  studio_name_variant now: {total} rows covering {covered}/{len(canonical)} canonical places")

    uncovered = sorted(canonical - {slug_of[sid] for sid, _ in pending})
    if uncovered:
        print(f"\n── Canonical places with no variant ({len(uncovered)}) ──")
        print("  (not an error — their canonical name is the only known wording)")
        for s in uncovered:
            print(f"    {s}")

    if args.dry_run:
        conn.rollback()
        print("\nDRY RUN — rolled back, nothing written")
    else:
        conn.commit()
        print("\nCommitted.")
    conn.close()


if __name__ == "__main__":
    main()
