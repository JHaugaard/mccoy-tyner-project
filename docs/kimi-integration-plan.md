# Kimi → Claude Integration Plan (evaluation only — no work yet)

**Date:** 2026-06-23
**Premise (given):** The Claude build (`mccoy-tyner`) is the solid base from here through the DB stage. Question: which strong elements of the Kimi build (`mccoy-tyner-kc`) are worth porting into it, and how?
**Status:** Evaluation + plan. Nothing implemented.

---

## 1. The honest framing

After reading both builds' actual artifacts, the integration story is **narrow and specific**, not a merge. The two builds are strong in *different layers*:

- **Claude's strength is the data model.** `data/schema.sql` already has: consensus tiering (`canon_tier` enum), first-class `production_credit` (producer/engineer/arranger/…), a `style` vocabulary table + `album_style` M2M, per-fact `citation` provenance with a CHECK constraint, collections, embeddings, and — importantly — a **lean track-personnel design** (`performance.scope='all-tracks'` + the `v_track_personnel` *view* that derives per-track rows on read).
- **Kimi's strength is process rigor.** A strict JSON Schema (`additionalProperties:false`), **validation-at-generation** (`validate-research.py` run inside each agent), cross-reference integrity checks, and a machine stats roll-up (obs/inf/unk counts, conflict-type breakdown, source-access flags).

**Consequence:** several "obvious" things to pull from Kimi are already present in the Claude schema, and in two cases the Claude version is *better*:

| Candidate pull from Kimi | Verdict | Why |
|---|---|---|
| Consensus tiering | **Already in Claude** | `canon_tier` enum exists |
| Production credits | **Already in Claude, better** | Structured `production_credit` table; Kimi's schema has no studio/producer/engineer fields |
| Track-level personnel | **Claude is better — do NOT pull Kimi's** | Kimi materializes 25 `inf` rows/album; Claude derives via `scope` + view. Kimi's is padding. |
| Controlled genre vocabulary | **Already in Claude** | `style` table + `album_style`; table-driven beats a hard enum |
| Python FastAPI backend | **Do NOT pull** | Conflicts with intent-defaults (PostgREST/static-first is the better-fit call) |
| Separate per-album JSON files | **Do NOT pull** | At DB stage everything is rows; single `canon-draft.json` is fine pre-ingest |

So the real transfer is **one theme: port Kimi's validation discipline to the seam between `canon-draft.json` and the Postgres loader.** The Claude build has an excellent destination schema but a *soft intermediate-artifact contract* — the 105 hand-touched merged records have no formal schema and no automated pre-ingest gate. That is exactly the gap Kimi closed, and it is the single highest-value thing to adopt.

---

## 2. What to pull, tiered

### Tier 1 — Record contract + validate-before-ingest gate  *(high value, low risk)*
Formalize the merged one-pass record (`data/canon-draft.json` album objects + nested `personnel_record`) as a **JSON Schema**, and write a **validator that must pass before the loader runs**. Three checks, mirroring Kimi:

1. **Structural** — required fields present, types correct, epistemic labels in `{obs,inf,unk}`, `scope` in the allowed set, no unexpected keys (`additionalProperties:false`).
2. **Cross-reference integrity** — every `sources` ref (S1…Sn) is defined and used; every name in `track.personnel` appears in album `personnel`; every instrument resolves against the taxonomy in `docs/personnel-contract.md`; ids are unique and slug-shaped.
3. **Coverage / stats report** (free byproduct) — emit obs/inf/unk distribution and a **null-field report**. This would have surfaced the 65/105 null-MBID gap automatically instead of by memory.

**Why it matters most:** the Claude data model is only as good as what reaches it. FKs catch referential errors at *ingest* (late, noisy, mid-transaction); a JSON-layer validator catches them at the *source file* (early, friendly, fixable). Kimi proved the pattern holds at 100 albums.

**Where it slots:** Segment C (schema lock) defines the JSON Schema; Segment D2 (loader/normalize) runs the validator as a hard gate before any `INSERT`.

### Tier 2 — JSON → Markdown review renderer  *(medium value, ergonomics)*
Kimi renders human-readable Markdown from each JSON record for the review gate. Adopt a small renderer that turns `canon-draft.json` into per-album review sheets. **Immediate payoff:** the 157-union reconciliation pass (the `consensus` tiering work) becomes a readable side-by-side instead of raw JSON diffing.

**Where it slots:** usable now for reconciliation; formalize at the Segment C/D review gate.

### Tier 3 — Structured conflict capture  *(optional — evaluate need first)*
Kimi stores `conflicts[]` arrays (524 preserved, typed). The Claude build currently keeps conflicting claims in prose `notes`/`rationale`. A structured `album_fact`/`conflict` table would be more queryable — **but** it is a schema change (proposal-first per intent rules) and may be over-engineering for a single-user tool. **Recommendation: do not adopt by default.** Revisit only if, during reconciliation, conflict density turns out high enough to be worth querying. Keep prose+epistemic until proven otherwise.

---

## 3. Explicitly NOT pulling (and why)

- **Track-personnel materialization** — Claude's scope-flag + view is strictly better; Kimi's is the one substantive weakness I found.
- **Python backend stack** — PostgREST views-as-API / static-export-first fits your health metrics (simplicity, operable-via-config, no hand-written backend).
- **Per-album file layout** — no benefit once data is in Postgres.
- **Genre enum** — `style` table already does this, more flexibly.

---

## 4. Experiment-integrity note (the wall)

Porting Kimi's *validator pattern* into the Claude build **does not breach the A/B wall.** The wall protects Kimi's *generation* from importing Claude's design (the transcription trap) — it is directional. This is the reverse: post-hoc reconciliation **downstream of both repos**, exactly the "third-position, read-only at the gate" pattern in the experiment's ground rules. And it adopts a *design idea* (validate-before-ingest), not Kimi's *data*.

Two house rules to keep it clean:
1. **Log it.** Add an adoption entry to `mccoy-tyner-kc/docs/divergence-log.md`: "Claude build adopted Kimi's validate-at-ingest discipline." The divergence log is the experiment's deliverable; adoptions belong in it.
2. **Don't touch Kimi's raw artifacts.** The port is new code in `mccoy-tyner` (a JSON Schema + a validator script). Kimi's `phase4-albums/*.json` stay pristine as the A/B record.

---

## 5. Sequencing & effort

| Step | Tier | Effort | Risk | Slots into |
|---|---|---|---|---|
| Write JSON Schema for the merged record | 1 | S | low | Segment C (schema lock) |
| `validate-canon.py`: structural + cross-ref + stats | 1 | M | low | Segment C / D2 (pre-ingest gate) |
| JSON → Markdown review renderer | 2 | S–M | low | now (reconciliation) → D review gate |
| Structured conflicts table | 3 | M | med (schema change) | only if proven needed |

**Recommended order:** Tier-1 schema + validator first (it hardens the DB migration you're about to do and would have caught the MBID gap), Tier-2 renderer alongside the 157 reconciliation (it makes that pass easier), Tier-3 deferred pending evidence.

---

## 6. One-sentence version

The Claude build wins on data model; Kimi wins on validation discipline — so pull **just the validation discipline** (a JSON-Schema record contract + a validate-before-ingest gate that also reports coverage), skip everything structural because the Claude schema already does it better, and log the adoption so the A/B record stays honest.
