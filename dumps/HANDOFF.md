# Handoff: MusicBrainz + Discogs enumeration

Prepared 2026-10-23. This is the entry point for the next session.

## Stable state

- The acquisition/integration plan is `research/docs/musicbrainz-discogs-enumeration-plan.md`, committed and pushed in `e69c827`.
- `dumps/` now exists in the mccoy-tyner repo. Raw MusicBrainz, Discogs, and working artifacts are gitignored; this README/handoff and `manifests/` are tracked.
- Reconnaissance is complete. No bulk dump has been intentionally acquired, no parser or `_canonpool` schema has been built, and there have been no database, drip, cron, export, or site changes.
- vps8 had 278 GiB free when checked. The `postgres` database was 63 MB and `_jazzcanon` 24 MB. The canon had 305 albums across all statuses, 297 with release-group MBIDs and none with release MBIDs.

## Next session: scope review before acquisition

John wants to pause and verify that the plan's scope is correct. Do not begin Stage 1 merely because the plan exists or because the dumps directory was requested. Stage 1 requires John's explicit go-ahead after this review.

Read the plan and `research/docs/jev-candidate-pool-assessment.md`. Review at least these scope choices:

1. The immediate purpose is enumeration, deduplication, and coverage analysis—not recording-session backfill, public republication, or automatic candidate staging.
2. The minimal acquisition is MusicBrainz release-group JSON plus Discogs releases XML, approximately 11.5 GB compressed. Larger MusicBrainz release data and other Discogs entities are deferred unless a demonstrated need justifies them.
3. Raw snapshots remain complete; the normalized pool is jazz-relevant but harvests years window-agnostically. The current canon window and style gates apply only when drawing candidates.
4. `_canonpool` is a rebuildable sibling schema in the existing `postgres` database, with no writes to `_jazzcanon` and no loose-JSON query layer.
5. Acquisition is MBP first, checksum, rsync to `mccoy-tyner/dumps/` on vps8, checksum again. The MBP's free space is still unknown.
6. Refresh is manual and slow, initially quarterly or before a major gap-fill. Full replicas and API enumeration are rejected for this phase; APIs remain available for targeted enrichment.
7. Discogs dump data is CC0. MusicBrainz is mostly CC0 but tags/genres/ratings/annotations are CC BY-NC-SA; those fields stay internal and license-marked. Public reuse is outside the current plan.

## After the review

If John approves the scope, the first execution authorization should be Stage 1 only: acquire the two pinned files, transfer and verify them, and report the manifest plus actual storage. Offline reader proof follows under Coder. Schema creation waits for reader samples and another go-ahead.
