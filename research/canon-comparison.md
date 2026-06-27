# Canon Album Comparison — Claude Code vs. Kimi Code

Artist — *Album* only. Generated 2026-06-23 from `data/canon-draft.json` (Claude, 105) and `mccoy-tyner-kc/research/phase4-albums/*.json` (Kimi, 100).

Matching is on normalized artist + title (case, punctuation, leading "The" ignored). Year differences between the two builds do **not** affect matching here — title only.

## At a glance

| | Count |
|---|---|
| Claude total | 105 |
| Kimi total | 100 |
| **In both** | **48** |
| Claude only | 57 |
| Kimi only | 52 |
| Union (distinct) | 157 |

## In both (48)

- Andrew Hill — *Point of Departure*
- Art Blakey & the Jazz Messengers — *Moanin'*
- Art Pepper — *Art Pepper Meets the Rhythm Section*
- Bill Evans — *Portrait in Jazz*
- Bill Evans — *Waltz for Debby*
- Bobby Hutcherson — *Dialogue*
- Cannonball Adderley — *Somethin' Else*
- Chet Baker — *Chet Baker Sings*
- Clifford Brown & Max Roach — *Study in Brown*  ·  _Kimi:_ Clifford Brown and Max Roach — *Study in Brown*
- The Dave Brubeck Quartet — *Time Out*
- Dexter Gordon — *Go*  ·  _Kimi:_ Dexter Gordon — *Go!*
- Donald Byrd — *A New Perspective*
- Freddie Hubbard — *Hub-Tones*
- Freddie Hubbard — *Ready for Freddie*
- Gil Evans — *New Bottle Old Wine*
- Grant Green — *Idle Moments*
- Hank Mobley — *Roll Call*
- Hank Mobley — *Soul Station*
- Herbie Hancock — *Empyrean Isles*
- Herbie Hancock — *Maiden Voyage*
- Horace Silver — *Song for My Father*
- Jackie McLean — *Let Freedom Ring*
- Jimmy Giuffre — *The Jimmy Giuffre 3*
- Jimmy Smith — *Back at the Chicken Shack*
- Jimmy Smith — *The Sermon!*
- Joe Henderson — *Inner Urge*
- Joe Henderson — *Mode for Joe*
- Joe Henderson — *Page One*
- John Coltrane — *A Love Supreme*
- John Coltrane — *My Favorite Things*
- Kenny Burrell — *Midnight Blue*
- Kenny Dorham — *Una Mas*
- Lee Konitz — *Subconscious-Lee*
- Lee Morgan — *The Sidewinder*
- Lennie Tristano — *Lennie Tristano*
- Lou Donaldson — *Alligator Bogaloo*
- McCoy Tyner — *The Real McCoy*
- Miles Davis — *Birth of the Cool*
- Miles Davis — *E.S.P.*
- Miles Davis — *Kind of Blue*
- The Modern Jazz Quartet — *Django*
- Sonny Clark — *Cool Struttin'*
- Sonny Rollins — *Saxophone Colossus*
- Stan Getz — *Focus*
- Stan Getz — *West Coast Jazz*
- Wayne Shorter — *Adam's Apple*
- Wayne Shorter — *JuJu*
- Wayne Shorter — *Speak No Evil*

## Interesting divergences — same artist, different albums (26 of 36 shared artists)

Both builds canonized this artist but picked a different slice of their catalog. This is taste forking *within* an agreed artist — the sharpest A/B signal, since source access and scope are held constant and only judgment differs.

**Andrew Hill**  
- both: Point of Departure  
- _Kimi only:_ Black Fire  

**Art Pepper**  
- both: Art Pepper Meets the Rhythm Section  
- _Claude only:_ Art Pepper + Eleven – Modern Jazz Classics  

**Bill Evans**  
- both: Portrait in Jazz; Waltz for Debby  
- _Claude only:_ Everybody Digs Bill Evans; Explorations; Sunday at the Village Vanguard  
- _Kimi only:_ Conversations with Myself  

**Cannonball Adderley**  
- both: Somethin' Else  
- _Claude only:_ The Cannonball Adderley Quintet in San Francisco  
- _Kimi only:_ Mercy, Mercy, Mercy! Live at "The Club"  

**Chet Baker**  
- both: Chet Baker Sings  
- _Claude only:_ Chet Baker & Crew  

**Clifford Brown & Max Roach**  
- both: Study in Brown  
- _Claude only:_ Clifford Brown and Max Roach  
- _Kimi only:_ Clifford Brown and Max Roach at Basin Street  

**Dexter Gordon**  
- both: Go  
- _Claude only:_ Our Man in Paris  
- _Kimi only:_ A Swingin' Affair  

**Freddie Hubbard**  
- both: Hub-Tones; Ready for Freddie  
- _Kimi only:_ Breaking Point!  

**Gil Evans**  
- both: New Bottle Old Wine  
- _Claude only:_ Gil Evans & Ten  
- _Kimi only:_ Out of the Cool  

**Grant Green**  
- both: Idle Moments  
- _Kimi only:_ Born to Be Blue; Grant's First Stand; Green Street  

**Herbie Hancock**  
- both: Empyrean Isles; Maiden Voyage  
- _Claude only:_ Speak Like a Child  

**Horace Silver**  
- both: Song for My Father  
- _Claude only:_ Blowin' the Blues Away; Horace Silver and the Jazz Messengers  

**Jackie McLean**  
- both: Let Freedom Ring  
- _Claude only:_ Bluesnik  
- _Kimi only:_ Destination... Out!  

**Jimmy Giuffre**  
- both: The Jimmy Giuffre 3  
- _Claude only:_ The Jimmy Giuffre Clarinet  

**Jimmy Smith**  
- both: Back at the Chicken Shack; The Sermon!  
- _Kimi only:_ Midnight Special  

**John Coltrane**  
- both: A Love Supreme; My Favorite Things  
- _Claude only:_ "Live" at the Village Vanguard; Africa/Brass; Ballads; Blue Train; Coltrane; Crescent  
- _Kimi only:_ Giant Steps  

**Lee Konitz**  
- both: Subconscious-Lee  
- _Claude only:_ Lee Konitz Plays with the Gerry Mulligan Quartet; Lee Konitz with Warne Marsh  

**Lee Morgan**  
- both: The Sidewinder  
- _Claude only:_ The Cooker  
- _Kimi only:_ Search for the New Land  

**McCoy Tyner**  
- both: The Real McCoy  
- _Claude only:_ Expansions; Sahara; Tender Moments  

**Miles Davis**  
- both: Birth of the Cool; E.S.P.; Kind of Blue  
- _Claude only:_ Miles Ahead; Miles Smiles; Nefertiti  
- _Kimi only:_ In a Silent Way; Milestones; Porgy and Bess  

**Shorty Rogers**  
- _Claude only:_ Martians Come Back!; Shorty Rogers and His Giants  
- _Kimi only:_ Cool and Crazy  

**Sonny Clark**  
- both: Cool Struttin'  
- _Kimi only:_ Leapin' and Lopin'  

**Sonny Rollins**  
- both: Saxophone Colossus  
- _Claude only:_ Way Out West  
- _Kimi only:_ The Bridge  

**The Dave Brubeck Quartet**  
- both: Time Out  
- _Claude only:_ Jazz at Oberlin  
- _Kimi only:_ Jazz Goes to College  

**The Modern Jazz Quartet**  
- both: Django  
- _Claude only:_ Fontessa  
- _Kimi only:_ Concorde  

**Wayne Shorter**  
- both: Adam's Apple; JuJu; Speak No Evil  
- _Claude only:_ Night Dreamer; The All Seeing Eye  
- _Kimi only:_ The Soothsayer  

_Shared artists where both picked the exact same album(s):_ Art Blakey & the Jazz Messengers, Bobby Hutcherson, Donald Byrd, Hank Mobley, Joe Henderson, Kenny Burrell, Kenny Dorham, Lennie Tristano, Lou Donaldson, Stan Getz.

## Claude only (57)

- Art Blakey Quintet — *A Night at Birdland, Vol. 1*
- Art Pepper — *Art Pepper + Eleven – Modern Jazz Classics*
- Barney Kessel — *The Poll Winners*
- Bill Evans — *Everybody Digs Bill Evans*
- Bill Evans — *Explorations*
- Bill Evans — *Sunday at the Village Vanguard*
- Bob Brookmeyer — *The Dual Role of Bob Brookmeyer*
- Cannonball Adderley — *The Cannonball Adderley Quintet in San Francisco*
- Charles Lloyd — *Forest Flower*
- Chet Baker — *Chet Baker & Crew*
- Chick Corea — *Now He Sings, Now He Sobs*
- Chico Hamilton — *Chico Hamilton Quintet featuring Buddy Collette*
- Clifford Brown & Max Roach — *Clifford Brown and Max Roach*
- The Dave Brubeck Quartet — *Jazz at Oberlin*
- Dexter Gordon — *Our Man in Paris*
- Gene Ammons — *Boss Tenor*
- Gerry Mulligan Quartet — *Gerry Mulligan Quartet*
- Gerry Mulligan Quartet — *What Is There to Say?*
- Gil Evans — *Gil Evans & Ten*
- Herbie Hancock — *Speak Like a Child*
- Horace Silver — *Blowin' the Blues Away*
- Horace Silver — *Horace Silver and the Jazz Messengers*
- Howard Rumsey's Lighthouse All-Stars — *Sunday Jazz a la Lighthouse, Vol. 1*
- Jackie McLean — *Bluesnik*
- Jimmy Giuffre — *The Jimmy Giuffre Clarinet*
- John Coltrane — *Africa/Brass*
- John Coltrane — *Ballads*
- John Coltrane — *Blue Train*
- John Coltrane — *Coltrane*
- John Coltrane — *Crescent*
- John Coltrane — *"Live" at the Village Vanguard*
- John Lewis — *Grand Encounter: 2° East / 3° West*
- June Christy — *Something Cool*
- Keith Jarrett — *The Köln Concert*
- Larry Young — *Unity*
- Lee Konitz — *Lee Konitz Plays with the Gerry Mulligan Quartet*
- Lee Konitz — *Lee Konitz with Warne Marsh*
- Lee Morgan — *The Cooker*
- McCoy Tyner — *Expansions*
- McCoy Tyner — *Sahara*
- McCoy Tyner — *Tender Moments*
- Mel Tormé — *Mel Tormé and the Marty Paich Dek-Tette*
- Miles Davis — *Miles Ahead*
- Miles Davis — *Miles Smiles*
- Miles Davis — *Nefertiti*
- The Modern Jazz Quartet — *Fontessa*
- Paul Desmond — *Take Ten*
- Shelly Manne — *My Fair Lady*
- Shorty Rogers — *Martians Come Back!*
- Shorty Rogers — *Shorty Rogers and His Giants*
- Sonny Rollins — *Way Out West*
- Stan Kenton — *Contemporary Concepts*
- Tina Brooks — *True Blue*
- Wayne Shorter — *The All Seeing Eye*
- Wayne Shorter — *Night Dreamer*
- Wes Montgomery — *Full House*
- Wes Montgomery — *The Incredible Jazz Guitar of Wes Montgomery*

## Kimi only (52)

- Ahmad Jamal — *At the Pershing: But Not for Me*
- Andrew Hill — *Black Fire*
- Art Farmer — *Farmer's Market*
- Baby Face Willette — *Face to Face*
- Benny Golson — *The Other Side of Benny Golson*
- Bill Evans — *Conversations with Myself*
- Blue Mitchell — *The Thing to Do*
- Booker Little — *Out Front*
- Brother Jack McDuff — *The Honeydripper*
- Cannonball Adderley — *Mercy, Mercy, Mercy! Live at "The Club"*
- Charles Mingus — *The Black Saint and the Sinner Lady*
- Charles Mingus — *Blues & Roots*
- Charles Mingus — *Mingus Ah Um*
- Charles Mingus — *Mingus Mingus Mingus Mingus Mingus*
- Clifford Brown & Max Roach — *Clifford Brown and Max Roach at Basin Street*
- The Dave Brubeck Quartet — *Jazz Goes to College*
- Dexter Gordon — *A Swingin' Affair*
- Eddie "Lockjaw" Davis & Johnny Griffin — *Blues Up & Down*
- Eric Dolphy — *Far Cry*
- Eric Dolphy — *Out to Lunch!*
- Freddie Hubbard — *Breaking Point!*
- Gerry Mulligan — *Mulligan Plays Mulligan*
- Gerry Mulligan & Chet Baker — *The Best of the Gerry Mulligan Quartet with Chet Baker*
- Gil Evans — *Out of the Cool*
- Grant Green — *Born to Be Blue*
- Grant Green — *Grant's First Stand*
- Grant Green — *Green Street*
- Ike Quebec — *Blue & Sentimental*
- Jackie McLean — *Destination... Out!*
- Jimmy Smith — *Midnight Special*
- John Coltrane — *Giant Steps*
- Johnny "Hammond" Smith — *Open House!*
- Lee Morgan — *Search for the New Land*
- Max Roach — *Deeds, Not Words*
- Miles Davis — *In a Silent Way*
- Miles Davis — *Milestones*
- Miles Davis — *Porgy and Bess*
- The Modern Jazz Quartet — *Concorde*
- Oliver Nelson — *The Blues and the Abstract Truth*
- The Ramsey Lewis Trio — *The In Crowd*
- Red Garland — *Rojo*
- Richard "Groove" Holmes — *Soul Power!*
- Sam Rivers — *Fuchsia Swing Song*
- Shirley Scott — *Soul Sister*
- Shorty Rogers — *Cool and Crazy*
- Sonny Clark — *Leapin' and Lopin'*
- Sonny Rollins — *The Bridge*
- Sonny Stitt — *Sonny Stitt Plays Arrangements from the Pen of Quincy Jones*
- Stanley Turrentine — *Blue Hour*
- Stanley Turrentine — *Sugar*
- Wayne Shorter — *The Soothsayer*
- Wynton Kelly — *Kelly Blue*

## Reconciliation — a take

### The shape of the disagreement
The two builds agree on **48 albums** and each carries ~50 the other lacks — a **157-album union**.
But the divergence is not random noise: of the **36 artists both canonized**, only a handful agreed on
the exact album set. The rest forked on *which* record represents the artist — e.g. Coltrane (Claude
took 6 more, including *Blue Train*, *Crescent*, *Ballads*; Kimi added *Giant Steps*), Bill Evans, Miles,
Grant Green, Wayne Shorter. That tells us the real action is **depth-of-catalog judgment**, not
"who's in the canon." Both models know the canon; they disagree on how many records per giant earns a slot.

### Options

**A. Start from the 157-union (recommended as the base).**
Treat the union as the candidate pool, not the final canon. Rationale: the experiment's durable asset is
the *personnel records*, and a union maximizes coverage while costing nothing to narrow later (membership
is the cheap, reversible layer — your own locked principle). You then run **one human pass** over the
~109 non-overlapping titles to accept/cull. This keeps both harnesses' discoveries on the table.

**B. Intersection-48 as a "high-confidence core," union as the long tail.**
Tier the canon: 48 albums both models independently chose = consensus core (highest curation confidence);
the 109 singletons = contested tier awaiting your gate. This mirrors the orchestrator's
consensus/contested ballot you already use — it just sources the two "voters" from two *harnesses*
instead of two genre agents.

**C. Pick a winner per forked artist.**
For each of the ~25 forked artists, decide how many records that artist deserves and which. More work,
but it's the cut that actually resolves the "depth" disagreement rather than deferring it.

### My recommendation
**Do B's tiering on top of A's union.** Concretely:
1. **Adopt the 157 union as the working candidate set.** Nothing is discarded yet.
2. **Tag each record with a `consensus` field:** `both` (48) / `claude_only` (57) / `kimi_only` (52).
   This is a 10-minute mechanical pass and it makes the A/B legible inside the data itself.
3. **Gate the singletons in artist-clusters, not flat.** Review Coltrane's 7-vs-Kimi's-1 as *one*
   decision ("how many Coltranes?"), not seven. The forked-artist section above is already that worklist.
4. **Keep both repos' raw research pristine.** Reconciliation writes only to the Claude-side
   `canon-draft.json` (your standing wall rule). Kimi's `phase4-albums/*.json` stay untouched as
   the A/B record.

### Why not just merge to 157 and stop
Because the divergences encode *information* — Kimi reaching for *Giant Steps* and *In a Silent Way*
while Claude reached for *Blue Train* and *Nefertiti* is a real difference in canon philosophy
(studio landmarks vs. live/spiritual peaks). Flattening to a union throws that signal away. Tiering
preserves it: you ship a richer canon **and** keep the comparison readable. The union is the *floor*;
the tiering is what makes it an experiment instead of a pile.

### One data caveat before you ponder
A few "forks" may be **metadata twins**, not real disagreements — e.g. Shorty Rogers' *Cool and Crazy*
(Kimi) is an alternate title for *Shorty Rogers and His Giants* (Claude). Budget a quick alias-check on
the forked-artist list before treating every singleton as a genuine pick. Real taste forks vs.
title-variance is itself a finding worth logging in `-kc/docs/divergence-log.md`.
