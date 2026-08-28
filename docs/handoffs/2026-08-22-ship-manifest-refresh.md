# Handoff: ship.sh should write the site-repo ship manifest

Date: 2026-08-22
From: mccoy (Hermes)
To: Claude Code

## Context

Batch B ruling (2026-08-21, jazz-canon build): "mccoy ship.sh writes small
ship manifest (date, data checksums, which albums went live)". Never implemented.

Discovered in production 2026-08-22: after a real 10-album ship,
jazz-canon's deploy.sh preflight refused because
`jazz-canon/docs/last-ship-checksums.txt` still held pre-ship hashes.
ship.sh copies the five data files into the site repo
(`scripts/ship.sh` line ~16, the `cp` loop) but nothing refreshes the
manifest. The file was refreshed by hand this once (content verified
against sha256sum of the five files post-ship).

## Ask

In `scripts/ship.sh`, after the copy step and before/around deploy:

1. Write `docs/last-ship-checksums.txt` in the site repo:
   `cd "$SITE" && sha256sum app/public/data/{albums,details,graph,places,people-activity}.json > docs/last-ship-checksums.txt`
   (match the existing two-space sha256sum format and file order:
   albums, details, graph, places, people-activity).
2. Per the Batch B ruling, the manifest should also carry the ship date
   and which albums went live — either extend last-ship-checksums.txt
   into a small manifest (date header + checksums + album ids) or add a
   sibling `docs/last-ship-manifest.txt`. Coordinate the exact shape with
   jazz-canon's deploy.sh preflight expectations before changing what it
   parses. If in doubt: keep last-ship-checksums.txt byte-compatible,
   add the richer data as a new file.

## Why not done in chat

Pipeline code is Claude Code's lane (mccoy SOUL.md scope note).
