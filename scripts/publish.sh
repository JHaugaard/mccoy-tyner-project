#!/usr/bin/env bash
# Publish the canon contract from the system of record, cut a dated eval
# snapshot, and commit both. Deploys nothing — safe to run for evals alone.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

"$ROOT/scripts/export.sh"

DATE="$(date +%F)"
SNAP="$ROOT/snapshots/canon-$DATE"
mkdir -p "$SNAP"
cp "$ROOT/exports/jazz-canon/"albums.json "$SNAP/"
cp "$ROOT/exports/jazz-canon/"details.json "$SNAP/"
cp "$ROOT/exports/jazz-canon/"graph.json "$SNAP/"

URL="$(grep -E '^JAZZCANON_DB_URL=' "$ROOT/.env.local" | cut -d= -f2-)"
counts="$(psql "$URL" -X -q -At -c "SELECT
  'albums='||(SELECT count(*) FROM _jazzcanon.album)||
  ' people='||(SELECT count(*) FROM _jazzcanon.person)||
  ' tracks='||(SELECT count(*) FROM _jazzcanon.track)||
  ' performances='||(SELECT count(*) FROM _jazzcanon.performance)||
  ' track_links='||(SELECT count(*) FROM _jazzcanon.performance_track)")"
printf 'The Jazz Canon — data snapshot\ndate: %s\n%s\n' "$DATE" "$counts" > "$SNAP/MANIFEST"

git add exports/jazz-canon "snapshots/canon-$DATE"
if git diff --cached --quiet; then
  echo "✓ Published — no data change since last publish ($DATE snapshot refreshed)"
else
  git commit -q -m "data: publish canon contract + snapshot $DATE

$counts

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
  echo "✓ Published & committed contract + snapshot ($DATE) — $counts"
fi
