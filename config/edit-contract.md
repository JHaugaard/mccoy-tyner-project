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

## Status transitions (John's verdicts, McCoy's hands)

`canon_status` and `site_status` changes are **never McCoy's initiative**.
McCoy executes them only on John's explicit instruction in conversation,
and logs each to `edit_log` with `reason = 'John: <his words>'`.

**The two dials are not the same kind of decision, and they do not batch
the same way** (established 2026-07-26, replacing a blanket "one album per
instruction, no bulk flips" that applied to both):

- **`canon_status` is an editorial judgment about one album.** It is
  irreducibly singular — the thing being recorded is John's reasoning
  about *this record*, and a batch destroys exactly that. **Never batched.**
- **`site_status` is a publication decision** — what goes out, and when.
  Nothing about it is per-album; the per-album judgment already happened
  upstream at the include gate. **Batching is legitimate here.**

| Transition | Dial | Batch? | Trigger |
|---|---|---|---|
| `candidate → included` | canon | **No** | John says include (the include gate) |
| `candidate → excluded` | canon | **No** | John says reject; reason also goes to `research/cull-notes.md` |
| `found → reviewed` | site | Yes | John has looked, verdict pending — the honest "not now" |
| `→ approved` | site | Yes | John greenlights for the site |
| `approved → live` | site | n/a | **Not chat.** The publish pipeline flips this at deploy |
| `live → retired` | site | **No** | John pulls a specific album from the site |

### Include and exclude: one album, one instruction, one reason

McCoy **refuses a blanket canon verdict** ("include all of these", "I
accept the batch") and offers the queue back one at a time. This is not
pedantry: the council already wrote `case_for` and `case_against`, so what
the record is missing is why *John* agreed. A few words carry it — "the
Shorter writing is the argument" is a real verdict; "I accept all 19" is
not a verdict for any of the 19.

The reason string is John's own words, per album, in that album's
`edit_log` row.

**Queue-depth tell.** The drip delivers two candidates a day so the include
gate stays a short daily habit. If the review queue reaches double digits,
the habit lapsed — drain the queue, do not relax this rule. A pile-up is
the signal, not the justification.

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

## Never editable (regenerated or structural)

`embedding`, `search_document` (pipeline: `scripts/embed.py`),
`id`, `created_at`, `updated_at`, any foreign-key spine
(`album_id`, `person_id` on performance, …) — relinking rows is
restructuring, hand it to Claude Code.
