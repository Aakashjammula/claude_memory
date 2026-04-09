---
type: concept
tags: [coding, python, audio, llm, ai-safety, insight]
sources: 2
---

## Definition

A speech-to-speech (S2S) agent is a voice AI system where a single model handles the full audio-in/audio-out pipeline in one persistent session — no separate STT, LLM, and TTS stages — enabling natural, low-latency conversation with sub-300ms response times and support for tool/function calling mid-conversation.

## Architecture: S2S vs Chained Pipeline

Two fundamental architectures for voice agents:

| | S2S (Realtime API) | Chained (STT → LLM → TTS) |
|---|---|---|
| Latency | 200–300ms | 800ms–2s |
| Naturalness | High (prosody, emotion preserved) | Lower (robotic cadence) |
| Tool use | Supported, mid-session | Easier to implement |
| Barge-in | Built-in via VAD | Requires custom logic |
| Flexibility | Less (locked to API model) | More (swap any component) |
| Cost | Higher | More controllable |

**Rule of thumb:** Use S2S when natural conversation feel and low latency matter (live customer agents, voice assistants). Use chained when you need fine-grained control over each stage, custom TTS voices, or cost efficiency at scale.

---

## Voice Activity Detection (VAD)

VAD is how the system detects when a user starts and stops speaking. Getting this right is the #1 determinant of conversation feel.

### Server VAD (default, simplest)
The API backend detects silence and auto-triggers response generation.
```python
"turn_detection": {
    "type": "server_vad",
    "threshold": 0.5,           # 0.0–1.0; higher = needs louder audio to trigger
    "prefix_padding_ms": 300,   # audio to keep before detected speech
    "silence_duration_ms": 500, # ms of silence before ending turn (tune per use case)
    "create_response": True,
}
```
**Tuning guidance:**
- Noisy environments → raise `threshold` (0.6–0.8)
- Faster turn detection → lower `silence_duration_ms` (200ms for snappy, 500ms for thoughtful)
- Keep `prefix_padding_ms` at 300ms minimum to avoid clipping word starts

### Semantic VAD (smarter, newer)
Uses a classifier to detect *intent to finish speaking*, not just silence. Scores audio on "probability user is done." When high probability → respond immediately; when low → wait for silence timeout. More natural, handles "um..." and trailing thoughts better.

### Client VAD (advanced, most control)
Run VAD client-side (e.g. Silero VAD, WebRTC VAD, Picovoice Cobra) and only stream voiced segments to the API. Benefits: 75%+ reduction in API data transfer, local noise filtering, no server VAD dependency.

**VAD engine comparison:**
| Engine | Type | Latency | Notes |
|--------|------|---------|-------|
| WebRTC VAD | Rule-based | ~10ms | Google open-source; fast; less accurate on edge cases |
| Silero VAD | Deep learning | ~10ms | Better accuracy; runs locally in Python |
| Picovoice Cobra | Deep learning | ~10ms | Production-ready; most accurate; paid |

---

## Tool / Function Calling

The S2S session supports tool use mid-conversation. The model can decide to call a function, pause audio generation, receive the result, and continue speaking — all without breaking the session.

### Tool definition (session config)
```python
await connection.session.update(session={
    "tools": [
        {
            "type": "function",
            "name": "get_weather",
            "description": "Get current weather for a city. Call this when user asks about weather.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"}
                },
                "required": ["city"]
            }
        }
    ],
    "tool_choice": "auto",  # or "none" / specific function name
})
```

### Tool call event flow
```
user speaks
    → VAD detects end of turn
    → model generates: response.output_item.added (type: function_call)
    → event: response.function_call_arguments.done  ← tool call complete
    → YOUR CODE: execute the function
    → send result back:
        await connection.conversation.item.create(item={
            "type": "function_call_output",
            "call_id": event.call_id,
            "output": json.dumps(result),
        })
    → trigger continuation:
        await connection.response.create()
    → model speaks the answer
```

### Best practices for tool definitions
- Be **extremely specific** in `description` — the model decides when to call based solely on this
- Include parameter types, constraints, and examples in the description
- Keep tool count low — each tool definition consumes tokens and adds latency
- Set `parallel_tool_calls: false` if your tools have side effects (prevents two calls firing simultaneously)
- Validate and sanitize all tool outputs before feeding back — model can act on bad data

---

## Barge-in / Interruption Handling

Barge-in = user speaks while model is speaking → model stops and listens. Critical for natural conversation feel. Without it the agent "talks over" users.

### What must happen on interruption
1. Detect user started speaking (VAD fires during model output)
2. Stop audio playback client-side immediately
3. Cancel in-flight audio generation: `await connection.response.cancel()`
4. Flush queued audio buffers
5. Let the new user turn proceed normally

### Tool call interruptions — special case
If user interrupts mid-tool-call, decide:
- **Reversible tool** (read-only query) → cancel, restart
- **Irreversible tool** (write, payment, send) → let it finish silently, then respond to new user input

```python
# In your tool handler, guard irreversible actions:
async def send_email(args):
    # Don't allow cancellation past this point
    await connection.response.disallow_interruptions()  # if API supports
    # ... execute send
```

### Interruption detection pattern
```python
async for event in connection:
    if event.type == "input_audio_buffer.speech_started":
        # user started talking — cancel current response
        await connection.response.cancel()
        clear_audio_queue()
    elif event.type == "response.audio.delta":
        audio_queue.append(base64.b64decode(event.delta))
    elif event.type == "response.done":
        break
```

---

## Session Lifecycle & Reconnection

- Sessions are stateful but not permanent — connections drop
- Design for reconnect: save conversation history locally, restore on new session via `conversation.item.create` for each prior message
- Keep sessions alive with periodic no-op messages if idle time is long
- Token limits: 32k input, 4096 output — for long conversations, summarize and trim history

---

## Latency Optimization Tips

- Use WebRTC over WebSocket if client-side is feasible (~100ms vs ~200ms)
- Stream audio output to speakers as chunks arrive — don't wait for `response.done`
- Use smaller realtime models (gpt-realtime-mini) for latency-sensitive flows; full model for complex tool reasoning
- Run client VAD to avoid streaming silence to the API
- Keep tool execution fast — every ms of tool latency adds to perceived response time
- Process audio in 10–20ms frames for barge-in detection

---

---

## Provider Comparison: Azure OpenAI vs Google Vertex Live API

Two major providers for production S2S. Key differences:

### Audio Format
| | Azure OpenAI | Google Vertex Live |
|---|---|---|
| Input format | PCM16, **24kHz**, mono | PCM16, **16kHz**, little-endian |
| Output format | PCM16, 24kHz | PCM16, 24kHz |
| Other input formats | PCM16 only | AAC, FLAC, MP3, OGG, WAV, WebM ✅ |

⚠️ **Critical for multi-provider builds:** input sample rates differ (24kHz vs 16kHz). Must resample when switching providers.

### Models
| | Azure OpenAI | Google Vertex Live |
|---|---|---|
| Recommended model | `gpt-realtime-1.5` (2026-02-23) | `gemini-live-2.5-flash-native-audio` |
| Context window | 32k tokens | **128k tokens** |
| Video input | ❌ No | ✅ Yes (1 FPS JPEG) |
| Knowledge cutoff | Sep 2024 | — |

### Pricing (per 1M tokens)
| Token type | Azure `gpt-realtime-1.5` | Google `gemini-live-2.5-flash` |
|------------|--------------------------|-------------------------------|
| Audio input | **$32.00** | **$3.00** (~10× cheaper) |
| Audio output | **$64.00** | **$12.00** (~5× cheaper) |
| Text input | $4.00 | $0.50 |
| Text output | $16.00 | $2.00 |

> **Google is dramatically cheaper.** For audio-heavy production workloads, cost savings are significant.

### Session & Rate Limits
| | Azure OpenAI | Google Vertex Live |
|---|---|---|
| Session duration | No explicit cap | **10–15 min** (extendable) |
| Context window | 32k tokens | 128k tokens |
| Concurrent sessions | 200 RPM (Tier 1–5) | **1,000 per project** |
| TPM | 100k (Tier 1–5) | **4M/min** |
| Session resumption | ❌ | ✅ Checkpoint-based |

### Features
| Feature | Azure OpenAI | Google Vertex Live |
|---------|-------------|-------------------|
| Function calling | ✅ | ✅ |
| Barge-in/interruption | ✅ | ✅ |
| Server VAD | ✅ | ✅ |
| Semantic VAD | ✅ | — |
| Affective dialog | ❌ | ✅ (tone adapts to user) |
| Session resumption | ❌ | ✅ |
| WebRTC (via partners) | ✅ Native | ✅ (Daily, LiveKit, Twilio) |
| SIP/telephony | ✅ | ❌ (via partners only) |

### When to use which
- **Azure `gpt-realtime-1.5`**: Best instruction following, SIP/telephony built-in, proven tool calling, no session time cap — use for complex voice agents with many tools or telephony requirements
- **Google `gemini-live-2.5-flash`**: Much cheaper, larger context, video input, session resumption — use for cost-sensitive builds, long-form sessions, or multimodal (audio + video) agents

### Multi-provider strategy
For production S2S systems, consider routing across both providers:
- Primary: Google for cost efficiency on standard calls
- Fallback: Azure for reliability / SIP / when session limits are hit
- Watch: input sample rate difference (resample 24kHz ↔ 16kHz at the routing layer)

---

## Connections

- Implemented via → [[realtime-audio-api]]
- Azure implementation reference → [[azure-openai-realtime-audio]], [[azure-openai-realtime-models]]
- Google implementation reference → [[google-vertex-live-api]]
- Being built in → [[my-projects]] (Generalized S2S Model)
- VAD concepts also apply to non-S2S pipelines

## Tensions & Open Questions

- Semantic VAD vs server VAD: when is the extra intelligence worth the complexity?
- How do you handle multi-language users with server VAD tuned for one language?
- At what conversation length do you need to start managing token limits, and what's the best summarization strategy?
- How to test S2S agents — synthetic audio? real user recordings?
