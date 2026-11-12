# Basemap handoff — Berlin region for 2026-11-12 ship

John's instruction in McCoy's session on 2026-11-12: verdicts on the six Nov 10–12 candidates; defer Charlie Parker; include the other five; ingest, ship, and deploy.

## Verified state

- The five newly approved albums exported cleanly; `publish.sh` produced commit `72677d4` and 340 publishable albums.
- The place-set diff adds only `philharmonic-hall-lincoln-center` (Miles Davis — *My Funny Valentine*). Its studio row is complete and sourced.
- After copying the six exports into `/home/john/dev/stable/jazz-canon/app/public/data/`, `node scripts/build-basemap.mjs` exited 1 without writing basemap output:

  ```text
  places outside every region bbox:
    deutschlandhalle (52.50028, 13.26972)
  ```

- `deutschlandhalle` is a pre-existing exported place, not one of this batch's new places. This is the stale-pin case in `canon-ship-operations/references/basemap-rebuild.md`.

## Bounded repair requested

In `/home/john/dev/stable/jazz-canon`, add the smallest Berlin city region to `REGIONS` in `scripts/build-basemap.mjs`, preserving all coverage, land, lake, and gzip-budget guards. No per-place exemption, coordinate change, or guard relaxation.

Required ±60 km window around Deutschlandhalle:

- latitude: `51.96028..53.04028` (52.50028 ± 0.54)
- longitude: `12.38433..14.15511` (60 / (111.32 · cos(latitude)))
- city-region fidelity: `tol` 0.0006–0.0008, `dec` 4

The new Philharmonic Hall pin must also pass the existing NYC region.

## Verification and scope

1. Run `node scripts/build-basemap.mjs`; require exit 0 and the `wrote …/basemap.json` line.
2. Run it a second time from the pinned cache and require byte-identical `app/public/map/basemap.json`.
3. Commit only `scripts/build-basemap.mjs` and `app/public/map/basemap.json` if changed. Do not commit or alter the gallery's unrelated dirty docs or `scripts/enrich-previews.mjs`, and do not deploy.
4. Report the region definition, verification output, and commit SHA to McCoy. McCoy owns the remaining `ship.sh --go` deploy and status flip.
