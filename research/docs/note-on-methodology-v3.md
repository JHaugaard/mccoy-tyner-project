# Note on Methodology

*Technical process summary for A Jazz Canon. Updated 2026-11-09.*

## 1. Purpose and system of record

A Jazz Canon is a personal, curated collection of jazz albums, not a comprehensive catalog. The current scope is 1945–1985 by original recording or release year. The primary selection test is whether an album is one the curator would hand a friend to explain what this music is.

PostgreSQL (`_jazzcanon`) is the system of record. The public website is a static export. Facts are corrected in the database, never in the exported site data.

## 2. Roles and authority

- **Curator (John):** listens to candidates and issues the only binding verdict: include, exclude, or defer.
- **Builder agent (McCoy):** selects candidates, gathers evidence, and stages complete records; it cannot advance an album beyond `candidate`.
- **Canon council:** two independent AI reviewers and an aggregator produce an advisory ballot; the council has no write or inclusion authority.
- **Publishing pipeline:** exports approved records and deploys the site; it makes no selection decisions.

## 3. Candidate workflow

1. **Precheck.** Read the live rubric and database state. Deduplicate against every album row, regardless of status, and against the known next-batch list. Stop if 10 unreviewed candidates are already queued.
2. **Select and gate.** Select up to two candidates for the daily run. Before research begins, verify the year window, validate the style, and repeat the deduplication check. A failed gate ends work on that candidate.
3. **Gather.** Build a JSON research file from live discographic and reference sources. The target is at least three independent sources per candidate. Model memory is not an accepted source.
4. **Judge.** Two independent reviewers assess the file against the rubric and supply cases for and against inclusion. An aggregator produces a structured ballot containing tier, priority, both cases, and any disagreement. If fewer than two reviewers answer, the run fails and nothing is staged.
5. **Stage.** Insert the album and its related records in one transaction with `canon_status='candidate'` and `site_status='found'`.
6. **Report and wait.** Send the curator the candidate names, queue size, research files, and streaming-availability flags. Automation then stops pending the curator's verdict.

## 4. Research-file contents

Each candidate file contains:

- album metadata and style classification;
- track-level personnel and instruments;
- producer, engineer, and label credits;
- recording dates and sites, with one entry per session date;
- MusicBrainz and Apple identifiers where available;
- cover-art source and provenance;
- a source map with citations and epistemic labels;
- an inclusion rationale, with a specific source for every named accolade.

Every fetched page must match the candidate's artist and album title before it can be cited.

## 5. Evaluation rubric

Candidates are assessed on five signals, in rough order of weight:

1. **Consensus:** repeated appearance across independent guides, polls, and musician lists.
2. **Defining statement:** the record establishes an artist's or scene's sound.
3. **Lineage:** the record influenced later work or made later developments possible.
4. **Session gravity:** the session brought together musicians who define the era.
5. **Living pleasure:** the album offers present-day musical value, not only historical importance.

Boundary cases use a bridge test: the album must connect to the canon's bebop, post-bebop, and modal lineage rather than merely belong to an admissible genre. These cases are normally classified as `contested` or `scope_call`.

## 6. Evidence and data controls

| Label | Meaning |
|---|---|
| `obs` | Directly stated by a named source |
| `inf` | Inferred from documented patterns or neighboring facts |
| `unk` | Missing, weakly supported, or conflicting evidence |

Controls applied throughout the workflow:

- Preserve conflicting claims and explain the conflict; do not silently choose a preferred version.
- Do not invent precision. An undocumented studio remains unknown rather than being replaced by a plausible one.
- Resolve recording sites against canonical place records. Create a new place only when its required identity, location, coordinates, epistemic label, and source are complete.
- Apply the edit contract to every database correction or status change. A fact edit updates its evidence metadata in the same operation and writes an audit-log row.
- Never delete album records. Exclusion retains the research and decision history.

## 7. Verdicts and publication

| Verdict | Result |
|---|---|
| Include | Set `canon_status='included'`; await site approval and publication |
| Exclude | Set `canon_status='excluded'`; retain the complete record and ballot |
| Defer | Keep `candidate`; append a `verdict_deferred` audit entry; do not automatically re-queue |

Record verdicts and status changes in the append-only `edit_log`. Publication occurs only when the curator calls for a ship: approved rows are exported, the static site is built and checked, the site is deployed, and `site_status` changes from `approved` to `live`.

## 8. Known limitations

- Selection from agent recall favors well-known consensus records; targeted gap-fill runs counter this bias.
- Web links, release identifiers, and streaming availability can change or decay. Citations preserve the route for later verification.
- Council output is advisory evidence, not an inclusion decision.

## 9. Current state

*Observed from the database on 2026-11-09: 325 published albums, 1,382 source records, and 1,619 individual citations.*
