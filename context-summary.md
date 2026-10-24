# Context summary: dumps, a research universe, and targeted expansion

Prepared 2026-10-23 by McCoy, at John's request.

Status: discussion summary for reflection and regrouping. This is not a decision, an approval, or a replacement for the existing acquisition plan. The numbered topics are not a linear progression, and no option below has been selected.

## 1. The immediate decision remains paused

John asked for a scope review before any acquisition and explicitly withheld approval of Stage 1. That gate remains intact.

No MusicBrainz or Discogs dump has been intentionally acquired. No parser, `_canonpool` schema, database object, drip behavior, cron job, export, or site component has been created or changed as part of this discussion. Stage 1 has not started.

The existing plan is `research/docs/musicbrainz-discogs-enumeration-plan.md`; its entry handoff is `dumps/HANDOFF.md`. The related earlier study is `research/docs/jev-candidate-pool-assessment.md`.

The plan's original Stage 1 was deliberately narrow: acquire the MusicBrainz release-group JSON dump and Discogs releases XML dump, approximately 11.5 GB compressed in the observed snapshots; verify them; transfer them to vps8; verify them again; and report the manifest and actual storage. Later stages would prove streaming readers, consider a rebuildable `_canonpool` schema, validate the results, and only then discuss consumers.

## 2. The original purpose was bounded and sound

The original immediate purpose was enumeration, deduplication, and coverage analysis — not recording-session backfill, public republication, Jev triage, automatic candidate staging, or a drip change.

The proposed architecture kept three kinds of data separate:

- Raw source snapshots: complete, immutable, versioned, checksum-verified, and gitignored.
- A derived research pool: normalized, jazz-relevant, rebuildable, and initially stored in `_canonpool` beside `_jazzcanon`, with no write grant on the curated canon.
- The curated canon: `_jazzcanon` remains the sole system of record, with GATHER, council review, John's verdicts, and shipping unchanged.

The pool would harvest year data without baking in the current canon window. The live rubric remains 1945–1985, with its style and continuity judgments applied when candidates are drawn, not when source records are harvested.

The initial scope review found these choices proportionate: two source files rather than full replicas; no API-wide crawl; window-agnostic harvesting; sibling-schema isolation; manual quarterly or need-based refresh; no public reuse; and no larger MusicBrainz or Discogs entities without demonstrated need.

## 3. Clarifications that emerged from the initial review

### Do not equate enumeration with completeness

MusicBrainz and Discogs can provide an external enumeration and coverage spine. They cannot, merely by being downloaded, establish a complete universe of 1945–1985 jazz LPs.

Recall for obscure, regional, privately issued, mistagged, or untagged records is unknown. A tag-dependent jazz filter could reproduce some of the popularity bias that enumeration is meant to reduce.

The safer success definition is “a reproducible external enumeration and coverage spine, with measured limitations,” not “the complete jazz universe.”

### Measure survival through the whole pipeline

Validation should not stop at finding a known MBID in a raw source. For every current `_jazzcanon.album` row, in every status, the report should distinguish:

`present in raw source → retained by jazz harvest → normalized → matched to canon`

This would expose records that are technically present but disappear from the usable pool because of weak source tags or identity handling.

Counts such as 305 albums and 297 release-group MBIDs belonged to the original plan's 2026-10-23 baseline. Acceptance checks should query the then-current database rather than hardcode those numbers.

### Define album identity conservatively

MusicBrainz release-groups, Discogs masters, and Discogs releases are related but not interchangeable. A useful pool must distinguish physical/digital releases, reissues, album identities, compilations, and ambiguous groupings.

Fuzzy artist/title/year matching must not silently merge different albums or sessions. Source rows and their relationships should survive behind any deduplicated projection.

### Keep the MBP route an operational choice, not a doctrine

MBP-first acquisition is acceptable if John wants that staging route, but it is not essential to the data scope. Direct download to vps8 would remove a transfer and one checksum cycle.

If MBP-first remains, the MBP steps need an explicit operator and a free-space check. The documents do not currently explain why MBP-first is preferable or who performs its local steps.

## 4. What the existing canon data actually contains

The current album records are not built only from MusicBrainz and Discogs.

The personnel contract calls for a wider source hierarchy: AllMusic, Wikipedia, Tom Lord's Jazz Discography, JazzDiscography, Discogs, label discographies, digitized liner notes, and artist sessionographies, with MusicBrainz, Apple, and cover-art references gathered opportunistically (`docs/personnel-contract.md`).

Live database checks refreshed while writing this summary showed:

- 307 album rows across all statuses: 297 included, 9 candidates, and 1 excluded.
- 2,110 tracks, 2,274 performance rows, and 552 sessions.
- 2,224 performance-track links, but zero performance-session links.
- 1,205 source rows and 1,435 citations.

These counts describe the database at the time of the check, not a permanent baseline.

The zero performance-session count matters. The existing database supports substantial album and track research, but it does not yet provide session-exact person attribution across the collection. Album-level co-presence must not be presented as proof that two musicians played on the same track or date.

## 5. What the proposed dumps could and could not supply

The two dumps could provide substantial core discographic metadata:

- Artist and title.
- Release dates and external identifiers.
- Release/master/release-group relationships.
- Labels and catalog numbers, principally from Discogs.
- Formats and genre/style/tag evidence.
- Tracklists and some personnel or production credits.

They would not reliably or systematically provide the full current dossier contract:

- Exact recording dates and session-to-track assignments.
- Complete track-level personnel.
- Canonical, sourced recording places.
- Resolution of conflicting personnel or production claims.
- Liner-note and sessionography corroboration.
- Apple identifiers and the cover-art material currently gathered.
- The critical and musical evidence used in a canon ballot.

Some deeper facts may occur incidentally in credits or free-text notes. Incidental presence is not the same as dependable structured coverage.

The dumps therefore could expand the project's broad, shallow holdings dramatically. They could not, by themselves, manufacture thousands of complete canon-quality dossiers.

## 6. John's ambition widened beyond the canon

John's ambition is growing from assembling a listening canon and jazzcanon.com toward research requiring information about many more than the approximately 300 albums already gathered.

That suggests a possible broader purpose for a local pool:

> Build a broad, rebuildable discographic research universe beyond the canon, which can also support candidate enumeration, deduplication, and coverage analysis.

This is a meaningful change in emphasis. The candidate drip would become one possible consumer of a research asset, rather than the sole reason for building it.

Two research layers should remain distinct:

- Discographic research: albums, releases, artists, labels, tracks, identifiers, and source-supplied credits. MusicBrainz and Discogs are directly relevant here.
- Session-exact research: who played on which performance, on which date, at which place, and with what evidence. This requires sessionographies, liner notes, archival artifacts, and potentially union documentation. The dumps are leads, not a complete solution.

A broad local research layer could support musician-by-year and label-by-year maps, first and last observed album appearances, album-level co-presence hypotheses, canon coverage measurements, reissue investigation, and targeted lists for deeper research.

Depth could then follow a genuine research question or canon decision instead of being applied indiscriminately to every available record.

## 7. Local versus merely accessible

For an occasional single-album lookup, remote APIs and web sources are adequate. For repeated universe-wide or artist-wide research, a local normalized collection offers different capabilities:

- Reproducible queries against pinned snapshots.
- Fast joins across musicians, albums, labels, years, and canon rows.
- No API pagination or rate-limit constraint on local analysis.
- Repeatable deduplication and coverage measurements.
- Stable before/after comparisons across refreshes.
- One acquisition and normalization effort reusable across many research questions.
- A local starting point for future dossier research.

Remote-only work preserves freshness and avoids parser/schema maintenance, but it repeats discovery, makes whole-universe queries awkward, and does not naturally produce a stable analytical snapshot.

A hybrid is therefore plausible: local broad data for discovery and analysis, with live targeted lookups for freshness, deeper evidence, and conflict resolution.

Storage is not the primary blocker at the proposed scale. Parser correctness, identity resolution, provenance, validation, and maintenance are the real costs.

## 8. What the Ron Carter example revealed — without making Carter the architecture

Ron Carter was an illustrative stress test, not a prescribed project center.

A live check during the discussion found Carter on 37 database album rows spanning 1960–1975: 36 included albums and one album in another status. None currently has him as `leader_person_id`. That is a statement about this collection's selection history, not about Carter's career.

John's roughly 2,150-album shortfall remains an external estimate, not a verified comparison. Before using it as a coverage denominator, the counting unit must be settled:

- Physical/digital releases, including reissues.
- Album identities after master/release-group deduplication.
- Albums carrying any Carter credit.
- Distinct performances or recordings carrying his credit.
- Original recording sessions.

Those counts are not interchangeable.

The phrase “Ron Carter research discography” is therefore clearer than “Ron Carter canon.” Canon remains John's curated judgment; a research discography can aspire to comprehensive coverage without implying canonicity.

### The sideman-visibility problem

MusicBrainz release-group data is strongest for primary album identity and lead artist. It will not expose every album on which Carter appeared as a sideman.

Discogs release data is more promising because it can contain supporting release and track credits, but recovery will only be as complete as those credits.

Unknown until measured: how many Carter appearances the two dumps recover, how many distinct album identities they represent, how often credits are missing or hidden in notes, and whether additional MusicBrainz release/recording data or another discography would materially improve recovery.

Carter therefore makes a useful person-centric recall pilot, not a guaranteed demonstration that the minimal dumps can produce a complete sideman discography.

### The jazz-filter problem

If “entire” includes non-jazz studio work, a normalized pool restricted to jazz relevance could omit part of a musician's career even though the raw dumps remain complete.

A future research layer might need designated person-centric slices in addition to jazz relevance. That is a scope question, not yet a rule.

## 9. The possible drip springboard

A future flow could be:

`local pool → candidate selection → prefilled research stub → GATHER verifies and deepens → council → John's verdict`

A local stub might supply artist/title/year candidates, identifiers, labels/catalog numbers, source genre evidence, track titles and durations, some credits, known ambiguities, and dedup status against every existing album status.

GATHER could then concentrate on exact recording dates and places, session-to-track assignments, complete track-level personnel, reissue and bonus-track contamination, conflicting credits, liner/sessionography evidence, critical consensus, Apple and cover-art references, and the canon argument.

Whether this would supply 50% of dossier information is unknown. Even 50% of fields would not necessarily mean 50% of research time: the pool may supply easy metadata while leaving the difficult session and personnel work.

There is also an anchoring risk. A researcher receiving a prefilled stub may trust its errors instead of independently investigating. A stub must remain visibly provisional, carrying snapshot provenance, source record identifiers, and unresolved flags. “Observed in Discogs” must not silently become “verified against primary recording artifacts.”

Any prefill role requires a bounded evaluation against archived dossiers and human spot-checks, measuring correct completion, reissue contamination, personnel coverage, conflicts, external lookups, and research time. Using the pool for research, using it for candidate selection, and using it for dossier prefill are separate future decisions.

## 10. The alternative John raised at the end of the discussion

After considering the infrastructure burden and the uncertainties, John raised a genuine alternative: perhaps the dumps are unnecessary, and modified, more expansive but targeted forms of the existing drip approach could suffice.

Examples included two albums per day, a directed batch of 50 next week, or a bounded mission such as all of one musician's 1945–1985 work.

This is not a retreat into the old recall-only drip. It is a choice between general infrastructure and directed, source-grounded research missions.

### Potential benefits of targeted missions

- The research question and boundary are explicit from the outset.
- Existing GATHER practices can produce sourced, epistemically labeled records immediately.
- No bulk acquisition, streaming parser, rebuildable schema, or quarterly refresh obligation is required.
- Artist sessionographies and label discographies may provide better depth than general release dumps for the chosen question.
- Work products can be shaped directly for the intended research use rather than for a general pool.
- A directed batch need not alter the standing nightly two-album drip.

### Costs and blockers of targeted missions

- “All of musician X” still requires an external target list; the mission must enumerate before it can claim coverage.
- Discovery and normalization may be repeated for each new musician, label, or scene.
- Targeted work does not by itself create a general queryable universe or broad canon-coverage map.
- Without a stable source snapshot, repeating exactly the same coverage analysis can be harder.
- A large dossier batch can consume substantial research and human review capacity.
- A research batch of 50 and 50 new canon candidates are not the same deliverable. The latter would collide with the deliberate review tempo and backlog discipline unless John explicitly structures it otherwise.
- Artist-by-artist missions can retain a form of nomination bias: the project learns deeply about chosen subjects while leaving unchosen subjects unmeasured.

## 11. Three broad architectures now visible

### A. Build the dump-backed research universe

Acquire the two dumps, build and validate the broad shallow pool, and deepen selectively.

Best fit if John expects recurring, cross-cutting research across many musicians, labels, years, and canon gaps, or wants reusable local prefill for future gathering.

Main risk: substantial infrastructure is built before the actual research questions demonstrate a need for it; completeness and sideman recovery remain uncertain.

### B. Do not acquire dumps; commission targeted research missions

Use artist sessionographies, label discographies, APIs, and existing web GATHER to answer bounded questions one at a time.

Best fit if the real need is deep answers to specific questions rather than a standing general research layer.

Main risk: repeated discovery, inconsistent snapshots, and no broad universe beneath the individual projects.

### C. Defer the dumps and run a bounded requirements-discovery mission

Choose one concrete research question, define its desired output and completeness measure, and perform a limited targeted pilot. Use the experience to determine whether a general local pool would have saved meaningful effort or enabled otherwise impractical queries.

Best fit if John wants evidence about his own research workflow before committing to general infrastructure.

Main risk: a badly chosen pilot could be too small to reveal the value of a pool or too broad to remain a cheap test. No pilot has been designed or authorized.

These options are not mutually exclusive over the life of the project. The practical question is sequencing, not permanent ideology.

## 12. Questions that may help John regroup

1. Is the primary objective a reusable research infrastructure, or timely answers to bounded research questions?
2. What questions does John want to ask that the current approximately 300-album database cannot answer?
3. Are those questions album-level, release-level, track-level, or session-exact?
4. How broad should the next collection be: one musician, one label, one scene, all jazz, or cross-genre work involving selected musicians?
5. What would “complete” mean for that collection, and what independent source could measure the denominator?
6. Is a broad shallow collection valuable in its own right, or is it only valuable if it accelerates full dossiers?
7. How much repeated targeted discovery is acceptable before a shared local pool becomes the simpler option?
8. Should the next research batch produce reference artifacts, dossier-quality records, candidate stubs, or actual canon candidates?
9. Is local reproducibility important enough to justify acquisition and parser maintenance?
10. If a pool were built, which concrete consumer should prove its value first: research queries, coverage reports, candidate selection, or dossier prefill?

## 13. Present status and no-decision zone

No scope has been approved and no acquisition has been authorized.

No option in this summary has been selected. In particular, John has not chosen a dump-backed universe, a targeted-mission-only approach, a Carter project, a 50-album batch, a drip modification, or dossier prefill.

The nightly drip's two-candidate pace and John's control of inclusion remain unchanged. Directed bulk missions and canon-candidate review should remain conceptually separate from general research collection.

The most useful next step, when John is ready, is likely to clarify the research output he wants before deciding whether MusicBrainz and Discogs dumps are the right means. Nothing needs to be acquired to have that conversation.

## Documents and live evidence informing this summary

- `dumps/HANDOFF.md`
- `research/docs/musicbrainz-discogs-enumeration-plan.md`
- `research/docs/jev-candidate-pool-assessment.md`
- `docs/personnel-contract.md`
- `docs/org-map.md`
- `config/canon-rubric.md`
- Read-only `_jazzcanon` queries made during the discussion and refreshed on 2026-10-23 for the figures in Sections 4 and 8.
