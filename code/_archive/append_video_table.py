"""
append_video_table.py
---------------------
Appends a complete 79-video reference table to prob-stats-plan.md.
Each row: Day | # | Title (linked) | Key Concepts | Duration (min)
Reads video metadata from the two raw JSON playlist files.

Run from code/:
    uv run python append_video_table.py
"""

import json
import os
from wiki_tools import RAW_DIR, CONCEPTS_DIR

# ── Concept annotations per video (hand-curated) ─────────────────────────────
STATS_CONCEPTS = [
    # index: concept string
    "What is statistics; data types; populations vs samples; descriptive vs inferential",
    "Population mean μ, variance σ²; random sampling; sampling with/without replacement",
    "E[X̄] = μ; Var(X̄) = σ²/n; why averaging reduces variance",
    "Finite population correction factor; sampling without replacement adjustment",
    "Sample variance s² as unbiased estimator of σ²; Bessel's correction (n−1)",
    "Normal approximation to X̄ via CLT; when to use z-interval",
    "Confidence interval construction; z* critical values; 95% CI interpretation",
    "CLT worked example; first look at hypothesis testing setup",
    "Null/alternative hypothesis; test statistic; rejection region; z-test",
    "Step-by-step hypothesis test procedure; one-tailed test; significance level α",
    "Type I error (false positive, α); Type II error (false negative, β); trade-offs",
    "Salk Vaccine real-world trial walkthrough; randomization; placebo control",
    "Two-sided rejection regions; two-tailed test; 'tobacco example'",
    "P-hacking; multiple comparisons problem; why p<0.05 is not enough",
    "Parameter estimation; fitting distributions to data; MoM introduction",
    "Method of Moments (MoM): match sample moments to theoretical moments",
    "Bias and variance of MoM estimator; when MoM fails",
    "Bootstrap resampling; Monte Carlo sampling; empirical distribution",
    "Log-likelihood; MLE for Bernoulli, Poisson, Exponential; maximize log L",
    "MLE for Normal: derive μ̂ = X̄, σ̂² = sample variance; Python example",
    "MLE properties: consistency, asymptotic normality, efficiency (Cramér-Rao)",
    "MAP = MLE + prior; Bayesian extension of MLE; regularization connection",
    "Consistency: estimator converges to true value as n→∞ (plim)",
    "Chi-squared goodness-of-fit test; are two distributions the same? Python example",
    "Student's t-distribution; when σ unknown; degrees of freedom; heavier tails than Normal",
    "Choosing test: Normal vs t vs χ²; matching test to data type and sample size",
    "Properties of χ² and t distributions; relationship to Normal; sum of squares",
    "Bayesian inference overview: prior → likelihood → posterior; Bayes' theorem for distributions",
    "Conjugate priors; Beta-Binomial; Bayesian updates with new data",
    "Normal conjugate prior; exponential family; analytical posterior derivation",
    "Gaussian Mixture Models (GMM); density estimation; empirical Bayes priors",
    "Monte Carlo in Bayesian inference; MCMC intuition; sampling from posterior",
    "Bayesian linear regression; connection to MLE; posterior over weights",
    "MAP estimate in regression = L2-regularized least squares (Gaussian prior)",
    "Full Bayesian linear regression Python implementation; posterior predictive",
]

PROB_CONCEPTS = [
    "Big-picture overview: probability theory roadmap; connections to statistics and ML",
    "Sample space; equally likely outcomes; counting coin flips, dice; P(E) = |E|/|Ω|",
    "Factorial n!; permutations nPr; combinations nCr; counting principle",
    "Set theory for probability: unions ∪, intersections ∩, complements Aᶜ; Venn diagrams",
    "Birthday paradox; complement rule P(A) = 1 − P(Aᶜ); inclusion-exclusion",
    "Quality control example; multinomial distribution; non-destructive inspection",
    "Binomial distribution PMF; mean np; variance np(1−p); multinomial generalisation",
    "Conditional probability P(A|B) = P(A∩B)/P(B); intuition and definition",
    "Law of total probability; partitioning the sample space",
    "Bayes' theorem derivation; worked example; prior × likelihood / evidence",
    "Bayes' theorem: drug test example; false positive paradox; base rate neglect",
    "Independence: P(A∩B) = P(A)P(B); pairwise vs mutual independence",
    "Random variables; PMF (discrete) vs PDF (continuous); CDF F(x); support",
    "Bernoulli(p) trial; Binomial(n,p) PMF, mean, variance; coin-flip connection",
    "Normal distribution as n→∞ limit of Binomial; bell curve; parameters μ, σ²",
    "Standard Normal Z = (X−μ)/σ; Φ(z) table; probability computations",
    "Poisson(λ): rare-event limit of Binomial; PMF; mean = variance = λ",
    "Geometric distribution: first-success; PMF P(X=k) = (1−p)^(k−1)p; memoryless",
    "Exponential distribution: waiting time between Poisson events; PDF λe^(−λx)",
    "Hazard rate; memoryless property of Exponential; P(X>s+t|X>s) = P(X>t)",
    "Exponential inter-arrival times of Poisson process; connection proved",
    "Gamma distribution: sum of k Exponentials; Gamma function Γ(k)",
    "Functions of a random variable; change-of-variable formula; Y = g(X)",
    "Rescaling Normal: Z = (X−μ)/σ derivation via change of variable",
    "Chi-squared distribution: χ²(k) = sum of k squared standard Normals",
    "Joint PDF/PMF f(x,y); joint CDF; support; probability as volume under surface",
    "Marginal distribution via integration/summation; conditional density f(x|y)",
    "E[X] definition (discrete and continuous); linearity; E[aX+b] = aE[X]+b",
    "Properties of expectation: linearity, E[X+Y] = E[X]+E[Y]; E[g(X)]",
    "Variance Var(X) = E[X²]−E[X]²; standard deviation; Var(aX+b) = a²Var(X)",
    "Worked example: E[X] and Var(X) for Exponential distribution",
    "Applied E[g(X)]: temperature C↔F example; kinetic theory of gases",
    "Markov's inequality: P(X≥a) ≤ E[X]/a; first-order concentration bound",
    "Chebyshev's inequality: P(|X−μ|≥kσ) ≤ 1/k²; second-order bound",
    "Law of Large Numbers: X̄ →^p μ as n→∞; weak vs strong LLN",
    "Central Limit Theorem: √n(X̄−μ)/σ → N(0,1); statement and intuition",
    "Moment Generating Function M(t) = E[e^(tX)]; generating moments M^(k)(0) = E[X^k]",
    "MGF of Exponential worked example; using MGF to find moments",
    "Lebesgue measure; Lebesgue integral vs Riemann integral; measure theory intuition",
    "Additive MGF property: M_{X+Y}(t) = M_X(t)·M_Y(t) for independent X,Y",
    "Covariance Cov(X,Y) = E[XY]−E[X]E[Y]; correlation ρ = Cov/σ_xσ_y",
    "Covariance matrix; multivariate Gaussian example; positive semi-definite",
    "Tail sum formula E[X] = ∫₀^∞ P(X>t)dt; proof and applications",
    "Full MGF-based proof of CLT; characteristic functions; convergence in distribution",
]

# ── Load raw data ─────────────────────────────────────────────────────────────
with open(os.path.join(RAW_DIR, "introduction-to-statistics-and-data-analysis.json"), encoding="utf-8") as f:
    stats = json.load(f)["videos"]

with open(os.path.join(RAW_DIR, "probability-bootcamp.json"), encoding="utf-8") as f:
    prob = json.load(f)["videos"]

# ── Day mapping: (day_num, playlist_label, indices_0based) ───────────────────
DAY_SCHEDULE = [
    # Stats videos (0-indexed into stats list)
    (1,  "Stats", [0,1,2]),
    (2,  "Stats", [3,4,5]),
    (3,  "Stats", [6,7,8]),
    (4,  "Stats", [9,10,11]),
    (5,  "Stats", [12,13,14]),
    (6,  "Stats", [15,16,17]),
    (7,  "Stats", [18,19,20]),
    (8,  "Stats", [21,22,23]),
    (9,  "Stats", [24,25,26]),
    (10, "Stats", [27,28,29]),
    (11, "Stats", [30,31,32]),
    (12, "Stats", [33,34]),
    # Prob videos (0-indexed into prob list)
    (13, "Prob",  [0,1,2]),
    (14, "Prob",  [3,4,5,6]),
    (15, "Prob",  [7,8,9]),
    (16, "Prob",  [10,11,12]),
    (17, "Prob",  [13,14,15]),
    (18, "Prob",  [16,17,18]),
    (19, "Prob",  [19,20,21]),
    (20, "Prob",  [22,23,24]),
    (21, "Prob",  [25,26,27]),
    (22, "Prob",  [28,29,30]),
    (23, "Prob",  [31,32,33]),
    (24, "Prob",  [34,35,36]),
    (25, "Prob",  [37,38,39]),
    (26, "Prob",  [40,41]),
    (27, "Prob",  [42,43]),
]

# ── Build table ───────────────────────────────────────────────────────────────
rows = []
rows.append("")
rows.append("---")
rows.append("")
rows.append("## All 79 Videos — Quick Reference")
rows.append("")
rows.append("| Day | # | Video | Concepts Taught | Min |")
rows.append("|-----|---|-------|-----------------|-----|")

for day_num, pl, indices in DAY_SCHEDULE:
    source = stats if pl == "Stats" else prob
    concepts = STATS_CONCEPTS if pl == "Stats" else PROB_CONCEPTS
    label = "S" if pl == "Stats" else "P"

    for idx in indices:
        v = source[idx]
        concept = concepts[idx]
        mins = round(v["duration"] / 60) if v["duration"] else "?"
        title = v["title"].replace("|", "\\|")
        url = v["url"]
        num = v["index"]
        rows.append(f"| {day_num} | {label}{num} | [{title}]({url}) | {concept} | {mins} |")

# ── Append to file ────────────────────────────────────────────────────────────
plan_path = os.path.join(CONCEPTS_DIR, "prob-stats-plan.md")
with open(plan_path, "a", encoding="utf-8") as f:
    f.write("\n".join(rows) + "\n")

total = sum(len(i) for _, _, i in DAY_SCHEDULE)
print(f"Appended {total} video rows to prob-stats-plan.md")
print(f"Stats: {sum(1 for _, pl, i in DAY_SCHEDULE for _ in i if pl=='Stats')} rows")
print(f"Prob:  {sum(1 for _, pl, i in DAY_SCHEDULE for _ in i if pl=='Prob')} rows")
