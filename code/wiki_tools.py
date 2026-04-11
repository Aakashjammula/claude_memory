"""
wiki_tools.py
-------------
Shared helpers for reading and writing the claude_memory wiki.
Import this in any tool script instead of duplicating path/date logic.

Provides:
  - BASE, NOTES_DIR, RAW_DIR, WIKI_DIR, CONCEPTS_DIR, SOURCES_DIR — canonical paths
  - date_to_slug(d)      → "apr-11"
  - date_to_dow(d)       → "Saturday"
  - date_to_display(d)   → "Saturday, April 11, 2026"
  - slug_to_date(slug)   → date object  (e.g. "apr-11-day1" → date(2026,4,11))
  - read_note(slug)      → str content
  - write_note(slug, content) → writes wiki/notes/<slug>.md
  - list_notes(pattern)  → [slug, ...] matching fnmatch pattern
  - read_index()         → str content of wiki/index.md
  - append_log(entry)    → appends a log entry to wiki/log.md
"""

import fnmatch
import os
from datetime import date
from typing import Optional

# ── Canonical paths ──────────────────────────────────────────────────────────
BASE           = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_DIR       = os.path.join(BASE, "wiki")
NOTES_DIR      = os.path.join(BASE, "notes")
STUDY_PLANS_DIR = os.path.join(BASE, "study-plans")
CONCEPTS_DIR   = os.path.join(WIKI_DIR, "concepts")
SOURCES_DIR    = os.path.join(WIKI_DIR, "sources")
ENTITIES_DIR   = os.path.join(WIKI_DIR, "entities")
RAW_DIR        = os.path.join(BASE, "raw")
PLAYLISTS_DIR  = os.path.join(RAW_DIR, "playlists")

# Ensure directories exist
for _d in [NOTES_DIR, STUDY_PLANS_DIR, CONCEPTS_DIR, SOURCES_DIR, ENTITIES_DIR,
           RAW_DIR, PLAYLISTS_DIR]:
    os.makedirs(_d, exist_ok=True)

# ── Date utilities ────────────────────────────────────────────────────────────
_MONTHS_SHORT = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
_MONTHS_FULL  = ["January","February","March","April","May","June",
                 "July","August","September","October","November","December"]
_DAYS         = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


def date_to_slug(d: date) -> str:
    """date(2026,4,11) → 'apr-11'"""
    return f"{_MONTHS_SHORT[d.month-1]}-{d.day:02d}"


def date_to_dow(d: date) -> str:
    """date(2026,4,11) → 'Saturday'"""
    return _DAYS[d.weekday()]


def date_to_display(d: date) -> str:
    """date(2026,4,11) → 'Saturday, April 11, 2026'"""
    return f"{date_to_dow(d)}, {_MONTHS_FULL[d.month-1]} {d.day}, {d.year}"


def slug_to_date(slug: str, year: int = 2026) -> Optional[date]:
    """
    'apr-11-day1' → date(2026, 4, 11)
    'may-09-ps-29' → date(2026, 5, 9)
    Returns None if the slug doesn't start with a recognizable mon-DD prefix.
    """
    parts = slug.split("-")
    if len(parts) < 2:
        return None
    try:
        month = _MONTHS_SHORT.index(parts[0].lower()) + 1
        day   = int(parts[1])
        return date(year, month, day)
    except (ValueError, IndexError):
        return None


# ── Note I/O ──────────────────────────────────────────────────────────────────

def note_path(slug: str) -> str:
    return os.path.join(NOTES_DIR, f"{slug}.md")


def read_note(slug: str) -> str:
    """Read and return the content of wiki/notes/<slug>.md."""
    with open(note_path(slug), encoding="utf-8") as f:
        return f.read()


def write_note(slug: str, content: str, overwrite: bool = True) -> str:
    """Write content to wiki/notes/<slug>.md. Returns the filepath."""
    path = note_path(slug)
    if not overwrite and os.path.exists(path):
        raise FileExistsError(f"Note already exists: {path}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def note_exists(slug: str) -> bool:
    return os.path.exists(note_path(slug))


def list_notes(pattern: str = "*") -> list[str]:
    """
    Return list of note slugs (without .md) matching an fnmatch pattern.
    Examples:
        list_notes("*-ps-*")   → all PS notes
        list_notes("*-day*")   → all DSA day notes
        list_notes("apr-*")    → all April notes
    """
    slugs = []
    for fn in sorted(os.listdir(NOTES_DIR)):
        if fn.endswith(".md"):
            slug = fn[:-3]
            if fnmatch.fnmatch(slug, pattern):
                slugs.append(slug)
    return slugs


# ── Wiki file helpers ─────────────────────────────────────────────────────────

def read_index() -> str:
    path = os.path.join(WIKI_DIR, "index.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_log() -> str:
    path = os.path.join(WIKI_DIR, "log.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def append_log(entry: str) -> None:
    """
    Append a log entry to wiki/log.md.
    entry should be a pre-formatted markdown block starting with ## [YYYY-MM-DD].
    """
    path = os.path.join(WIKI_DIR, "log.md")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"\n{entry.strip()}\n")


def read_concept(slug: str) -> str:
    path = os.path.join(CONCEPTS_DIR, f"{slug}.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def write_concept(slug: str, content: str, overwrite: bool = True) -> str:
    path = os.path.join(CONCEPTS_DIR, f"{slug}.md")
    if not overwrite and os.path.exists(path):
        raise FileExistsError(f"Concept already exists: {path}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
