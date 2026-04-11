"""
fetch_playlist.py
-----------------
Uses yt-dlp to extract playlist metadata (titles, URLs, descriptions)
and saves them as JSON files in raw/

Install: uv add yt-dlp  (inside code/ folder)

Usage:
    # Fetch default playlists (hardcoded)
    uv run python fetch_playlist.py

    # Fetch a specific playlist URL
    uv run python fetch_playlist.py "https://www.youtube.com/playlist?list=PLxxx"

    # Fetch multiple URLs
    uv run python fetch_playlist.py "https://..." "https://..."
"""

import json
import os
import re
import subprocess
import sys
from urllib.parse import urlparse, parse_qs

RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "raw")
os.makedirs(RAW_DIR, exist_ok=True)

# Default playlists — used when no URL is passed as argument
DEFAULT_PLAYLISTS = [
    {
        "url": "https://www.youtube.com/playlist?list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
    },
    {
        "url": "https://www.youtube.com/playlist?list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
    },
]


def url_to_slug(url: str) -> str:
    """Derive a filename slug from a YouTube playlist URL."""
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    playlist_id = qs.get("list", ["unknown"])[0]
    return f"playlist-{playlist_id[:12]}"


def fetch_playlist(url: str) -> tuple[str, list[dict]]:
    """
    Run yt-dlp --flat-playlist on a URL.
    Returns (playlist_title, list_of_video_dicts).
    """
    print(f"\nFetching: {url}")

    # First grab playlist title
    title_cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--print", "%(playlist_title)s",
        "--playlist-items", "1",
        "--no-warnings",
        url,
    ]
    try:
        title_result = subprocess.run(title_cmd, capture_output=True, text=True, timeout=60)
        playlist_title = title_result.stdout.strip().splitlines()[0] if title_result.stdout.strip() else "Unknown Playlist"
    except Exception:
        playlist_title = "Unknown Playlist"

    # Now grab all video metadata
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--print-json",
        "--no-warnings",
        url,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=120)
    except FileNotFoundError:
        print("ERROR: yt-dlp not found. Run: uv add yt-dlp")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: yt-dlp failed.\n{e.stderr}")
        sys.exit(1)

    videos = []
    for i, line in enumerate(result.stdout.strip().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            videos.append({
                "index": i,
                "title": entry.get("title", "Unknown"),
                "url": f"https://www.youtube.com/watch?v={entry.get('id', '')}" if entry.get("id") else entry.get("url", ""),
                "id": entry.get("id", ""),
                "duration": entry.get("duration"),
                "description": entry.get("description", ""),
            })
        except json.JSONDecodeError:
            continue

    return playlist_title, videos


def save(url: str, playlist_title: str, videos: list[dict]) -> str:
    """Save extracted data as JSON in raw/. Returns the filepath."""
    slug = url_to_slug(url)
    # Use cleaned playlist title as slug if available
    if playlist_title and playlist_title != "Unknown Playlist":
        clean = re.sub(r"[^a-z0-9]+", "-", playlist_title.lower()).strip("-")
        slug = clean[:50]

    out = {
        "playlist_title": playlist_title,
        "playlist_url": url,
        "total_videos": len(videos),
        "videos": videos,
    }
    filepath = os.path.join(RAW_DIR, f"{slug}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(videos)} videos → {filepath}")
    return filepath


def main():
    urls = sys.argv[1:] if len(sys.argv) > 1 else [p["url"] for p in DEFAULT_PLAYLISTS]

    for url in urls:
        url = url.strip().strip('"').strip("'")
        if "youtube.com" not in url and "youtu.be" not in url:
            print(f"Skipping non-YouTube URL: {url}")
            continue

        playlist_title, videos = fetch_playlist(url)
        filepath = save(url, playlist_title, videos)

        print(f"\nPlaylist: '{playlist_title}' ({len(videos)} videos)")
        print("First 5 videos:")
        for v in videos[:5]:
            print(f"  {v['index']:>2}. {v['title']}")
        if len(videos) > 5:
            print(f"  ... and {len(videos) - 5} more")
        print(f"\nJSON saved → {filepath}")
        print("Tell Claude to ingest it to build the notes pages.")


if __name__ == "__main__":
    main()
