"""
generate_calendar.py
--------------------
Generates an ICS calendar file with all study events (DSA + System Design + Prob/Stats)
that can be imported directly into Google Calendar.

Run from claude_memory/code/:
    uv run python generate_calendar.py

Then import raw/study-plan.ics into Google Calendar:
  Google Calendar → Settings → Import & Export → Import
"""

import os
from datetime import datetime, date

BASE = os.path.dirname(os.path.dirname(__file__))
RAW_DIR = os.path.join(BASE, "raw")
os.makedirs(RAW_DIR, exist_ok=True)

# Study hours: 7:00 PM – 11:00 PM IST (adjust if needed)
START_HOUR = 19  # 7 PM
END_HOUR   = 23  # 11 PM

def ics_dt(d: date, hour: int) -> str:
    """Format datetime for ICS (local time, no timezone = floating)."""
    return f"{d.year}{d.month:02d}{d.day:02d}T{hour:02d}0000"

def make_event(uid, dt: date, title, description, category):
    start = ics_dt(dt, START_HOUR)
    end   = ics_dt(dt, END_HOUR)
    desc  = description.replace("\n", "\\n").replace(",", "\\,")
    return "\n".join([
        "BEGIN:VEVENT",
        f"UID:{uid}@claude-memory",
        f"DTSTART:{start}",
        f"DTEND:{end}",
        f"SUMMARY:{title}",
        f"DESCRIPTION:{desc}",
        f"CATEGORIES:{category}",
        "STATUS:CONFIRMED",
        "END:VEVENT",
    ])

events = []

# ── DSA + System Design (Apr 9 – May 9) ─────────────────────────────────────
dsa_schedule = [
    (date(2026, 4,  9), "Day 1 — Python DSA Toolkit",          "defaultdict, Counter, deque, heapq, bisect, sorted(key=)\\nProblems: Two Sum, Valid Anagram", "DSA-Prep"),
    (date(2026, 4, 10), "Day 2 — Python Patterns + JS Toolkit", "Comprehensions, enumerate, zip, Big-O\\nJS: Map, Set, filter/map/reduce", "DSA-Prep"),
    (date(2026, 4, 11), "Day 3 — Arrays + Hashing",             "Contains Duplicate, Valid Anagram, Two Sum, Group Anagrams, Top K Frequent", "DSA-Prep"),
    (date(2026, 4, 12), "SD #1 — Fundamentals",                 "Load balancer, CDN, caching, DNS\\nByteByteGo: Scale From Zero to Millions", "System-Design"),
    (date(2026, 4, 13), "Day 5 — Strings",                      "Encode/Decode Strings, Longest Consecutive Sequence, Valid Palindrome", "DSA-Prep"),
    (date(2026, 4, 14), "Day 6 — Two Pointers",                 "Two Sum II, 3Sum, Container With Most Water", "DSA-Prep"),
    (date(2026, 4, 15), "Day 7 — Two Pointers + Sliding Window","Trapping Rain Water, Longest Substring Without Repeating", "DSA-Prep"),
    (date(2026, 4, 16), "Day 8 — Sliding Window",               "Longest Repeating Char Replacement, Permutation in String", "DSA-Prep"),
    (date(2026, 4, 17), "Day 9 — Sliding Window Hard + Review", "Minimum Window Substring + re-do hardest problems of week", "DSA-Prep"),
    (date(2026, 4, 18), "SD #2 — Databases",                    "SQL vs NoSQL, indexing, replication, sharding\\nDDIA Chapter 3", "System-Design"),
    (date(2026, 4, 19), "Day 11 — Binary Search",               "Binary Search, Search 2D Matrix, Koko Eating Bananas", "DSA-Prep"),
    (date(2026, 4, 20), "Day 12 — Binary Search",               "Find Min Rotated Array, Search Rotated Array, Time-Based Key-Value", "DSA-Prep"),
    (date(2026, 4, 21), "Day 13 — Stack",                       "Valid Parentheses, Min Stack, Evaluate Reverse Polish Notation", "DSA-Prep"),
    (date(2026, 4, 22), "Day 14 — Monotonic Stack",             "Generate Parentheses, Daily Temperatures, Car Fleet", "DSA-Prep"),
    (date(2026, 4, 23), "Day 15 — Linked Lists",                "Reverse Linked List, Merge Two Lists, Reorder List, Remove Nth Node", "DSA-Prep"),
    (date(2026, 4, 24), "Day 16 — Linked Lists Fast/Slow",      "Linked List Cycle, Find Duplicate, LRU Cache", "DSA-Prep"),
    (date(2026, 4, 25), "SD #3 — CAP + Message Queues",         "CAP theorem, consistency models, Kafka pub/sub\\nDDIA Chapter 9", "System-Design"),
    (date(2026, 4, 26), "Day 18 — Trees DFS",                   "Invert Tree, Max Depth, Diameter, Balanced Tree, Same Tree", "DSA-Prep"),
    (date(2026, 4, 27), "Day 19 — Trees BFS + BST",             "Level Order, Right Side View, Valid BST, LCA, Kth Smallest", "DSA-Prep"),
    (date(2026, 4, 28), "Day 20 — Trees Hard",                  "Max Path Sum, Serialize/Deserialize, Construct from Pre+Inorder", "DSA-Prep"),
    (date(2026, 4, 29), "Day 21 — Graphs BFS/DFS",              "Number of Islands, Clone Graph, Max Area of Island, Pacific Atlantic", "DSA-Prep"),
    (date(2026, 4, 30), "Day 22 — Graphs Topo + Union-Find",    "Course Schedule I & II, Redundant Connection, Connected Components", "DSA-Prep"),
    (date(2026, 5,  1), "Day 23 — Heap",                        "Kth Largest in Stream, K Closest Points, Task Scheduler, Find Median", "DSA-Prep"),
    (date(2026, 5,  2), "SD #4 — URL Shortener + Rate Limiter", "Full end-to-end design of URL shortener and rate limiter", "System-Design"),
    (date(2026, 5,  3), "MOCK INTERVIEW #1",                    "Pramp or interviewing.io — 2 timed medium problems\\nLink: https://www.pramp.com", "Mock-Interview"),
    (date(2026, 5,  4), "Day 26 — Greedy",                      "Jump Game I & II, Gas Station, Merge Intervals, Non-Overlapping Intervals", "DSA-Prep"),
    (date(2026, 5,  5), "Day 27 — DP 1D",                       "Climbing Stairs, House Robber I & II, Coin Change, LIS", "DSA-Prep"),
    (date(2026, 5,  6), "Day 28 — DP 1D + 2D",                  "Word Break, Partition Equal Subset Sum, Unique Paths, LCS", "DSA-Prep"),
    (date(2026, 5,  7), "Day 29 — Backtracking",                "Subsets, Combination Sum, Permutations, Word Search", "DSA-Prep"),
    (date(2026, 5,  8), "MOCK INTERVIEW #2",                    "Pramp or interviewing.io — 2 timed medium/hard problems", "Mock-Interview"),
    (date(2026, 5,  9), "SD #5 + Final Review — START APPLYING","Design Twitter Feed or WhatsApp\\nFinal review + submit applications!", "System-Design"),
]

for i, (d, title, desc, cat) in enumerate(dsa_schedule):
    uid = f"dsa-{d.strftime('%Y%m%d')}-{i:02d}"
    events.append(make_event(uid, d, f"[Study] {title}", desc, cat))

# ── Probability & Statistics (May 10 – Jun 7) ────────────────────────────────
prob_schedule = [
    (date(2026, 5, 10), "PS Day 1 — Intro to Statistics",          "Stats #1-3: Introduction, Population Statistics, Random Sampling", "Prob-Stats"),
    (date(2026, 5, 11), "PS Day 2 — Descriptive Stats",            "Stats #4-6: Sample Variance, Normal Approximation, Confidence Intervals", "Prob-Stats"),
    (date(2026, 5, 12), "PS Day 3 — CLT + Hypothesis Testing",     "Stats #7-9: CLT Example, Hypothesis Testing, Testing Procedure", "Prob-Stats"),
    (date(2026, 5, 13), "PS Day 4 — Type I/II Errors",             "Stats #10-12: Type I/II Errors, Salk Vaccine, Two-Sided Rejection", "Prob-Stats"),
    (date(2026, 5, 14), "PS Day 5 — P-Hacking + MoM",             "Stats #13-15: P-Hacking, Parameter Estimation, Method of Moments", "Prob-Stats"),
    (date(2026, 5, 15), "PS Day 6 — MLE with Examples",            "Stats #16-18: Error in MoM, Bootstrapping, MLE with Examples", "Prob-Stats"),
    (date(2026, 5, 16), "PS Day 7 — MLE Properties + MAP",         "Stats #19-21: MLE Normal Fit, MLE Properties, MAP Estimation", "Prob-Stats"),
    (date(2026, 5, 17), "PS Day 8 — Chi-Squared + t-distribution", "Stats #22-24: Consistency, Chi-Squared Test, Student's t", "Prob-Stats"),
    (date(2026, 5, 18), "PS Day 9 — Bayesian Inference Overview",  "Stats #25-27: Hypothesis Testing Revisited, Bayesian Inference Overview", "Prob-Stats"),
    (date(2026, 5, 19), "PS Day 10 — Conjugate Priors",            "Stats #28-30: Bayesian Updates, Conjugate Priors, Normal Conjugate", "Prob-Stats"),
    (date(2026, 5, 20), "PS Day 11 — GMM + Bayesian Regression",   "Stats #31-33: Gaussian Mixture Models, Monte Carlo Bayesian, Bayesian Linear Regression", "Prob-Stats"),
    (date(2026, 5, 21), "PS Day 12 — Stats Wrap-up",               "Stats #34-35: Bayesian Linear Regression MAP + Python Example", "Prob-Stats"),
    (date(2026, 5, 22), "PS Day 13 — Probability Overview",        "Prob #1-3: Overview, Counting Coin Flips, Combinatorics", "Prob-Stats"),
    (date(2026, 5, 23), "PS Day 14 — Set Theory + Binomial",       "Prob #4-7: Set Theory, Birthday Problem, Quality Control, Binomial", "Prob-Stats"),
    (date(2026, 5, 24), "PS Day 15 — Bayes' Theorem",              "Prob #8-10: Conditional Probability, Law of Total Probability, Bayes", "Prob-Stats"),
    (date(2026, 5, 25), "PS Day 16 — Independence + Random Vars",  "Prob #11-13: Bayes Drug Test, Independence, Random Variables", "Prob-Stats"),
    (date(2026, 5, 26), "PS Day 17 — Normal Distribution",         "Prob #14-16: Bernoulli & Binomial, Normal Distribution, Standard Normal", "Prob-Stats"),
    (date(2026, 5, 27), "PS Day 18 — Poisson + Exponential",       "Prob #17-19: Poisson, Geometric, Exponential Distribution", "Prob-Stats"),
    (date(2026, 5, 28), "PS Day 19 — Gamma + Functions of RV",     "Prob #20-22: Hazard Rate, Exponential-Poisson, Gamma Distribution", "Prob-Stats"),
    (date(2026, 5, 29), "PS Day 20 — Chi-Squared + Joint Dists",   "Prob #23-25: Functions of RV, Rescaling Normal, Chi-Squared", "Prob-Stats"),
    (date(2026, 5, 30), "PS Day 21 — Expected Value",              "Prob #26-28: Joint Distributions, Marginal/Conditional, Expected Value", "Prob-Stats"),
    (date(2026, 5, 31), "PS Day 22 — Variance + Exponential E&V",  "Prob #29-31: Properties of EV, Variance, Exponential E & Var", "Prob-Stats"),
    (date(2026, 6,  1), "PS Day 23 — Markov + Chebyshev",          "Prob #32-34: Two EV Examples, Markov's Inequality, Chebyshev's", "Prob-Stats"),
    (date(2026, 6,  2), "PS Day 24 — LLN + CLT + MGF",            "Prob #35-37: Law of Large Numbers, CLT, Moment Generating Function", "Prob-Stats"),
    (date(2026, 6,  3), "PS Day 25 — MGF + Lebesgue",             "Prob #38-40: MGF Example, Lebesgue Measure, Additive MGF", "Prob-Stats"),
    (date(2026, 6,  4), "PS Day 26 — Covariance + Correlation",    "Prob #41-42: Covariance & Correlation, Gaussian Covariance Example", "Prob-Stats"),
    (date(2026, 6,  5), "PS Day 27 — Tail Sum + Proof of CLT",     "Prob #43-44: Tail Sum Formula, Proof of Central Limit Theorem", "Prob-Stats"),
    (date(2026, 6,  6), "PS Day 28 — Review Day",                  "Re-watch hardest videos + write formula sheet from memory", "Prob-Stats"),
    (date(2026, 6,  7), "PS Day 29 — Consolidation",               "Write full 1-page summary from memory. Done!", "Prob-Stats"),
]

for i, (d, title, desc, cat) in enumerate(prob_schedule):
    uid = f"ps-{d.strftime('%Y%m%d')}-{i:02d}"
    events.append(make_event(uid, d, f"[Study] {title}", desc, cat))

# ── Assemble ICS ──────────────────────────────────────────────────────────────
ics_lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Claude Memory//Study Plan//EN",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "X-WR-CALNAME:Study Plan 2026",
    "X-WR-CALDESC:DSA + System Design + Probability & Statistics",
]
ics_lines.extend(events)
ics_lines.append("END:VCALENDAR")

ics_content = "\r\n".join(ics_lines)
out_path = os.path.join(RAW_DIR, "study-plan.ics")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"Generated {len(events)} calendar events")
print(f"Saved -> {out_path}")
print("\nTo import into Google Calendar:")
print("  1. Go to calendar.google.com")
print("  2. Settings (gear icon) -> Import & Export -> Import")
print("  3. Upload raw/study-plan.ics")
print("  4. Choose which calendar to add to -> Import")
