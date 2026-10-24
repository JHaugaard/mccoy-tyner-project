# MusicBrainz + Discogs enumeration data: acquisition and Postgres plan

Prepared 2026-10-23 by McCoy. Status: recommended plan; no dumps, schema, pipeline, cron, or site changes have been made.

## 1. Recommendation in one paragraph

Download the MusicBrainz release-group JSON dump and the Discogs monthly release XML dump to the MBP, verify them, and rsync the untouched artifacts into versioned directories under `dumps/` in the workshop repo on vps8. Stream-parse them without unpacking the full XML/JSON onto disk. Load only the jazz-relevant, normalized records into a new `_canonpool` schema beside `_jazzcanon` in the existing `postgres` database on vps8:5433. Keep the raw dumps and `_canonpool` fully rebuildable and separate from the curated canon. Do not build full MusicBrainz or Discogs replicas, do not enumerate through their APIs, and do not change the drip until John has reviewed the resulting universe table.

## 2. What was verified on 2026-10-23

### Local capacity and current database

- **obs:** vps8 has 278 GiB available on the single 387 GiB root filesystem. It has 31 GiB RAM and 8 CPU cores.
- **obs:** The `postgres` database is 63 MB. `_jazzcanon` occupies 24 MB including indexes; `_foundry` occupies 49 MB.
- **obs:** `_jazzcanon.album` has 305 rows across all statuses: 297 `included/live`, 7 `candidate/found`, and 1 `excluded/found`. 297 rows have a MusicBrainz release-group MBID; none has a release MBID.
- **obs:** PostgreSQL 16 is running on port 5433. The existing hardware and database configuration are more than sufficient for the proposed distilled pool; no tuning is indicated for this phase.
- **unk:** Free space on the MBP was not checked from vps8. Check it before acquisition.

### Source files for the first pass

| Source | Snapshot observed | File | Compressed size shown by official index | Purpose |
|---|---|---|---|---|
| MusicBrainz | 20261021-001001 | `release-group.tar.xz` | approximately 1 GB | Album-group identity, artist/title/date/type, MBID, relationships, tags/genres |
| Discogs | 20261001 | `discogs_20261001_releases.xml.gz` | 10.5 GB | Release/master IDs, artist/title, label/catno, format, genre/style, dates, tracks and credits |

The first-pass download is therefore approximately **11.5 GB** using the indices' displayed units (**obs**, rounded). MusicBrainz publishes JSON dumps twice weekly; Discogs publishes full monthly replacements. Both publish checksums; MusicBrainz also publishes signatures (**obs**).

The larger MusicBrainz `release.tar.xz` is 23 GB (**obs**). It is not needed for the first pass: release-groups supply the album-level spine, while Discogs supplies label and catalog detail. Add it only if validation demonstrates a need for MusicBrainz release-level disambiguation.

The Discogs masters, artists, and labels dumps are also available (600.5 MB, 475.7 MB, and 87.0 MB respectively in the October snapshot, **obs**). They are optional later additions, not part of the minimal first pass.

### Uncompressed and working footprint

- **obs:** No official uncompressed sizes are published for these files.
- **inf:** The Discogs release XML is likely tens of GB uncompressed. It should be streamed from gzip, never materialized as one XML file or loaded into Postgres `XMLTABLE` as a single document.
- **inf:** Keeping two compressed first-pass snapshots costs about 23 GB. With streaming parsers, modest staging files, and a distilled pool, a 50 GB working budget should be ample. The loader must measure and report actual disk use rather than rely on this estimate.
- **Storage gate:** stop before acquisition or refresh if the operation would leave less than 75 GiB free on vps8. Do not trade away the host's operating headroom merely because the files technically fit.

## 3. Architecture and boundaries

```text
MBP download staging
        │  checksums, then rsync
        ▼
mccoy-tyner/dumps/ raw snapshot dirs (untouched, gitignored artifacts)
        │  streaming parsers; no full uncompressed extraction
        ▼
_canonpool staging schema ──validate──► _canonpool
        │                                  │
        │                                  ├─ MusicBrainz release-group rows
        │                                  ├─ Discogs release rows
        │                                  ├─ dump manifest/provenance
        │                                  └─ deduplicated album-universe rows
        │
        └──────── read-only joins to _jazzcanon for dedup/coverage reports

_jazzcanon remains the sole system of record. The site export is unchanged.
GATHER, council, John’s verdicts, and ship remain unchanged.
```

### Why the same database but a sibling schema

The pool's first job is deduplication and coverage analysis against `_jazzcanon.album`. A sibling schema makes those plain SQL joins while preserving a hard namespace and permission boundary. A separate database would add dblink/FDW plumbing without improving the separation that matters. Loose JSON files would make every consumer reimplement matching and deduplication.

`_canonpool` is derived data: mine, validate, replace. It contains no hand-curated facts and no editorial statuses. The loader role may write `_canonpool` only; it receives no write grant on `_jazzcanon`. Read access for McCoy/the future drip can be granted explicitly. No `_canonpool` row becomes a canon fact merely by being imported.

### Harvest window-agnostic

Apply the standing design rule from `research/docs/jev-candidate-pool-assessment.md`: harvest jazz records without baking the 1945–1985 window into the universe table. Keep year as data and apply the current rubric window only when drawing candidates. The raw dumps remain complete source artifacts; the normalized mining step selects jazz relevance, not the current year gate.

## 4. Licensing and evidentiary limits

- **obs:** Discogs monthly dump data is CC0. Images, user data, and marketplace data are restricted and are outside this plan. Do not fetch Discogs images as part of enumeration.
- **obs:** Most MusicBrainz JSON content is CC0, but each item's `annotation`, `genres`, `ratings`, and `tags` fields are CC BY-NC-SA 3.0. The earlier conversational shorthand that treated the dumps as uniformly CC0 was too loose.
- Keep MusicBrainz tags/genres in the internal, noncommercial pool with their license class recorded in the manifest. This phase does not export them to the public site. Any later public republication of NC-SA-derived material needs a separate attribution/share-alike review.
- **obs:** Discogs is user-generated and supplies no per-field evidence trail. Its release dates are not recording-session dates, and masters group releases rather than performances or takes. MusicBrainz has the same fundamental limitation for this project: it is discography, not sessionography.
- **inf:** These sources are strong for enumeration, identifiers, versions, label/catalog metadata, and research leads. They do not remove the need for live-source GATHER, liner/sessionography checks, epistemic labels, or citations. This project does not become a session database by importing them.

## 5. Execution sequence

### Stage 1 — acquire and verify (McCoy; no Postgres changes)

1. On the MBP, confirm at least 30 GB free and use `dumps/` in the local `mccoy-tyner` checkout as the staging workspace. Thirty GB allows one current set plus a subsequent set without automatic cleanup.
2. Download only the two source files plus their checksum/signature files from the official snapshot URLs. Pin the snapshot names in the manifest; do not use a mutable `LATEST` pointer as the recorded provenance.
3. Do not assume byte-range resume works on the Discogs proxy. Use a resumable client where supported, allow a single-shot download where necessary, and treat checksum verification—not a completed HTTP status—as the completion test.
4. Record source, snapshot, original URL, byte count, SHA-256, license class, and download time in a small tracked manifest under `dumps/manifests/`. Keep the downloaded bytes unchanged.
5. Rsync to `/home/john/dev/active/mccoy-tyner/dumps/<source>/<snapshot>/` on vps8. The raw source directories and `dumps/work/` are gitignored; `dumps/README.md` and `dumps/manifests/` are tracked. Verify SHA-256 again on vps8 and confirm the 75 GiB free-space floor.
6. Keep the MBP copies until vps8 verification is complete. Any later local cleanup is a separate, explicit step, never an automatic part of acquisition.

**Stage 1 deliverable:** two verified raw artifacts on vps8 plus a manifest and actual free-space reading. No database writes.

### Stage 2 — prove the readers offline (Coder; no Postgres changes initially)

1. Read MusicBrainz `.tar.xz` as JSON Lines and Discogs `.xml.gz` with a streaming XML parser. Do not extract the full entity files to disk.
2. Emit counts, malformed-record counts, field-presence reports, runtime, peak memory, actual temporary-disk use, and a small representative sample of jazz rows.
3. Test the readers on small checked-in fixtures before running the full files. Include Various Artists, multi-artist credits, missing/zero years, reissues, compilations, missing catalog numbers, and malformed or incomplete source rows.
4. Use inclusive jazz detection for enumeration and preserve the source's genre/style/tag evidence. Do not use the canon's current style list as a hard harvest filter and do not silently drop ambiguous boundary records.

**Stage 2 acceptance:** the full files stream within the 50 GB working budget, no full uncompressed artifact appears, counts reconcile to the parser logs, and McCoy can inspect real sample rows before any schema is created.

### Stage 3 — build `_canonpool` (Coder; engineering-lane schema work)

1. Create a loader-owned staging schema and a read-only consumer grant. Do not alter `_jazzcanon` tables or roles beyond the intended pool read grant.
2. Load source-specific normalized rows with stable external IDs and dump-snapshot provenance. Build a deduplicated album-universe projection carrying artist, title, year, label/catalog where available, source identifiers, and source genre/style/tag evidence.
3. Match canon rows by exact MBID first, then Discogs master/release relationships, then conservative normalized artist/title/year and label/catalog comparisons. Quarantine ambiguous matches for review; never auto-merge canon identities on a fuzzy score.
4. Deduplicate against every `_jazzcanon.album` status, not only live albums.
5. Build into a new staging generation, validate it, and swap generations only after success. A failed refresh leaves the previous pool intact. The schema is mine-and-rebuild; no hand edits.

### Stage 4 — validate before any consumer changes (McCoy + John)

Technical acceptance:

- Both raw files pass their published SHA-256 checks on MBP and vps8.
- A repeated parse of the same snapshot produces the same normalized counts and universe output.
- Source IDs are unique within their source tables; malformed rows and missing required fields are reported, not silently discarded.
- Actual memory, runtime, disk use, and vps8 free space are recorded.
- `_jazzcanon` canon/site status counts are unchanged; there is no export, ship, deploy, cron, or drip change.

Data acceptance:

- Run all 305 canon albums through the matching report. Separately report exact recovery of the 297 known release-group MBIDs, unmatched/stale MBIDs, the 8 albums without release-group MBIDs, Discogs matches, and ambiguous matches. Do not hide misses behind an aggregate percentage.
- Review a stratified sample of proposed universe rows: familiar canon albums, obscure records, reissues, compilations, Various Artists, boundary genres, and missing-year rows. John reviews the sample before the pool is considered usable for nomination.
- Produce label-by-year and source-coverage reports as omission finders only. They measure catalog coverage, not canonicity.

Fallback:

- If parsing or matching is poor, stop with the raw artifacts and diagnostic reports. Drop only the derived pool generation; the canon is untouched.
- If release-group data cannot resolve necessary version ambiguity, add the 23 GB MusicBrainz release dump as a second iteration. If Discogs master grouping is insufficient, add the masters dump. Do not respond to a first-pass data problem by building full replicas or launching an API crawl.

### Stage 5 — refresh slowly and manually at first

Refresh quarterly or before a major gap-fill, whichever is useful. Both sources are full replacements; hourly MusicBrainz replication and API delta chasing add operational complexity without helping a candidate pool. Keep current and previous raw snapshots until the new generation validates. Do not schedule a cron job until the manual procedure has succeeded repeatedly and John asks for automation.

## 6. Alternatives considered

### Full local replicas — reject for this phase

A full MusicBrainz server/replica and a full relational Discogs import would add large schemas, importer maintenance, version alignment, indexes, replication decisions, and much more storage. They answer questions far beyond enumeration. The official MusicBrainz server route is a distinct application stack, and Discogs supplies no official Postgres importer. The selective JSON/XML route preserves the data we need without acquiring either operational burden.

### API-only enumeration — reject; retain APIs for targeted enrichment

MusicBrainz throttles by source IP at about one request/second; Discogs allows 60 authenticated or 25 unauthenticated requests/minute. Paginated API enumeration would be slow, difficult to reproduce, and incomplete as a coverage spine. Dumps provide stable snapshots and offline joins. Continue using the APIs for current, per-candidate lookups when a dossier needs them.

### A separate adjacent database — reject in favor of a sibling schema

A separate database would make routine pool-to-canon dedup require cross-database plumbing. The sibling schema already supplies the needed rebuild, permission, and export boundaries while keeping joins simple.

## 7. Explicitly outside this plan

No Jev triage, no drip prompt or selection change, no candidate auto-staging, no canon-status changes, no public universe export, no Discogs images, no full MusicBrainz release/Postgres replica, no recording-session backfill, and no automatic refresh. Those are separate decisions after the universe table proves itself.

## 8. Next action

Authorize **Stage 1 only** first: McCoy acquires the two pinned files, transfers and verifies them on vps8, and reports the manifest plus actual storage. With that evidence in hand, hand Coder the bounded Stage 2 reader brief. Schema creation waits for the offline reader samples and John’s go-ahead.

## Official sources checked

- MusicBrainz JSON dump structure, entity files, embedded fields, and per-field licenses: https://musicbrainz.org/doc/Development/JSON_Data_Dumps
- MusicBrainz current JSON snapshot index: https://data.metabrainz.org/pub/musicbrainz/data/json-dumps/20261021-001001/
- MusicBrainz data license: https://musicbrainz.org/doc/About/Data_License
- MusicBrainz PostgreSQL dumps and alternative full-replica route: https://musicbrainz.org/doc/MusicBrainz_Database/Download
- MusicBrainz API rate limits: https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting
- Discogs dump description and CC0 license: https://data.discogs.com/
- Discogs 2026 dump index, dates, and sizes: https://data.discogs.com/?prefix=data%2F2026%2F
- Discogs API formats, authentication, pagination, and rate limits: https://www.discogs.com/developers/
- Discogs API/CC0/restricted-data terms: https://support.discogs.com/hc/en-us/articles/360009334593-API-Terms-of-Use

Internal references: `research/docs/jev-candidate-pool-assessment.md` (enumeration architecture and window-agnostic harvest), `docs/org-map.md` (database and engineering boundaries), `config/edit-contract.md` (canon write boundary), and the 2026-10-23 live database/storage checks described above.
