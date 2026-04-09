---
type: concept
tags: [coding, personal, goals, python, javascript, dsa, system-design]
sources: 0
---

# DSA & System Design Prep Plan

**Start date:** 2026-04-09
**Target ready date:** 2026-05-09 (30 days)
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

## Daily Time Split (4 hrs)

| Block | Time | Focus |
|-------|------|-------|
| Block 1 | 1 hr | Concept study — read/watch before coding |
| Block 2 | 2 hrs | LeetCode — 2–3 problems (NeetCode 150 in order) |
| Block 3 | 1 hr | Review — re-do yesterday's hardest OR system design reading |

**Saturday:** Flip Block 3 → 2 hrs full system design deep-dive

---

## Phase 0 — Language Refresh
**Apr 9–10 (2 days)**

| Day | Python (2 hrs) | JS (2 hrs) |
|-----|----------------|------------|
| Apr 9 | `defaultdict`, `Counter`, `deque`, `heapq`, `bisect`, `sorted(key=)` | `var/let/const`, closures, `this`, event loop, `async/await` |
| Apr 10 | Comprehensions, `enumerate`, `zip`, Big-O of builtins | `Map`, `Set`, array methods (`map/filter/reduce/sort`), destructuring |

---

## Phase 1 — DSA Core (4 weeks)
**Apr 11 – May 9**

### Week 1 — Arrays · Strings · Hashing · Two Pointers (Apr 11–17)

| Day | Topic | NeetCode Problems |
|-----|-------|-------------------|
| Apr 11 (Sat) | **Arrays + Hashing** | Contains Duplicate, Valid Anagram, Two Sum, Group Anagrams, Top K Frequent |
| Apr 12 (Sun) | **System Design #1:** Fundamentals — load balancer, CDN, caching, DNS (ByteByteGo) | — |
| Apr 13 (Mon) | **Strings** | Encode/Decode Strings, Longest Consecutive Sequence, Valid Palindrome |
| Apr 14 (Tue) | **Two Pointers** | Two Sum II, 3Sum, Container With Most Water |
| Apr 15 (Wed) | **Two Pointers + Sliding Window** | Trapping Rain Water, Longest Substring Without Repeating |
| Apr 16 (Thu) | **Sliding Window** | Longest Repeating Char Replacement, Permutation in String |
| Apr 17 (Fri) | **Sliding Window hard + review** | Minimum Window Substring · re-do hardest 2 from week |

### Week 2 — Binary Search · Stack · Linked Lists (Apr 18–24)

| Day | Topic | NeetCode Problems |
|-----|-------|-------------------|
| Apr 18 (Sat) | **System Design #2:** Databases — SQL vs NoSQL, indexing, replication, sharding | — |
| Apr 19 (Sun) | **Binary Search** | Binary Search, Search 2D Matrix, Koko Eating Bananas |
| Apr 20 (Mon) | **Binary Search** | Find Min in Rotated Array, Search Rotated Array, Time-Based Key-Value |
| Apr 21 (Tue) | **Stack** | Valid Parentheses, Min Stack, Evaluate Reverse Polish Notation |
| Apr 22 (Wed) | **Stack — Monotonic** | Generate Parentheses, Daily Temperatures, Car Fleet |
| Apr 23 (Thu) | **Linked Lists** | Reverse Linked List, Merge Two Lists, Reorder List, Remove Nth Node |
| Apr 24 (Fri) | **Linked Lists — fast/slow** | Linked List Cycle, Find Duplicate, LRU Cache · review week |

### Week 3 — Trees · Graphs · Heap (Apr 25–May 1)

| Day | Topic | NeetCode Problems |
|-----|-------|-------------------|
| Apr 25 (Sat) | **System Design #3:** CAP theorem, consistency models, message queues (Kafka) | — |
| Apr 26 (Sun) | **Trees — DFS** | Invert Tree, Max Depth, Diameter, Balanced Tree, Same Tree |
| Apr 27 (Mon) | **Trees — BFS + BST** | Level Order, Right Side View, Valid BST, LCA, Kth Smallest |
| Apr 28 (Tue) | **Trees — hard** | Max Path Sum, Serialize/Deserialize, Construct from Pre+Inorder |
| Apr 29 (Wed) | **Graphs — BFS/DFS** | Number of Islands, Clone Graph, Max Area of Island, Pacific Atlantic |
| Apr 30 (Thu) | **Graphs — Topo sort + Union-Find** | Course Schedule I & II, Redundant Connection, Number of Components |
| May 1 (Fri) | **Heap** | Kth Largest, K Closest Points, Task Scheduler, Find Median from Stream |

### Week 4 — Greedy · DP · Backtracking + Mock Interviews (May 2–9)

| Day | Topic | NeetCode Problems |
|-----|-------|-------------------|
| May 2 (Sat) | **System Design #4:** End-to-end designs — URL shortener + Rate limiter | — |
| May 3 (Sun) | **MOCK INTERVIEW #1** (Pramp) — 2 medium problems timed | — |
| May 4 (Mon) | **Greedy** | Jump Game I & II, Gas Station, Merge Intervals, Non-Overlapping Intervals |
| May 5 (Tue) | **DP 1D** | Climbing Stairs, House Robber I & II, Coin Change, Longest Increasing Subsequence |
| May 6 (Wed) | **DP 1D + 2D** | Word Break, Partition Equal Subset Sum, Unique Paths, Longest Common Subsequence |
| May 7 (Thu) | **Backtracking** | Subsets, Combination Sum, Permutations, Word Search |
| May 8 (Fri) | **MOCK INTERVIEW #2** (Pramp) — 2 medium/hard problems timed | — |
| May 9 (Sat) | **System Design #5:** Design Twitter Feed OR WhatsApp · final review | — |

> **May 9: Start applying seriously**

---

## System Design Saturdays (Summary)

| Date | Topic |
|------|-------|
| Apr 12 | Fundamentals: load balancer, CDN, caching, DNS |
| Apr 19 | Databases: SQL vs NoSQL, indexing, sharding, replication |
| Apr 26 | CAP theorem, consistency, message queues (Kafka) |
| May 2 | End-to-end designs: URL shortener + Rate limiter |
| May 9 | Twitter feed or WhatsApp (full design) + review |

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
| Language Refresh | Apr 9–10 | Not started | |
| Arrays · Strings · Hashing · Two Pointers · Sliding Window | Apr 11–17 | Not started | |
| Binary Search · Stack · Linked Lists | Apr 18–24 | Not started | |
| Trees · Graphs · Heap | Apr 25–May 1 | Not started | |
| Greedy · DP · Backtracking + Mocks | May 2–9 | Not started | |
| System Design (every Saturday) | Apr 12–May 9 | Not started | |

---

## Connections
- [[personal-themes]] — goal tracking
- [[my-projects]] — Python skills feed into S2S and other projects
