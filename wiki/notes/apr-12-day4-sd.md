---
type: note
date: 2026-04-12
day: 4
phase: System Design
topic: SD #1 — Fundamentals (Load Balancer, CDN, Caching, DNS)
tags: [system-design, coding, backend]
---

# Day 4 — System Design #1: Fundamentals
**Date:** Sunday, April 12, 2026
**Phase:** System Design (Session 1 of 5)
**Goal:** Understand the core building blocks that appear in every system design interview

---

## Resources

| Resource | Link |
|----------|------|
| ByteByteGo — Scale From Zero To Millions Of Users | https://www.youtube.com/watch?v=hnpzNAPiC0E |
| ByteByteGo — Load Balancer | https://www.youtube.com/watch?v=sCR3SAVdyCc |
| ByteByteGo — CDN Explained | https://www.youtube.com/watch?v=RI9np1LWzqw |
| ByteByteGo — Cache Systems | https://www.youtube.com/watch?v=dGAgxozNWFE |
| ByteByteGo — DNS Explained | https://www.youtube.com/watch?v=27r4Bzuj5NQ |
| DDIA — Chapter 1: Reliability, Scalability, Maintainability | (read alongside) |

---

## How to Use This Session (4 hrs)

| Block | Time | Task |
|-------|------|------|
| Block 1 | 1 hr | Watch all 5 ByteByteGo videos above |
| Block 2 | 1 hr | Fill in notes for each concept below |
| Block 3 | 1 hr | Draw the full architecture diagram from scratch (no peeking) |
| Block 4 | 1 hr | Write a mock answer to the design question at the bottom |

---

## Concept Notes

### DNS (Domain Name System)
- **What it is:**
- **How it works (step by step):**
- **Key terms:** recursive resolver, authoritative server, TTL
```
Notes here
```

---

### Load Balancer
- **What it is:**
- **L4 vs L7:**
- **Algorithms:** Round robin, least connections, IP hash
- **Why it matters in interviews:**
```
Notes here
```

---

### CDN (Content Delivery Network)
- **What it is:**
- **Push vs Pull CDN:**
- **When to use it:**
```
Notes here
```

---

### Caching
- **What it is:**
- **Cache-aside (lazy loading):**
- **Write-through:**
- **Write-back:**
- **Eviction policies:** LRU, LFU, TTL
- **Redis vs Memcached:**
```
Notes here
```

---

### Putting It Together — Web Request Flow
*Trace a user clicking a URL end to end. Fill in each hop:*

```
User types URL
  → DNS lookup: ___
  → CDN check: ___
  → Load balancer: ___
  → App server: ___
  → Cache check: ___
  → Database: ___
  → Response back: ___
```

---

## Architecture Diagram
*Draw this yourself after watching the videos. Paste a photo or ASCII art here.*

```
[ Draw here ]
```

---

## Mock Design Question
**"Design a system that serves a high-traffic read-heavy website (e.g. Wikipedia). Walk me through the architecture."**

*Write your answer below — aim for 10–15 minutes as if in a real interview:*

```
Answer here
```

---

## Key Takeaways
-
-
-

## Terms to Remember
-
-

## What Was Confusing
-

## What to Revisit
-

---

_Next SD session: [[apr-19-day11-sd]] — Databases: SQL vs NoSQL, indexing, sharding_
_Next DSA day: [[apr-13-day5]] — Strings_
