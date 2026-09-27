#!/usr/bin/env python3
"""Update jazz-canon's recently-added.json from the current ship batch.

By default the batch is read from _jazzcanon.edit_log: each included album whose
latest site-status transition is found/reviewed -> approved and whose current
status is still approved. A completed ship changes that latest transition to
approved -> live, so only unshipped approvals remain. Repeated --batch-id
arguments are a database-free test/dry-run input.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
from typing import Any

BATCH_SQL = r"""
WITH latest_site_transition AS (
  SELECT DISTINCT ON (record_id) record_id, old_value, new_value
    FROM _jazzcanon.edit_log
   WHERE table_name = 'album'
     AND field = 'site_status'
   ORDER BY record_id, id DESC
)
SELECT transition.record_id
  FROM latest_site_transition AS transition
  JOIN _jazzcanon.album AS a ON a.id = transition.record_id
 WHERE transition.old_value IN ('found', 'reviewed')
   AND transition.new_value = 'approved'
   AND a.canon_status = 'included'
   AND a.site_status = 'approved'
 ORDER BY transition.record_id;
"""


class SchemaError(ValueError):
    """The gallery-owned JSON format does not match this generator's contract."""


def iso_date(value: str) -> str:
    try:
        parsed = dt.date.fromisoformat(value)
    except ValueError as exc:
        raise SchemaError(f"invalid ISO ship date {value!r}") from exc
    if parsed.isoformat() != value:
        raise SchemaError(f"ship date must be YYYY-MM-DD, got {value!r}")
    return value


def validate_document(document: Any) -> list[dict[str, str]]:
    if not isinstance(document, list):
        raise SchemaError("top level must be a JSON array")

    seen: set[str] = set()
    previous_date: str | None = None
    for index, item in enumerate(document):
        if not isinstance(item, dict):
            raise SchemaError(f"entry {index} must be an object")
        if list(item) != ["id", "added"]:
            raise SchemaError(
                f"entry {index} must have exactly the ordered keys 'id', 'added'"
            )
        album_id = item["id"]
        added = item["added"]
        if not isinstance(album_id, str) or not album_id:
            raise SchemaError(f"entry {index} has an invalid id")
        if album_id in seen:
            raise SchemaError(f"duplicate album id {album_id!r}")
        if not isinstance(added, str):
            raise SchemaError(f"entry {index} has a non-string added date")
        iso_date(added)
        if previous_date is not None and added > previous_date:
            raise SchemaError("entries must remain most-recent-first")
        seen.add(album_id)
        previous_date = added

    return document


def parse_document(original: bytes, source: Path) -> list[dict[str, str]]:
    try:
        document = json.loads(original)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SchemaError(f"{source} is not valid UTF-8 JSON: {exc}") from exc
    return validate_document(document)


def load_document(path: Path) -> list[dict[str, str]]:
    return parse_document(path.read_bytes(), path)


def query_batch(database_url: str) -> list[str]:
    result = subprocess.run(
        ["psql", database_url, "-X", "-q", "-A", "-t", "-v", "ON_ERROR_STOP=1", "-c", BATCH_SQL],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or "psql returned no diagnostic"
        raise RuntimeError(f"could not derive ship batch from edit_log: {message}")
    return [line for line in result.stdout.splitlines() if line]


def validate_batch(batch_ids: list[str]) -> list[str]:
    if any(not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", album_id) for album_id in batch_ids):
        raise ValueError("batch ids must be lowercase hyphenated slugs")
    if len(batch_ids) != len(set(batch_ids)):
        raise ValueError("ship batch contains duplicate album ids")
    return batch_ids


def validate_exported_albums(path: Path, batch_ids: list[str]) -> None:
    try:
        albums = json.loads(path.read_bytes())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"could not parse exported albums file {path}: {exc}") from exc
    if not isinstance(albums, list) or any(not isinstance(album, dict) for album in albums):
        raise RuntimeError(f"{path} must be a JSON array of album objects")
    exported_ids = {album.get("id") for album in albums}
    missing = [album_id for album_id in batch_ids if album_id not in exported_ids]
    if missing:
        raise RuntimeError(
            "approved batch changed after export; rerun the ship so these ids are exported: "
            + ", ".join(missing)
        )


def updated_document(
    document: list[dict[str, str]], batch_ids: list[str], ship_date: str
) -> tuple[list[dict[str, str]], bool]:
    batch = set(batch_ids)
    retained = [item for item in document if item["id"] not in batch]
    current_entries = [{"id": album_id, "added": ship_date} for album_id in batch_ids]
    result = current_entries + retained
    validate_document(result)
    if result[: len(batch_ids)] != current_entries:
        raise RuntimeError("generated document does not begin with the exact dated ship batch")
    return result, result != document


def atomic_write_json(
    path: Path, document: list[dict[str, str]], expected_source: bytes | None = None
) -> None:
    payload = (json.dumps(document, indent=2, ensure_ascii=False) + "\n").encode()
    destination_mode = stat.S_IMODE(path.stat().st_mode)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            os.fchmod(handle.fileno(), destination_mode)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        if expected_source is not None and path.read_bytes() != expected_source:
            raise RuntimeError(f"{path} changed after validation; refusing to overwrite it")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def atomic_write_batch(path: Path, batch_ids: list[str]) -> None:
    payload = "".join(f"{album_id}\n" for album_id in batch_ids).encode()
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, type=Path)
    parser.add_argument("--ship-date", default=dt.date.today().isoformat())
    parser.add_argument("--batch-id", action="append", default=[])
    parser.add_argument("--batch-output", type=Path, help="write the exact validated batch for the later live flip")
    parser.add_argument("--albums-file", type=Path, help="require every batch id in this exported albums JSON")
    parser.add_argument("--check", action="store_true", help="validate and report without writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        ship_date = iso_date(args.ship_date)
        source_bytes = args.file.read_bytes()
        document = parse_document(source_bytes, args.file)
        if args.batch_id:
            batch_ids = validate_batch(args.batch_id)
        else:
            database_url = os.environ.get("JAZZCANON_DB_URL")
            if not database_url:
                raise RuntimeError("JAZZCANON_DB_URL is required when --batch-id is not used")
            batch_ids = validate_batch(query_batch(database_url))
        if args.albums_file is not None:
            validate_exported_albums(args.albums_file, batch_ids)
        result, changed = updated_document(document, batch_ids, ship_date)
        if not args.check and changed:
            atomic_write_json(args.file, result, expected_source=source_bytes)
            # Read back from disk so the ship gate verifies the actual replacement.
            written = load_document(args.file)
            expected = [{"id": album_id, "added": ship_date} for album_id in batch_ids]
            if written[: len(batch_ids)] != expected:
                raise RuntimeError("post-write validation failed: exact dated batch is absent")
        if not args.check and args.batch_output is not None:
            atomic_write_batch(args.batch_output, batch_ids)
        action = "would change" if args.check else "changed"
        print(f"recently-added: batch={len(batch_ids)} {action}={int(changed)}")
        return 0
    except (OSError, RuntimeError, SchemaError, ValueError) as exc:
        print(f"recently-added: REFUSED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
