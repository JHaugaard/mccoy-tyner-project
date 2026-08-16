#!/usr/bin/env bash
# run-migrate-6a.sh — wrapper for migrate-6a-studio-name-variant.sql
# Creates _jazzcanon.studio_name_variant (recording-place alias table).
# Schema only — no data is written; run the seed after.
#
# Run from the repo root:  bash scripts/run-migrate-6a.sh
#
# No roles or credentials touched. Superuser is needed only to
# SET ROLE _jazzcanon_role, which owns the schema's tables — and owning the
# table is what puts it in the right grant lane (see the migration header).
set -euo pipefail

cd "$(dirname "$0")/.."

sudo -u postgres psql -p 5433 -d postgres \
  -v ON_ERROR_STOP=1 \
  -f scripts/migrate-6a-studio-name-variant.sql

echo ""
echo "OK — migration 6a applied."
echo "Next: .venv/bin/python3 scripts/seed-studio-name-variants.py --dry-run"
echo "then drop --dry-run to write."
