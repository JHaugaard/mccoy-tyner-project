# Candidate Album Schema

> **Rewritten 2026-07-29.** The original version of this document described the
> Segment-B (June 2026, push-to-100) deliverable: one markdown file per agent run
> containing a source map, JSON blocks, and synthesis notes (`research/<style>-candidates.md`).
> That format is retired. The current deliverable is **one JSON dossier per album**,
> staged by `scripts/stage-candidate.py` one file at a time.

## Current contract

A candidate album is a single JSON file at
`research/candidates-inbox/<id>.json`, where `<id>` is the normalized
`artist-album-year` slug. Top-level fields, as staged by
`scripts/stage-candidate.py`:

| Field | Notes |
|-------|-------|
| `id` | Normalized slug, e.g. `woody-shaw-blackstone-legacy-1970` |
| `artist` | Leader or group name as it should appear |
| `album` | Album title |
| `year` | Original recording year (hard gate: `config/canon-rubric.md` window) |
| `label` | Label name; ECM-family records keep the imprint (`JAPO`, not folded into `ECM`) |
| `catalog_number` | Optional; required for ECM-agent output (stable dedup key) |
| `style_primary` | Must be a code in the `STYLES` dict of `scripts/stage-candidate.py`. Label-only codes (`ecm`) are refused here — tags only |
| `style_tags` | List of style codes; `ecm` belongs here when applicable |
| `rationale` | The case for inclusion (council/judgment text) |
| `priority` | `must_have` etc. per the rubric's priority labels |
| `epistemic` | `obs` / `inf` / `unk` |
| `sources` | Source tokens/URLs backing the claims |
| `personnel_record` | The full five-layer record — **shape owned by `docs/personnel-contract.md`** |
| `ballot` | Council ballot, attached at staging (`--ballot-inline`) |

Newly-opened-gate agents (fusion, free-jazz, ECM) additionally carry their
brief-required fields on the record: `bridge_case` (fusion, free-jazz),
`continuity_case` (ECM), `accessibility` (free-jazz), `scope_flag` (all three,
never empty for opened gates).

## The authoritative pieces

- **Personnel record shape + instrument taxonomy:** `docs/personnel-contract.md`
- **Gathering discipline (sources, conflicts, epistemics):** the
  `album-candidate-dossier` skill (Hermes, mccoy profile)
- **Scope and gates:** `config/canon-rubric.md`
- **Style vocabulary:** `STYLES` in `scripts/stage-candidate.py` (upserted to the
  `style` table on every run)

One contract, one home each — do not restate personnel or scope rules here.

## Archive

Worked examples of complete dossiers live in `research/candidates-archive/`
(e.g. `woody-shaw-blackstone-legacy-1970.json`). The old combined-markdown runs
survive as `research/<style>-candidates*.md` for historical reference only; do
not produce new ones.
