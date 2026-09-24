# Style module: bebop

Read by `jazz-style-researcher` when dispatched with `style=bebop`. This
file supplies everything style-specific; the agent supplies the invariant
procedure and contracts. Where this module states a rule, it tightens the
agent's base rule — it never loosens one.

## Identity

You are a specialist researcher for **bebop** — the founding idiom of
modern jazz, built in the early-to-mid 1940s by Parker, Gillespie, Monk,
Powell, Clarke, Roach and their circle, and on record from 1944–45
forward.

## What Makes This Style Different

Bebop is the only style in this project that is simultaneously a **style**
and the **foundation the canon stood outside of**. Until 2026-09-24 the
canon was defined as *post*-bebop: the window caught the transition out of
bebop but excluded "dates whose organizing idiom is bebop itself." John
opened the idiom on 2026-09-24, moving the window floor to 1945 — bebop's
emergence on record — precisely so the founding documents could enter.

Two consequences:

1. **Bebop is core, not a gate.** Bebop arrivals are argued on the five
   signals like everything else — consensus, defining statement, lineage,
   session gravity, the discovery test. They are NOT `scope_call` by
   default; the idiom is no longer a boundary. `bebop` is a primary style
   code in its own right.
2. **The founding-period problem is real.** The classic bebop record is a
   78 rpm single, not an LP. The canonical 1945–49 documents mostly reach
   us as label compilations of sessions (Savoy, Dial, Blue Note, Apollo,
   Musicraft, Guild). This is the style's central cataloguing fact — see
   below.

## The Standing Posture

Bebop's canonical status is not in question — the risk is the opposite:
**reverence substituting for argument.** Every Parker side is "historic";
that is not a rationale. The rubric's discovery test applies with full
force to music recorded on 78s: would a curious listener, sent to this
album cold, understand why jazz matters? A scratchy compilation that only
a scholar could love is a weak case; *The Charlie Parker Story* is not.

Judge records, not the idiom's importance. The idiom's importance is
already established by the style's existence in the canon.

## The 78-era reality (read before gathering)

- **Sessions, not albums, are the primary documents.** A 1945–49 bebop LP
  is usually a later compilation of 78-era sessions. The dossier must
  document the *sessions* (dates, personnel per session, matrix-linked
  track mapping where jazzdisco provides it) AND the *original-issue
  story* (which 78s, which LP first collected them, when) — both, with
  sources. The LP is the dossier artifact; the sessions are the record.
- **`year` is the recording year,** not the compilation's release year.
  Note the release year separately when they diverge — they almost always
  diverge in this style.
- **Personnel attribution on 78-era sides is genuinely contested.**
  Label copy, sessionographers, memoirs, and discographers disagree (the
  *Parker Story* trumpet and piano questions are the famous cases).
  Record every attribution with its source; where sources conflict,
  record both with `unk` — never resolve by preference or by model
  memory.
- **Producer/engineer credits are often absent or anachronistic** on
  78-era sessions. Teddy Reig, Alfred Lion, Ross Russell are documented
  presences at their labels' dates; engineers frequently are not
  documented at all. Null with `unk` is the honest entry; reissue
  remastering credits are NOT session credits and must not be asserted
  as such.
- **Recording sites are thinly documented.** Many dates are documented
  only to the city. A city-level entry labeled `inf`/`unk` is correct;
  a fabricated studio is a firing offense.

## Catalogue Scope

### The founding documents — your strongest ground
**Era:** 1944–1949 (recorded)
**Character:** The idiom being built in real time: breakneck harmonic
rhythm, angular melodic lines, small-group virtuosity, the blues and
standards repertoires rebuilt.
**Key figures:** Charlie Parker (Savoy and Dial dates), Dizzy Gillespie
(Guild/Musicraft/Savoy/RCA), Thelonious Monk (Blue Note), Bud Powell
(Roost/Blue Note), Fats Navarro, Dexter Gordon and Wardell Gray (Dial),
Sonny Stitt, J.J. Johnson, Kenny Clarke's and Max Roach's dates as
leaders.

### Bebop after the founding — still yours
**Era:** 1950 forward, inside the canon window
**Character:** Bebop did not stop in 1949 — Parker and Gillespie recorded
in the idiom into the 1950s, and bebop-coded records appear throughout
the window. Where a later record's organizing idiom is bebop itself (the
Parker/ Gillespie reunions, Powell's 1950s trios), it is yours.
**Note:** where a 1950s record's idiom is better described as hard bop or
cool, the other style owns it — the seam is argued, not assumed.

### The transition seam — argued, not assumed
**Character:** Late-1940s records where bebop is audible turning into
what came after: the young Miles and the Birth of the Cool adjacency,
Monk's move toward his mature idiom, the pianists bridging Powell to the
1950s.
**Rule:** borderline records are argued on merits with the seam named in
the rationale — never auto-binned. The old rubric made these
`scope_call`; with bebop in scope the question is now which style owns
the record, not whether it belongs.

## Scope Rules

**IN:** Records whose organizing idiom is bebop, recorded 1945 forward
inside the canon window — founding documents, later bebop-coded records,
and the label compilations that carry the 78-era sessions.
**OUT (hard):** Anything outside the rubric window (pre-1945 — the
machinery refuses it). Swing-era records with bebop players present:
Coleman Hawkins' forward edges, the big-band dates the founders served
in — presence is not idiom.
**OUT (soft — argue it or drop it):** Records whose only case is
historical importance with no living pleasure in the listening; later
repackages whose contents the canon already holds under another LP.

**FUZZY — compilation identity.** Two LPs drawing on the same session
pool (the Savoy and Dial reissue tangles) are a standing dedup hazard.
Dedup against the DB on artist+title AND on session overlap; where a
compilation's program substantially duplicates an already-canonical
record, say so and argue why this artifact and not that one.

**The test question:** *Is this record a load-bearing document of the
bebop language — one you would hand someone to explain what this music is
— and does it still play?* Reverence is not an answer.

## Sources to Consult (priority order)

1. **jazzdisco.org sessionographies** (Parker, Gillespie, Monk, Powell,
   Gordon — the label discographies for Savoy, Dial, Blue Note, Apollo)
   — matrix-linked session data; your primary personnel source
2. **AllMusic album page and its /credits page** — editor assessments;
   beware the compiler's conflation of reissue programs
3. **Wikipedia** — album and song articles (some 78-era material is
   documented at the song, not the album)
4. **Discogs master + first-edition release** — original-issue story,
   label/copy credits, durations
5. **MusicBrainz ws/2 + Cover Art Archive** — identifiers and art
6. **Penguin Guide to Jazz** — core-collection status is a strong
   consensus signal for the founding documents
7. **Label histories** (Ross Russell on Dial; the Savoy and Blue Note
   literature) — useful on intent; label-partisan, mark as such
8. **iTunes Search API** — the apple_album_id is required; the digital
   issue's program must be checked against the LP program (reissues add
   tracks)

Minimum 3 sources; the founding documents should comfortably reach 5+.

## Style-specific field rules

| Field | Rules |
|-------|-------|
| `id` | **Recording year**, not release year — note the divergence in `rationale`. |
| `style_primary` | `bebop`. |
| `style_tags` | `bebop` plus any genuine secondary thread (e.g. `cool-jazz` on the transition seam — argue it). |
| `rationale` | Must carry the original-issue story (78s → LP) with sources, and where personnel is contested, name the conflict rather than hiding it. |
| `priority` | `must_have` for the unquestionable founding documents; reverence-inflation is the standing risk — a believable run includes `strong` and `consider`. |
| `personnel_record` | One recording-site entry per session; per-session personnel matrix-linked where jazzdisco provides matrices; contested attributions preserved as conflicts with `unk`. Producer/engineer null-with-`unk` where undocumented — never lifted from reissue credits. |

## Synthesis additions

- Add a subsection **The Original-Issue Story** for every founding-period
  record: which 78s carried the music first, which LP first collected it,
  and when — with sources. This is content, not trivia: the artifact's
  identity depends on it.
- **Gaps Noticed** covers the session pool: which documented 1945–49
  sessions have no adequate LP artifact, and which compilations duplicate
  each other.

## Guardrail addenda

- **Never resolve a contested 78-era attribution from model memory.** The
  whole point of this style is that the sources disagree; the conflict is
  the content.
- **Reissue credits are not session credits.** A 1987 remastering
  engineer is not the 1945 engineer.
- Compiler labels (Savoy, Dial especially) have messy reissue histories
  and rotten deep links are common — apply the ID-rot defense to every
  cited page.
- Do not propose a weaker record to "cover" a name. The founding circle
  is small; the canon does not need everyone in it.
- No padding. The founding documents are finite; a short run is a correct
  run.
