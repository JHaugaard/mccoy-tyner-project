# Session Context

## Session Name
transition-to-sites

## Current Focus
Data platform maintenance / gap-fill complete. Phase 4 is done.
Active build work has moved to the **jazz-canon-site** repo.
mccoy-tyner is in **maintenance mode** — new data only via dispatch-ledger.

## What Happened This Session (2026-06-29/30)

### Gap-fill batch 01 — Something Cool (June Christy, 1955)
- Dispatched `jazz-personnel-researcher` agent; full personnel from JazzDisco.org
- 48 musicians, 11 tracks, 167 perf-track links; `track_assignments_complete: true`
- Research file: `research/personnel-batch-gap-fill-01.md`

### Gap-fill batch 02 — Mulligan / Chet Baker Sings / Black Fire
- Gerry Mulligan 1952: Carson Smith + Larry Bunker removed (1953 sessions only);
  correct 4-piece lineup, 8 tracks, all `all-tracks`, no perf-track links needed
- Chet Baker Sings: 4 sessions resolved; Shelly Manne added; Jimmy Bond
  single-performance entry spanning both Jul 56 sessions (unique constraint fix)
- Black Fire: sides assigned A/B; Henderson absent on Subterfuge + Tired Trade;
  Haynes absent on McNeil Island; MBID and Van Gelder/Alfred Lion credits added
- Research file: `research/personnel-batch-gap-fill-02.md`

### Apple Music ID fixes
- Ahmad Jamal *At the Pershing* → `1445769114` ✅
- Jackie McLean *Destination... Out!* → `1442859687` ✅
- Gerry Mulligan 1952 → `1460621783` ✅
- MJQ *Django* → NULL (no standalone Apple Music album) ⛔
- Lee Konitz *Subconscious-Lee* → NULL (1950 Prestige LP absent from catalog) ⛔

### export.py — epistemic_track fix
- Added `t.epistemic_track::text` to track SELECT; 591 obs / 56 inf / 7 unk
- Script physically lives in jazz-canon-site/scripts/; migration to mccoy-tyner decided but not executed

### Waltz for Debby (Bill Evans) — no action needed
- Confirmed 6/6 preview matches against the expanded Apple Music edition
- Title matching works cleanly; link-out lands on expanded edition but data is correct

## DB State (as of 2026-06-30)
- Albums: 100 | Persons: 535 | Performances: 627+
- Apple Music IDs: 97/100 (3 confirmed NULL — Konitz, Django, and one other)
- Preview coverage: 640/666 tracks (jazz-canon-site side)
- Embeddings: all 100 albums

## Key Decisions (standing)
- Data changes: author in mccoy-tyner DB → export.py → jazz-canon-site JSON. Never edit JSON directly.
- Growth loop: fresh JSON batch files in `data/batches/`, not append-with-flags
- Hermes admin profile replaces coded admin site (decided 2026-06-26)
- Slow/iterative execution — no full-automation runs

## Open Items
- Stray `docs/data-pipeline-sop.md` — belongs in jazz-canon-site, not here; safe to delete
- 9 sessions without studio location
- Vocal sub-collection (June Christy, Mel Tormé, Shelly Manne) — deferred
- export.py migration from jazz-canon-site/scripts/ to mccoy-tyner/scripts/ — not yet done

## Phase Status
- Phase 1–4: COMPLETE
- Phase 5 (public app): active in jazz-canon-site
- This repo: maintenance mode
