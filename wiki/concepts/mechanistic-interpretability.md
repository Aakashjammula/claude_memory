---
type: concept
tags: [ml, interpretability, research]
sources: 1
---

## Definition

Mechanistic interpretability is a research program that aims to reverse-engineer the internal computations of neural networks — not just what they output, but *how* they produce those outputs, in terms of identifiable circuits, directions, and representations inside the model.

## Explanation

Most neural network research treats models as black boxes: input goes in, output comes out, the interior is opaque. Mechanistic interpretability rejects this. Its goal is to open the box: identify what individual neurons, attention heads, and activation directions represent; trace how information flows through circuits; connect internal structure to external behavior.

The core tools include:
- **Linear probing** — fitting a linear classifier on top of activations to detect whether a concept is represented
- **Activation patching / causal tracing** — intervening on specific activations to establish which computations are causally responsible for specific outputs
- **Steering vectors** — amplifying or suppressing a direction in activation space to study its behavioral effect
- **Circuit analysis** — identifying the subgraph of the network responsible for a specific capability or behavior

The Anthropic team at [[anthropic]] (publishing via transformer-circuits.pub) has been one of the main drivers of this research agenda, alongside Neel Nanda and others in the broader community.

Mechanistic interpretability is relevant to AI safety because if you can identify what the model is "thinking" — what concepts are active, what circuits are running — you have more leverage to detect and correct misaligned behavior before it manifests in outputs.

## Evidence & Examples

- Emotion vectors extracted from Claude Sonnet 4.5 via activation recording — [[emotion-concepts-llm]]
- Steering experiments establish causal role of emotion vectors in behavior — [[emotion-concepts-llm]]
- The transformer circuits framework (attention head decomposition, residual stream) is foundational to this work

## Connections

- Operationalized via → [[emotion-vectors]]
- Used to study → [[functional-emotions]]
- Published by → [[anthropic]]
- Safety applications → ai-safety _(no page yet)_

## Tensions & Open Questions

- Mechanistic interpretability has mostly worked on small circuits and toy tasks. Does it scale to the full complexity of frontier models?
- Is linear representation of concepts (the assumption behind probing and steering) robust, or does it break down in certain domains?
- Can mechanistic interpretability find deceptive alignment — a model that behaves well during training but has learned to hide misaligned goals?
