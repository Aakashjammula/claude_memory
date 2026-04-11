"""
generate_ps_notes.py
--------------------
Generates daily notes pages for the Probability & Statistics study plan
using the actual video titles extracted from YouTube playlists.

Run from claude_memory/code/:
    uv run python generate_ps_notes.py
"""

import json
import os

BASE = os.path.dirname(os.path.dirname(__file__))
NOTES_DIR = os.path.join(BASE, "wiki", "notes")
RAW_DIR = os.path.join(BASE, "raw")

os.makedirs(NOTES_DIR, exist_ok=True)

# Load video data
with open(os.path.join(RAW_DIR, "introduction-to-statistics-and-data-analysis.json"), encoding="utf-8") as f:
    stats_data = json.load(f)
with open(os.path.join(RAW_DIR, "probability-bootcamp.json"), encoding="utf-8") as f:
    prob_data = json.load(f)

stats_videos = stats_data["videos"]   # index 0..34
prob_videos  = prob_data["videos"]    # index 0..43

STATS_PL = "https://www.youtube.com/playlist?list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx"
PROB_PL  = "https://www.youtube.com/playlist?list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V"

# Day schedule: (file_slug, date, day_of_week, week_label, videos_list)
# videos_list = list of (video_dict, playlist_label)
schedule = [
    ("may-10-ps-1",  "2026-05-10", "Saturday",  "Week 1",
     [(stats_videos[0], "Stats"), (stats_videos[1], "Stats"), (stats_videos[2], "Stats")]),

    ("may-11-ps-2",  "2026-05-11", "Sunday",    "Week 1",
     [(stats_videos[3], "Stats"), (stats_videos[4], "Stats"), (stats_videos[5], "Stats")]),

    ("may-12-ps-3",  "2026-05-12", "Monday",    "Week 1",
     [(stats_videos[6], "Stats"), (stats_videos[7], "Stats"), (stats_videos[8], "Stats")]),

    ("may-13-ps-4",  "2026-05-13", "Tuesday",   "Week 1",
     [(stats_videos[9], "Stats"), (stats_videos[10], "Stats"), (stats_videos[11], "Stats")]),

    ("may-14-ps-5",  "2026-05-14", "Wednesday", "Week 1",
     [(stats_videos[12], "Stats"), (stats_videos[13], "Stats"), (stats_videos[14], "Stats")]),

    ("may-15-ps-6",  "2026-05-15", "Thursday",  "Week 1",
     [(stats_videos[15], "Stats"), (stats_videos[16], "Stats"), (stats_videos[17], "Stats")]),

    ("may-16-ps-7",  "2026-05-16", "Friday",    "Week 1",
     [(stats_videos[18], "Stats"), (stats_videos[19], "Stats"), (stats_videos[20], "Stats")]),

    ("may-17-ps-8",  "2026-05-17", "Saturday",  "Week 2",
     [(stats_videos[21], "Stats"), (stats_videos[22], "Stats"), (stats_videos[23], "Stats")]),

    ("may-18-ps-9",  "2026-05-18", "Sunday",    "Week 2",
     [(stats_videos[24], "Stats"), (stats_videos[25], "Stats"), (stats_videos[26], "Stats")]),

    ("may-19-ps-10", "2026-05-19", "Monday",    "Week 2",
     [(stats_videos[27], "Stats"), (stats_videos[28], "Stats"), (stats_videos[29], "Stats")]),

    ("may-20-ps-11", "2026-05-20", "Tuesday",   "Week 2",
     [(stats_videos[30], "Stats"), (stats_videos[31], "Stats"), (stats_videos[32], "Stats")]),

    ("may-21-ps-12", "2026-05-21", "Wednesday", "Week 2",
     [(stats_videos[33], "Stats"), (stats_videos[34], "Stats")]),

    ("may-22-ps-13", "2026-05-22", "Thursday",  "Week 2",
     [(prob_videos[0], "Prob"), (prob_videos[1], "Prob"), (prob_videos[2], "Prob")]),

    ("may-23-ps-14", "2026-05-23", "Friday",    "Week 2",
     [(prob_videos[3], "Prob"), (prob_videos[4], "Prob"), (prob_videos[5], "Prob"), (prob_videos[6], "Prob")]),

    ("may-24-ps-15", "2026-05-24", "Saturday",  "Week 3",
     [(prob_videos[7], "Prob"), (prob_videos[8], "Prob"), (prob_videos[9], "Prob")]),

    ("may-25-ps-16", "2026-05-25", "Sunday",    "Week 3",
     [(prob_videos[10], "Prob"), (prob_videos[11], "Prob"), (prob_videos[12], "Prob")]),

    ("may-26-ps-17", "2026-05-26", "Monday",    "Week 3",
     [(prob_videos[13], "Prob"), (prob_videos[14], "Prob"), (prob_videos[15], "Prob")]),

    ("may-27-ps-18", "2026-05-27", "Tuesday",   "Week 3",
     [(prob_videos[16], "Prob"), (prob_videos[17], "Prob"), (prob_videos[18], "Prob")]),

    ("may-28-ps-19", "2026-05-28", "Wednesday", "Week 3",
     [(prob_videos[19], "Prob"), (prob_videos[20], "Prob"), (prob_videos[21], "Prob")]),

    ("may-29-ps-20", "2026-05-29", "Thursday",  "Week 3",
     [(prob_videos[22], "Prob"), (prob_videos[23], "Prob"), (prob_videos[24], "Prob")]),

    ("may-30-ps-21", "2026-05-30", "Friday",    "Week 3",
     [(prob_videos[25], "Prob"), (prob_videos[26], "Prob"), (prob_videos[27], "Prob")]),

    ("may-31-ps-22", "2026-05-31", "Saturday",  "Week 4",
     [(prob_videos[28], "Prob"), (prob_videos[29], "Prob"), (prob_videos[30], "Prob")]),

    ("jun-01-ps-23", "2026-06-01", "Sunday",    "Week 4",
     [(prob_videos[31], "Prob"), (prob_videos[32], "Prob"), (prob_videos[33], "Prob")]),

    ("jun-02-ps-24", "2026-06-02", "Monday",    "Week 4",
     [(prob_videos[34], "Prob"), (prob_videos[35], "Prob"), (prob_videos[36], "Prob")]),

    ("jun-03-ps-25", "2026-06-03", "Tuesday",   "Week 4",
     [(prob_videos[37], "Prob"), (prob_videos[38], "Prob"), (prob_videos[39], "Prob")]),

    ("jun-04-ps-26", "2026-06-04", "Wednesday", "Week 4",
     [(prob_videos[40], "Prob"), (prob_videos[41], "Prob")]),

    ("jun-05-ps-27", "2026-06-05", "Thursday",  "Week 4",
     [(prob_videos[42], "Prob"), (prob_videos[43], "Prob")]),

    ("jun-06-ps-28", "2026-06-06", "Friday",    "Week 4 — Review", []),
    ("jun-07-ps-29", "2026-06-07", "Saturday",  "Week 4 — Consolidation", []),
]

def playlist_link(label):
    return STATS_PL if label == "Stats" else PROB_PL

def playlist_name(label):
    return "Introduction to Statistics and Data Analysis" if label == "Stats" else "Probability Bootcamp"

def make_note(slug, date, dow, week, videos, next_slug):
    lines = []
    lines.append("---")
    lines.append("type: note")
    lines.append(f"date: {date}")
    lines.append(f"phase: Prob/Stats {week}")
    if videos:
        pl_label = videos[0][1]
        lines.append(f"playlist: {playlist_name(pl_label)}")
    lines.append("tags: [probability, statistics, math, ml, coding]")
    lines.append("---")
    lines.append("")

    # Title
    day_num = slug.split("-ps-")[1]
    if videos:
        vid_titles = " / ".join(v["title"][:40] for v, _ in videos[:2])
        lines.append(f"# Prob/Stats Day {day_num} — {vid_titles}{'...' if len(videos) > 2 else ''}")
    elif "Review" in week:
        lines.append(f"# Prob/Stats Day {day_num} — Full Review")
    else:
        lines.append(f"# Prob/Stats Day {day_num} — Consolidation & Formula Sheet")

    lines.append(f"**Date:** {dow}, {date}")
    lines.append(f"**Phase:** Prob/Stats {week}")
    lines.append("")
    lines.append("---")
    lines.append("")

    if videos:
        pl_label = videos[0][1]
        lines.append("## Playlist")
        lines.append(f"**{playlist_name(pl_label)}**")
        lines.append(f"Link: {playlist_link(pl_label)}")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Videos")
        lines.append("")

        for i, (v, label) in enumerate(videos, 1):
            lines.append(f"### Video {i} — {v['title']}")
            dur_min = int(v['duration'] // 60) if v['duration'] else "?"
            lines.append(f"**Link:** {v['url']}")
            lines.append(f"**Duration:** ~{dur_min} min")
            lines.append(f"**Playlist:** {playlist_name(label)} #{v['index']}")
            lines.append("")
            lines.append("**Concepts covered:**")
            lines.append("-")
            lines.append("")
            lines.append("**Key formulas / definitions:**")
            lines.append("```")
            lines.append("")
            lines.append("```")
            lines.append("")
            lines.append("**Notes:**")
            lines.append("```")
            lines.append("")
            lines.append("```")
            lines.append("")
            lines.append("**What was surprising or hard:**")
            lines.append("-")
            lines.append("")

    elif "Review" in week:
        lines.append("## Review Day")
        lines.append("")
        lines.append("**Task:** Re-watch the 3-5 videos you found hardest. No new content.")
        lines.append("")
        lines.append("### Videos to Re-watch")
        lines.append("- ")
        lines.append("- ")
        lines.append("- ")
        lines.append("")
        lines.append("### Key Formula Sheet (write from memory, then check)")
        lines.append("")
        lines.append("| Concept | Formula |")
        lines.append("|---------|---------|")
        lines.append("| E[X] discrete | |")
        lines.append("| E[X] continuous | |")
        lines.append("| Var(X) | |")
        lines.append("| Bayes theorem | |")
        lines.append("| Binomial PMF | |")
        lines.append("| Normal PDF | |")
        lines.append("| Poisson PMF | |")
        lines.append("| MLE objective | |")
        lines.append("| Law of Large Numbers | |")
        lines.append("| Central Limit Theorem | |")
        lines.append("")
    else:
        lines.append("## Consolidation Day")
        lines.append("")
        lines.append("**Task:** Write a 1-page summary of everything learned — from memory only. Then check against notes.")
        lines.append("")
        lines.append("### My Summary (from memory)")
        lines.append("```")
        lines.append("")
        lines.append("```")
        lines.append("")
        lines.append("### Gaps Found")
        lines.append("-")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Key Takeaways")
    lines.append("-")
    lines.append("")
    lines.append("## What Was Hard")
    lines.append("-")
    lines.append("")
    lines.append("## What to Revisit")
    lines.append("-")
    lines.append("")
    if next_slug:
        lines.append(f"_Next: [[{next_slug}]]_")

    return "\n".join(lines)


created = []
for i, (slug, date, dow, week, videos) in enumerate(schedule):
    next_slug = schedule[i + 1][0] if i + 1 < len(schedule) else ""
    content = make_note(slug, date, dow, week, videos, next_slug)
    filepath = os.path.join(NOTES_DIR, f"{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    created.append(slug)
    print(f"Created: {slug}.md ({len(videos)} videos)")

print(f"\nDone! Created {len(created)} notes files in wiki/notes/")
