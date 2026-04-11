---
type: concept
tags: [coding, personal, goals, python, javascript, dsa, system-design]
sources: 0
---

# DSA & System Design Prep Plan

**Start date:** 2026-04-11
**Target ready date:** 2026-05-11 (31 days)
**Daily commitment:** 4 hours/day
**Target level:** FAANG L3/E3 (1yr exp + 9mo internship, GenAI SWE)
**Primary language:** Python | **Secondary:** JavaScript
**Problem list:** NeetCode 150

---

## Resources

| Type | Resource |
|------|----------|
| Problems | NeetCode 150 — neetcode.io/roadmap |
| DSA videos | NeetCode YouTube |
| System Design | ByteByteGo + Gaurav Sen YouTube |
| Books | CTCI (patterns + behavioral) · DDIA (system design) |
| Mock interviews | Pramp / interviewing.io |

---

## Daily Time Split (4 hrs, parallel with PS)

| Block | Time | Focus |
|-------|------|-------|
| Block 1 | 7–9 PM | DSA — LeetCode problems, concept study, review |
| Block 2 | 9–11 PM | Prob/Stats — Steve Brunton videos (3/day) |

**System Design days:** Replace evening DSA block with 2-hr SD deep-dive
**Mock Interview days:** 45 min timed problem × 2, then review

---

## Phase 0 — Language Refresh
**Apr 11–12 (2 days)**

| Day | Python (2 hrs) | JS (2 hrs) |
|-----|----------------|------------|
| Apr 11 | `defaultdict`, `Counter`, `deque`, `heapq`, `bisect`, `sorted(key=)` | `var/let/const`, closures, `this`, event loop, `async/await` |
| Apr 12 | Comprehensions, `enumerate`, `zip`, Big-O of builtins | `Map`, `Set`, array methods (`map/filter/reduce/sort`), destructuring |

---

## Phase 1 — DSA Core (4 weeks)
**Apr 13 – May 11**

### Week 1 — Arrays · Strings · Hashing · Two Pointers (Apr 13–19)

| Day | Topic | NeetCode Problems |
|-----|-------|-------------------|
| May 11 (Mon) | **Arrays + Hashing** | Contains Duplicate, Valid Anagram, Two Sum, Group Anagrams, Top K Frequent |
| May 10 (Sun) | **System Design #1:** Fundamentals — load balancer, CDN, caching, DNS (ByteByteGo) | — |
| May 11 (Mon) | **Strings** | Encode/Decode Strings, Longest Consecutive Sequence, Valid Palindrome |
| May 10 (Sun) | **Two Pointers** | Two Sum II, 3Sum, Container With Most Water |
| May 11 (Mon) | **Two Pointers + Sliding Window** | Trapping Rain Water, Longest Substring Without Repeating |
| May 10 (Sun) | **Sliding Window** | Longest Repeating Char Replacement, Permutation in String |
| May 11 (Mon) | **Sliding Window hard + review** | Minimum Window Substring · re-do hardest 2 from week |

### Week 2 — Binary Search · Stack · Linked Lists (Apr 20–26)

| Day | Topic | NeetCode Problems |
|-----|-------|-------------------|
| May 10 (Sun) | **System Design #2:** Databases — SQL vs NoSQL, indexing, replication, sharding | — |
| May 11 (Mon) | **Binary Search** | Binary Search, Search 2D Matrix, Koko Eating Bananas |
| May 10 (Sun) | **Binary Search** | Find Min in Rotated Array, Search Rotated Array, Time-Based Key-Value |
| May 11 (Mon) | **Stack** | Valid Parentheses, Min Stack, Evaluate Reverse Polish Notation |
| May 10 (Sun) | **Stack — Monotonic** | Generate Parentheses, Daily Temperatures, Car Fleet |
| May 11 (Mon) | **Linked Lists** | Reverse Linked List, Merge Two Lists, Reorder List, Remove Nth Node |
| May 10 (Sun) | **Linked Lists — fast/slow** | Linked List Cycle, Find Duplicate, LRU Cache · review week |

### Week 3 — Trees · Graphs · Heap (Apr 27–May 3)

| Day | Topic | NeetCode Problems |
|-----|-------|-------------------|
| May 11 (Mon) | **System Design #3:** CAP theorem, consistency models, message queues (Kafka) | — |
| May 10 (Sun) | **Trees — DFS** | Invert Tree, Max Depth, Diameter, Balanced Tree, Same Tree |
| May 11 (Mon) | **Trees — BFS + BST** | Level Order, Right Side View, Valid BST, LCA, Kth Smallest |
| May 10 (Sun) | **Trees — hard** | Max Path Sum, Serialize/Deserialize, Construct from Pre+Inorder |
| May 11 (Mon) | **Graphs — BFS/DFS** | Number of Islands, Clone Graph, Max Area of Island, Pacific Atlantic |
| May 10 (Sun) | **Graphs — Topo sort + Union-Find** | Course Schedule I & II, Redundant Connection, Number of Components |
| May 11 (Mon) | **Heap** | Kth Largest, K Closest Points, Task Scheduler, Find Median from Stream |

### Week 4 — Greedy · DP · Backtracking + Mock Interviews (May 4–11)

| Day | Topic | NeetCode Problems |
|-----|-------|-------------------|
| May 10 (Sun) | **System Design #4:** End-to-end designs — URL shortener + Rate limiter | — |
| May 11 (Mon) | **MOCK INTERVIEW #1** (Pramp) — 2 medium problems timed | — |
| May 10 (Sun) | **Greedy** | Jump Game I & II, Gas Station, Merge Intervals, Non-Overlapping Intervals |
| May 11 (Mon) | **DP 1D** | Climbing Stairs, House Robber I & II, Coin Change, Longest Increasing Subsequence |
| May 10 (Sun) | **DP 1D + 2D** | Word Break, Partition Equal Subset Sum, Unique Paths, Longest Common Subsequence |
| May 11 (Mon) | **Backtracking** | Subsets, Combination Sum, Permutations, Word Search |
| May 10 (Sun) | **MOCK INTERVIEW #2** (Pramp) — 2 medium/hard problems timed | — |
| May 11 (Mon) | **System Design #5:** Design Twitter Feed OR WhatsApp · final review | — |

> **May 11: Start applying seriously**

---

## System Design Saturdays (Summary)

| Date | Topic |
|------|-------|
| Apr 14 | Fundamentals: load balancer, CDN, caching, DNS |
| Apr 20 | Databases: SQL vs NoSQL, indexing, sharding, replication |
| Apr 27 | CAP theorem, consistency, message queues (Kafka) |
| May 4 | End-to-end designs: URL shortener + Rate limiter |
| May 11 | Twitter feed or WhatsApp (full design) + review |

**For each Saturday:** Watch 2 ByteByteGo videos → read relevant DDIA chapter → draw the architecture yourself from scratch

**DDIA chapters to read alongside:** Ch 1, Ch 3, Ch 5 (replication), Ch 6 (partitioning), Ch 9 (consistency)

---

## FAANG Notes

- **L3 bar:** Solve Mediums in 20–25 min confidently; Hard is a bonus
- **Behavioral:** Prepare 5–6 STAR stories (impact, failure, conflict, leadership, collaboration)
- **GenAI angle:** May get ML system design — prep RAG pipeline, embedding search, LLM serving

---

## Progress Tracker

| Phase | Dates | Status | Notes |
|-------|-------|--------|-------|
| Language Refresh | Apr 11–12 | Not started | |
| Arrays · Strings · Hashing · Two Pointers · Sliding Window | Apr 13–19 | Not started | |
| Binary Search · Stack · Linked Lists | Apr 20–26 | Not started | |
| Trees · Graphs · Heap | Apr 27–May 3 | Not started | |
| Greedy · DP · Backtracking + Mocks | May 4–11 | Not started | |
| System Design (every 7th day) | Apr 14–May 11 | Not started | |

---

## Connections
- [[personal-themes]] — goal tracking
- [[my-projects]] — Python skills feed into S2S and other projects
