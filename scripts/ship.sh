#!/usr/bin/env bash
# One transparent command: publish the contract, build the site, (preview),
# deploy to jazzcanon.com, verify. Preview pause is ON by default; pass --go
# to skip it. Data is committed by publish; deploy uses wrangler (not git).
set -euo pipefail

PLATFORM="$(cd "$(dirname "$0")/.." && pwd)"
SITE="$HOME/dev/stable/jazz-canon"
GO=0; case "${1:-}" in --go|--no-preview) GO=1 ;; esac
SHIP_DATE="$(TZ=America/New_York date +%F)"
BATCH_FILE="$(mktemp)"
CHECKSUM_TMP=""
cleanup() {
  rm -f "$BATCH_FILE"
  [ -z "$CHECKSUM_TMP" ] || rm -f "$CHECKSUM_TMP"
}
trap cleanup EXIT
DATA_FILES=(
  app/public/data/albums.json
  app/public/data/details.json
  app/public/data/graph.json
  app/public/data/places.json
  app/public/data/people-activity.json
)
SITE_COMMIT_FILES=(
  app/public/data/recently-added.json
  docs/last-ship-checksums.txt
  app/public/data/places.json
  app/public/data/people-activity.json
)

"$PLATFORM/scripts/publish.sh"

# Same rule as publish.sh's snapshot: everything export.sh writes ships.
# places.json was hand-carried once (site commit f4b92f5) and never wired in.
for f in albums.json details.json graph.json places.json people-activity.json; do
  cp "$PLATFORM/exports/jazz-canon/$f" "$SITE/app/public/data/"
done
echo "✓ Copied contract into site (5 files)"

# The gallery owns this file's shape. The generator validates the whole existing
# document before any write and refuses atomically if that contract has drifted.
DB_URL="$(grep -E '^JAZZCANON_DB_URL=' "$PLATFORM/.env.local" | cut -d= -f2-)"
JAZZCANON_DB_URL="$DB_URL" "$PLATFORM/.venv/bin/python" \
  "$PLATFORM/scripts/recently-added.py" \
  --file "$SITE/app/public/data/recently-added.json" \
  --albums-file "$SITE/app/public/data/albums.json" \
  --batch-output "$BATCH_FILE" \
  --ship-date "$SHIP_DATE"
echo "✓ Recently-added batch generated and validated"

# Apple 30-sec preview URLs are not in the DB — fetch them from iTunes and write
# them into the site's details.json. Best-effort (resilient to per-album misses);
# non-fatal so a network hiccup can't block a ship — but the preview pause below
# is your chance to confirm previews actually play before deploying.
echo "… Enriching Apple previews (iTunes lookup; needs internet)…"
node "$SITE/scripts/enrich-previews.mjs" || echo "⚠ preview enrichment incomplete (non-fatal) — verify at the preview before deploying"
echo "✓ Previews enriched"

# Hash the final bytes that will ship (details.json changes during enrichment).
# Build and verify a temporary manifest before replacing the durable one.
cd "$SITE"
CHECKSUM_TMP="$(mktemp "$SITE/docs/.last-ship-checksums.XXXXXX")"
chmod --reference=docs/last-ship-checksums.txt "$CHECKSUM_TMP"
sha256sum "${DATA_FILES[@]}" > "$CHECKSUM_TMP"
sha256sum --check "$CHECKSUM_TMP"
mv "$CHECKSUM_TMP" docs/last-ship-checksums.txt
CHECKSUM_TMP=""
sha256sum --check docs/last-ship-checksums.txt
echo "✓ Checksum manifest regenerated and verified (5 files)"

# Commit only the tracked ship outputs. --only leaves any unrelated staged or
# dirty work exactly where it was; ignored generated exports remain uncommitted.
if ! git diff HEAD --quiet -- "${SITE_COMMIT_FILES[@]}"; then
  git commit --only -q -m "Ship $SHIP_DATE: refresh site data metadata" -- \
    "${SITE_COMMIT_FILES[@]}"
  echo "✓ Committed tracked site ship outputs"
else
  echo "✓ Tracked site ship outputs unchanged"
fi

cd "$SITE/app"
npm run build >/dev/null
echo "✓ Built site (app/dist/)"

if [ "$GO" -eq 0 ]; then
  echo "… Preview at http://vps8-core:4173 — review it in your browser."
  npm run preview -- --host >/tmp/jazzcanon-preview.log 2>&1 &
  PREV=$!
  trap 'kill "$PREV" 2>/dev/null || true; cleanup' EXIT
  read -rp "Press [Enter] to deploy to jazzcanon.com, or Ctrl-C to abort... "
  kill "$PREV" 2>/dev/null || true
  trap cleanup EXIT
fi

set -a; source "$SITE/.env"; set +a
npx wrangler pages deploy dist --branch main
code="$(curl -s -o /dev/null -w '%{http_code}' https://jazzcanon.com/)"
if [ "$code" = "200" ]; then
  echo "✓ Deployed & verified (HTTP $code) — https://jazzcanon.com"
  # Publication axis: flip exactly the captured batch, not approvals that may
  # have arrived while the build or attended preview was in progress.
  BATCH_COUNT="$(wc -l < "$BATCH_FILE")"
  if [ "$BATCH_COUNT" -ne 0 ]; then
    APP_URL="$(grep -E '^JAZZCANON_APP_DB_URL=' "$PLATFORM/.env.local" | cut -d= -f2- || true)"
    if [ -z "$APP_URL" ]; then
      echo "✗ Batch deployed but JAZZCANON_APP_DB_URL is unavailable; statuses were not flipped" >&2
      exit 1
    fi
    BATCH_CSV="$(paste -sd, "$BATCH_FILE")"
    flipped=$(psql "$APP_URL" -X -q -At -v ON_ERROR_STOP=1 -v batch_ids="$BATCH_CSV" <<'SQL'
WITH requested(id) AS (
  SELECT unnest(string_to_array(:'batch_ids', ','))
), eligible AS (
  SELECT a.id
    FROM _jazzcanon.album AS a
    JOIN requested AS r ON r.id = a.id
   WHERE a.canon_status='included'
     AND a.site_status='approved'
), complete AS (
  SELECT (SELECT count(*) FROM requested) = (SELECT count(*) FROM eligible) AS ok
), f AS (
  UPDATE _jazzcanon.album AS a SET site_status='live'
    FROM eligible AS e, complete
   WHERE complete.ok AND a.id = e.id
  RETURNING a.id
), logged AS (
  INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
  SELECT 'ship.sh', 'album', id, 'site_status', 'approved', 'live', 'published by ship.sh deploy'
    FROM f RETURNING 1
)
SELECT count(*) FROM f;
SQL
)
    if [ "$flipped" -ne "$BATCH_COUNT" ]; then
      echo "✗ Deployed batch/status flip mismatch: expected $BATCH_COUNT, flipped $flipped" >&2
      exit 1
    fi
    echo "✓ site_status: $flipped album(s) approved → live"
  fi
  echo "✓ Done. Data already committed by publish; deploy is not a git act."
else
  echo "✗ Verify FAILED: HTTP $code — check the Cloudflare dashboard / rollback if needed" >&2
  exit 1
fi
