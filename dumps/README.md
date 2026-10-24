# External source dumps

This directory is the workshop for versioned MusicBrainz and Discogs source artifacts and the enumeration work built from them. Raw dumps are source evidence, not canon data; `_jazzcanon` remains the sole system of record.

## Layout

- `musicbrainz/<snapshot>/` — untouched MusicBrainz `.tar.xz` files and their upstream verification files; gitignored.
- `discogs/<snapshot>/` — untouched Discogs `.xml.gz` files and checksum files; gitignored.
- `work/` — temporary parser output, samples, and staging files; gitignored.
- `manifests/` — small, tracked acquisition manifests recording source URLs, snapshots, byte counts, SHA-256 hashes, licenses, and verification results.

## Rules

Keep raw files unchanged. Verify published checksums after download and again after transfer. Stream compressed input; do not leave full uncompressed XML or JSON entity files in `work/`. Keep at most current and previous raw snapshots, and stop an acquisition or refresh if it would leave vps8 with less than 75 GiB free. Do not commit bulk data. The implementation plan is `research/docs/musicbrainz-discogs-enumeration-plan.md`.
