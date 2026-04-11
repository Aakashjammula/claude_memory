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
