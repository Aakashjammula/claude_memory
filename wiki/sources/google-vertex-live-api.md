---
type: source
title: "Gemini Live API — Vertex AI"
author: Google
date: Unknown
ingested: 2026-04-08
tags: [coding, python, google, llm, audio, api, s2s]
raw: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api
---

## Summary

Google's Gemini Live API is their equivalent of the OpenAI Realtime API — a stateful WebSocket connection enabling low-latency bidirectional audio (and video) interaction with Gemini models. It supports native speech-to-speech, function calling, VAD, barge-in, and multimodal input (text, audio, image, video). The flagship model is `gemini-live-2.5-flash-native-audio`.

Key differentiator from Azure OpenAI Realtime: significantly cheaper (audio input ~10× less expensive), larger context window (128k vs 32k tokens), and native video input support. Trade-off: session duration is capped at 10–15 min, and audio input uses 16kHz (vs Azure's 24kHz).

## Key Points

- **Two models:** `gemini-live-2.5-flash-native-audio` (GA, use this) and a preview variant deprecated 2026-03-19
- **Audio input format:** 16-bit PCM, **16kHz**, little-endian ← note: different from Azure (24kHz)
- **Audio output format:** 16-bit PCM, **24kHz**, little-endian
- **Supports many input formats:** AAC, FLAC, MP3, OGG, WAV, WebM, video formats
- **Context window:** 128k tokens (4× larger than Azure's 32k)
- **Session limits:** ~10 min connection, 15 min audio-only, 2 min video+audio
- **Session extension:** Use context window compression to extend beyond limits
- **Concurrent sessions:** 1,000 per project (Vertex AI)
- **TPM:** 4M tokens/minute
- **Video input:** ✅ Yes — JPEG at 1 FPS, 768×768 recommended
- **Function calling:** ✅ Yes — multi-function per turn, chain outputs
- **Barge-in:** ✅ Built-in — VAD detects interruption, cancels generation immediately
- **Session resumption:** ✅ `SessionResumptionUpdate` checkpoints for reconnect
- **Affective dialog:** ✅ Model adapts tone/expression to user speech
- **Languages:** 24 languages supported
- **Connection options:** Gen AI SDK (Python), raw WebSocket, ADK, partner WebRTC (Daily, LiveKit, Twilio, Voximplant)

## Pricing (Gemini 2.5 Flash Live API)

| Token Type | Price per 1M tokens |
|------------|-------------------|
| Text input | $0.50 |
| Audio input | **$3.00** |
| Video/image input | $3.00 |
| Text output | $2.00 |
| Audio output | **$12.00** |

⚠️ **Billing note:** Charged per turn for ALL tokens in session context window (new tokens + accumulated history). Long sessions get expensive fast.

## Session Config (Python Gen AI SDK)

```python
from google import genai

client = genai.Client()

config = {
    "model": "gemini-live-2.5-flash-native-audio",
    "generation_config": {
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {
                "prebuilt_voice_config": {"voice_name": "Puck"}
            }
        }
    },
    "system_instruction": "You are a helpful assistant.",
    "tools": [...]  # function definitions
}

async with client.aio.live.connect(model=config["model"], config=config) as session:
    # send audio
    await session.send(input=audio_bytes, end_of_turn=False)
    # receive
    async for response in session.receive():
        if response.data:
            audio_out = response.data  # PCM bytes
```

## Key Events / Message Types

| Message | Direction | Purpose |
|---------|-----------|---------|
| `BidiGenerateContentSetup` | Client → Server | Initial session config |
| `BidiGenerateContentRealtimeInput` | Client → Server | Stream audio/video |
| `BidiGenerateContentClientContent` | Client → Server | Text input or turn end |
| `BidiGenerateContentToolResponse` | Client → Server | Return tool call result |
| `BidiGenerateContentServerContent` | Server → Client | Audio/text response chunks |
| `BidiGenerateContentToolCall` | Server → Client | Function call request |
| `BidiGenerateContentToolCallCancellation` | Server → Client | Tool call cancelled (barge-in) |
| `BidiGenerateContentTranscription` | Server → Client | Speech transcript |
| `SessionResumptionUpdate` | Server → Client | Checkpoint for reconnect |
| `GoAway` | Server → Client | Connection about to close |
| `UsageMetadata` | Server → Client | Token usage stats |

## Models

| Model | Status | Notes |
|-------|--------|-------|
| `gemini-live-2.5-flash-native-audio` | GA ✅ | Recommended — low latency voice agents |
| `gemini-live-2.5-flash-preview-native-audio-09-2025` | ~~Preview~~ **Deprecated 2026-03-19** | Do not use |

## Connections

- Platform → [[google-vertex-ai]]
- Architecture comparison → [[speech-to-speech-agents]]
- Competitor reference → [[azure-openai-realtime-audio]], [[azure-openai-realtime-models]]

## Open Questions

- Does context window compression affect response quality for long voice sessions?
- How does affective dialog interact with function calling — does emotional tone persist through tool use turns?
- What's the latency difference vs Azure in practice for European/Asian regions?
- Is there a PTU (provisioned throughput) equivalent for guaranteed session capacity?
