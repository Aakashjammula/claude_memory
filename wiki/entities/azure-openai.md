---
type: entity
subtype: product
aliases: [Azure OpenAI Service, Microsoft Azure OpenAI, Microsoft Foundry]
tags: [coding, azure, llm, api, python]
sources: 1
---

## Overview

Azure OpenAI is Microsoft's cloud-hosted deployment of OpenAI models (GPT-4o, GPT-realtime, etc.) via Azure infrastructure. It offers the same models as OpenAI's API but with Azure's enterprise authentication (Microsoft Entra ID), compliance, and regional availability. Recently rebranded under the Microsoft Foundry umbrella.

## Key Facts

- Hosts GPT Realtime API with WebSocket, WebRTC, and SIP connection modes — [[azure-openai-realtime-audio]]
- Supports Microsoft Entra ID (keyless auth) as the recommended production auth method — [[azure-openai-realtime-audio]]
- Uses the standard OpenAI Python SDK — just swap base URL and auth token — [[azure-openai-realtime-audio]]
- Endpoint format: `https://{resource}.openai.azure.com` → `wss://{resource}.openai.azure.com/openai/v1` for realtime — [[azure-openai-realtime-audio]]
- Realtime models available: gpt-realtime, gpt-realtime-1.5, gpt-4o-realtime-preview — [[azure-openai-realtime-audio]]

## Role in Wiki

Azure OpenAI is the primary cloud API platform appearing in the coding thread so far. Relevant when building LLM-powered applications on Azure infrastructure, particularly voice/audio applications.

## Appearances

- [[azure-openai-realtime-audio]] — How-to guide for GPT Realtime API (WebSocket, Python)

## Open Questions

- How does Azure OpenAI pricing compare to OpenAI direct API for realtime models?
- Which Azure regions support the latest gpt-realtime models?
