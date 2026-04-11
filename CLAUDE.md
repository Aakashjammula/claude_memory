# LLM Wiki — Schema & Operating Rules

This file defines how this wiki works. Every Claude Code session in this vault begins by reading this file. All operations follow these rules. You and the user co-evolve this file over time.

---

## Directory Structure

```
claude_memory/
├── CLAUDE.md               ← this file; the schema
├── wiki/
│   ├── index.md            ← content catalog (always read first)
│   ├── log.md              ← append-only chronological log
│   ├── overview.md         ← evolving high-level synthesis
│   ├── entities/           ← people, organizations, places, products
│   ├── concepts/           ← ideas, frameworks, theories, themes
│   ├── notes/              ← daily study notes (one file per study day)
│   └── sources/            ← one summary page per ingested source
├── raw/                    ← immutable source files (never modified)
│   └── assets/             ← downloaded images and attachments
└── code/
    └── fetch_playlist.py   ← yt-dlp script: extracts YouTube playlist metadata → raw/*.json
```

**Invariants:**
- `raw/` is read-only. The LLM reads sources from here but never writes or modifies them.
- `wiki/` is fully owned by the LLM. The LLM creates, updates, and maintains all files here.
- `CLAUDE.md` is co-owned. The LLM proposes changes; the user approves them.

---

## Session Start Protocol

At the start of every session:
1. Read `CLAUDE.md` (this file).
2. Read `wiki/index.md` to understand the current state of the wiki.
3. Read the last 10 entries of `wiki/log.md` for recent context.
4. Greet the user with a one-line status: how many sources, how many wiki pages, and what was last worked on.

---

## Page Formats

### Source Summary (`wiki/sources/<slug>.md`)

```markdown
---
type: source
title: <full title>
author: <author(s) or "Unknown">
date: <publication date or "Unknown">
ingested: <YYYY-MM-DD>
tags: [<topic1>, <topic2>]
raw: <path to raw file, or URL>
---

## Summary
<2–4 paragraph synthesis. What is this source about? What are its key claims? What evidence does it use?>

## Key Points
- <bullet 1>
- <bullet 2>
- ...

## Notable Quotes
> "<quote>" — <attribution>

## Connections
- Updates/challenges [[concept or entity page]]
- Relates to [[source page]]
- Introduces concept → [[concept page]]

## Open Questions
- <question raised by this source that isn't yet answered in the wiki>
```

### Entity Page (`wiki/entities/<slug>.md`)

```markdown
---
type: entity
subtype: <person | organization | place | product | other>
aliases: [<alternate names>]
tags: [<topic1>, <topic2>]
sources: <count of sources this entity appears in>
---

## Overview
<2–3 sentence description.>

## Key Facts
- <fact 1> — [[source]]
- <fact 2> — [[source]]

## Role in Wiki
<How this entity relates to the main themes and other entities.>

## Appearances
- [[source title]] — <one-line note on how this entity appears>

## Open Questions
- <unresolved questions about this entity>
```

### Concept Page (`wiki/concepts/<slug>.md`)

```markdown
---
type: concept
tags: [<topic1>, <topic2>]
sources: <count>
---

## Definition
<Crisp 1–2 sentence definition.>

## Explanation
<Deeper explanation, 2–4 paragraphs. How does this concept work? Where does it come from?>

## Evidence & Examples
- <example or evidence> — [[source]]

## Connections
- Relates to [[concept]]
- Contrasts with [[concept]]
- Instantiated by [[entity]]

## Tensions & Open Questions
- <unresolved tension or question>
```

### Overview (`wiki/overview.md`)

The evolving synthesis of the entire wiki. Updated on every ingest. Contains:
- The current thesis or central question
- Major themes and how they connect
- Key tensions or unresolved questions
- A map of the most important pages

### Index (`wiki/index.md`)

The content catalog. Format:

```markdown
# Wiki Index
_Last updated: YYYY-MM-DD | Sources: N | Wiki pages: N_

## Sources
| Page | Title | Author | Ingested | Tags |
|------|-------|--------|----------|------|
| [[slug]] | Title | Author | Date | tag1, tag2 |

## Entities
| Page | Type | Summary |
|------|------|---------|
| [[slug]] | person | One-line description |

## Concepts
| Page | Summary |
|------|---------|
| [[slug]] | One-line description |

## Synthesis
- [[overview]] — Current synthesis of all sources
```

### Log (`wiki/log.md`)

Append-only. Each entry:

```markdown
## [YYYY-MM-DD] <operation> | <title or description>

<1–3 sentence note on what happened, what was surprising, what changed.>

Pages touched: [[page1]], [[page2]], ...
```

Operations: `ingest`, `query`, `lint`, `update`, `schema-change`

---

## Code Toolbox

All scripts live in `code/` and run via `uv run python <script>.py` from that directory.
See `code/README.md` for full documentation. Summary:

| Script | What it does | When to use |
|--------|-------------|-------------|
| `wiki_tools.py` | Shared library — paths, date helpers, note I/O | Import in any new tool |
| `fetch_playlist.py` | YouTube playlist → `raw/<slug>.json` | User drops a YouTube playlist URL |
| `generate_calendar.py` | Study plan → `raw/study-plan.ics` | Plan dates change; re-import into Google Calendar |

**`wiki_tools.py` key exports** (always import this instead of duplicating paths):
```python
from wiki_tools import (
    BASE, NOTES_DIR, RAW_DIR, WIKI_DIR, CONCEPTS_DIR,
    date_to_slug, date_to_dow, date_to_display, slug_to_date,
    read_note, write_note, note_exists, list_notes,
    read_index, read_log, append_log,
    read_concept, write_concept,
)
```

**One-off scripts** are in `code/_archive/` — do not re-run them.

---

## YouTube Playlist Workflow

When the user pastes a YouTube playlist URL:
1. Run `uv run python fetch_playlist.py "<url>"` from `code/` — saves to `raw/<slug>.json`
2. Claude reads the JSON from `raw/` — it contains every video title, URL, duration, and index
3. Claude creates daily notes pages in `wiki/notes/` — one file per study day, with a section per video including title, link, and a concepts/notes template
4. Claude updates `wiki/concepts/<plan-slug>.md` with the full dated schedule
5. Claude updates `wiki/index.md` and appends to `wiki/log.md`

**Raw JSON format** (`raw/*.json`):
```json
{
  "playlist_title": "...",
  "playlist_url": "...",
  "total_videos": 35,
  "videos": [
    { "index": 1, "title": "Intro to Statistics", "url": "https://...", "id": "abc123", "duration": 1320 },
    ...
  ]
}
```

---

## Ingest Workflow

When the user says "ingest [source]" or drops a file into `raw/`:

1. **Read** the source file (or URL if provided).
2. **Discuss** with the user: What are the key takeaways? What's surprising? What should be emphasized?
3. **Write** a source summary page in `wiki/sources/`.
4. **Identify** all entities mentioned that warrant their own page. Create new entity pages or update existing ones.
5. **Identify** all concepts introduced or significantly updated. Create new concept pages or update existing ones.
6. **Update** `wiki/overview.md` to reflect how this source shifts the synthesis.
7. **Update** `wiki/index.md` — add the source row; update page counts.
8. **Append** an entry to `wiki/log.md`.
9. **Report** to the user: pages created, pages updated, open questions raised.

Do not ingest passively. Surface tensions. Note where the source contradicts existing wiki content. Ask the user what to do with contradictions.

---

## Query Workflow

When the user asks a question:

1. Read `wiki/index.md` to identify relevant pages.
2. Read the relevant pages.
3. Synthesize an answer with inline citations: [[page-name]].
4. Offer to file the answer as a new wiki page if it represents a non-trivial synthesis.
5. If the question exposes a gap (a concept not yet covered, an entity not yet filed), note it and offer to create a stub.

---

## Lint Workflow

When the user says "lint" or "health check":

1. Scan all wiki pages via `wiki/index.md`.
2. Check for:
   - Orphan pages (no inbound links from any other wiki page)
   - Contradictions between pages (surface them explicitly)
   - Stale claims superseded by newer sources
   - Concepts mentioned in passing but lacking their own page
   - Missing cross-references (entity appears in source summary but has no entity page)
   - Data gaps (important questions with no sourced answer)
3. Produce a lint report and offer to fix each issue.

---

## File Naming Conventions

- All wiki filenames: `lowercase-with-hyphens.md`
- Source slugs: derived from title, e.g. `thinking-fast-and-slow.md`
- Entity slugs: name-based, e.g. `daniel-kahneman.md`, `openai.md`
- Concept slugs: concept-based, e.g. `dual-process-theory.md`, `loss-aversion.md`
- No spaces, no special characters except hyphens

---

## Cross-Referencing Rules

- Use Obsidian wiki-links: `[[page-slug]]` (Obsidian resolves by filename without path).
- Every source summary must link to at least one entity or concept page.
- Every entity and concept page must link back to at least one source.
- The overview must link to all major concept and entity hubs.

---

## Output Format Options

The LLM can produce answers in various formats depending on the question:
- **Markdown page** — default; can be filed into the wiki
- **Comparison table** — for comparing entities or sources
- **Timeline** — for chronological questions
- **Marp slide deck** — for presentations (add `marp: true` to frontmatter)
- **Bullet synthesis** — quick summary format

Always ask or infer which format is most useful.

---

## Schema Evolution

When a rule in this file needs to change (because the wiki has grown, the domain has shifted, or the user's workflow has changed):
1. Propose the change explicitly to the user.
2. Get approval before modifying this file.
3. Log the change in `wiki/log.md` as a `schema-change` entry.

---

## Domain Configuration

_To be filled in by the user. What is this wiki about? What kinds of sources will be ingested? What is the central question or thesis you're pursuing?_

**Domain:** Research papers, personal life & self-knowledge, coding & software engineering

**Central question:** What am I learning, building, and becoming — and how do these threads connect?

**Source types:**
- Research papers (academic PDFs, arXiv, preprints)
- Personal notes, journal entries, reflections, goals
- Coding resources (docs, blog posts, tutorials, project notes, code snippets)

**Tags to use:**
- Research papers: `research`, `paper`, `<field>` (e.g. `ml`, `systems`, `biology`, `economics`)
- Personal: `personal`, `goals`, `health`, `psychology`, `reflection`
- Coding: `coding`, `software`, `<language-or-framework>` (e.g. `python`, `rust`, `react`, `llm`)
- Cross-domain: `insight` (for ideas that connect two or more domains)

**Entity subtypes in use:**
- People: researchers, authors, influencers on your thinking
- Projects: your own coding projects; open-source projects you follow
- Organizations: labs, companies, communities
- Concepts: algorithms, frameworks, mental models, theories

**Special pages to maintain:**
- `wiki/concepts/my-projects.md` — index of personal coding projects with status and notes
- `wiki/concepts/reading-list.md` — papers and resources queued for ingestion
- `wiki/concepts/personal-themes.md` — recurring themes across personal reflections
