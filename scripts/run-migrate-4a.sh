#!/usr/bin/env bash
# run-migrate-4a.sh — wrapper for migrate-4a-ballot-fields.sql
# Adds album.case_for / album.case_against and extends v_album_detail.
# Schema only — no data is written; run scripts/backfill-ballot-fields.py after.
#
# Run from the repo root:  bash scripts/run-migrate-4a.sh
#
# Unlike run-migrate-3b.sh there is no password to generate: this migration
# creates no roles and touches no credentials. Superuser is needed only to
# SET ROLE _jazzcanon_role, which owns album and v_album_detail.
set -euo pipefail

cd "$(dirname "$0")/.."

sudo -u postgres psql -p 5433 -d postgres \
  -v ON_ERROR_STOP=1 \
  -f scripts/migrate-4a-ballot-fields.sql

echo ""
echo "OK — migration 4a applied."
echo "Next: .venv/bin/python3 scripts/backfill-ballot-fields.py --dry-run"
