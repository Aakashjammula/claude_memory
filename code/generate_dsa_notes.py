"""
generate_dsa_notes.py
---------------------
Generates daily notes pages for all DSA + System Design days
(Apr 13 – May 9, 2026). Days 1-4 already exist.

Run from claude_memory/code/:
    uv run python generate_dsa_notes.py
"""

import os

BASE = os.path.dirname(os.path.dirname(__file__))
NOTES_DIR = os.path.join(BASE, "wiki", "notes")
os.makedirs(NOTES_DIR, exist_ok=True)

# LeetCode base URL
LC = "https://leetcode.com/problems"

# Schedule: (slug, date, dow, topic, problems, notes_type)
# notes_type: "dsa" | "sd" | "mock"
# problems: list of (name, lc_slug, difficulty)
# sd_topic: for system design days

schedule = [
    # ── Week 1 remaining ──────────────────────────────────────────
    ("apr-13-day5", "2026-04-13", "Monday", "Strings",
     [("Encode and Decode Strings", "encode-and-decode-strings", "Medium"),
      ("Longest Consecutive Sequence", "longest-consecutive-sequence", "Medium"),
      ("Valid Palindrome", "valid-palindrome", "Easy")],
     "dsa", "Week 1 — Strings"),

    ("apr-14-day6", "2026-04-14", "Tuesday", "Two Pointers",
     [("Two Sum II", "two-sum-ii-input-array-is-sorted", "Medium"),
      ("3Sum", "3sum", "Medium"),
      ("Container With Most Water", "container-with-most-water", "Medium")],
     "dsa", "Week 1 — Two Pointers"),

    ("apr-15-day7", "2026-04-15", "Wednesday", "Two Pointers + Sliding Window",
     [("Trapping Rain Water", "trapping-rain-water", "Hard"),
      ("Longest Substring Without Repeating Characters", "longest-substring-without-repeating-characters", "Medium")],
     "dsa", "Week 1 — Two Pointers + Sliding Window"),

    ("apr-16-day8", "2026-04-16", "Thursday", "Sliding Window",
     [("Longest Repeating Character Replacement", "longest-repeating-character-replacement", "Medium"),
      ("Permutation in String", "permutation-in-string", "Medium")],
     "dsa", "Week 1 — Sliding Window"),

    ("apr-17-day9", "2026-04-17", "Friday", "Sliding Window Hard + Week Review",
     [("Minimum Window Substring", "minimum-window-substring", "Hard")],
     "dsa", "Week 1 — Review"),

    # ── Week 2 ────────────────────────────────────────────────────
    ("apr-18-day10-sd", "2026-04-18", "Saturday", "System Design #2: Databases",
     [], "sd",
     "Databases — SQL vs NoSQL, indexing, replication, sharding"),

    ("apr-19-day11", "2026-04-19", "Sunday", "Binary Search",
     [("Binary Search", "binary-search", "Easy"),
      ("Search a 2D Matrix", "search-a-2d-matrix", "Medium"),
      ("Koko Eating Bananas", "koko-eating-bananas", "Medium")],
     "dsa", "Week 2 — Binary Search"),

    ("apr-20-day12", "2026-04-20", "Monday", "Binary Search",
     [("Find Minimum in Rotated Sorted Array", "find-minimum-in-rotated-sorted-array", "Medium"),
      ("Search in Rotated Sorted Array", "search-in-rotated-sorted-array", "Medium"),
      ("Time Based Key-Value Store", "time-based-key-value-store", "Medium")],
     "dsa", "Week 2 — Binary Search"),

    ("apr-21-day13", "2026-04-21", "Tuesday", "Stack",
     [("Valid Parentheses", "valid-parentheses", "Easy"),
      ("Min Stack", "min-stack", "Medium"),
      ("Evaluate Reverse Polish Notation", "evaluate-reverse-polish-notation", "Medium")],
     "dsa", "Week 2 — Stack"),

    ("apr-22-day14", "2026-04-22", "Wednesday", "Monotonic Stack",
     [("Generate Parentheses", "generate-parentheses", "Medium"),
      ("Daily Temperatures", "daily-temperatures", "Medium"),
      ("Car Fleet", "car-fleet", "Medium")],
     "dsa", "Week 2 — Monotonic Stack"),

    ("apr-23-day15", "2026-04-23", "Thursday", "Linked Lists",
     [("Reverse Linked List", "reverse-linked-list", "Easy"),
      ("Merge Two Sorted Lists", "merge-two-sorted-lists", "Easy"),
      ("Reorder List", "reorder-list", "Medium"),
      ("Remove Nth Node From End of List", "remove-nth-node-from-end-of-list", "Medium")],
     "dsa", "Week 2 — Linked Lists"),

    ("apr-24-day16", "2026-04-24", "Friday", "Linked Lists — Fast/Slow Pointers",
     [("Linked List Cycle", "linked-list-cycle", "Easy"),
      ("Find the Duplicate Number", "find-the-duplicate-number", "Medium"),
      ("LRU Cache", "lru-cache", "Medium")],
     "dsa", "Week 2 — Linked Lists Fast/Slow"),

    # ── Week 3 ────────────────────────────────────────────────────
    ("apr-25-day17-sd", "2026-04-25", "Saturday", "System Design #3: CAP Theorem + Message Queues",
     [], "sd",
     "CAP theorem, consistency models, message queues (Kafka), pub/sub"),

    ("apr-26-day18", "2026-04-26", "Sunday", "Trees — DFS",
     [("Invert Binary Tree", "invert-binary-tree", "Easy"),
      ("Maximum Depth of Binary Tree", "maximum-depth-of-binary-tree", "Easy"),
      ("Diameter of Binary Tree", "diameter-of-binary-tree", "Easy"),
      ("Balanced Binary Tree", "balanced-binary-tree", "Easy"),
      ("Same Tree", "same-tree", "Easy")],
     "dsa", "Week 3 — Trees DFS"),

    ("apr-27-day19", "2026-04-27", "Monday", "Trees — BFS + BST",
     [("Binary Tree Level Order Traversal", "binary-tree-level-order-traversal", "Medium"),
      ("Binary Tree Right Side View", "binary-tree-right-side-view", "Medium"),
      ("Validate Binary Search Tree", "validate-binary-search-tree", "Medium"),
      ("Lowest Common Ancestor of a BST", "lowest-common-ancestor-of-a-binary-search-tree", "Medium"),
      ("Kth Smallest Element in a BST", "kth-smallest-element-in-a-bst", "Medium")],
     "dsa", "Week 3 — Trees BFS + BST"),

    ("apr-28-day20", "2026-04-28", "Tuesday", "Trees — Hard",
     [("Binary Tree Maximum Path Sum", "binary-tree-maximum-path-sum", "Hard"),
      ("Serialize and Deserialize Binary Tree", "serialize-and-deserialize-binary-tree", "Hard"),
      ("Construct Binary Tree from Preorder and Inorder Traversal", "construct-binary-tree-from-preorder-and-inorder-traversal", "Medium")],
     "dsa", "Week 3 — Trees Hard"),

    ("apr-29-day21", "2026-04-29", "Wednesday", "Graphs — BFS/DFS",
     [("Number of Islands", "number-of-islands", "Medium"),
      ("Clone Graph", "clone-graph", "Medium"),
      ("Max Area of Island", "max-area-of-island", "Medium"),
      ("Pacific Atlantic Water Flow", "pacific-atlantic-water-flow", "Medium")],
     "dsa", "Week 3 — Graphs BFS/DFS"),

    ("apr-30-day22", "2026-04-30", "Thursday", "Graphs — Topological Sort + Union-Find",
     [("Course Schedule", "course-schedule", "Medium"),
      ("Course Schedule II", "course-schedule-ii", "Medium"),
      ("Redundant Connection", "redundant-connection", "Medium"),
      ("Number of Connected Components in an Undirected Graph", "number-of-connected-components-in-an-undirected-graph", "Medium")],
     "dsa", "Week 3 — Graphs Topo Sort + Union-Find"),

    ("may-01-day23", "2026-05-01", "Friday", "Heap / Priority Queue",
     [("Kth Largest Element in a Stream", "kth-largest-element-in-a-stream", "Easy"),
      ("K Closest Points to Origin", "k-closest-points-to-origin", "Medium"),
      ("Task Scheduler", "task-scheduler", "Medium"),
      ("Find Median from Data Stream", "find-median-from-data-stream", "Hard")],
     "dsa", "Week 3 — Heap"),

    # ── Week 4 ────────────────────────────────────────────────────
    ("may-02-day24-sd", "2026-05-02", "Saturday", "System Design #4: URL Shortener + Rate Limiter",
     [], "sd",
     "End-to-end designs — URL shortener + Rate limiter (full architecture)"),

    ("may-03-day25-mock", "2026-05-03", "Sunday", "Mock Interview #1",
     [], "mock",
     "Mock Interview #1 — 2 medium problems timed (Pramp / interviewing.io)"),

    ("may-04-day26", "2026-05-04", "Monday", "Greedy",
     [("Jump Game", "jump-game", "Medium"),
      ("Jump Game II", "jump-game-ii", "Medium"),
      ("Gas Station", "gas-station", "Medium"),
      ("Merge Intervals", "merge-intervals", "Medium"),
      ("Non-overlapping Intervals", "non-overlapping-intervals", "Medium")],
     "dsa", "Week 4 — Greedy"),

    ("may-05-day27", "2026-05-05", "Tuesday", "Dynamic Programming 1D",
     [("Climbing Stairs", "climbing-stairs", "Easy"),
      ("House Robber", "house-robber", "Medium"),
      ("House Robber II", "house-robber-ii", "Medium"),
      ("Coin Change", "coin-change", "Medium"),
      ("Longest Increasing Subsequence", "longest-increasing-subsequence", "Medium")],
     "dsa", "Week 4 — DP 1D"),

    ("may-06-day28", "2026-05-06", "Wednesday", "DP 1D + 2D",
     [("Word Break", "word-break", "Medium"),
      ("Partition Equal Subset Sum", "partition-equal-subset-sum", "Medium"),
      ("Unique Paths", "unique-paths", "Medium"),
      ("Longest Common Subsequence", "longest-common-subsequence", "Medium")],
     "dsa", "Week 4 — DP 1D + 2D"),

    ("may-07-day29", "2026-05-07", "Thursday", "Backtracking",
     [("Subsets", "subsets", "Medium"),
      ("Combination Sum", "combination-sum", "Medium"),
      ("Permutations", "permutations", "Medium"),
      ("Word Search", "word-search", "Medium")],
     "dsa", "Week 4 — Backtracking"),

    ("may-08-day30-mock", "2026-05-08", "Friday", "Mock Interview #2",
     [], "mock",
     "Mock Interview #2 — 2 medium/hard problems timed (Pramp / interviewing.io)"),

    ("may-09-day31-sd", "2026-05-09", "Saturday", "System Design #5 + Final Review",
     [], "sd",
     "Design Twitter Feed OR WhatsApp (full architecture) + final review + START APPLYING"),
]

SD_RESOURCES = {
    "Databases — SQL vs NoSQL, indexing, replication, sharding": [
        ("ByteByteGo — SQL vs NoSQL", "https://www.youtube.com/watch?v=_Ss42Vb1SU4"),
        ("ByteByteGo — Database Indexing", "https://www.youtube.com/watch?v=-qNSXK7s7_w"),
        ("DDIA Chapter 3: Storage Engines", "https://dataintensive.net"),
    ],
    "CAP theorem, consistency models, message queues (Kafka), pub/sub": [
        ("ByteByteGo — CAP Theorem", "https://www.youtube.com/watch?v=BHqjEjzAicA"),
        ("ByteByteGo — Kafka in 5 Minutes", "https://www.youtube.com/watch?v=PzPXRmVHMxI"),
        ("DDIA Chapter 9: Consistency and Consensus", "https://dataintensive.net"),
    ],
    "End-to-end designs — URL shortener + Rate limiter (full architecture)": [
        ("ByteByteGo — Design URL Shortener", "https://www.youtube.com/watch?v=fMZMm_0ZhK4"),
        ("ByteByteGo — Rate Limiter", "https://www.youtube.com/watch?v=FU4WlwfS3G0"),
    ],
    "Design Twitter Feed OR WhatsApp (full architecture) + final review + START APPLYING": [
        ("ByteByteGo — Design Twitter", "https://www.youtube.com/watch?v=wYk0xPP_P_8"),
        ("ByteByteGo — Design WhatsApp", "https://www.youtube.com/watch?v=vvhC64hQZMk"),
    ],
}

MOCK_RESOURCES = [
    ("Pramp — Free mock interviews", "https://www.pramp.com"),
    ("interviewing.io — Anonymous mock interviews", "https://interviewing.io"),
    ("LeetCode — Company-tagged problems", "https://leetcode.com/problemset/"),
]


def make_dsa_note(slug, date, dow, topic, problems, week_label, next_slug):
    lines = []
    lines.append("---")
    lines.append("type: note")
    lines.append(f"date: {date}")
    lines.append(f"phase: DSA — {week_label}")
    lines.append(f"topic: {topic}")
    lines.append("tags: [dsa, python, leetcode, coding]")
    lines.append("---")
    lines.append("")
    lines.append(f"# {topic}")
    lines.append(f"**Date:** {dow}, {date}")
    lines.append(f"**Phase:** {week_label}")
    lines.append(f"**Goal:** Solve each problem within 20–25 min")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Resources")
    lines.append("- NeetCode Roadmap: https://neetcode.io/roadmap")
    lines.append("- NeetCode YouTube: https://www.youtube.com/@NeetCode")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Problems")
    lines.append("")

    for i, (name, lc_slug, diff) in enumerate(problems, 1):
        url = f"https://leetcode.com/problems/{lc_slug}/"
        lines.append(f"### {i}. {name}")
        lines.append(f"**Link:** {url}")
        lines.append(f"**Difficulty:** {diff}")
        lines.append(f"**Pattern:**")
        lines.append(f"**Approach:**")
        lines.append(f"**Time:** &nbsp;&nbsp; **Space:**")
        lines.append(f"**Struggled with:**")
        lines.append("```python")
        lines.append("")
        lines.append("```")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Patterns Identified Today")
    lines.append("-")
    lines.append("")
    lines.append("## Key Takeaways")
    lines.append("-")
    lines.append("")
    lines.append("## What Was Hard")
    lines.append("-")
    lines.append("")
    lines.append("## What to Revisit")
    lines.append("-")
    lines.append("")
    if next_slug:
        lines.append(f"_Next: [[{next_slug}]]_")
    return "\n".join(lines)


def make_sd_note(slug, date, dow, topic, week_label, next_slug):
    resources = SD_RESOURCES.get(week_label, [])
    lines = []
    lines.append("---")
    lines.append("type: note")
    lines.append(f"date: {date}")
    lines.append(f"phase: System Design")
    lines.append(f"topic: {topic}")
    lines.append("tags: [system-design, coding, backend]")
    lines.append("---")
    lines.append("")
    lines.append(f"# System Design — {topic}")
    lines.append(f"**Date:** {dow}, {date}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Resources")
    for name, url in resources:
        lines.append(f"- [{name}]({url})")
    if not resources:
        lines.append("- ByteByteGo: https://www.youtube.com/@ByteByteGo")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## How to Use This Session (4 hrs)")
    lines.append("| Block | Time | Task |")
    lines.append("|-------|------|------|")
    lines.append("| Block 1 | 1 hr | Watch videos + read DDIA chapter |")
    lines.append("| Block 2 | 1 hr | Fill in concept notes below |")
    lines.append("| Block 3 | 1 hr | Draw architecture diagram from scratch |")
    lines.append("| Block 4 | 1 hr | Answer mock design question |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Concept Notes")
    lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("## Architecture Diagram")
    lines.append("*(draw from scratch after watching — paste photo or ASCII here)*")
    lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("## Mock Design Question")
    lines.append("*(write your answer as if in a real interview — 10–15 min)*")
    lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Key Takeaways")
    lines.append("-")
    lines.append("")
    lines.append("## What Was Confusing")
    lines.append("-")
    lines.append("")
    lines.append("## What to Revisit")
    lines.append("-")
    lines.append("")
    if next_slug:
        lines.append(f"_Next: [[{next_slug}]]_")
    return "\n".join(lines)


def make_mock_note(slug, date, dow, topic, week_label, next_slug):
    lines = []
    lines.append("---")
    lines.append("type: note")
    lines.append(f"date: {date}")
    lines.append(f"phase: Mock Interview")
    lines.append(f"topic: {topic}")
    lines.append("tags: [mock-interview, dsa, coding]")
    lines.append("---")
    lines.append("")
    lines.append(f"# {topic}")
    lines.append(f"**Date:** {dow}, {date}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Resources")
    for name, url in MOCK_RESOURCES:
        lines.append(f"- [{name}]({url})")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Instructions")
    lines.append("- Set a 45-minute timer per problem")
    lines.append("- No hints, no looking up solutions")
    lines.append("- Think out loud as if in a real interview")
    lines.append("- After each problem: rate confidence (1-5) and note what you'd do differently")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Problem 1")
    lines.append("**Title:**")
    lines.append("**Link:**")
    lines.append("**Difficulty:**")
    lines.append("**Time taken:**")
    lines.append("**Approach:**")
    lines.append("**Did you solve it?**")
    lines.append("**What would you do differently?**")
    lines.append("")
    lines.append("```python")
    lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("## Problem 2")
    lines.append("**Title:**")
    lines.append("**Link:**")
    lines.append("**Difficulty:**")
    lines.append("**Time taken:**")
    lines.append("**Approach:**")
    lines.append("**Did you solve it?**")
    lines.append("**What would you do differently?**")
    lines.append("")
    lines.append("```python")
    lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Overall Feedback")
    lines.append("**Confidence rating (1-5):**")
    lines.append("**Biggest weakness identified:**")
    lines.append("**What to focus on next:**")
    lines.append("")
    if next_slug:
        lines.append(f"_Next: [[{next_slug}]]_")
    return "\n".join(lines)


created = []
for i, entry in enumerate(schedule):
    slug, date, dow, topic, problems, notes_type, week_label = entry
    next_slug = schedule[i + 1][0] if i + 1 < len(schedule) else ""
    filepath = os.path.join(NOTES_DIR, f"{slug}.md")

    if notes_type == "dsa":
        content = make_dsa_note(slug, date, dow, topic, problems, week_label, next_slug)
    elif notes_type == "sd":
        content = make_sd_note(slug, date, dow, topic, week_label, next_slug)
    else:  # mock
        content = make_mock_note(slug, date, dow, topic, week_label, next_slug)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    created.append(slug)
    print(f"Created: {slug}.md ({notes_type})")

print(f"\nDone! Created {len(created)} DSA/SD notes in wiki/notes/")
