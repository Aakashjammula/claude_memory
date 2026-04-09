---
type: source
title: "Use the GPT Realtime API for speech and audio with Azure OpenAI"
author: Microsoft
date: Unknown
ingested: 2026-04-08
tags: [coding, python, azure, llm, audio, api]
raw: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/realtime-audio?tabs=keyless%2Cwindows&pivots=programming-language-python
---

## Summary

Microsoft's official how-to guide for the Azure OpenAI GPT Realtime API — a low-latency "speech in, speech out" API supporting real-time conversational AI with latencies as low as ~100ms (WebRTC) or ~200ms (WebSocket). The API is designed for server-side integration, not direct end-user device connection; your backend manages the audio stream on behalf of users.

The guide covers three connection methods (WebRTC, WebSocket, SIP/telephony), supported models, Python setup, session configuration, audio format requirements, and two full code examples: text-in/audio-out and audio-in/audio-out. Authentication is via Microsoft Entra ID (recommended for production) or API key.

## Key Points

- **Three connection modes:** WebRTC (~100ms, client-side), WebSocket (~200ms, server-side), SIP (telephony/call centers)
- **Audio format is strict:** PCM16, 24kHz, mono. Use `ffmpeg -i input.wav -ar 24000 -ac 1 -f s16le input.pcm` to convert
- **Endpoint is WSS:** `endpoint.replace("https://", "wss://").rstrip("/") + "/openai/v1"`
- **Client:** `AsyncOpenAI(websocket_base_url=base_url, api_key=token)` — same OpenAI SDK, different base URL
- **Session config:** Set instructions, voice, VAD parameters, input/output formats in `connection.session.update()`
- **Server VAD** handles turn detection automatically — no need to manually signal end of speech
- **Send audio in chunks:** 4800 bytes = 100ms at 24kHz 16-bit mono
- **Commit when done:** `connection.input_audio_buffer.commit()` triggers response generation
- **Token limits:** 32k input, 4096 output
- **Entra ID auth:** Get bearer token via `DefaultAzureCredential` + `get_bearer_token_provider`; pass token as `api_key`
- **Don't mix auth:** Unset `AZURE_OPENAI_API_KEY` env var when using Entra ID — they conflict

## Connection Setup Pattern

```python
from openai import AsyncOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(credential, "https://ai.azure.com/.default")
token = token_provider()

base_url = endpoint.replace("https://", "wss://").rstrip("/") + "/openai/v1"
client = AsyncOpenAI(websocket_base_url=base_url, api_key=token)

async with client.realtime.connect(model=deployment_name) as connection:
    await connection.session.update(session={...})
```

## Session Config Reference

```python
{
    "instructions": "You are a helpful assistant.",
    "input_audio_format": "pcm16",
    "output_audio_format": "pcm16",
    "input_audio_transcription": {"model": "whisper-1"},
    "turn_detection": {
        "type": "server_vad",
        "threshold": 0.5,          # VAD confidence (0.0–1.0)
        "prefix_padding_ms": 300,  # audio to include before speech
        "silence_duration_ms": 500, # silence to end turn
        "create_response": True,
    },
    "voice": "alloy",
}
```

## Key Events

| Event | Meaning |
|-------|---------|
| `response.output_text.delta` | Text chunk |
| `response.output_audio.delta` | Audio chunk (base64 PCM16) |
| `response.audio_transcript.delta` | Transcript of audio output |
| `conversation.item.input_audio_transcription.completed` | User speech transcribed |
| `response.done` | Response complete |
| `error` | Something went wrong |

## Sending Audio (chunked)

```python
chunk_size = 4800  # 100ms at 24kHz 16-bit
for i in range(0, len(audio_data), chunk_size):
    chunk = audio_data[i:i + chunk_size]
    await connection.input_audio_buffer.append(audio=base64.b64encode(chunk).decode())
    await asyncio.sleep(0.05)
await connection.input_audio_buffer.commit()
```

## Supported Models

| Model | Version | Notes |
|-------|---------|-------|
| ~~gpt-4o-realtime-preview~~ | 2024-12-17 | ⛔ RETIRED 2026-03-24 — do not use |
| ~~gpt-4o-mini-realtime-preview~~ | 2024-12-17 | ⛔ RETIRED 2026-03-24 — do not use |
| gpt-realtime | 2025-08-28 | GA ✅ — production standard, retires 2027-02-28 |
| gpt-realtime-mini | 2025-12-15 | GA ✅ — latency/cost optimized, retires 2026-12-15 |
| gpt-realtime-1.5 | 2026-02-23 | GA ✅ **Latest** — best tool calling + multilingual, retires no earlier than 2027-02-23 |

→ Full quota limits by tier: [[azure-openai-realtime-models]]

## Connections

- Published by → [[azure-openai]]
- Implements → [[realtime-audio-api]]

## Open Questions

- What are the pricing differences between WebRTC and WebSocket modes?
- Can the session be kept alive across multiple user turns without reconnecting?
- How does server VAD perform with noisy audio / non-English speakers?
- What's the max concurrent sessions per Azure resource?
