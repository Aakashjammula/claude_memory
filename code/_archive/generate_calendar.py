"""
generate_calendar.py
--------------------
Generates raw/study-plan.ics from the canonical DSA + PS schedule data.

This is the SOURCE OF TRUTH for calendar dates. If you change dates here,
re-run this script to regenerate the ICS, then re-import into Google Calendar.

Usage:
    uv run python generate_calendar.py

Import into Google Calendar:
    calendar.google.com → Settings (gear) → Import & Export → Import
    Upload: raw/study-plan.ics
"""

import os
from datetime import date, timedelta

BASE    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE, "raw")
os.makedirs(RAW_DIR, exist_ok=True)

# ── Config (change these to rebase the entire plan) ──────────────────────────
DSA_START = date(2026, 4, 11)   # Day 1 of DSA
PS_START  = date(2026, 4, 11)   # Day 1 of Prob/Stats (parallel)
DSA_BLOCK = (19, 21)            # 7–9 PM
PS_BLOCK  = (21, 23)            # 9–11 PM


# ── DSA + System Design schedule (31 days) ───────────────────────────────────
# Format: (summary, description, category)
# Category: DSA-Prep | System-Design | Mock-Interview
DSA_TOPICS = [
    ("Day 1 — Python DSA Toolkit",
     "defaultdict, Counter, deque, heapq, bisect, sorted(key=)\\nProblems: Two Sum, Valid Anagram",
     "DSA-Prep"),
    ("Day 2 — Python Patterns + JS Toolkit",
     "Comprehensions, enumerate, zip, Big-O\\nJS: Map, Set, filter/map/reduce",
     "DSA-Prep"),
    ("Day 3 — Arrays + Hashing",
     "Contains Duplicate, Valid Anagram, Two Sum, Group Anagrams, Top K Frequent",
     "DSA-Prep"),
    ("SD #1 — Fundamentals",
     "Load balancer, CDN, caching, DNS\\nByteByteGo: Scale From Zero to Millions",
     "System-Design"),
    ("Day 5 — Strings",
     "Encode/Decode Strings, Longest Consecutive Sequence, Valid Palindrome",
     "DSA-Prep"),
    ("Day 6 — Two Pointers",
     "Two Sum II, 3Sum, Container With Most Water",
     "DSA-Prep"),
    ("Day 7 — Two Pointers + Sliding Window",
     "Trapping Rain Water, Longest Substring Without Repeating",
     "DSA-Prep"),
    ("Day 8 — Sliding Window",
     "Longest Repeating Char Replacement, Permutation in String",
     "DSA-Prep"),
    ("Day 9 — Sliding Window Hard + Review",
     "Minimum Window Substring + re-do hardest problems of week",
     "DSA-Prep"),
    ("SD #2 — Databases",
     "SQL vs NoSQL, indexing, replication, sharding\\nDDIA Chapter 3",
     "System-Design"),
    ("Day 11 — Binary Search",
     "Binary Search, Search 2D Matrix, Koko Eating Bananas",
     "DSA-Prep"),
    ("Day 12 — Binary Search",
     "Find Min Rotated Array, Search Rotated Array, Time-Based Key-Value",
     "DSA-Prep"),
    ("Day 13 — Stack",
     "Valid Parentheses, Min Stack, Evaluate Reverse Polish Notation",
     "DSA-Prep"),
    ("Day 14 — Monotonic Stack",
     "Generate Parentheses, Daily Temperatures, Car Fleet",
     "DSA-Prep"),
    ("Day 15 — Linked Lists",
     "Reverse Linked List, Merge Two Lists, Reorder List, Remove Nth Node",
     "DSA-Prep"),
    ("Day 16 — Linked Lists Fast/Slow",
     "Linked List Cycle, Find Duplicate, LRU Cache",
     "DSA-Prep"),
    ("SD #3 — CAP + Message Queues",
     "CAP theorem, consistency models, Kafka pub/sub\\nDDIA Chapter 9",
     "System-Design"),
    ("Day 18 — Trees DFS",
     "Invert Tree, Max Depth, Diameter, Balanced Tree, Same Tree",
     "DSA-Prep"),
    ("Day 19 — Trees BFS + BST",
     "Level Order, Right Side View, Valid BST, LCA, Kth Smallest",
     "DSA-Prep"),
    ("Day 20 — Trees Hard",
     "Max Path Sum, Serialize/Deserialize, Construct from Pre+Inorder",
     "DSA-Prep"),
    ("Day 21 — Graphs BFS/DFS",
     "Number of Islands, Clone Graph, Max Area of Island, Pacific Atlantic",
     "DSA-Prep"),
    ("Day 22 — Graphs Topo + Union-Find",
     "Course Schedule I & II, Redundant Connection, Connected Components",
     "DSA-Prep"),
    ("Day 23 — Heap",
     "Kth Largest in Stream, K Closest Points, Task Scheduler, Find Median",
     "DSA-Prep"),
    ("SD #4 — URL Shortener + Rate Limiter",
     "Full end-to-end design of URL shortener and rate limiter",
     "System-Design"),
    ("MOCK INTERVIEW #1",
     "Pramp or interviewing.io — 2 timed medium problems\\nLink: https://www.pramp.com",
     "Mock-Interview"),
    ("Day 26 — Greedy",
     "Jump Game I & II, Gas Station, Merge Intervals, Non-Overlapping Intervals",
     "DSA-Prep"),
    ("Day 27 — DP 1D",
     "Climbing Stairs, House Robber I & II, Coin Change, LIS",
     "DSA-Prep"),
    ("Day 28 — DP 1D + 2D",
     "Word Break, Partition Equal Subset Sum, Unique Paths, LCS",
     "DSA-Prep"),
    ("Day 29 — Backtracking",
     "Subsets, Combination Sum, Permutations, Word Search",
     "DSA-Prep"),
    ("MOCK INTERVIEW #2",
     "Pramp or interviewing.io — 2 timed medium/hard problems",
     "Mock-Interview"),
    ("SD #5 + Final Review — START APPLYING",
     "Design Twitter Feed or WhatsApp\\nFinal review + submit applications!",
     "System-Design"),
]

# ── Prob/Stats schedule (29 days) ────────────────────────────────────────────
PS_TOPICS = [
    ("PS Day 1 — Intro to Statistics",
     "Stats #1-3: Introduction, Population Statistics, Random Sampling",
     "Prob-Stats"),
    ("PS Day 2 — Descriptive Stats",
     "Stats #4-6: Sample Variance, Normal Approximation, Confidence Intervals",
     "Prob-Stats"),
    ("PS Day 3 — CLT + Hypothesis Testing",
     "Stats #7-9: CLT Example, Hypothesis Testing, Testing Procedure",
     "Prob-Stats"),
    ("PS Day 4 — Type I/II Errors",
     "Stats #10-12: Type I/II Errors, Salk Vaccine, Two-Sided Rejection",
     "Prob-Stats"),
    ("PS Day 5 — P-Hacking + MoM",
     "Stats #13-15: P-Hacking, Parameter Estimation, Method of Moments",
     "Prob-Stats"),
    ("PS Day 6 — MLE with Examples",
     "Stats #16-18: Error in MoM, Bootstrapping, MLE with Examples",
     "Prob-Stats"),
    ("PS Day 7 — MLE Properties + MAP",
     "Stats #19-21: MLE Normal Fit, MLE Properties, MAP Estimation",
     "Prob-Stats"),
    ("PS Day 8 — Chi-Squared + t-distribution",
     "Stats #22-24: Consistency, Chi-Squared Test, Student's t",
     "Prob-Stats"),
    ("PS Day 9 — Bayesian Inference Overview",
     "Stats #25-27: Hypothesis Testing Revisited, Bayesian Inference Overview",
     "Prob-Stats"),
    ("PS Day 10 — Conjugate Priors",
     "Stats #28-30: Bayesian Updates, Conjugate Priors, Normal Conjugate",
     "Prob-Stats"),
    ("PS Day 11 — GMM + Bayesian Regression",
     "Stats #31-33: Gaussian Mixture Models, Monte Carlo Bayesian, Bayesian Linear Regression",
     "Prob-Stats"),
    ("PS Day 12 — Stats Wrap-up",
     "Stats #34-35: Bayesian Linear Regression MAP + Python Example",
     "Prob-Stats"),
    ("PS Day 13 — Probability Overview",
     "Prob #1-3: Overview, Counting Coin Flips, Combinatorics",
     "Prob-Stats"),
    ("PS Day 14 — Set Theory + Binomial",
     "Prob #4-7: Set Theory, Birthday Problem, Quality Control, Binomial",
     "Prob-Stats"),
    ("PS Day 15 — Bayes' Theorem",
     "Prob #8-10: Conditional Probability, Law of Total Probability, Bayes",
     "Prob-Stats"),
    ("PS Day 16 — Independence + Random Vars",
     "Prob #11-13: Bayes Drug Test, Independence, Random Variables",
     "Prob-Stats"),
    ("PS Day 17 — Normal Distribution",
     "Prob #14-16: Bernoulli & Binomial, Normal Distribution, Standard Normal",
     "Prob-Stats"),
    ("PS Day 18 — Poisson + Exponential",
     "Prob #17-19: Poisson, Geometric, Exponential Distribution",
     "Prob-Stats"),
    ("PS Day 19 — Gamma + Functions of RV",
     "Prob #20-22: Hazard Rate, Exponential-Poisson, Gamma Distribution",
     "Prob-Stats"),
    ("PS Day 20 — Chi-Squared + Joint Dists",
     "Prob #23-25: Functions of RV, Rescaling Normal, Chi-Squared",
     "Prob-Stats"),
    ("PS Day 21 — Expected Value",
     "Prob #26-28: Joint Distributions, Marginal/Conditional, Expected Value",
     "Prob-Stats"),
    ("PS Day 22 — Variance + Exponential E&V",
     "Prob #29-31: Properties of EV, Variance, Exponential E & Var",
     "Prob-Stats"),
    ("PS Day 23 — Markov + Chebyshev",
     "Prob #32-34: Two EV Examples, Markov's Inequality, Chebyshev's",
     "Prob-Stats"),
    ("PS Day 24 — LLN + CLT + MGF",
     "Prob #35-37: Law of Large Numbers, CLT, Moment Generating Function",
     "Prob-Stats"),
    ("PS Day 25 — MGF + Lebesgue",
     "Prob #38-40: MGF Example, Lebesgue Measure, Additive MGF",
     "Prob-Stats"),
    ("PS Day 26 — Covariance + Correlation",
     "Prob #41-42: Covariance & Correlation, Gaussian Covariance Example",
     "Prob-Stats"),
    ("PS Day 27 — Tail Sum + Proof of CLT",
     "Prob #43-44: Tail Sum Formula, Proof of Central Limit Theorem",
     "Prob-Stats"),
    ("PS Day 28 — Review Day",
     "Re-watch hardest videos + write formula sheet from memory",
     "Prob-Stats"),
    ("PS Day 29 — Consolidation",
     "Write full 1-page summary from memory. Done!",
     "Prob-Stats"),
]


# ── ICS helpers ───────────────────────────────────────────────────────────────

def _ics_dt(d: date, hour: int) -> str:
    return f"{d.year}{d.month:02d}{d.day:02d}T{hour:02d}0000"


def _make_event(uid: str, d: date, title: str, desc: str, category: str,
                start_hour: int, end_hour: int) -> str:
    desc_esc = desc.replace("\n", "\\n").replace(",", "\\,")
    return "\n".join([
        "BEGIN:VEVENT",
        f"UID:{uid}@claude-memory",
        f"DTSTART:{_ics_dt(d, start_hour)}",
        f"DTEND:{_ics_dt(d, end_hour)}",
        f"SUMMARY:[Study] {title}",
        f"DESCRIPTION:{desc_esc}",
        f"CATEGORIES:{category}",
        "STATUS:CONFIRMED",
        "END:VEVENT",
    ])


def generate(out_path: str | None = None) -> str:
    """Generate the ICS file and return the output path."""
    out_path = out_path or os.path.join(RAW_DIR, "study-plan.ics")

    events = []
    for i, (title, desc, cat) in enumerate(DSA_TOPICS):
        d = DSA_START + timedelta(days=i)
        events.append(_make_event(f"dsa-{d:%Y%m%d}-{i:02d}", d, title, desc, cat, *DSA_BLOCK))

    for i, (title, desc, cat) in enumerate(PS_TOPICS):
        d = PS_START + timedelta(days=i)
        events.append(_make_event(f"ps-{d:%Y%m%d}-{i:02d}", d, title, desc, cat, *PS_BLOCK))

    header = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Claude Memory//Study Plan//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Study Plan 2026",
        f"X-WR-CALDESC:DSA ({DSA_BLOCK[0]}-{DSA_BLOCK[1]}h) + Prob/Stats ({PS_BLOCK[0]}-{PS_BLOCK[1]}h) — Parallel from {DSA_START}",
    ]
    footer = ["END:VCALENDAR"]

    ics = "\r\n".join(header + events + footer)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ics)

    return out_path


if __name__ == "__main__":
    path = generate()
    print(f"Generated {len(DSA_TOPICS) + len(PS_TOPICS)} events → {path}")
    print(f"  DSA:  {DSA_START} – {DSA_START + timedelta(days=len(DSA_TOPICS)-1)}  ({DSA_BLOCK[0]}:00–{DSA_BLOCK[1]}:00)")
    print(f"  PS:   {PS_START} – {PS_START + timedelta(days=len(PS_TOPICS)-1)}  ({PS_BLOCK[0]}:00–{PS_BLOCK[1]}:00)")
    print("\nImport into Google Calendar:")
    print("  calendar.google.com → Settings → Import & Export → Import")
