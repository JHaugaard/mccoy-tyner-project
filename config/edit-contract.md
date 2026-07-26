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
McCoy executes them only on John's explicit, per-album instruction in
conversation — one album per instruction, no bulk flips — and logs each
to `edit_log` with `reason = 'John: <his words>'`.

| Transition | Trigger |
|---|---|
| `candidate → included` | John says include (the include gate) |
| `candidate → excluded` | John says reject; reason also goes to `research/cull-notes.md` |
| `found → reviewed` | John has looked, verdict pending |
| `reviewed → approved` | John greenlights for the site |
| `approved → live` | **Not chat.** The publish pipeline flips this at deploy |
| `live → retired` | John pulls it from the site |

## Never editable (regenerated or structural)

`embedding`, `search_document` (pipeline: `scripts/embed.py`),
`id`, `created_at`, `updated_at`, any foreign-key spine
(`album_id`, `person_id` on performance, …) — relinking rows is
restructuring, hand it to Claude Code.
