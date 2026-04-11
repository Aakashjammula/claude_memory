# `code/` — Claude's Tool Folder

All Python scripts here are run via `uv run python <script>.py` from inside this directory.

---

## Tools

### `wiki_tools.py` — Shared library
**Import this in all tool scripts.** Provides:
- Canonical path constants: `BASE`, `WIKI_DIR`, `NOTES_DIR`, `RAW_DIR`, etc.
- Date helpers: `date_to_slug()`, `date_to_dow()`, `date_to_display()`, `slug_to_date()`
- Note I/O: `read_note()`, `write_note()`, `note_exists()`, `list_notes(pattern)`
- Wiki helpers: `read_index()`, `read_log()`, `append_log()`, `read_concept()`, `write_concept()`

---

### `fetch_playlist.py` — YouTube playlist → raw JSON
Fetches video metadata from a YouTube playlist and saves it to `raw/<playlist-slug>.json`.

```bash
# Default playlists (Steve Brunton Stat + Prob playlists)
uv run python fetch_playlist.py

# Any YouTube playlist URL
uv run python fetch_playlist.py "https://www.youtube.com/playlist?list=PLxxx"

# Multiple playlists
uv run python fetch_playlist.py "https://..." "https://..."
```

Output JSON format:
```json
{
  "playlist_title": "...",
  "playlist_url": "...",
  "total_videos": 35,
  "videos": [
    { "index": 1, "title": "...", "url": "...", "id": "...", "duration": 1320 }
  ]
}
```

---

### `generate_calendar.py` — Study plan → Google Calendar ICS
The **source of truth** for study plan dates. Edit `DSA_START`, `PS_START`, or
the topic lists here if the plan changes, then regenerate.

```bash
uv run python generate_calendar.py
# → Writes raw/study-plan.ics
```

Import into Google Calendar:
> calendar.google.com → Settings (⚙) → Import & Export → Import → Upload `raw/study-plan.ics`

Config (top of file):
- `DSA_START` — first day of DSA (currently `2026-04-11`)
- `PS_START` — first day of Prob/Stats (currently `2026-04-11`, parallel)
- `DSA_BLOCK` — time slot `(19, 21)` = 7–9 PM
- `PS_BLOCK` — time slot `(21, 23)` = 9–11 PM

---

## `_archive/`
One-off scripts that were run once and are kept for reference only.
Do not run these again — they assume a previous state of the wiki.

- `generate_dsa_notes.py` — generated the 31 DSA daily notes (Apr 11 – May 11)
- `generate_ps_notes.py` — generated the 29 PS daily notes (Apr 11 – May 9)
- `generate_calendar.old.py` — original calendar with old dates (Apr 9 start)

---

## Runtime

All scripts use `uv` (see `pyproject.toml`).
- Python 3.12+
- Dependency: `yt-dlp` (for `fetch_playlist.py`)

```bash
# Install deps (one-time)
uv sync

# Run any tool
uv run python <tool>.py
```
