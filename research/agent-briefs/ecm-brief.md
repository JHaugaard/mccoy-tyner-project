# ECM Specialist — Agent Brief

> **Canonical agent:** `~/.claude/agents/jazz-ecm-researcher.md` (self-contained, model-scoped: Opus).
> Written 2026-07-28, alongside the agent — unlike the 2026-06-11 briefs, this one was
> never the operative document. It is the **design record**: why the gate opened, what was
> decided, and what stayed open. The agent file is authoritative on behaviour; when the two
> disagree, the agent file wins and this brief is stale.

## Why this gate opened

ECM is the boundary case John investigated first, and the one he likes best. He framed it
precisely: **"modal jazz after 1970."** It offers a route from the modal and post-bop
tradition into later, more genre-fluid music *without* requiring an immediate leap into
fusion — the preferred middle path, and the reason `year_max` was pushed from 1972 to 1979
before this session (rubric, 2026-07-25).

Keith Jarrett's *The Köln Concert* (1975) is central: one of John's most-listened-to
recordings, possibly his number two after *Kind of Blue*, a record he considers a
masterpiece that must eventually enter the canon.

The gate is the most sympathetic of the three. That is exactly why the agent is built with
the most bias-control machinery.

## The category problem, and how it was resolved

**ECM is a label, not a genre.** This agent is the only specialist in the project organized
around one, and that needed a deliberate ruling rather than a shrug.

ECM 1969–1979 is a **producer's sensibility applied across several styles** — post-bop,
late modal, European chamber jazz, Nordic improvisation, free jazz, and fusion all appear
in the first decade. What unifies them is Eicher's production: recorded space as a
compositional element, decay and silence given weight, chamber-music balance. That is an
aesthetic, and aesthetics are not scope.

**Ruling: the agent owns a *boundary*, not a bin.** The other two new specialists hand it
every ECM release in the window and note it in Gaps; the ECM agent decides whether each
belongs and by what argument.

*Rationale:* without this, *Return to Forever* (1972) gets argued as fusion by one agent and
as late modal by another, with different framings and no shared record — the same album
proposed twice, resolved never. One owner, one framing, one dedup key.

**Corollary, stated explicitly in the agent:** it owns the label, not the aesthetic.
Non-ECM records that sound ECM-ish are out of its scope.

## Design decisions

**1. Judge on continuity, never by label or decade.** The test question is whether the
record extends the post-bebop / modal tradition the canon is built on — the 1960s lineage
reaching forward — with a second half unique to this agent: *would I make the same argument
if the label were not ECM?* Encoded as a **required `continuity_case` field**.

**2. Sympathy is not a licence.** The rubric's opened-gate rules apply here as much as to
the other two: arrivals lean `scope_call` or `contested`, `scope_flag` is never empty. That
John loves one ECM record is not evidence for the other three hundred.

**3. An eighth synthesis section: The House-Sound Check.** The agent names, honestly, which
records in a run it would still have proposed had they appeared on Impulse! or Milestone,
and which are carried partly by the label's aesthetic. Written last, after the records are
chosen, and the records are not to be revised to make it read better.

*Rationale:* this is the central design idea of the agent. ECM's catalogue is the most
internally consistent body of work in jazz, which makes **every** record look defensible.
Over-inclusion is the standing risk, and a bias audit the agent performs on itself is
cheaper than a council that has to perform it every time.

**4. `catalog_number` is a required field.** ECM numbers (ECM 1001, ECM 1050…) are stable
across pressings and reissues and are the most reliable dedup key in the catalogue. No other
specialist has this affordance.

**5. House sources are `obs` for facts and never for merit.** ecmrecords.com is
authoritative that a record exists with those credits on that date; it is not evidence that
the record is good. Same treatment for *Horizons Touched* (the label's own history).
At least two independent sources required per source map, at least one non-house source per
record. The Penguin Guide's well-known affection for ECM is named as a source bias to
declare rather than inherit.

**6. Default run size 8** — between fusion's 6 and the established specialists' 10. The
catalogue is well documented and the continuity case is often genuinely strong; the risk
here is over-inclusion, not scarcity.

**7. Personnel extraction exploits the catalogue.** This is the best-documented body of work
in the project: catalogue number, recording date, studio, and engineer are almost always on
the sleeve. Jan Erik Kongshaug (Rainbow Studio Oslo) and Manfred Eicher as near-constant
producer are recorded rather than dismissed as noise — they are the connective tissue the
label's coherence rests on. Thin personnel on a solo or duo record is stated as fact in
Personnel Coverage, so sparseness does not read as a failed extraction.

**8. Original recording year governs.** ECM has reissued extensively; `year` is the
recording year, with release year noted separately when they differ.

## The window — a deliberate small step

**Scope is ECM 1969–1979 only.** `year_max` stays at 1979.

This was John's explicit choice on 2026-07-28, made from a stated preference for small
steps, with the equally explicit expectation that the end date moves out in the coming weeks
and months. Options considered and declined: raising `year_max` to admit the full ECM canon
(the label's reputation rests heavily on the 1980s and after), and scoping by ECM *aesthetic*
across any label.

The agent is instructed not to argue for moving the ceiling. It may record, without
advocacy, which post-1979 ECM records the sources kept naming — intelligence for when John
does move the line.

Practically, 1969–1979 covers ECM 1001 (Mal Waldron, *Free at Last*) through roughly the
ECM 1100s: Jarrett's solo concerts and both quartets, the Garbarek–Rypdal–Christensen
Nordic axis, Towner and Oregon, Weber, Abercrombie and Gateway, early Corea and Burton,
the first Metheny records, and the late-1970s opening to the AACM and the Ornette diaspora.

## Boundary ownership

| Border | Ruling |
|--------|--------|
| **The modal specialist's prior claim** | `jazz-modal-jazz-researcher` has had standing eligibility for late-modal ECM (Jarrett explicitly) since before this gate existed. Ledger checked first; where a record is arguably either agent's, the modal specialist keeps what it already collected and new seam records carry `overlap_risk`. No re-litigating what is already in the collection. |
| **ECM's fusion edge** | This agent, not `jazz-fusion-researcher` — Return to Forever 1972, Abercrombie *Timeless* 1975 and Gateway, Metheny 1976–79, Rypdal's electric records. The rubric's standing framing of early Pat Metheny Group as the border case (acoustic/swinging/song-form = arguable; electric-rock vocabulary = the exclusion bites) predates the opened gates and remains the right way to argue it. |
| **ECM's free-jazz edge** | This agent, not `jazz-free-jazz-researcher` — *Conference of the Birds* 1972, Marion Brown, Old and New Dreams 1979, the Art Ensemble's ECM sides. Noted that these are usually *more* legible than the same players' work elsewhere, because the ECM production is itself the bridge. That is a real argument and the agent may make it. |
| **ECM New Series** | Contemporary-classical releases with no jazz improvisation are out. Steve Reich's *Music for 18 Musicians* (1978, ECM 1129) named explicitly as the trap. |
| **Sister labels** | Black Saint/Soul Note, Enja — not this agent's unless dispatched. **JAPO is IN** (John, 2026-07-28): an ECM subsidiary inside the 1969–1979 window, catalogued like any ECM release, with the label recorded as `JAPO` rather than folded into `ECM` so the imprint survives in the data. |

## Open questions

- **When `year_max` moves, does this agent's remit move with it automatically?** The agent
  reads the rubric window at run time, so mechanically yes. But the 1980s ECM catalogue is
  a different proposition — larger, further from the modal lineage, and where the label's
  reputation actually sits. Worth an explicit decision rather than an inherited one.
- **JAPO — RESOLVED 2026-07-28.** John ruled JAPO inside this agent's remit; see the
  boundary table above. The label is recorded as `JAPO`, not folded into `ECM`.
- **`catalog_number` — no action needed (verified 2026-07-28).** `scripts/stage-candidate.py`
  already reads `record.get("catalog_number")` off the candidate JSON and writes it to
  `_jazzcanon.album`. Making the field required on this agent therefore feeds an existing
  path rather than creating a new one. Noted here because it was checked, not assumed.
