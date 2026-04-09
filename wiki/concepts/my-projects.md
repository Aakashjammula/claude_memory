---
type: concept
tags: [coding, personal]
sources: 0
---

# My Projects

_Index of personal coding projects. Updated as projects are added or discussed._

| Project | Status | Stack | Notes |
|---------|--------|-------|-------|
| Generalized S2S Model | Active | Python, Azure OpenAI Realtime API | Reusable speech-to-speech framework with tool/function calling support |

---

## Generalized S2S Model

**Status:** Active
**Stack:** Python, Azure OpenAI Realtime API (WebSocket), PCM16 audio
**Goal:** A generalized, reusable speech-to-speech agent framework that handles the full real-time voice pipeline — audio streaming, VAD, tool use, interruption/barge-in — so individual projects can be built on top without re-implementing the plumbing.

**Key capabilities being built:**
- Persistent WebSocket session to Azure OpenAI gpt-realtime
- Server VAD for automatic turn detection
- Tool/function calling mid-conversation (user speaks → model decides to call a tool → result fed back → model responds by voice)
- Barge-in / interruption handling (user interrupts model mid-speech)
- Chunked PCM16 audio streaming (4800 bytes / 100ms chunks)

**Relevant wiki pages:**
- [[azure-openai-realtime-audio]] — Core API reference (session config, event types, auth)
- [[speech-to-speech-agents]] — Architecture patterns, tool use flow, VAD choices, barge-in
- [[realtime-audio-api]] — The paradigm (why S2S vs STT→LLM→TTS)

---

_Add projects by telling Claude: "add project X — [brief description, stack, status]"_
