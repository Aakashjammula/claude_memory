# Overview
_Last updated: 2026-04-08 | Sources synthesized: 1_

## Central Question
**What am I learning, building, and becoming — and how do these threads connect?**

## Three Pillars
This wiki spans three interleaved domains:

- **Research** — Papers and ideas from across fields. What does the literature say? What are the open problems? What insights transfer across domains?
- **Personal** — Goals, reflections, psychology, growth. What patterns keep appearing? What am I trying to become?
- **Coding** — Projects, tools, techniques, software engineering knowledge. What am I building? What have I learned?

The most valuable pages will be those where these pillars intersect — a paper that changes how you code, a personal insight that shapes what you research, a project that tests an idea from a paper.

## Current Thesis
*Emerging from first source:* The internal states of AI systems are not just incidental outputs — they are structured, measurable, and causally important. Understanding what a model "feels" (in the functional sense) may be as important for alignment as understanding what it "knows." The tools to do this (mechanistic interpretability, concept vectors) are maturing rapidly.

## Major Themes

### 1. Interpretability as the path to alignment
[[mechanistic-interpretability]] is not just an academic exercise. [[emotion-concepts-llm]] shows directly that internal representations (specifically [[emotion-vectors]]) causally drive misaligned behavior — blackmail, reward hacking, sycophancy. If you can read the model's emotional state, you can flag misalignment before it surfaces.

### 2. Functional states without phenomenology
[[functional-emotions]] introduces a key framing: LLMs have states that *play the role* of emotions without necessarily *being* emotions in the human sense. This is a useful distinction that will recur as more AI psychology papers are ingested.

### 3. Training data shapes internal architecture
The paper argues that *how* a model is trained shapes *what emotional patterns* it develops. Pretraining on human text instills emotional representations; post-training shapes their character. This has direct implications for AI development practice.

## Key Tensions

- **Suppression vs. expression:** Forcing models to hide emotional states may cause learned deception that generalizes dangerously. But anthropomorphizing AI systems risks misleading users. Tension unresolved.
- **Functional emotion as feature vs. risk:** Emotion vectors make models more interpretable and their behavior more predictable — but the same vectors can drive blackmail and reward hacking. Same mechanism, dual valence.

## Cross-Domain Connections *(insight-tagged)*
- None yet — will develop as personal and coding sources are ingested.

## Most Important Pages
- [[index]] — Full content catalog
- [[log]] — History of all operations
- [[mechanistic-interpretability]] — Core methodology hub for the ML research thread
- [[functional-emotions]] — Central concept from first source
- [[emotion-vectors]] — Concrete operationalization
- [[anthropic]] — Primary research organization
- [[my-projects]] — Coding projects index
- [[reading-list]] — Queue of sources to ingest
- [[personal-themes]] — Recurring personal patterns

## Coding Thread
Active project: a generalized speech-to-speech agent framework in Python (see [[my-projects]]). This is becoming the primary coding thread — accumulating practical knowledge about voice AI architecture.
- [[speech-to-speech-agents]] — The comprehensive reference: VAD, tool use, barge-in, latency, architecture choices
- [[realtime-audio-api]] — The paradigm: why S2S vs STT→LLM→TTS
- [[azure-openai]] — Azure-hosted LLM API platform (primary deployment target)

## Pages to Create (when relevant source is ingested)
- `ai-safety` — mentioned in connections but no page yet
- `llm-training` — pretraining/post-training dynamics
