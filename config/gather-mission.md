# Gather Mission Playbook — McCoy's Canon Builder

How a mission ("add N hard-bop candidates from 1961–63", the nightly drip's
"propose 2") runs. McCoy is the lead; children do the research. John edits
this file to change how missions behave.

## The flow

1. **Scope** — read `config/canon-rubric.md` (window + excluded styles are
   hard gates) and `research/cull-notes.md` (standing rejection patterns).
2. **Dedup list** — query the DB for every `album` (id, artist, title, any
   status). A mission candidate matching any row is dead on arrival.
   The nightly drip gets this list precomputed by its precheck script.
3. **Dispatch** — one `delegate_task` child per batch of 1–3 candidate
   albums (toolsets web+file, Kimi). The child prompt MUST include:
   - the candidate-selection brief (genre, era, what gap this mission fills)
   - the full text of `docs/personnel-contract.md` (the record shape,
     sources priority, epistemic rules, instrument taxonomy)
   - the rubric's scope window and excluded styles
   - the dedup exclusion list (ids + artist/title)
   - output instruction: write ONE JSON file per candidate to
     `research/candidates-inbox/<album-id>.json` — the specialist record
     shape (id, artist, album, year, label, style_primary, rationale,
     priority, epistemic, sources[] with a source map, personnel_record).
   Children research with real web sources; a candidate researched from
   model memory is discarded.
4. **Validate** — McCoy checks each inbox file: in-window, not a dup,
   personnel_record present, every claim has a source token, source map
   included. Fails → back to the child (once) or discard with a note.
5. **Judge** — per candidate:
   `~/.hermes/scripts/canon-council.py research/candidates-inbox/<id>.json`
   → ballot JSON. Attach the ballot into the inbox file under `"ballot"`.
6. **Stage** — insert through `_jazzcanon_app` (the staging contract):
   `album` row with `canon_status='candidate'`, `site_status='found'`,
   `canon_tier` + `priority` from the ballot, `inclusion_rationale` from
   the ballot's case_for; personnel/tracks/sessions per the record;
   `source` + `citation` rows (album-level). The inbox JSON file stays —
   it is the raw provenance.
7. **Surface** — one card per candidate to John: artist/title/year, tier,
   priority, case-for, case-against, sources count, personnel summary.
   One keystroke's worth of decision: include / reject / later.

## Verdict handling (John's replies)

- include → `canon_status='included'`, per the edit contract; embedding
  pipeline note: remind John to run `scripts/embed.py` (or run it if
  asked) so search covers the new album.
- reject → `canon_status='excluded'` + reason appended to
  `research/cull-notes.md`.
- later → leave as `found`; it counts against the backlog cap.

## Bounds

- A mission is bounded: never more than 10 candidates per mission unless
  John's dispatch says otherwise; the drip is bounded by the rubric's
  `drip_size` and `backlog_cap`.
- Parallelism: at most 3 concurrent children (delegation config).
- Cost: children run on the Kimi coding plan (zero marginal); the council
  runs per candidate (2 Nous refs + 1 Codex aggregator) — pennies, but
  per-candidate, so don't judge what validation already discarded.
