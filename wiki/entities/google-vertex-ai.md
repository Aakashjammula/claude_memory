---
type: entity
subtype: product
aliases: [Google Cloud AI, Vertex AI, Google AI, Gemini API]
tags: [coding, google, llm, audio, api]
sources: 1
---

## Overview

Google's cloud AI platform hosting Gemini models via Vertex AI. The Live API is their realtime speech-to-speech offering — a direct competitor to Azure OpenAI's Realtime API. Significantly cheaper on audio tokens (~10× less than Azure), with larger context windows and native video input, but with session duration caps and a 16kHz audio input format.

## Key Facts

- Live API uses `gemini-live-2.5-flash-native-audio` as the GA realtime model — [[google-vertex-live-api]]
- Audio pricing: $3/1M audio input, $12/1M audio output — [[google-vertex-live-api]]
- Context window: 128k tokens (4× Azure's 32k) — [[google-vertex-live-api]]
- Concurrent sessions: 1,000 per project; TPM: 4M/min — [[google-vertex-live-api]]
- Session cap: 10–15 min (extendable with context compression) — [[google-vertex-live-api]]
- Supports video input (1 FPS JPEG) — unique vs Azure — [[google-vertex-live-api]]

## Role in Wiki

Primary alternative to Azure OpenAI for S2S projects. Cost advantage is substantial for audio-heavy applications. Relevant when evaluating multi-provider strategy or building cost-sensitive voice agents.

## Appearances

- [[google-vertex-live-api]] — Live API how-to and reference

## Open Questions

- How does Vertex AI regional pricing vary vs Azure for non-US deployments?
- Is there a PTU/provisioned throughput equivalent for Live API?
