# To-Do — Known Issues & Pending Work

Running list. Add here as issues surface. Clear when resolved.

---

## Data Quality

- ~~**Cannonball Adderley duplicate**~~ ✓ DONE 2026-06-26 — Merged `Julian 'Cannonball' Adderley` into `Cannonball Adderley`. His Milestones performance migrated. Name variants added. Script: `scripts/data-quality-sweep.py`.
- ~~**Person identity resolution sweep**~~ ✓ DONE 2026-06-26 — Full pass over 535 persons. No additional duplicates beyond Cannonball. Script: `scripts/data-quality-sweep.py`. 27 near-pairs in review list — all genuinely different people (e.g. Bill Evans vs Gil Evans, Hank Jones vs Thad Jones). See session notes for full review list.
- ~~**`recording_dates` anomaly**~~ ✓ VERIFIED 2026-06-26 — `june-christy-something-cool-1955` `session_date_text` is `"1953-08/1955-07"`, a valid ISO 8601 multi-session range. The original report was incorrect. No fix needed.
- [ ] **3 albums with null Apple ID** — not found on iTunes: `lee-konitz-subconscious-lee-1950`, `jackie-mclean-destination-out`, `ahmad-jamal-at-the-pershing-but-not-for-me`. Low priority; may not be on Apple Music.

---

## Phase 4 Remaining

- ~~**14 Kimi-only gap-fill**~~ ✓ DONE 2026-06-26 — MBIDs, Apple IDs, studios, engineers/producers filled. Scripts: `scripts/mbid-apple-lookup.py`.
- ~~**65 records with null MusicBrainz MBIDs**~~ ✓ DONE 2026-06-26 — 100/100 MBIDs populated. All TLS-failure albums resolved.
- ~~**D5 cover art fetch**~~ ✓ DONE 2026-06-26 — 100/100 albums have cover art. Files in `data/album-art/`. Scripts: `scripts/cover-art-fetch.py`.
- ~~**`catalog_number` gap-fill for Claude records**~~ ✓ DONE 2026-06-26 — 100/100 albums have catalog numbers. Scripts: `scripts/catalog-lookup.py`.
- ~~**Embeddings**~~ ✓ DONE 2026-06-26 — nomic-embed-text (768-dim) via Ollama on vps4. `album.embedding` + `person.embedding` + HNSW indexes. Script: `scripts/embed.py`.
- [ ] **Static export** — JSON bundle + precomputed album×album neighbors + art → `app/data/`. Build step script needed.
- [ ] **PostgREST** — single binary on vps8, `db-schemas = "_jazzcanon"`, `db-anon-role = "_jazzcanon_ro"`. Set up when a live consumer appears.
- [ ] **DB roles** — create `_jazzcanon_role` and `_jazzcanon_ro` with passwords, add to vault (`jazzcanon_*` secrets). Currently running as postgres superuser.

---

## Phase 5 — App

- [ ] **Stack decision** — TBD (see session discussion). Admin front end and public app may differ. See `docs/phase5-and-beyond.md`.
- [ ] **Admin front end** — personal research tool. CRUD for notes/writing, gap-fill UI, query interface.
- [ ] **Public app** — the "wow" shareable experience. Core features: Album Grid, Deep Dive, Personnel Network.
- [ ] **MusicKit / Apple Music** — connect `apple_album_id` to previews/links/player via MusicKit JS.
- [ ] **Studio geocoordinates** — populate `lat`/`lon` on `studio` table (~12–15 studios). Enables Venue Map feature.

---

## Growth (Post-v1)

- [ ] **19 next-batch albums** — queued for v2 research pass when ready.
- [ ] **Vocal sub-collection decision** — June Christy, Mel Tormé, Shelly Manne currently in active 100; flagged for a future vocal sub-collection call.
- [ ] **Notes/writing schema** — user-facing CRUD for album and artist notes. New tables, additive migration.
