<intent>
Goal: A curated, source-grounded collection of ~100 canonical jazz albums spanning post-bebop through pre-fusion (Cool Jazz, Hard Bop, Modal Jazz), with personnel tracked to track level, delivered as an interactive web app that lets me explore album→track→musician relationships — all built through deliberate, deliberate phases where research precedes structure and I learn using Hermes Agent as part of a coding team.

Done when: The web app is live on vps2, queryable by album/musician/track, backed by validated data from ~100 albums with full personnel (primary musicians + production team), and I can hand off the codebase to myself for future maintenance without needing AI assistance to understand it.

Don't: Premature schema lock before Phases 1–3 reveal the data shape; one-shot research without epistemic labeling; building the app before the corpus is settled; letting coding model write code I can't read or modify; skipping John review gates; treating "best of" lists as ground truth without evaluative sorting.

Context: Three-phase time proxy (1940s-1969), no Free Jazz, no rigid genre quotas, Miles/Tyner expected across phases. Research-first: compile ~100 albums from multiple critic/historian sources with source-grounded artifacts, then personnel extraction, then track-level mapping. Hermes orchestrates research and handles the hand-off to the coding phases with John-in-the-loop prompt crafting.

Verify: Phase 0 conventions approved; Phase 1 canon list passes John's taste review (~100 albums); Phase 2-3 personnel data spot-checked on 5-10 albums; Phase 4 schema supports album→track→personnel + musician→albums→tracks queries; Phase 5 architecture doc approved before code; Phase 6 app meets "fun, cool, informative" UX bar on vps2; all code is readable and modifiable by John without AI.
</intent>