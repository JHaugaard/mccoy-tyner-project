# Status

_Last updated 2026-08-14, end of the studios-map platform session._

## Where are we?

**The Studios map data work is done, end to end.** The database can now answer
"where was every session recorded, at what coordinates, with what confidence"
— which is what this session existed to make true:

- The 46 messy studio strings (plus one that arrived mid-session with *Seven
  Steps to Heaven*) were researched, ruled on by you item by item, and cleaned
  into **47 canonical places** — every one with a venue kind, a city, a
  documented address or an honest "city-level only" label, and a citation.
  The ruling document is `research/studios-cleanup-worksheet.md`.
- **All 47 places have coordinates**: 34 street-grade (from venue Wikipedia
  pages or geocoded from documented addresses), 13 deliberately-coarse city
  centroids. Nothing invented — four wrong-pin traps were caught and dodged
  along the way.
- The **Van Gelder problem is fixed**: Hackensack and Englewood Cliffs are two
  places now, with ~100 sessions correctly divided at the documented July 1959
  boundary. Three factual errors found and corrected with sources (*Karma* was
  NYC not Hollywood; *Inner Mounting Flame* was NYC not Paris; *The Sermon!*
  was a Manhattan hotel ballroom, not Van Gelder's).
- The exporter now emits **places.json** (46 places — one waits on an album
  still in your review queue), the site session confirmed the contract point
  by point, and the file is landed in the site repo. The `studios` branch over
  there is unparked and building.
- Everything is audited (~170 edit-log rows), committed locally
  (five commits, `54e1865` → `e8ee8f7`), **not yet pushed**.

This was also the first project use of **cross-session messaging** — this
session and the jazz-canon site session coordinated directly (contract
negotiation, verification, forward briefing) with you ruling on decisions but
out of the paste-carrying business. It worked well.

## What's unresolved?

Nothing blocking. The follow-ups live in `docs/follow-ups.md` items 7–12;
the ones that will actually tap you on the shoulder:

- **The ingest pipeline doesn't know any of this happened** (item 7, the big
  one). New albums from the drip still arrive with raw messy studio strings —
  no kind, no coordinates, no canonical matching. Until the gather mission and
  staging script are taught to resolve places at ingest (a spec change needing
  your approval), each new place needs a quick manual ruling.
- **The per-place editorial note** for the site's venue cards ("Rudy Van
  Gelder's parents' living room") awaits a curation pass you'd review — the
  notes column holds good material mixed with internal bookkeeping.
- **One coordinate call is yours to override**: Tristano's home studio address
  is documented but extinct (the block became Kips Bay Towers), so its pin is
  labeled approximate. Flip it back to street-grade if you disagree.
- **Carried from July, still open**: per-musician citations (additive upgrade,
  reminder on file) and rotating the read-only DB password.

## What's next?

If you sat down right now:

1. **Watch the site session build the map** — the platform side owes it
   nothing further; your next involvement there is seeing pins on a screen.
2. **Push the five local commits** when you're ready (`git push` in
   mccoy-tyner; the site repo's places.json commit belongs to that session).
3. **Pore over follow-ups 7–12** as you said you would — item 7 (teach the
   ingest pipeline about places) is the one worth scheduling a session for
   before the drip delivers many more albums.
4. *Heliocentric Worlds Vol. 1* (Sun Ra) is still in your review queue — when
   you rule on it, RLA Studios joins the map automatically.
