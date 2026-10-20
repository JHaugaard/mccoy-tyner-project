# Window-extension styles — a reasoned assessment

**Date:** 2026-10-17 · **Author:** McCoy, at John's direction
**Purpose:** prepare the style/taxonomy thinking that the pinned-pane jobs
(MusicBrainz dump, Discogs dump, JEV evaluation) will need, against two
horizons — the live window (1945–1985) and a possible someday window
(1945–present). Every canon-state claim below was verified against the DB
today; dump-vocabulary claims are marked for verification during the dump
jobs themselves.

---

## 1. Where the vocabulary stands (obs)

Seventeen style codes exist in `_jazzcanon.style`. Usage among the 292
included albums:

| code | albums | | code | albums |
|---|---|---|---|---|
| hard-bop | 108 | | fusion | 4 |
| post-bop | 81 | | avant-garde-jazz | 2 |
| cool-jazz | 36 | | jazz-rock | 2 |
| modal-jazz | 31 | | european-jazz | 1 |
| soul-jazz | 11 | | jazz-funk | 1 |
| free-jazz | 8 | | ecm (tag-only) | 0 |
| bebop | 7 | | free-improvisation, loft-jazz, spiritual-jazz, aacm | 0 |

**Two of John's six candidates already exist as codes:** `jazz-funk` and
`spiritual-jazz`. Missing: third stream, chamber jazz, smooth jazz, acid
jazz, nu jazz.

**Live finding — the zero-use codes matter.** Alice Coltrane's devotional
trilogy (*Karma* 1969, *Journey in Satchidananda*, *Ptah, the El Daoud* —
both 1970) currently rides `modal-jazz`. That is defensible — modal IS the
language; spiritual is the frame — but it means `spiritual-jazz` is
vocabulary we minted and never spent. A window-extension conversation is
the right moment to decide whether that code is a display lane or a
recognition label (see §3).

**Live finding — the chamber tendency is already absorbed.** *Focus*
(Getz, 1961) and both MJQ albums ride `cool-jazz`. John's "maybe we
already have chamber jazz implicitly": confirmed (obs) — the question is
whether absorption is *good enough* or hides a distinction worth keeping.

## 2. The structural point the dump work must design for

The style table currently serves two masters without strain:

1. **Display taxonomy** — the site's era ribbons, card hues, and style
   lines. Seventeen codes is already visually rich.
2. **Recognition vocabulary** — what the pipeline can NAME when a source
   (a dossier, a dump row, a JEV signal) carries a genre tag.

Window extension to the present makes these diverge. The dump jobs will
meet thousands of "Smooth Jazz"/"Acid Jazz"-tagged rows that the canon
will never display — but the tooling must still *file* them somewhere.
**Recommendation: design the recognition map as data (a style-map config
file), wider than the display taxonomy, with an explicit `route:` per tag
— `display`, `tag-only` (the ECM precedent), or `park`** (recognized,
mapped, judgment-gated). That keeps future vocabulary moves one-line edits
in the rubric's spirit rather than schema work.

## 3. The six candidates

### jazz-funk — already coded; healthy; no action
Groove-first fusion on funk vamps and electric bass; era ~1970–1985 with a
real post-window continuation (the 1990s soul-jazz revival feeds straight
from it). One album today. The code earns its keep and needs nothing.

### spiritual-jazz — coded; under-spent; decision for John
Devotional, modal/free frame, non-Western color; era 1964–1975 with a
major post-2000 revival (Kamasi Washington's lineage is unthinkable
without Alice). The code exists; its canonical artifacts currently sit in
`modal-jazz`. **Recommendation:** keep the code; put the recode question
(Alice's trilogy → spiritual-jazz) to John as an edit-contract judgment,
not an autonomous sweep. Post-window yield: high.

### third stream — ADD as a primary style (recommendation)
Gunther Schuller's 1957 coinage: composed, notated classical frames
through which jazz improvisation passes — not "classical-flavored jazz"
(timbre) but a written structural argument no blowing session would
produce. Era ~1957–1965; entirely in-window. The canon already holds its
artifacts miscoded: *Focus* (1961) is cool-jazz today; *Jazz
Abstractions* (1961, with Ornette) is the boundary case waiting to be
proposed. **Boundary rule:** third stream owns "notated classical
structure × jazz improvisers"; it loses pure jazz-with-strings (that's
the leader's style + orchestration) and pure chamber intimacy (§below).
**Test question:** *is there a written classical-structure argument here
that a blowing session would not produce?* Gate posture: uncontested —
tradition-internal, pre-fusion. Machinery: one style code (schema-lane
seed via stage-candidate's STYLES dict), one STYLE_INK hue, and a
possible thin era ribbon (1957–1965) — John's design call.

### chamber jazz — TAG, never primary (follows the ECM precedent)
John's instinct is right: we have it implicitly. Chamber jazz names an
instrumentation-and-intimacy stance (MJQ, Chico Hamilton's cello quintet,
the Giuffre trio, much of the ECM catalog), not a period movement with its
own dates. Every strong chamber artifact already has a better primary
home (cool-jazz, european-jazz, ecm-tagged). **Recommendation:**
`chamber-jazz` as a style_tag only — searchable, never displayed as a
lane. This is exactly the precedent ECM set: a label/strength that rides
on records, never claims them.

### smooth jazz — recognition-only for now 😳 (recommendation)
The emoji is earned, but the honest analysis first: smooth jazz is a
radio-format polish on jazz-funk — backbeat-pop production, the soloist
as singer, melody foregrounded over development. Era ~1978–present, so
the window's tail (1980–85) already touches its founding records
(*Winelight* is 1980; Benson's CTI run skirts it). The tradition clause
("load-bearing record of the bebop/post-bebop tradition") would exclude
nearly all of it at council even if dated in-window — the two-layer
defense works here. **Recommendation:** add `smooth-jazz` to the
*recognition map* with `route: park`, hold it out of the display taxonomy
until a genuine candidate forces the question (early Grover Washington
Jr. is the real boundary case; *Mr. Magic* is already jazz-funk's).
Recognition vocabulary ≠ canon membership — the dump must file thousands
of these rows without any of them ever knocking.

### acid jazz — recognition-only; a post-window gate (recommendation)
UK, ~1987–mid-90s: jazz-funk revivalism through hip-hop sampling and
club culture (the Acid Jazz label, Jamiroquai, Brand New Heavies,
Incognito). Zero in-window yield. The tradition link is real but
secondhand — its jazz content is sampled and revived rather than played
forward, though the best bands genuinely played. **Recommendation:**
recognition map, `route: park`; if the window ever opens to the present,
it arrives as a *gated* style (the fusion/free-jazz posture: lean
contested/scope_call, no genre advocacy).

### nu jazz — recognition-only; the post-window gate with the strongest
###   canon-adjacent lineage (recommendation)
~1997–present: electronic production wrapped around live jazz language
(St. Germain, Jazzanova, The Cinematic Orchestra) and, later, the
spiritual-jazz revival it partially carried (Kamasi's *The Epic* is
nu-jazz-adjacent in production and spiritual in soul). Zero in-window.
**Recommendation:** recognition map, `route: park`; gated style if the
window opens. Notable: nu jazz is where spiritual-jazz's post-window
continuation lives — the two codes will need a boundary note then
("devotional content wins over production technique").

## 4. The dump-mapping table (the tooling artifact)

Proposed recognition map skeleton — **verify each left-hand tag against
the live Discogs/MusicBrainz vocabularies inside the pinned-pane jobs**
(unk until then; both vocabularies drift):

| dump tag (Discogs / MB spelling varies) | canon code | route |
|---|---|---|
| Bop | bebop | display |
| Hard Bop | hard-bop | display |
| Cool Jazz | cool-jazz | display |
| Modal | modal-jazz | display |
| Post Bop | post-bop | display |
| Soul-Jazz | soul-jazz | display |
| Free Jazz | free-jazz | display |
| Avant-garde Jazz | avant-garde-jazz | display |
| Fusion | fusion | display |
| Jazz-Rock | jazz-rock | display |
| Jazz-Funk | jazz-funk | display |
| Third Stream | third-stream (proposed) | display |
| Spiritual / Spiritual Jazz | spiritual-jazz | display |
| Chamber Jazz | chamber-jazz (proposed) | tag-only |
| Smooth Jazz | smooth-jazz (proposed) | park |
| Acid Jazz | acid-jazz (proposed) | park |
| Nu Jazz / Nu-Jazz | nu-jazz (proposed) | park |
| Contemporary Jazz | (unmapped — the dump's junk drawer; route: park) | park |

Two warnings from the existing corpus: **(1)** neither dump distinguishes
post-bop from hard bop reliably — date, label and personnel do that work
for us, never the tag; **(2)** dump genre tags are contributor-applied
and follow reissue marketing, so a tag is a lead, never evidence — every
canon claim still needs the dossier's own sources (obs discipline
unchanged).

## 5. Machinery checklist when a code is added (standing recipe)

1. `stage-candidate.py` STYLES dict — the upsert seed IS the DB insert
   (schema-lane / Coder work per org-map).
2. `STYLE_INK` hue in `timeline-layout.ts`; era-ribbon decision (only
   third-stream merits the question among these six).
3. Rubric frontmatter: `excluded_styles` stays empty; gated arrivals lean
   contested per the standing rule.
4. A style module under `config/style-research/` only if the style gets
   a gather lane (none of these six needs one today).

## 6. Summary

| style | recommendation | gate posture |
|---|---|---|
| jazz-funk | already coded; healthy | open |
| spiritual-jazz | keep code; recode question to John | open |
| third-stream | **add as primary style** | uncontested, in-window |
| chamber-jazz | **add as tag-only** (ECM precedent) | n/a |
| smooth-jazz | recognition map, park | judgment-excluded by tradition clause |
| acid-jazz | recognition map, park | gated if window opens |
| nu-jazz | recognition map, park | gated if window opens |

## Open decisions for John

1. Third-stream: add the code now (in-window, artifacts waiting), or hold
   until a candidate arrives? *My recommendation: add now — Focus deserves
   its real name, and the dump jobs benefit from the code existing.*
2. Spiritual-jazz: recode Alice's trilogy from modal-jazz? (Edit-contract
   work, his ruling — the site would show it on the next ship.)
3. The recognition-map-as-data design (`display` / `tag-only` / `park`
   routes): bless the frame before the pinned-pane dump jobs begin?
