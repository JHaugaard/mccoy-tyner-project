# Sonos Favorites proof of concept

Date: 2026-11-13

Status: research summary only. No code has been run against John's Sonos system, and no Favorites have been added, changed, or removed.

## Question

Can we programmatically push albums into the Sonos Favorites list shown as My Sonos in the Sonos app?

## Short answer

Yes, through the speakers' local UPnP interface, using the third-party Python library SoCo. The official Sonos cloud Control API does not expose an add-favorite operation.

This distinction matters: the official API can list and play existing Favorites, while the local route can now create, update, rename, and remove them.

## What the official Sonos API provides

The published Control API includes:

- `getFavorites`: retrieve the Favorites for a household.
- `loadFavorite`: load an existing Favorite into a group's playback queue.
- Favorites subscriptions: receive change notifications.

The published Favorites namespace has no `createFavorite` or general add-album endpoint.

Sonos also documents an “Add favorites” facility for music-service integrations. That is a different mechanism: a service exposes actions that a listener chooses in the Sonos app, and it can maintain favorites within that service. It is not a general external API for pushing arbitrary albums into My Sonos.

The official API documents a limit of 70 Sonos Favorites.

Sources:

- https://docs.sonos.com/reference/favorites-getfavorites-householdid
- https://docs.sonos.com/reference/favorites-loadfavorite-groupid
- https://docs.sonos.com/docs/add-favorites

## The useful local route

Sonos speakers store Favorites in the local UPnP ContentDirectory container `FV:2`.

SoCo version 0.32.0, released 2026-10-15, added a write API for that container. The current release found during this research is SoCo 0.32.2, released 2026-11-06.

The library exposes:

```python
device.favorites.add(item)
device.favorites.remove(favorite)
device.favorites.update(favorite, title=None, description=None)
device.favorites.rename(favorite, new_title)
```

`add()` accepts a Sonos DIDL object representing a track, album, playlist, radio station, or music-service container. It therefore supports album Favorites, not merely individual tracks.

The SoCo contributor reported live add/read/update/remove testing on S2 hardware; the maintainer subsequently reported a successful S1 test. Those are project-reported tests, not tests performed for this brief.

Sources:

- https://soco.readthedocs.io/en/latest/api/soco.favorites.html
- https://github.com/SoCo/SoCo/pull/1018
- https://github.com/SoCo/SoCo/releases/tag/v0.32.0
- https://pypi.org/project/soco/

## Why older answers say this is impossible

The write capability is recent. Older projects and documentation commonly describe Favorites as readable and playable through UPnP but creatable only in the official Sonos app.

SoCo's October 2026 release now packages the local `CreateObject`, `UpdateObject`, and `DestroyObject` behavior, including Sonos-specific quirks. “Sonos Favorites are read-only” is therefore stale as a blanket statement, although it remains true of the official cloud Control API.

The local UPnP interface is not a supported public Sonos API. A firmware update could change its behavior; SoCo is the compatibility layer, not Sonos's contractual guarantee.

## Proposed proof-of-concept shape

```text
Album identity
    ↓
Resolve the album in a Sonos-visible source
    ↓
Obtain its Sonos DIDL object
    ↓
device.favorites.add(album)
    ↓
Read Favorites back and verify the exact entry
    ↓
Confirm it appears in the Sonos app
    ↓
Remove the test entry and verify removal
```

The Favorites-write step is no longer the main uncertainty. Resolving the desired album into the correct Sonos DIDL object is.

### Source cases

**Local Sonos music library — simplest first test.** Search the local library, select the exact album, and pass that album object to `device.favorites.add()`.

**Apple Music, Spotify, and other streaming services — second experiment.** SoCo's API supports music-service containers, but the project currently warns that music-service authentication changes have caused problems for Apple Music, Amazon Music, Spotify, and Napster. An Apple album ID or an artist/title string alone is not sufficient; we need the album as represented by the relevant Sonos music service.

For a canon-related experiment, prove the complete round trip with one local-library album before attempting streaming-service resolution or any drip integration.

## Environment and safety constraints

- Run the proof on a machine with local-network access to the speakers, initially expected to be one of John's Macs rather than vps8.
- UPnP must be enabled on the Sonos system.
- Start with discovery and read-only operations. Do not combine discovery with a write.
- Use one known album for the first write test.
- Check the current Favorites count before adding anything; the documented capacity is 70.
- Expect explicit exceptions for a duplicate Favorite and a full Favorites list.
- The initial test must not start playback, replace the queue, or change volume.
- No streaming-service credentials belong in the repository or in this document.

Unknown at this stage: John's source service for the test album, speaker firmware behavior on his system, network reachability from the chosen terminal, and whether streaming-service album resolution works with his linked account.

## Terminal plan

Run these steps individually on the chosen Mac, in a fresh working directory. They are deliberately separated so discovery, reading, writing, and removal each remain visible decisions.

### 1. Create an isolated Python environment

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
python -m pip install "soco==0.32.2"
```

```bash
python -m pip show soco
```

### 2. Discover speakers — read-only

```bash
python - <<'PY'
from soco import discover

for device in discover() or []:
    print(device.player_name, device.ip_address)
PY
```

Stop if this returns nothing. Do not troubleshoot that by attempting a write.

### 3. Read the existing Favorites — read-only

```bash
python - <<'PY'
from soco import discover

device = next(iter(discover()))
favorites = device.music_library.get_sonos_favorites()
print("Favorite count:", len(favorites))
for favorite in favorites:
    print(favorite.item_id, favorite.title)
PY
```

### 4. Resolve one local-library album — read-only

Replace the search text with an album known to exist in the local Sonos music library. Inspect the matches and confirm the exact edition before proceeding.

```bash
python - <<'PY'
from soco import discover

device = next(iter(discover()))
albums = device.music_library.get_albums(
    search_term="Live at the Lighthouse",
    complete_result=True,
)
for index, album in enumerate(albums):
    print(index, album.title, album.item_id)
PY
```

If this produces no reliable match, the local-library path is unavailable for that album; stop there or choose another known local album.

### 5. Add the checked album — the first write

Use the index verified in the previous step. This example intentionally uses index zero only as a placeholder; confirm that zero identified the intended album in your own output.

```bash
python - <<'PY'
from soco import discover

device = next(iter(discover()))
albums = device.music_library.get_albums(
    search_term="Live at the Lighthouse",
    complete_result=True,
)
album = albums[0]
created = device.favorites.add(album)
print("Created:", created.item_id, created.title)
PY
```

### 6. Verify independently

Repeat step 3 and find the new entry. Then confirm that it appears in My Sonos in the official app and that no playback or queue change occurred.

### 7. Remove the test entry

Use the item ID returned by the add operation, substituting its actual value below.

```bash
python - <<'PY'
from soco import discover

device = next(iter(discover()))
device.favorites.remove("FV:2/REPLACE_WITH_RETURNED_ID")
PY
```

Repeat step 3 once more to verify removal.

## Acceptance test and fallback

The proof succeeds if one exact local-library album is added, read back through a separate Favorites query, seen in the official Sonos app, and removed cleanly, with no playback or queue side effects.

If discovery fails, investigate network and UPnP visibility first. If album resolution fails, change the album or source rather than constructing metadata blindly. If a streaming service fails authentication or search, retain the successful local-library result and treat streaming resolution as a separate problem; do not respond by building a custom Sonos music service.

## Assessment

**obs:** The official cloud API lists and loads Favorites but exposes no general create operation. SoCo 0.32.x exposes album-capable Favorites writes through local UPnP.

**inf:** A small local-library round trip is now a credible proof of concept and the right first terminal experiment.

**unk:** Whether the albums John actually wants to push—especially Apple Music albums associated with canon records—can be resolved and added reliably on his system.
