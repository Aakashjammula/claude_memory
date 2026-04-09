---
type: concept
tags: [coding, azure, llm, audio, api, reference]
sources: 1
---

# Azure OpenAI Realtime Models — Reference

_Last updated: 2026-04-08. Sources: Azure Foundry Model Retirements page + Quotas & Limits + OpenAI model docs._

---

## ⚠️ Critical: Preview Models Already Retired

`gpt-4o-realtime-preview` and `gpt-4o-mini-realtime-preview` (both version 2024-12-17) **retired on 2026-03-24**. Any existing deployments of these models now return error responses. Use `gpt-realtime` or `gpt-realtime-1.5` instead.

---

## Full Model Catalogue

| Model | Version | Status | Deprecation Date | Retirement Date | Replacement |
|-------|---------|--------|-----------------|-----------------|-------------|
| `gpt-4o-realtime-preview` | 2024-12-17 | ~~Preview~~ **RETIRED** | n/a | **2026-03-24** ✅ gone | `gpt-realtime` |
| `gpt-4o-mini-realtime-preview` | 2024-12-17 | ~~Preview~~ **RETIRED** | n/a | **2026-03-24** ✅ gone | _(none listed)_ |
| `gpt-realtime` | 2025-08-28 | GA ✅ | 2026-08-28 | 2027-02-28 | TBD |
| `gpt-realtime-mini` | 2025-10-06 | GA ✅ | n/a | _(not listed — may be superseded by 12-15 version)_ | |
| `gpt-realtime-mini` | 2025-12-15 | GA ✅ | n/a | **2026-12-15** | TBD |
| `gpt-realtime-1.5` | 2026-02-23 | GA ✅ **Latest** | n/a | No earlier than **2027-02-23** | TBD |

**Deployment type for all:** GlobalStandard only.

---

## Model Capabilities

### `gpt-realtime-1.5` (2026-02-23) — Flagship / Recommended

| Property | Value |
|----------|-------|
| Context window | 32,000 tokens |
| Max output tokens | 4,096 tokens |
| Knowledge cutoff | September 30, 2024 |
| Input modalities | Text, Audio, Image |
| Output modalities | Text, Audio |
| Function calling | ✅ Yes |
| Structured outputs | ❌ No |
| Fine-tuning | ❌ No |
| Performance | Highest |
| Speed | Fast |

### `gpt-realtime` (2025-08-28) — Production Standard

| Property | Value |
|----------|-------|
| Context window | 32,000 tokens |
| Max output tokens | 4,096 tokens |
| Input modalities | Text, Audio |
| Output modalities | Text, Audio |
| Function calling | ✅ Yes |
| Structured outputs | ❌ No |

### `gpt-realtime-mini` (2025-12-15) — Latency/Cost Optimized

| Property | Value |
|----------|-------|
| Input/Output | Audio ↔ Audio |
| Function calling | ✅ Yes |
| Best for | Latency-sensitive flows, cost reduction |
| Retirement | 2026-12-15 |

---

## Pricing — `gpt-realtime-1.5`

| Token Type | Price per 1M tokens |
|------------|-------------------|
| Text input | $4.00 |
| Text output | $16.00 |
| Audio input | $32.00 |
| Audio output | $64.00 |
| Cached input | $0.40 |

> **Note:** Audio is ~8× more expensive than text input. Keep tool responses and system prompts as text where possible to reduce cost.

---

## Token Limits (all realtime models)

| Limit | Value |
|-------|-------|
| Max input tokens | 32,000 |
| Max output tokens | 4,096 |
| Audio format | PCM16, 24kHz, mono |
| Chunk size | 4,800 bytes = 100ms |

---

## Rate Limits by Quota Tier

### `gpt-realtime` — GA (production use)

| Tier | RPM | TPM |
|------|-----|-----|
| Tier 1–5 | 200 | 100,000 |
| Tier 6 | 300 | 150,000 |

### `gpt-4o-realtime-preview` / `gpt-4o-mini-realtime-preview` — RETIRED (historical reference only)

| Tier | RPM | TPM |
|------|-----|-----|
| Tier 1–5 | 36 | 6,000 |
| Tier 6 | 54 | 9,000 |

> These models are gone. `gpt-realtime` offers ~5.5× more RPM and ~16× more TPM even at Tier 1.

---

## Quota Tier System

| Feature | Detail |
|---------|--------|
| Tiers | Free + Tiers 1–6 (Tier 6 = highest) |
| Auto-upgrade | Yes — based on consumption trends |
| Enterprise/MCA-E | Start at higher tiers automatically |
| Manual request | [quota request form](https://aka.ms/oai/stuquotarequest) |
| Opt out | Set `tierUpgradePolicy: NoAutoUpgrade` via management API |
| Scope | Per region × per subscription × per model (quotas do NOT combine across regions) |

---

## Retirement Policy

| Model Type | Minimum Availability | Notice Period |
|-----------|---------------------|---------------|
| GA models | 12 months from launch | 60 days before retirement |
| Preview models | 90–120 days from launch | 30 days before upgrade |
| After 12 months | Existing customers get 6 more months | New customers lose access |

Notifications are sent via **Azure Resource Health** and **email to subscription owners**. Set up Service Health alerts for `azure OpenAI service` → `Health advisories = Upgrade, Deprecation & Retirement Notifications`.

---

## Choosing the Right Model

| Scenario | Use |
|----------|-----|
| Production voice agent | `gpt-realtime-1.5` (2026-02-23) |
| Cost/latency sensitive | `gpt-realtime-mini` (2025-12-15) |
| Stable, proven production | `gpt-realtime` (2025-08-28) — retires Feb 2027 |
| Dev/test (local) | `gpt-realtime` — preview models are retired |
| Multi-language + tool use | `gpt-realtime-1.5` — best instruction following |

---

## Multi-Region Scaling

Quotas are **isolated per region** and do NOT combine. Deploying in 2 regions (e.g. East US + West Europe) = 200 RPM × 2 effectively. Route traffic across both to double throughput ceiling.

---

## Connections

- Core API reference → [[azure-openai-realtime-audio]]
- Architecture patterns → [[speech-to-speech-agents]]
- Used in → [[my-projects]] (Generalized S2S Model)
- Platform entity → [[azure-openai]]
