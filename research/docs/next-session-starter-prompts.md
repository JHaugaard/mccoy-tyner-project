# Starter prompts — next two sessions

Prepared 2026-10-19. Paste either prompt into a fresh McCoy session. Each is self-contained; nothing here assumes the prior conversation.

---

## Session 1 — Jev evaluation and possible integration

McCoy — this session is about evaluating Jev (TypeSafe AI's decision model) and deciding whether it earns any role in the canon pipeline. Read /home/john/dev/active/mccoy-tyner/research/docs/jev-candidate-pool-assessment.md first — it is the study document: what Jev is, the candidate-pool architecture, design principles 1–5 (including harvest window-agnostic, filter at draw time), validation Tests 1–2, risks, and sequencing. Nothing is approved yet and nothing has been built. The first question for this session is Test 1 — the style-agreement trial: run all 292 published albums (ground truth = curated style_primary in _jazzcanon.album) through Jev as an 8-way Choice over our style codes, measure agreement, report only — offline, reversible, no pipeline or DB writes. If that goes well, Test 2 is a citation-audit Noul pass on one archived dossier. Only after both would we discuss the enumeration brief for coder (MusicBrainz JSON dump + Discogs monthly releases dump, CC0 ~10.5 GB, dumps-first, download to the MBP then rsync to vps8, refresh on a slow cadence). Coder has already been informed this exploration exists (Bot Chat, 2026-10-19). Start by walking me through the assessment and your honest read, then we'll rule on Test 1.

---

## Session 2 — Revise the selection report; draft the Note on Methodology

McCoy — this session is document work on /home/john/dev/active/mccoy-tyner/research/docs/how-albums-are-selected.md (committed, with Appends A–C). Two deliverables. (1) Revise the main report to be more objective, less conversational, and remove AI-isms; it remains a private reference for me. Keep the Appends as the dated question log, and add a dated update line to Appendix A: the council roster changed 2026-10-19 (both judges moved openrouter → nous, same models; aggregator gpt-6-luna → gpt-6.1-sol via nous; rehearsal passed with an identical verdict on the same dossier). (2) Then derive the "Note on Methodology" for jazzcanon.com — an academic-in-tone summary of the selection process, linked from the About page but NOT in site navigation, public audience, roughly one page. I will also draw 1–2 paragraphs for the About page and 1–2 sentences for my friends from §11, so keep that section quotable. New formatting convention (ruled 2026-10-19): new documents are one line per paragraph, no hard wrapping — I print them. Commit per the git ritual when done.

---

*Housekeeping note: the canon-drip-operations skill was updated 2026-10-19 with the all-Nous roster change and rehearsal result, so both sessions inherit that context automatically.*
