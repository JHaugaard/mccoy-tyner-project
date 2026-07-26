# McCoy Tyner Project — Conventions

**Version:** 1.2
**Date:** 2026-07-26 (orig. 2026-06-04)

Product name: **A Jazz Canon**. `mccoy-tyner` is the repo codename and stays that way.

This file owns file layout, naming, epistemic discipline, citation format, git, and
environment. It does not restate rules that live elsewhere:

| For | Read |
|-----|------|
| Departments, roles, who-does-what | `docs/org-map.md` |
| Write protocol, whitelisted fields, status transitions | `config/edit-contract.md` |
| Scope gates, drip pace, backlog cap | `config/canon-rubric.md` |
| Tables, columns, views | `docs/schema.md` |
| Dossier record shape | `docs/personnel-contract.md` |

---

## Directory Structure

```
mccoy-tyner/            # the workshop
├── config/         # steering files: canon-rubric.md, edit-contract.md, gather-mission.md
├── data/           # source JSON, schema.sql, album-art/ (binaries ignored, manifest tracked)
├── docs/           # documentation, plans, SOPs, handoffs/, cron-notes/
├── exports/        # generated site contract (albums/details/graph.json) — regenerable
├── research/       # candidate dossiers: candidates-inbox/, candidates-archive/, cull-notes.md
├── scripts/        # pipeline: export.sh, publish.sh, ship.sh, ingest.py, embed.py, …
├── snapshots/      # dated eval snapshots of the contract
├── .venv/          # python 3.11
├── .env.local      # secrets, gitignored (JAZZCANON_DB_URL, JAZZCANON_APP_DB_URL)
└── .env.example    # template
```

The site is a **separate repo**, `~/dev/active/jazz-canon` (Svelte + Vite → Cloudflare Pages).
`scripts/ship.sh` writes into it for you — you should rarely need to be in it by hand.

---

## Naming Conventions

- **Files/directories**: kebab-case (e.g., `canon-draft.json`, `source-penguin-guide.md`)
- **Research compiles**: `source-<name>-compile.md` (e.g., `source-penguin-guide-compile.md`)
- **Data files**: `<entity>-<stage>.json` (e.g., `canon-draft.json`, `personnel-draft.json`)
- **Dates in filenames**: ISO 8601 prefix (e.g., `2026-06-04-canon-synthesis.md`)
- **Migrations**: `migrate-<phase><letter>-<subject>.sql` with a matching `run-migrate-*.sh`

---

## Where Truth Lives

The Postgres `_jazzcanon` schema on `vps8-core:5433` is the system of record. Truth flows one
direction: **DB → export → site.** A fact needing correction is fixed in the database per
`config/edit-contract.md`; the site is regenerated, never hand-edited.

- **Postgres 16**, extensions `vector` (pgvector) and `pg_cron`
- **Roles**: `_jazzcanon_role` owns the schema (DDL, migrations); `_jazzcanon_app` is the
  write surface, deliberately without a DELETE grant; `_jazzcanon_ro` is read-only for
  exports, agents, and search
- **Connection**: `JAZZCANON_DB_URL` (read-only) and `JAZZCANON_APP_DB_URL` (writes) in
  `.env.local`. Parse with Python, not shell grep — passwords may contain `#`.

### Data files

JSON is an **interchange and export format**, not a source of truth. `exports/` and
`snapshots/` are regenerable; `data/` holds source material and original draft artifacts;
dossiers in `research/` are the archival record behind what the DB projects.

- **Encoding**: UTF-8; **indentation**: 2 spaces
- **Album art**: images under `data/album-art/` (git-ignored, regenerable from stored
  MBIDs/URLs); `manifest.json` is tracked. The DB stores paths and metadata, never bytes.

---

## Epistemic Labels (Required on All Research Artifacts)

Every claim in research compiles and data files must carry one of:

| Label | Meaning | Prefix in Notes |
|-------|---------|-----------------|
| `obs` | Direct observation / tool output / source quote | `obs:` |
| `inf` | Inference / reasoned conclusion | `inf:` |
| `unk` | Unknown / absent / weakly supported | `unk:` |

Example:
```markdown
- obs: Penguin Guide lists "Kind of Blue" as 4-star core collection (p. 124)
- inf: This suggests consensus canonical status across jazz critics
- unk: No record of Japanese pressing personnel differences
```

A fact edit in the database carries its label in the same statement: if the source is gone,
the label degrades honestly (`obs` → `inf`/`unk`) rather than the claim standing unsupported.

---

## Source Citation Standard

Every research artifact must include a source map with:

```markdown
## Source Map

| ID | Title | Type | URL | Date Accessed | Notes |
|----|-------|------|-----|---------------|-------|
| S1 | Penguin Guide to Jazz, 10th ed. | Book | — | 2026-06-05 | Core reference |
| S2 | DownBeat Critics Poll 2023 | Web | https://... | 2026-06-05 | Contemporary list |
```

All claims reference source IDs (e.g., `[S1]`, `[S2p45]` for page 45). Citations in the
database are album-level for v1; per-line citation is a deferred additive backfill.

---

## Version Control

- **Repo**: `github.com/JHaugaard/mccoy-tyner-project`
- **Branch**: `master` only (no feature branches for solo work)
- **Commits**: Conventional-ish subject lines (e.g., `Add canon draft from Penguin Guide`)
- **Scope**: one repo per commit and per push. Don't push `mccoy-tyner` and `jazz-canon` in
  the same turn — the site has CI/CD consequences the workshop doesn't.
- **Separate commits** for config/rubric edits (gate moves must be individually auditable),
  and for migrations, script patches, and data backfills.
- **Ritual**: end every canon work session with `git status`; commit what the session touched;
  push to origin.
- **Secrets**: `pre-commit install` once per clone — hooks block `.env*` files and run gitleaks.

---

## Research Compile Workflow

Per the `research-compile` skill (also loaded by the `researcher` subagent):

1. **Scope**: Define question, depth (quick/standard/deep), output path
2. **Gather**: 4–8 quality sources (not exhaustive)
3. **Source notes**: Per-source, with epistemic labels
4. **Compare**: Agreement, disagreement, gaps, terminology drift
5. **Synthesize**: Separate obs / inf / unk explicitly
6. **Recommend**: Vault promotion? Honcho conclusions? Follow-up?

**Gate**: John reviews the artifact before any data enters the database.

Album dossiers are a different lane: McCoy's gather pass writes to `research/candidates-inbox/`
per `config/gather-mission.md`, the canon-council attaches a ballot, and
`scripts/stage-candidate.py` stages the result. The council proposes; it never disposes.

---

## Environment

- **vps8** — Postgres 5433 (system of record), Hermes, Honcho, Syncthing, Caddy
- **vps4** — Ollama, reached from vps8 at `172.18.0.1:11435`. Embeddings are
  `nomic-embed-text` (768-dim) via `scripts/embed.py`, which runs as the `postgres` OS user.
- **Deploy target** — Cloudflare Pages via `scripts/ship.sh` (wrangler, not git). vps2 is no
  longer in this project's path.
- **Secrets** — `.env.local` (gitignored); template in `.env.example`
- **Tooling** — Claude Code is the engineering contractor for schema and pipeline work;
  handoffs land in `docs/handoffs/`. The Claude Code vs. Kimi Code A/B closed 2026-06-25.

---

## Historical: Phase Gates 0–4

The original build phases are complete and their gates closed: conventions approved (0),
~100-album canon confirmed (1), personnel spot-checked (2), schema locked with semantic
search (3), enrichment and ingest finished (4). Retained for provenance; the live protocol is
the status lifecycle in `config/edit-contract.md`. Phase history is in `docs/plan-v2.md`.

---

*Update this file as conventions evolve. Commit changes.*
