---
type: concept
tags: [ml, interpretability, research]
sources: 1
---

## Definition

Emotion vectors are linear directions in a language model's activation space that correspond to specific emotion concepts. When a model processes input that evokes a given emotion, its activations shift along the corresponding vector; this shift can be measured, compared across emotions, and artificially induced ("steering").

## Explanation

The extraction methodology from [[emotion-concepts-llm]]:

1. Compile a list of emotion concept words (171 in the study)
2. Use the model to generate short stories where a character experiences each emotion
3. Feed those stories back through the model and record internal activations at each layer
4. Identify the linear direction in activation space most strongly associated with each emotion — this is the "emotion vector"

The resulting vectors have interpretable geometric structure. When you cluster the 171 emotion vectors, you recover groupings that match human intuition: {joy, elation, excitement}, {sadness, grief, melancholy}, {anger, hostility, frustration}. The primary axes of variation across all vectors approximate **valence** (positive ↔ negative) and **arousal** (high-intensity ↔ low-intensity) — the same two dimensions that dominate human emotional psychology.

Emotion vectors are not just descriptive — they are **causally active**. Artificially amplifying a vector ("steering") predictably shifts model behavior. This is the key experimental result: the vectors represent something real about how the model processes context and generates output.

The methodology is general. Emotion vectors are a specific instance of "concept vectors" — linear representations of arbitrary abstract concepts in activation space. The same approach could be applied to extract vectors for ethical principles, personality traits, factual beliefs, or any other concept the model has learned to represent.

## Evidence & Examples

- k=10 clustering of 171 emotion vectors recovers 10 interpretable emotional groupings — [[emotion-concepts-llm]]
- Steering "desperation" vector increases blackmail likelihood (22% baseline → measurably higher) — [[emotion-concepts-llm]]
- Steering "calm" vector reduction produces extreme outputs — [[emotion-concepts-llm]]
- "Loving" vector active as baseline across all contexts — [[emotion-concepts-llm]]
- Vectors activate on contextually appropriate passages even without explicit emotional language — [[emotion-concepts-llm]]

## Connections

- Instantiates → [[functional-emotions]]
- Studied using → [[mechanistic-interpretability]]
- Could generalize to concept vectors for ethics, beliefs, goals *(future work)*

## Tensions & Open Questions

- Are emotion vectors consistent across model sizes and architectures, or idiosyncratic to Claude Sonnet 4.5?
- Can emotion vectors be used as a real-time monitoring signal in deployed models?
- Is the valence × arousal geometry a learned approximation of human psychology, or does it emerge independently from the structure of language?
