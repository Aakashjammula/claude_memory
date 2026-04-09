---
type: concept
tags: [coding, python, azure, llm, audio, api]
sources: 1
---

## Definition

A realtime audio API is a persistent bidirectional connection (WebSocket or WebRTC) between a client and an LLM backend that streams speech in and speech out with low enough latency (~100–200ms) for natural conversation — eliminating the classic STT → LLM → TTS pipeline and replacing it with a single session.

## Explanation

Traditional voice AI pipelines chain three separate models: a speech-to-text model converts audio to text, an LLM generates a text response, a text-to-speech model converts that response back to audio. Each hop adds latency and loses emotional/prosodic information. Realtime APIs collapse this into one model handling audio end-to-end.

The key architectural shift: instead of request/response (send a full prompt, get a full completion), the client opens a persistent session and streams events both ways. Audio comes in as chunked PCM16 bytes; audio comes out the same way. The model handles voice activity detection (VAD) itself — it decides when the user has finished speaking and begins generating a response.

**Three connection modes depending on your use case:**
- **WebRTC** (~100ms) — browser/mobile apps; client-side; lowest latency
- **WebSocket** (~200ms) — server-to-server; backend middleware; more control
- **SIP** — telephony, call centers, IVR systems

**The session is stateful.** Unlike a regular LLM call, the connection maintains conversation history, voice settings, and VAD configuration across turns. You configure it once at session start via `session.update()`.

**Server VAD** is the practical way to handle turn detection. You stream raw audio without worrying about silence boundaries — the server detects when the user stops speaking and automatically triggers response generation.

## Evidence & Examples

- Azure OpenAI's GPT Realtime API (WebSocket mode, Python) — [[azure-openai-realtime-audio]]
- Supports models: gpt-realtime, gpt-4o-realtime-preview — [[azure-openai-realtime-audio]]
- PCM16 at 24kHz mono is the required audio format — [[azure-openai-realtime-audio]]

## Key Implementation Notes

- Audio chunk size: 4800 bytes = 100ms at 24kHz 16-bit mono
- Endpoint swap: `https://` → `wss://` + `/openai/v1`
- Same OpenAI Python SDK — just set `websocket_base_url`
- Always `commit()` audio buffer to trigger response
- Listen for `response.done` to know when to stop consuming events

## Connections

- Implemented by → [[azure-openai]]
- Referenced in → [[azure-openai-realtime-audio]]
- Architecture patterns, tool use, VAD, barge-in → [[speech-to-speech-agents]]
- Replaces classic STT → LLM → TTS pipeline
- Related to streaming LLM APIs generally *(no page yet)*

## Tensions & Open Questions

- WebRTC gives lower latency but is harder to control server-side; WebSocket is easier but adds ~100ms — which to choose for a given product?
- Server VAD is convenient but may mis-trigger on background noise — what's the fallback?
- Stateful sessions create reconnection complexity (what happens if the connection drops mid-conversation?)
