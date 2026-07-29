# A Jazz Canon (repo codename: mccoy-tyner)

Workshop repo: research, the Postgres system of record, and the pipeline that publishes the site.

<intent>
Objective: Curate a personal jazz canon (post-bebop → pre-fusion) as a source-grounded
database, and publish it as a static site.
Outcomes: (1) `_jazzcanon` schema is the sole system of record; (2) every personnel claim
carries an epistemic label and citation; (3) `scripts/ship.sh` regenerates the live site from the DB.
Override: John's `include` verdict and every status transition are human-only.
</intent>

<stack>
- runtime: python 3.11 (`.venv/`), bash, psql
- database: Postgres 16 on vps8-core:5433, schema `_jazzcanon` (pgvector, pg_cron)
- site: separate repo `~/dev/active/jazz-canon` (Svelte + Vite → Cloudflare Pages)
- deploy: `scripts/ship.sh` — export → build → preview pause → wrangler
</stack>

<commands>

| Task | Command |
|------|---------|
| Export contract from DB | `scripts/export.sh` |
| Export + snapshot + commit | `scripts/publish.sh` |
| Full ship | `scripts/ship.sh` (`--go` skips the preview pause) |
| Search the canon | `.venv/bin/python scripts/canon-search.py` |
| Install secret hooks | `pre-commit install` |

</commands>

<gotchas>

- Truth flows DB → export → site. Fix facts in Postgres per `config/edit-contract.md`; never edit data in the `jazz-canon` repo.
- Writes use `_jazzcanon_app`, which has no DELETE grant. Rejection is `canon_status='excluded'`.
- A fact edit updates its epistemic label in the same statement and adds one `edit_log` row.
- The canon = rows where `canon_status='included'` and `site_status IN ('approved','live')`. Everything else stays in the DB, export-invisible.
- Scope = 1940–1979 window (the only gate code enforces). Free jazz, fusion, and ECM opened 2026-07-28 — *gated*, not excluded: each has a specialist, arrivals lean `scope_call`/`contested`, no genre advocacy. Rules in `config/canon-rubric.md`.
- Epistemic labels: `obs` = sourced observation, `inf` = inference, `unk` = unknown or weakly supported.
- Scope commits and pushes to one repo per turn.
- `docs/org-map.md` answers "whose job is this" — read it before restructuring anything.

</gotchas>

<references>
Project docs (read on demand): docs/org-map.md (departments, roles, three rules),
docs/schema.md, docs/personnel-contract.md, docs/conventions.md, docs/follow-ups.md.
Shared knowledge at ~/.claude/references/ — anthropic-best-practices/, contract-principles.md,
agent-teams/.
</references>
