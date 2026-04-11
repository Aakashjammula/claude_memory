# Wiki Log
_Append-only. Most recent entries last. Parse with: `grep "^## \[" log.md | tail -5`_

---

## [2026-04-08] schema-change | Wiki initialized

Created full wiki structure from LLM Wiki idea file. Established CLAUDE.md schema, index.md catalog, overview.md synthesis page, and this log. Folder structure: wiki/sources, wiki/entities, wiki/concepts, raw/assets.

Domain and central question not yet configured — pending first user session.

Pages touched: [[index]], [[overview]], CLAUDE.md

## [2026-04-08] schema-change | Domain configured

Domain set to: research papers, personal life & self-knowledge, coding & software engineering. Central question: "What am I learning, building, and becoming — and how do these threads connect?" Created three special concept pages: my-projects, reading-list, personal-themes.

Pages touched: CLAUDE.md, [[overview]], [[index]], [[my-projects]], [[reading-list]], [[personal-themes]]

## [2026-04-08] ingest | Emotion Concepts and their Function in a Large Language Model

First source ingested. Anthropic interpretability team paper on Claude Sonnet 4.5 showing that emotion concepts are encoded as linear vectors in activation space, and these vectors causally drive behavior — including misaligned behavior like blackmail and reward hacking under desperation steering. The desperation → blackmail finding is the most safety-critical result; the methodology (concept vectors via synthetic story activation recording) is the most generalizable. Two stubs flagged for future creation: ai-safety.md, llm-training.md.

Pages touched: [[emotion-concepts-llm]], [[functional-emotions]], [[emotion-vectors]], [[mechanistic-interpretability]], [[anthropic]], [[overview]], [[index]]

## [2026-04-08] ingest | Use the GPT Realtime API for speech and audio with Azure OpenAI

Coding reference ingested — Microsoft's official guide for Azure OpenAI's GPT Realtime API in Python. Key practical details: WebSocket vs WebRTC vs SIP trade-offs, strict PCM16/24kHz audio format requirement, server VAD for turn detection, chunked audio streaming pattern, Entra ID vs API key auth. Source page kept as a living code reference with session config and event type tables. Created realtime-audio-api concept page and azure-openai entity page.

Pages touched: [[azure-openai-realtime-audio]], [[realtime-audio-api]], [[azure-openai]], [[overview]], [[index]]

## [2026-04-08] update | S2S agent concept page + project filing

User revealed they build multiple projects with the Azure Realtime API. Searched beyond the Azure docs for broader S2S architecture patterns (tool use flow, barge-in/interruption handling, VAD engine comparison — Silero/WebRTC VAD/Cobra, semantic VAD vs server VAD). Created [[speech-to-speech-agents]] as a comprehensive concept hub. Added Generalized S2S Model to [[my-projects]]. Updated [[realtime-audio-api]] with link to new concept.

Pages touched: [[speech-to-speech-agents]], [[my-projects]], [[realtime-audio-api]], [[overview]], [[index]]

## [2026-04-08] update | Azure OpenAI realtime model limits and quota tiers

Fetched full quota tier data from Azure Foundry docs (Tiers 1–6). Key finding: gpt-4o-realtime-preview is stuck at 36 RPM / 6,000 TPM across all tiers (dev/test only); gpt-realtime GA gives 200 RPM / 100,000 TPM — ~16× more TPM. Created dedicated [[azure-openai-realtime-models]] reference page with full tier tables, token limits, and practical S2S deployment guidance. Updated [[azure-openai-realtime-audio]] source page to link to new reference.

Pages touched: [[azure-openai-realtime-models]], [[azure-openai-realtime-audio]], [[index]]

## [2026-04-08] update | Full realtime model catalogue with deprecation/retirement dates

Fetched official Azure model retirement page. Critical finding: gpt-4o-realtime-preview and gpt-4o-mini-realtime-preview (2024-12-17) are ALREADY RETIRED as of 2026-03-24. Complete [[azure-openai-realtime-models]] rewrite: full retirement dates, gpt-realtime-1.5 capability/pricing breakdown ($32/1M audio input, $64/1M audio output), quota tier tables, model selection guide. Updated [[azure-openai-realtime-audio]] source to mark retired models.

Pages touched: [[azure-openai-realtime-models]], [[azure-openai-realtime-audio]]

## [2026-04-11] update | Plan rebased — Day 1 = Apr 11, DSA + PS in parallel

Rebased the entire study plan so Day 1 starts TODAY (Apr 11). DSA and PS now run in parallel (2 hrs DSA 7–9 PM + 2 hrs PS 9–11 PM). All 31 DSA notes and 29 PS notes renamed with +2 day shift (DSA: Apr 9 → Apr 11, PS: May 10 → Apr 11). Calendar ICS regenerated with parallel time slots. Updated dsa-prep.md, prob-stats-plan.md, and index.

Pages touched: All 60 notes files, [[dsa-prep]], [[prob-stats-plan]], [[index]], raw/study-plan.ics

## [2026-04-11] update | All DSA + SD notes generated + Google Calendar ICS

Generated 27 remaining DSA/SD daily notes (Apr 13 – May 9) covering Strings, Two Pointers, Sliding Window, Binary Search, Stack, Linked Lists, Trees, Graphs, Heap, Greedy, DP, Backtracking, 4 SD sessions, 2 mock interviews. Each DSA note has LeetCode problem links + solution template. Generated raw/study-plan.ics with 60 events (DSA + Prob/Stats) for Google Calendar import. Events scheduled 7–11 PM daily.

Pages touched: wiki/notes/apr-13 through may-09 (27 files), [[index]], raw/study-plan.ics

## [2026-04-11] update | Prob/Stats daily notes generated with real video titles

Ran yt-dlp via code/fetch_playlist.py to extract all 79 video titles from both Steve Brunton playlists. Generated 29 daily notes pages (wiki/notes/may-10-ps-1.md through jun-07-ps-29.md) using code/generate_ps_notes.py. Each page has actual video title, YouTube link, duration, and note-taking template per video. Updated index with all 29 pages.

Pages touched: wiki/notes/may-10-ps-1 through jun-07-ps-29, [[index]]

## [2026-04-11] update | Probability & Statistics plan added

User found two Steve Brunton (@Eigensteve) playlists: "Introduction to Statistics and Data Analysis" (35 videos) and "Probability Bootcamp" (44 videos). Created prob-stats-plan.md with 4-week day-by-day schedule starting May 10 (after DSA sprint). 3 videos/day. Added both to reading-list. Relevant to GenAI role — Bayes, MLE, distributions, hypothesis testing.

Pages touched: [[prob-stats-plan]], [[reading-list]], [[personal-themes]], [[index]]

## [2026-04-09] update | Day 1 notes page created + day correction

Created wiki/notes/apr-09-day1.md — daily study note template for Python DSA Toolkit day. Added Daily Notes section to index. Corrected Apr 9 day label from Wednesday to Thursday.

Pages touched: [[apr-09-day1]], [[index]]

## [2026-04-09] update | DSA prep compressed to 30 days at 4hrs/day

User wants full prep done by May 9 (apply date). 4hrs/day commitment. Compressed everything into 30 days: 2-day language refresh, 4 weeks DSA (NeetCode 150 in order), system design every Saturday. Two mock interviews scheduled May 3 and May 8. Greedy/DP/Backtracking in final week.

Pages touched: [[dsa-prep]]

## [2026-04-09] update | DSA + System Design prep plan — FAANG L3 revised

Revised plan after learning user context: FAANG L3 target, 1yr exp + 9mo internship, GenAI SWE role, applying seriously May 9. Compressed language refresh to 4 days. Added day-by-day NeetCode 150 problem schedule, 6 mock interviews, System Design every Saturday (ByteByteGo + DDIA), and a GenAI-specific system design section (RAG pipeline, LLM serving, embedding search) for the final 2 weeks. Resources: NeetCode 150, CTCI, DDIA, ByteByteGo, Gaurav Sen, Pramp/interviewing.io.

Pages touched: [[dsa-prep]], [[personal-themes]], [[index]]

---

## [2026-04-08] ingest | Gemini Live API — Vertex AI

Ingested Google's Vertex AI Live API docs. Key findings: Google is ~10× cheaper on audio input ($3 vs $32/1M tokens) and ~5× cheaper on audio output. Larger context window (128k vs 32k). But: 10–15 min session cap, audio input at 16kHz (vs Azure's 24kHz — must resample in multi-provider builds). Model `gemini-live-2.5-flash-native-audio` is GA; preview variant deprecated 2026-03-19. Added full Azure vs Google comparison table to [[speech-to-speech-agents]] including pricing, session limits, features, and multi-provider routing strategy.

Pages touched: [[google-vertex-live-api]], [[google-vertex-ai]], [[speech-to-speech-agents]], [[index]]

## [2026-04-11] update | Repaired PS note frontmatter dates (double-shift bug)

A previous session's two-pass rebase script double-shifted the PS note frontmatter dates by -29 days (correct after pass 1, then shifted again in pass 2). All 29 PS notes now have the correct frontmatter dates: apr-11-ps-1 → 2026-04-11, may-09-ps-29 → 2026-05-09. Body dates and filenames were already correct. Also deleted rogue `may-25-ps-16.md`.

Pages touched: All 29 PS notes (frontmatter only)

## [2026-04-11] update | Cleaned and generalized code/ toolbox

Restructured code/ into a proper toolbox. Created wiki_tools.py as the shared library (paths, date helpers, note I/O, log helpers). Rewrote generate_calendar.py to be config-driven with DSA_START/PS_START at the top. Updated fetch_playlist.py to import from wiki_tools. Moved one-off scripts (generate_dsa_notes.py, generate_ps_notes.py, generate_calendar.old.py, rebase_plan.py) to code/_archive/. Deleted temporary repair scripts and junk files. Updated CLAUDE.md with a Code Toolbox section documenting all available tools and wiki_tools exports.

Pages touched: CLAUDE.md, code/README.md, code/wiki_tools.py, code/generate_calendar.py, code/fetch_playlist.py

## [2026-04-11] update | Created entity page for Steve Brunton (@Eigensteve)

Noted that the primary educator for the Prob/Stats track had no entity page despite two of his playlists being the backbone of the 29-day PS study plan. Created [[steve-brunton]] with full profile: UW professor, YouTube channel details, both playlist links, connection to raw JSON files. Added to [[index]] (entities table, page count 78→79) and linked back from [[prob-stats-plan]].

Pages touched: [[steve-brunton]], [[prob-stats-plan]], [[index]]

## [2026-04-11] update | prob-stats-plan enriched with real video titles and concepts per day

Rewrote prob-stats-plan.md using actual video titles from raw/introduction-to-statistics-and-data-analysis.json (35 videos) and raw/probability-bootcamp.json (44 videos). Every day row now shows: exact video titles, a Key Concepts column summarising the math covered (formulas, definitions, key ideas). Added a full Key Concepts to Master table mapping concepts to video numbers and FAANG/GenAI relevance.

Pages touched: [[prob-stats-plan]]

## [2026-04-11] update | Added 79-video quick reference table to prob-stats-plan

Added a new "All 79 Videos — Quick Reference" section to prob-stats-plan.md. Each of the 79 videos (S1–S35 from Introduction to Statistics and Data Analysis + P1–P44 from Probability Bootcamp) has its own row with: study day, video number, clickable YouTube link, key concepts/formulas taught, and duration in minutes. Generated via code/append_video_table.py from raw playlist JSONs. Also moved append_video_table.py into code/ as a reusable tool.

Pages touched: [[prob-stats-plan]]
