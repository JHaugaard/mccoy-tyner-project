#!/usr/bin/env python3
"""
rebuild-canon.py — Apply reconciliation decisions to canon-draft.json.

What this does:
  1. Adds `consensus` field to every existing record (both/claude_only/kimi_only)
  2. Sets include:false for the 19 albums moving to next-batch
  3. Loads 14 adapted Kimi records from data/kimi-adapted/ and sets include:true
  4. Updates _meta (count, date, status note)

Run from the mccoy-tyner project root:
    python3 scripts/rebuild-canon.py

Output overwrites data/canon-draft.json in place.
A backup is written to data/canon-draft.backup.json before any changes.
"""

import json
import shutil
from datetime import date
from pathlib import Path

CANON_PATH = Path("data/canon-draft.json")
BACKUP_PATH = Path("data/canon-draft.backup.json")
KIMI_ADAPTED_DIR = Path("data/kimi-adapted")

# 48 albums present in BOTH harnesses → exact IDs from canon-draft.json
BOTH = {
    "andrew-hill-point-of-departure-1964",
    "art-blakey-moanin-1958",
    "art-pepper-art-pepper-meets-the-rhythm-section-1957",
    "bill-evans-portrait-in-jazz-1959",
    "bill-evans-waltz-for-debby-1961",
    "bobby-hutcherson-dialogue-1965",
    "cannonball-adderley-somethin-else-1958",
    "chet-baker-chet-baker-sings-1954",
    "clifford-brown-max-roach-study-in-brown-1955",
    "dave-brubeck-quartet-time-out-1959",
    "dexter-gordon-go-1962",
    "donald-byrd-a-new-perspective-1963",
    "freddie-hubbard-hub-tones-1962",
    "freddie-hubbard-ready-for-freddie-1961",
    "gil-evans-new-bottle-old-wine-1958",
    "grant-green-idle-moments-1963",
    "hank-mobley-roll-call-1960",
    "hank-mobley-soul-station-1960",
    "herbie-hancock-empyrean-isles-1964",
    "herbie-hancock-maiden-voyage-1965",
    "horace-silver-song-for-my-father-1964",
    "jackie-mclean-let-freedom-ring-1962",
    "jimmy-giuffre-the-jimmy-giuffre-3-1956",
    "jimmy-smith-back-at-the-chicken-shack-1960",
    "jimmy-smith-the-sermon-1958",
    "joe-henderson-inner-urge-1964",
    "joe-henderson-mode-for-joe-1966",
    "joe-henderson-page-one-1963",
    "john-coltrane-a-love-supreme-1964",
    "john-coltrane-my-favorite-things-1960",
    "kenny-burrell-midnight-blue-1963",
    "kenny-dorham-una-mas-1963",
    "lee-konitz-subconscious-lee-1950",
    "lee-morgan-the-sidewinder-1963",
    "lennie-tristano-lennie-tristano-1955",
    "lou-donaldson-alligator-bogaloo-1967",
    "mccoy-tyner-the-real-mccoy-1967",
    "miles-davis-birth-of-the-cool-1950",
    "miles-davis-e-s-p-1965",
    "miles-davis-kind-of-blue-1959",
    "modern-jazz-quartet-django-1955",
    "sonny-clark-cool-struttin-1958",
    "sonny-rollins-saxophone-colossus-1956",
    "stan-getz-focus-1961",
    "stan-getz-west-coast-jazz-1955",
    "wayne-shorter-adams-apple-1966",
    "wayne-shorter-juju-1964",
    "wayne-shorter-speak-no-evil-1964",
}

# 19 Claude albums moving to next-batch (include:false) — exact IDs
# Note: 6 originally flagged as NEXT were reinstated by John to reach 100:
#   miles-davis-nefertiti-1967, sonny-rollins-way-out-west-1957,
#   mccoy-tyner-expansions-1968, chet-baker-chet-baker-and-crew-1956,
#   horace-silver-blowin-the-blues-away-1959, gerry-mulligan-what-is-there-to-say-1959
NEXT_BATCH = {
    # Coltrane (John chose 4: Love Supreme, My Fav Things, Giant Steps, Blue Train)
    "john-coltrane-crescent-1964",
    "john-coltrane-live-at-the-village-vanguard-1961",
    "john-coltrane-africa-brass-1961",
    "john-coltrane-ballads-1962",
    "john-coltrane-coltrane-1962",
    # Bill Evans (triptych: Portrait, Waltz, Sunday)
    "bill-evans-everybody-digs-bill-evans-1958",
    "bill-evans-explorations-1961",
    # McCoy Tyner (2 only: Real McCoy + Sahara; Tender Moments out)
    "mccoy-tyner-tender-moments-1967",
    # Art Pepper (one album enough)
    "art-pepper-art-pepper-plus-eleven-1959",
    # Dave Brubeck (Time Out only)
    "dave-brubeck-jazz-at-oberlin-1953",
    # Jackie McLean (Let Freedom Ring + Destination...Out! suffice)
    "jackie-mclean-bluesnik-1961",
    # Jimmy Giuffre (The Jimmy Giuffre 3 only)
    "jimmy-giuffre-the-jimmy-giuffre-clarinet-1956",
    # Lee Konitz (Subconscious-Lee only)
    "lee-konitz-plays-with-the-gerry-mulligan-quartet-1953",
    "lee-konitz-lee-konitz-with-warne-marsh-1955",
    # Lee Morgan (Sidewinder + Search for the New Land suffice)
    "lee-morgan-the-cooker-1957",
    # Wayne Shorter (4-album set: Night Dreamer, JuJu, Speak No Evil, Adam's Apple)
    "wayne-shorter-the-all-seeing-eye-1965",
    # Scope / John's explicit decisions
    "keith-jarrett-the-koln-concert-1975",
    "shorty-rogers-martians-come-back-1955",
    "shorty-rogers-and-his-giants-1953",
}


def find_consensus(record):
    """Return consensus tag — exact ID match only."""
    rid = record.get("id", "").lower().strip()
    return "both" if rid in BOTH else "claude_only"


def is_next_batch(record):
    """Exact ID match only."""
    rid = record.get("id", "").lower().strip()
    return rid in NEXT_BATCH


def main():
    # Backup
    shutil.copy(CANON_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH}")

    with open(CANON_PATH) as f:
        data = json.load(f)

    albums = data["albums"]
    print(f"Loaded {len(albums)} existing records")

    # Step 1: Tag all existing records with consensus + handle next-batch
    # Reset all include values first (handles stale data from any prior partial run)
    next_batch_count = 0
    both_count = 0
    claude_only_count = 0

    for record in albums:
        # Detect kimi-adapted records by source signature and restore their tag
        sources = record.get("sources", [])
        is_kimi = any(str(s).startswith("kimi:") for s in sources)
        if is_kimi:
            record["consensus"] = "kimi_only"
            record["include"] = True
            continue

        consensus = find_consensus(record)
        record["consensus"] = consensus
        if consensus == "both":
            both_count += 1
        else:
            claude_only_count += 1

        if is_next_batch(record):
            record["include"] = False
            next_batch_count += 1
        else:
            record["include"] = True  # reset any stale False from prior runs

    print(f"Consensus tagged: {both_count} both, {claude_only_count} claude_only")
    print(f"Moved to next-batch: {next_batch_count}")

    # Step 2: Load and add Kimi adapted records
    kimi_files = sorted(KIMI_ADAPTED_DIR.glob("*.json"))
    kimi_added = 0
    existing_ids = {r["id"] for r in albums}

    for kf in kimi_files:
        with open(kf) as f:
            record = json.load(f)
        if record["id"] in existing_ids:
            print(f"  SKIP (already exists): {record['id']}")
            continue
        record["include"] = True
        record["consensus"] = "kimi_only"
        albums.append(record)
        existing_ids.add(record["id"])
        kimi_added += 1
        print(f"  Added: {record['artist']} — {record['album']}")

    # Step 3: Count and verify
    active = [r for r in albums if r.get("include")]
    next_b  = [r for r in albums if not r.get("include")]

    print(f"\nActive canon (include:true):  {len(active)}")
    print(f"Next-batch (include:false):   {len(next_b)}")
    print(f"Total records in file:        {len(albums)}")

    # Step 4: Update _meta
    data["_meta"]["status"] = (
        f"Reconciled v1 canon — {len(active)} albums. "
        f"Post-reconciliation: 48 consensus (both harnesses), "
        f"{'X'} claude_only, {kimi_added} kimi_only. "
        f"{len(next_b)} albums in next-batch."
    )
    data["_meta"]["count"] = len(active)
    data["_meta"]["date"] = str(date.today())
    data["_meta"]["record_shape"] = (
        "Merged one-pass specialist record (canon fields + nested personnel_record). "
        "consensus field: both | claude_only | kimi_only. "
        "include:false = next-batch (not deleted)."
    )

    # Fix _meta status with real counts
    claude_only_active = len([r for r in albums if r.get("include") and r.get("consensus") == "claude_only"])
    kimi_only_active   = len([r for r in albums if r.get("include") and r.get("consensus") == "kimi_only"])
    both_active        = len([r for r in albums if r.get("include") and r.get("consensus") == "both"])
    data["_meta"]["status"] = (
        f"Reconciled v1 canon — {len(active)} albums. "
        f"{both_active} consensus (both harnesses), "
        f"{claude_only_active} claude_only, {kimi_only_active} kimi_only. "
        f"{len(next_b)} albums in next-batch (include:false)."
    )

    with open(CANON_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\n✓ canon-draft.json written")
    print(f"  Active:     {len(active)} (target: 100)")
    print(f"  Next-batch: {len(next_b)}")
    if len(active) != 100:
        print(f"  ⚠ COUNT MISMATCH — expected 100, got {len(active)}")


if __name__ == "__main__":
    main()
