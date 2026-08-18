-- Normalize gil-evans-out-of-the-cool's session rows (Claude Code, 2026-08-18).
--
-- The album's four sessions were recorded in three rows: two compound rows
-- ("1960 November 18 & 30", "1960 December 10 & 15") and one vestigial
-- year-only row ("1960"). album.recording_dates_text — "November 18 & 30,
-- December 10 & 15, 1960" — independently confirms four dates, all at Van
-- Gelder Studio, Englewood Cliffs.
--
-- This asserts NO new fact. Every date below is already present, already
-- labelled obs, already sourced; it is moved from prose into the structured
-- column so one row means one session. Nothing is deleted: each compound row
-- keeps its own first date, one new row carries the date split out of it, and
-- the vague "1960" row is refined to the remaining date (1960 is true of it).
BEGIN;

UPDATE _jazzcanon.session SET session_date = DATE '1960-11-18',
       session_date_text = '1960-11-18', sequence = 1
 WHERE id = 'c3a0b5d1-17da-4b0c-ac82-e7c10d7cd5a3';

UPDATE _jazzcanon.session SET session_date = DATE '1960-12-10',
       session_date_text = '1960-12-10', sequence = 3
 WHERE id = '7beb8ac5-8457-4f42-8953-80d2a4392780';

UPDATE _jazzcanon.session SET session_date = DATE '1960-12-15',
       session_date_text = '1960-12-15', sequence = 4
 WHERE id = '401235ec-966c-44d3-9141-9d94d703fa66';

INSERT INTO _jazzcanon.session (album_id, session_date, session_date_text, studio_id, sequence, epistemic)
VALUES ('gil-evans-out-of-the-cool', DATE '1960-11-30', '1960-11-30', 137, 2, 'obs');

INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason) VALUES
 ('claude-code','session','c3a0b5d1-17da-4b0c-ac82-e7c10d7cd5a3','session_date','NULL (text: 1960 November 18 & 30)','1960-11-18','Structural normalization: one compound row held two sessions. No new claim — date already obs in session_date_text and album.recording_dates_text. John authorized 2026-08-18.'),
 ('claude-code','session','7beb8ac5-8457-4f42-8953-80d2a4392780','session_date','NULL (text: 1960 December 10 & 15)','1960-12-10','Structural normalization: one compound row held two sessions. No new claim. John authorized 2026-08-18.'),
 ('claude-code','session','401235ec-966c-44d3-9141-9d94d703fa66','session_date','NULL (text: 1960)','1960-12-15','Vestigial year-only row refined to the fourth documented date rather than deleted; 1960 remains true of it. No new claim. John authorized 2026-08-18.'),
 ('claude-code','session','gil-evans-out-of-the-cool','session_date',NULL,'1960-11-30','New row: second date split out of the compound row 1960 November 18 & 30. No new claim. John authorized 2026-08-18.');
COMMIT;
