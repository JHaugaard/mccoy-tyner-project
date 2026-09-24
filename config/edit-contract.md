# Edit Contract — McCoy's write surface

McCoy's only write path into `_jazzcanon`. Role: `_jazzcanon_app`
(SELECT/INSERT/UPDATE — DELETE is not granted, by design). Everything
outside this contract is read-only or Claude Code's job.

## The protocol (every edit, no exceptions)

1. **Read first** — show John the current value before changing it.
2. **Whitelist check** — the field must be listed below.
3. **Epistemic pairing** — if the edit changes a *fact* (not a status or
   a note), update the row's epistemic label in the same UPDATE, and ask
   John for the source; if there is none, the label degrades honestly
   (obs → inf/unk). A fact edit without its label is refused.
4. **Audit row** — one `edit_log` INSERT per changed field, same
   transaction:
   ```sql
   INSERT INTO _jazzcanon.edit_log
     (editor, table_name, record_id, field, old_value, new_value, reason)
   VALUES
     ('mccoy', 'album', '<album id>', 'year', '1959', '1958',
      'John: original Blue Note release, not the reissue. Source: S-token/URL.');
   ```
5. **Report** — field, old → new, one line, done.

## Whitelisted fields

**album** — `title`, `artist_name`, `year`, `catalog_number`,
`recording_dates_text`, `multi_session`, `musicbrainz_release_group_mbid`,
`musicbrainz_release_mbid`, `apple_album_id`, `description`, `notes`,
`inclusion_rationale`, `epistemic`, `canon_tier`, `priority`

**performance** (a personnel line) — `instrument_id`, `scope`,
`epistemic`, `notes`

**track** — `title`, `track_number`, `side`, `duration_text`,
`session_date`, `epistemic_track`, `apple_track_id`

**person** — `canonical_name` (plus `person_name_variant` inserts)

**production_credit** — `person_id`, `role`, `epistemic`

**source / citation** — inserts only (new provenance is always welcome);
never rewrite an existing source row's identity.

**studio** (a recording place) — inserts, plus enrichment `UPDATE` on
`kind`, `address`, `lat`, `lon`, `location_epistemic`, `location_source`
when an existing row is missing one (plus `studio_name_variant` inserts).
Two hard conditions:

- **Complete or not at all.** A new row carries `name`, `city`, `kind`,
  `lat`, `lon`, `location_epistemic`, `location_source` in the same
  statement, or it is not created and the session's site stays empty. A
  partial row passes every DB constraint and then aborts `export.sh`'s
  place validator the day John promotes the album — the failure surfaces
  weeks downstream of the mistake, which is why this is a contract rule
  and not just a code check.
- **`name` and `name_slug` are identity, never rewritten**, and a
  `merged-*` tombstone is never resurrected or matched. Those rows record
  merge and split rulings John already made (2026-08-14); re-minting one
  discards a decision.

Deciding that two places are the same room, or that one string is really
two venues, is a **merge/split ruling — John's, not McCoy's**. McCoy
resolves against the existing set and creates genuinely new places; it
never consolidates existing ones.

**studio_name_variant** — **inserts only**, exactly as `person_name_variant`
is for people: recording a wording a source uses for a place already in the
canon. Never rewrite or repoint an existing variant — that is re-deciding
what a past wording meant, which is a ruling, not a note. Three rules:

- **One venue per variant.** A string naming two venues is never a variant;
  it is two entries in the record. Seeding deliberately excluded the five
  compound raws for this reason.
- **Never point at a tombstone.** A variant points *from* a merged row's raw
  string *to* the surviving place, never the other way. Enforced by a trigger
  as well as stated here.
- **Ambiguous wordings stay out.** If a wording could honestly mean two
  different places — "Van Gelder Studio", "CBS Studios" — it is not a
  variant, it is a disambiguation rule, and it belongs in the drip's
  guidance rather than in this table. A missing alias costs a match; a wrong
  one silently mis-files a session.

**session** — `studio_id` **only**, and only to fill a NULL. See the
carve-out under *Never editable* below.

## Status transitions (John's verdicts, McCoy's hands)

`canon_status` and `site_status` changes are **never McCoy's initiative**.
McCoy executes them only on John's explicit instruction in conversation,
and logs each to `edit_log` with `reason = 'John: <his words>'`.

**The two dials are not the same kind of decision, but both may be batched**
(revised 2026-09-20):

- **`canon_status` is an editorial judgment.** John may render that judgment
  for one album, a named group, or the whole pending queue. A batch verdict
  is a genuine verdict and requires no per-album rationale.
- **`site_status` is a publication decision** — what goes out, and when.
  Nothing about it is per-album; the per-album judgment already happened
  upstream at the include gate. **Batching is legitimate here.**

| Transition | Dial | Batch? | Trigger |
|---|---|---|---|
| `candidate → included` | canon | Yes | John says include (the include gate) |
| `candidate → excluded` | canon | Yes | John says reject; reason also goes to `research/cull-notes.md` |
| `found → reviewed` | site | Yes | John has looked, verdict pending — the honest "not now" |
| `→ approved` | site | Yes | John greenlights for the site |
| `approved → live` | site | n/a | **Not chat.** The publish pipeline flips this at deploy |
| `live → retired` | site | **No** | John pulls a specific album from the site |

### Include and exclude

McCoy accepts verdicts in any shape John gives them — one album, a named
group, or the whole pending queue. "All pending are IN," "all except X and
Y," and "include A, exclude B" are all valid instructions. McCoy executes
them as given, with one `edit_log` row per affected album. Each row carries
John's words as the reason; no per-album rationale is required.

The council's `case_for` and `case_against` remain in the dossier as the
research argument. John's batch decision is the editorial verdict and is
complete in itself.

An exception is not silently treated as a rejection. In "all pending except
X and Y are IN," X and Y remain candidates unless John explicitly excludes
or otherwise disposes of them. Explicit exclusions are also recorded in
`research/cull-notes.md` using John's words.

### Approve: one instruction may cover many albums

"Approve everything included since the last ship" is a single coherent
decision and McCoy executes it as given. Still **one `edit_log` row per
album** — batching the instruction never batches the audit trail. Each
row's reason carries John's words plus a batch marker so the batch is
reconstructable afterwards:

```sql
INSERT INTO _jazzcanon.edit_log
  (editor, table_name, record_id, field, old_value, new_value, reason)
VALUES
  ('mccoy', 'album', '<album id>', 'site_status', 'found', 'approved',
   'John: ship everything included since the last deploy. '
   '[batch approve 2026-07-26, 5 albums]');
```

Before executing a batch, McCoy lists the affected albums and gets John's
confirmation on the list. `retired` is excluded from batching — pulling a
record off the public site is a specific act about a specific album.

## The audit log is append-only (adopted 2026-08-09)

`_jazzcanon_app` can INSERT into `edit_log` but holds no UPDATE or DELETE
on it — deliberately: an audit trail the editor can rewrite is a diary,
not an audit trail. Canon data takes corrections by UPDATE; the log does
not.

So when the *text* of a log row is wrong (a typo in John's quoted verdict,
a mis-dated session tag), the correction is a new row, never a rewrite:

- `field` = `verdict_text_correction` (or `<field>_correction` generally)
- `old_value` / `new_value` = the wrong and right text
- `reason` = who authorized it and why, naming the row it corrects
- the original row stands untouched, so the trail shows both the slip and
  the fix

Worked example: the Red Clay include row's "Hard Bob with a Fender
Rhodes" was corrected to "Hard Bop …" by an appended correction row
(2026-08-09). Escape hatch if corrections ever get frequent: a column-level
`GRANT UPDATE (reason)` — Claude Code's lane, parked until then.

## Never editable (regenerated or structural)

`embedding`, `search_document` (pipeline: `scripts/embed.py`),
`id`, `created_at`, `updated_at`, any foreign-key spine
(`album_id`, `person_id` on performance, …) — relinking rows is
restructuring, hand it to Claude Code.

**One narrow carve-out (John, 2026-08-16): `session.studio_id`.** McCoy may
set it **when it is NULL** — that is not relinking, it is filling in a fact
that was never recorded. Changing a `studio_id` that already points
somewhere *is* relinking and stays Claude Code's, because it means one of
the two places is wrong, which is a merge/split ruling. The rest of the
spine is untouched by this carve-out.

`case_for`, `case_against` (John's ruling, 2026-07-26) — these are
**projections of the album's research dossier**, not source records. The
dossier JSON under `research/candidates-archive/` is the archival source;
editing the column in place would silently diverge the database from it.
A change goes to the dossier's `ballot` block first, then
`scripts/backfill-ballot-fields.py` carries it into the DB with its own
`edit_log` row (the script is idempotent — it only writes what differs).
Later wordsmithing of ballot prose is John's own, done at the dossier.
