---
type: concept
tags: [coding, personal, goals, probability, statistics, math, ml]
sources: 0
---

# Probability & Statistics Study Plan

**Channel:** Steve Brunton (@Eigensteve) — [[steve-brunton]]
**Start date:** 2026-04-11 (parallel with DSA)
**End date:** 2026-05-09 (4 weeks, parallel with DSA)
**Daily commitment:** 3 videos/day (~2 hrs evening, after 2 hrs DSA)
**Total videos:** 79 (35 + 44)

---

## Playlists

| # | Playlist | Videos | Link |
|---|----------|--------|------|
| 1 | Introduction to Statistics and Data Analysis | 35 | https://www.youtube.com/playlist?list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx |
| 2 | Probability Bootcamp | 44 | https://www.youtube.com/playlist?list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V |

---

## Why This Matters (GenAI SWE)

- Probability is foundational for ML system design interviews
- Bayesian thinking, distributions, expectation appear in FAANG ML rounds
- Stats underpins model evaluation, A/B testing, data pipelines
- Directly relevant to GenAI work: sampling, temperature, token probabilities

---

## Week 1 — Introduction to Statistics (Apr 11–17)
**Playlist 1, Videos 1–21 | 3 videos/day**

| Day | Date | Videos | Titles | Key Concepts |
|-----|------|--------|--------|-------------|
| 1 | Apr 11 (Sat) | Stats #1–3 | Introduction to Statistics and Data Analysis · Population Statistics and Random Sampling · Random Sampling: Expected Value and Variance of the Sample Mean | What is statistics; data types; population vs sample; μ, σ; E[X̄], Var(X̄) |
| 2 | Apr 12 (Sun) | Stats #4–6 | Random Sampling Without Replacement (Finite n Correction) · Sample Variance in Random Population Sampling · Normal Approximation to Sample Mean | Finite population correction; unbiased sample variance s²; CLT-based normal approximation |
| 3 | Apr 13 (Mon) | Stats #7–9 | Confidence Intervals · Central Limit Theorem Example & Hypothesis Testing · Hypothesis Testing in Statistics | CI construction; z-interval; CLT applied end-to-end; null/alternative hypothesis; test statistic |
| 4 | Apr 14 (Tue) | Stats #10–12 | Hypothesis Testing Procedure · Hypothesis Testing: Type I and Type II Errors · Hypothesis Testing Example: Salk Vaccine Trial | Rejection region; α, β; power; real-world clinical trial walkthrough |
| 5 | Apr 15 (Wed) | Stats #13–15 | Two-Sided Rejection Regions in Hypothesis Testing · P-Hacking · Parameter Estimation and Fitting Distributions | Two-tailed tests; multiple comparisons problem; p-hacking risks; MoM intro |
| 6 | Apr 16 (Thu) | Stats #16–18 | Method of Moments to Fit Distributions from Data · Error in the Method of Moments · Bootstrapping and Monte Carlo Sampling | MoM estimator derivation; bias/variance of MoM; bootstrap resampling; Monte Carlo |
| 7 | Apr 17 (Fri) | Stats #19–21 | Maximum Likelihood Estimation (MLE) with Examples · MLE: Fitting a Normal Distribution · Properties of MLE | Log-likelihood; MLE for Bernoulli, Poisson, Normal; consistency, asymptotic normality, efficiency |

---

## Week 2 — Statistics cont. + Probability starts (Apr 18–24)
**Playlist 1 #22–35 finish + Playlist 2 #1–7**

| Day | Date | Videos | Titles | Key Concepts |
|-----|------|--------|--------|-------------|
| 8 | Apr 18 (Sat) | Stats #22–24 | Bayesian MAP Estimation · Consistency of Parameter Estimates · The Chi-Squared Test | MAP = MLE + prior; consistency (plim); χ² goodness-of-fit test; Python example |
| 9 | Apr 19 (Sun) | Stats #25–27 | Student's t-distribution · Hypothesis Testing Revisited: Normal, t, χ² · Properties of Chi-Squared and Student's t | t-distribution when σ unknown; choosing the right test; degrees of freedom, heavier tails |
| 10 | Apr 20 (Mon) | Stats #28–30 | Bayesian Inference: Overview · Bayesian Updates and Conjugate Priors · Conjugate Priors Example: Normal + Exponential Family | Prior → posterior via Bayes; conjugate priors; Beta-Binomial, Normal-Normal; exponential family |
| 11 | Apr 21 (Tue) | Stats #31–33 | Density Estimation with GMMs and Empirical Priors · Monte Carlo Sampling in Bayesian Inference · Bayesian Linear Regression and MLE | GMM; EM intuition; MCMC via Monte Carlo; Bayesian regression vs frequentist |
| 12 | Apr 22 (Wed) | Stats #34–35 | Bayesian Linear Regression and MAP · Bayesian Linear Regression [Python Example] | MAP as regularized regression (L2 = Gaussian prior); full Python implementation |
| 13 | Apr 23 (Thu) | Prob #1–3 | Probability and Statistics: Overview · Gentle Introduction: Counting Coin Flips and Dice · Counting Probabilities with Combinatorics and the Factorial | Sample space; equiprobable outcomes; n!, nPr, nCr; counting principles |
| 14 | Apr 24 (Fri) | Prob #4–7 | Set Theory in Probability: Sample Spaces and Events · The Birthday Problem · Quality Control and Multinomial Distribution · Binomial Distribution and Multinomial | Unions/intersections; complement rule; birthday paradox; P(A) = 1 − P(Aᶜ); multinomial; binomial PMF |

---

## Week 3 — Probability Core (Apr 25–May 1)
**Playlist 2, Videos 8–28 | 3 videos/day**

| Day | Date | Videos | Titles | Key Concepts |
|-----|------|--------|--------|-------------|
| 15 | Apr 25 (Sat) | Prob #8–10 | Conditional Probabilities · The Law of Total Probability · Bayes' Theorem (with Example!) | P(A\|B); conditional probability definition; law of total prob; Bayes' theorem derivation + worked example |
| 16 | Apr 26 (Sun) | Prob #11–13 | Bayes' Theorem Example: Drug Testing · Independence in Probability · Random Variables and Probability Distributions | False positive intuition; P(A∩B) = P(A)P(B); PMF vs PDF; CDF; discrete vs continuous RVs |
| 17 | Apr 27 (Mon) | Prob #14–16 | Bernoulli and Binomial Random Variables · The Normal Distribution: Limit of Binomial for Large n · The Standard Unit Normal | Bernoulli trials; Binomial PMF mean/variance; Normal as Binomial limit; z-score; Φ(z) lookup |
| 18 | Apr 28 (Tue) | Prob #17–19 | The Poisson Distribution · The Geometric Distribution · The Exponential Distribution | Poisson as rare-event Binomial limit; Geometric = first-success; Exponential as continuous waiting time |
| 19 | Apr 29 (Wed) | Prob #20–22 | The Hazard Rate and Memoryless Property · Exponential–Poisson Connection · The Gamma Distribution | Hazard rate λ; memoryless property; inter-arrival times of Poisson process; Gamma as sum of Exponentials |
| 20 | Apr 30 (Thu) | Prob #23–25 | Functions of a Random Variable · Rescaling the Normal to Mean 0, Variance 1 · The Chi-Squared Distribution | Change-of-variable formula; standardization Z = (X−μ)/σ; χ²(k) = sum of k squared normals |
| 21 | May 1 (Fri) | Prob #26–28 | Joint Probability Distributions · Joint Distributions: Marginal and Conditional Densities · The Expected Value (Mean) | Joint PDF/PMF; marginalization; conditional density f(x\|y); E[X] = ∫x·f(x)dx |

---

## Week 4 — Probability Advanced + Review (May 2–9)
**Playlist 2, Videos 29–44 + full review**

| Day | Date | Videos | Titles | Key Concepts |
|-----|------|--------|--------|-------------|
| 22 | May 2 (Sat) | Prob #29–31 | Properties of the Expected Value · Variance and Standard Deviation · Expectation and Variance of an Exponential Distribution | Linearity of E; E[aX+b]; Var(X) = E[X²]−E[X]²; worked Exponential E & Var example |
| 23 | May 3 (Sun) | Prob #32–34 | Two Examples of Expected Values (Temperature & Kinetic Theory) · Markov's Inequality · Chebyshev's Inequality | Applied E[g(X)]; P(X≥a) ≤ E[X]/a; P(\|X−μ\|≥kσ) ≤ 1/k²; tail bound intuition |
| 24 | May 4 (Mon) | Prob #35–37 | The Law of Large Numbers · The Central Limit Theorem · The Moment Generating Function | LLN: X̄ → μ; CLT: √n(X̄−μ)/σ → N(0,1); MGF M(t) = E[eᵗˣ]; moments from MGF |
| 25 | May 5 (Tue) | Prob #38–40 | Example of the MGF · The Lebesgue Measure in Probability · Additive Property of the MGF | MGF of Exponential; Lebesgue integral vs Riemann; MGF of sum = product of MGFs |
| 26 | May 6 (Wed) | Prob #41–42 | Covariance and Correlation · Covariance Example with Gaussian Distributions | Cov(X,Y) = E[XY]−E[X]E[Y]; ρ = Cov/σ_xσ_y; correlation matrix; multivariate Gaussian |
| 27 | May 7 (Thu) | Prob #43–44 | The Tail Sum Formula · Proof of the Central Limit Theorem | E[X] = ∫P(X>t)dt; full MGF-based CLT proof |
| 28 | May 8 (Fri) | — | **Review Day** | Re-watch 3–5 hardest videos; write formula sheet from memory |
| 29 | May 9 (Sat) | — | **Consolidation** | Write 1-page summary from memory; check against notes |

---

## Key Concepts to Master

| Concept | Video(s) | Why It Matters for GenAI/FAANG |
|---------|----------|-------------------------------|
| Bayes' theorem | Stats #28–30, Prob #10–11 | ML priors, Bayesian inference, spam filters |
| Central Limit Theorem | Stats #8, Prob #36, #44 | Justifies normal approximations everywhere |
| MLE | Stats #19–21 | Foundation of neural network training (cross-entropy = neg log-likelihood) |
| MAP estimation | Stats #22 | Regularization = Bayesian prior (L2 = Gaussian prior) |
| Conditional probability | Prob #8 | Probabilistic reasoning, chains, directed graphical models |
| Distributions (Normal, Poisson, Binomial, Exponential) | Prob #14–22 | Everywhere in ML: token sampling, latency, traffic modeling |
| Hypothesis testing + p-values | Stats #7–13 | A/B testing, model evaluation, statistical significance |
| Expectation, Variance, Moments | Prob #28–31, #37 | Loss functions, risk, model calibration |
| Markov's + Chebyshev's inequalities | Prob #33–34 | Concentration bounds; PAC learning theory |
| LLN + CLT | Prob #35–36 | Why large datasets work; averaging reduces variance |
| Covariance + Correlation | Prob #41–42 | Feature correlation, covariance matrices, PCA |

---

## Progress Tracker

| Week | Dates | Videos | Status | Notes |
|------|-------|--------|--------|-------|
| Stats #1–21 | Apr 11–17 | Stats 1–21 | Not started | |
| Stats #22–35 + Prob #1–7 | Apr 18–24 | Stats 22–35, Prob 1–7 | Not started | |
| Prob #8–28 | Apr 25–May 1 | Prob 8–28 | Not started | |
| Prob #29–44 + Review | May 2–9 | Prob 29–44 + review | Not started | |

---

## Connections
- [[steve-brunton]] — primary educator; both playlists are his
- [[dsa-prep]] — runs in parallel (Apr 11 – May 11)
- [[personal-themes]] — learning goals
- [[my-projects]] — probability directly applies to GenAI/S2S projects

---

## All 79 Videos — Quick Reference

| Day | # | Video | Concepts Taught | Min |
|-----|---|-------|-----------------|-----|
| 1 | S1 | [Introduction to Statistics and Data Analysis](https://www.youtube.com/watch?v=QIXUTsdj_oA) | What is statistics; data types; populations vs samples; descriptive vs inferential | 22 |
| 1 | S2 | [Population Statistics and Random Sampling](https://www.youtube.com/watch?v=OlkL1YatyHI) | Population mean μ, variance σ²; random sampling; sampling with/without replacement | 24 |
| 1 | S3 | [Random Sampling in Statistics: Expected Value and Variance of the Sample Mean](https://www.youtube.com/watch?v=Gg3d-rn9eEU) | E[X̄] = μ; Var(X̄) = σ²/n; why averaging reduces variance | 16 |
| 2 | S4 | [Random Sampling Without Replacement (Finite "n" Correction)](https://www.youtube.com/watch?v=IDvp3pMm16k) | Finite population correction factor; sampling without replacement adjustment | 12 |
| 2 | S5 | [Sample Variance in Random Population Sampling](https://www.youtube.com/watch?v=yNnUVHfX5yQ) | Sample variance s² as unbiased estimator of σ²; Bessel's correction (n−1) | 12 |
| 2 | S6 | [Normal Approximation to Sample Mean](https://www.youtube.com/watch?v=Arbj9SoU9Cs) | Normal approximation to X̄ via CLT; when to use z-interval | 20 |
| 3 | S7 | [Confidence Intervals](https://www.youtube.com/watch?v=qTVdV8ITZfk) | Confidence interval construction; z* critical values; 95% CI interpretation | 17 |
| 3 | S8 | [Central Limit Theorem Example & Hypothesis Testing](https://www.youtube.com/watch?v=bOrihOzYXWA) | CLT worked example; first look at hypothesis testing setup | 10 |
| 3 | S9 | [Hypothesis Testing in Statistics](https://www.youtube.com/watch?v=vVDahuv1bq8) | Null/alternative hypothesis; test statistic; rejection region; z-test | 25 |
| 4 | S10 | [Hypothesis Testing Procedure](https://www.youtube.com/watch?v=WYifBkNg1r8) | Step-by-step hypothesis test procedure; one-tailed test; significance level α | 18 |
| 4 | S11 | [Hypothesis Testing: Type I and Type II Errors](https://www.youtube.com/watch?v=129NuU3A7rM) | Type I error (false positive, α); Type II error (false negative, β); trade-offs | 10 |
| 4 | S12 | [Hypothesis Testing Example: Salk Vaccine Trial](https://www.youtube.com/watch?v=V3aYG8mLmkI) | Salk Vaccine real-world trial walkthrough; randomization; placebo control | 16 |
| 5 | S13 | [Could Tobacco be Good for you?  Two Sided Rejection Regions in Hypothesis Testing](https://www.youtube.com/watch?v=znnim8MTl0c) | Two-sided rejection regions; two-tailed test; 'tobacco example' | 12 |
| 5 | S14 | [Lies, Damn Lies, and Statistics... P-Hacking](https://www.youtube.com/watch?v=Et9pORQHR2A) | P-hacking; multiple comparisons problem; why p<0.05 is not enough | 19 |
| 5 | S15 | [Parameter Estimation and Fitting Distributions](https://www.youtube.com/watch?v=7XVA2JRzYoE) | Parameter estimation; fitting distributions to data; MoM introduction | 24 |
| 6 | S16 | [Method of Moments to Fit Distributions from Data](https://www.youtube.com/watch?v=IZk0Iq2hI3c) | Method of Moments (MoM): match sample moments to theoretical moments | 11 |
| 6 | S17 | [Error in the Method of Moments](https://www.youtube.com/watch?v=341Ecdkfb-s) | Bias and variance of MoM estimator; when MoM fails | 19 |
| 6 | S18 | [Bootstrapping and Monte Carlo Sampling in Statistics](https://www.youtube.com/watch?v=wsU7YLcPXmE) | Bootstrap resampling; Monte Carlo sampling; empirical distribution | 17 |
| 7 | S19 | [Maximum Likelihood Estimation (MLE) with Examples](https://www.youtube.com/watch?v=rCdxlN6Ph14) | Log-likelihood; MLE for Bernoulli, Poisson, Exponential; maximize log L | 24 |
| 7 | S20 | [Maximum Likelihood Estimation Example: Fitting a Normal Distribution with Data](https://www.youtube.com/watch?v=x5GOUgCTkjM) | MLE for Normal: derive μ̂ = X̄, σ̂² = sample variance; Python example | 16 |
| 7 | S21 | [Properties of Maximum Likelihood Estimation](https://www.youtube.com/watch?v=QVF0oOh7s8c) | MLE properties: consistency, asymptotic normality, efficiency (Cramér-Rao) | 14 |
| 8 | S22 | [Bayesian Maximum Aposteriori Estimation (MAP): Extending Maximum Likelihood Estimation](https://www.youtube.com/watch?v=xgfexqYxrDU) | MAP = MLE + prior; Bayesian extension of MLE; regularization connection | 13 |
| 8 | S23 | [Consistency of Parameter Estimates in Statistics](https://www.youtube.com/watch?v=27wRPAg3H28) | Consistency: estimator converges to true value as n→∞ (plim) | 10 |
| 8 | S24 | [The Chi-Squared Test : Are Two Distributions the Same?  (with Python Example)](https://www.youtube.com/watch?v=63S3FLISKMs) | Chi-squared goodness-of-fit test; are two distributions the same? Python example | 23 |
| 9 | S25 | [Student's t-distribution in Statistics](https://www.youtube.com/watch?v=kQoPUR0hQNo) | Student's t-distribution; when σ unknown; degrees of freedom; heavier tails than Normal | 17 |
| 9 | S26 | [Hypothesis Testing Revisited: Normal, t, and Chi-Squared Distribution Tests](https://www.youtube.com/watch?v=u793OrRvZBk) | Choosing test: Normal vs t vs χ²; matching test to data type and sample size | 11 |
| 9 | S27 | [Properties of Chi-Squared and Student's t Distributions](https://www.youtube.com/watch?v=so04ygeccwk) | Properties of χ² and t distributions; relationship to Normal; sum of squares | 10 |
| 10 | S28 | [Bayesian Inference: Overview](https://www.youtube.com/watch?v=XCEpIBqKogo) | Bayesian inference overview: prior → likelihood → posterior; Bayes' theorem for distributions | 30 |
| 10 | S29 | [Bayesian Updates and Conjugate Priors](https://www.youtube.com/watch?v=GqSX-8AQL90) | Conjugate priors; Beta-Binomial; Bayesian updates with new data | 18 |
| 10 | S30 | [Conjugate Priors Example: Normal Distribution and the Exponential Family of Distributions](https://www.youtube.com/watch?v=q8ypTSQotXQ) | Normal conjugate prior; exponential family; analytical posterior derivation | 19 |
| 11 | S31 | [Density Estimation with Gaussian Mixture Models (GMM) and Empirical Priors](https://www.youtube.com/watch?v=a1pvm1QGXYg) | Gaussian Mixture Models (GMM); density estimation; empirical Bayes priors | 18 |
| 11 | S32 | [Monte Carlo Sampling and Bootstrapping in Bayesian Inference](https://www.youtube.com/watch?v=f1Vcc-bPfnU) | Monte Carlo in Bayesian inference; MCMC intuition; sampling from posterior | 18 |
| 11 | S33 | [Bayesian Linear Regression and Maximum Likelihood Estimates](https://www.youtube.com/watch?v=qTRgdhgmFyc) | Bayesian linear regression; connection to MLE; posterior over weights | 19 |
| 12 | S34 | [Bayesian Linear Regression and Maximum a Posteriori (MAP) Estimate](https://www.youtube.com/watch?v=wdWHbYdhfG8) | MAP estimate in regression = L2-regularized least squares (Gaussian prior) | 15 |
| 12 | S35 | [Bayesian Linear Regression [Python Example]](https://www.youtube.com/watch?v=GiIxJ5tqGoE) | Full Bayesian linear regression Python implementation; posterior predictive | 17 |
| 13 | P1 | [Probability and Statistics: Overview](https://www.youtube.com/watch?v=sQqniayndb4) | Big-picture overview: probability theory roadmap; connections to statistics and ML | 30 |
| 13 | P2 | [Gentle Introduction to Probability: Counting Coin Flips and Dice](https://www.youtube.com/watch?v=4T3aOIfNdTY) | Sample space; equally likely outcomes; counting coin flips, dice; P(E) = |E|/|Ω| | 20 |
| 13 | P3 | [Counting Probabilities with Combinatorics and the Factorial](https://www.youtube.com/watch?v=5mDYZMwTAF8) | Factorial n!; permutations nPr; combinations nCr; counting principle | 18 |
| 14 | P4 | [Set Theory in Probability: Sample Spaces and Events](https://www.youtube.com/watch?v=b_ev4Hdzh-U) | Set theory for probability: unions ∪, intersections ∩, complements Aᶜ; Venn diagrams | 24 |
| 14 | P5 | [The Birthday Problem in Probability: P(A) = 1 - P(not A)](https://www.youtube.com/watch?v=m7hI2LulMxE) | Birthday paradox; complement rule P(A) = 1 − P(Aᶜ); inclusion-exclusion | 20 |
| 14 | P6 | [Quality Control, Non-Destructive Inspection, and the Multinomial Distribution](https://www.youtube.com/watch?v=e7RAK_iQBp0) | Quality control example; multinomial distribution; non-destructive inspection | 14 |
| 14 | P7 | [The Binomial Distribution and the Multinomial Distribution](https://www.youtube.com/watch?v=UXB9eeMZfwo) | Binomial distribution PMF; mean np; variance np(1−p); multinomial generalisation | 17 |
| 15 | P8 | [Conditional Probabilities](https://www.youtube.com/watch?v=KjdS_o5HNII) | Conditional probability P(A|B) = P(A∩B)/P(B); intuition and definition | 13 |
| 15 | P9 | [The Law of Total Probability](https://www.youtube.com/watch?v=UzEPJEQF4W0) | Law of total probability; partitioning the sample space | 10 |
| 15 | P10 | [Bayes' Theorem (with Example!)](https://www.youtube.com/watch?v=akClB1J6b28) | Bayes' theorem derivation; worked example; prior × likelihood / evidence | 18 |
| 16 | P11 | [Bayes' Theorem Example: Drug Testing 🌿](https://www.youtube.com/watch?v=gE6RnZJixUw) | Bayes' theorem: drug test example; false positive paradox; base rate neglect | 13 |
| 16 | P12 | [Independence in Probability](https://www.youtube.com/watch?v=2nDYX8IKrwo) | Independence: P(A∩B) = P(A)P(B); pairwise vs mutual independence | 13 |
| 16 | P13 | [Random Variables and Probability Distributions](https://www.youtube.com/watch?v=-7QG2itL1u4) | Random variables; PMF (discrete) vs PDF (continuous); CDF F(x); support | 22 |
| 17 | P14 | [Bernoulli and Binomial Random Variables](https://www.youtube.com/watch?v=Tc6g-Y-l0Rg) | Bernoulli(p) trial; Binomial(n,p) PMF, mean, variance; coin-flip connection | 25 |
| 17 | P15 | [The Normal Distribution: The Limit of Binomial Distribution for Large "n"](https://www.youtube.com/watch?v=8n1n0OM4gLk) | Normal distribution as n→∞ limit of Binomial; bell curve; parameters μ, σ² | 17 |
| 17 | P16 | [The Standard Unit Normal and Probability Computations](https://www.youtube.com/watch?v=X9Pkzaw0SpE) | Standard Normal Z = (X−μ)/σ; Φ(z) table; probability computations | 17 |
| 18 | P17 | [The Poisson Distribution: The Rare Event Limit of a Binomial Distribution](https://www.youtube.com/watch?v=7vXLH2H6fZw) | Poisson(λ): rare-event limit of Binomial; PMF; mean = variance = λ | 13 |
| 18 | P18 | [The Geometric Distribution: The First Success of a Bernoulli Distribution](https://www.youtube.com/watch?v=0lpOeU6JZZw) | Geometric distribution: first-success; PMF P(X=k) = (1−p)^(k−1)p; memoryless | 13 |
| 18 | P19 | [The Exponential Distribution: Time Between Poisson Events](https://www.youtube.com/watch?v=C7V3d2yB58U) | Exponential distribution: waiting time between Poisson events; PDF λe^(−λx) | 19 |
| 19 | P20 | [The Hazard Rate and Memoryless Property of the Exponential Distribution](https://www.youtube.com/watch?v=8qZilAKQM6s) | Hazard rate; memoryless property of Exponential; P(X>s+t|X>s) = P(X>t) | 7 |
| 19 | P21 | [The Connection Between the Exponential Distribution and the Poisson Process](https://www.youtube.com/watch?v=OWYGlwy0lkI) | Exponential inter-arrival times of Poisson process; connection proved | 10 |
| 19 | P22 | [The Gamma Distribution](https://www.youtube.com/watch?v=9IIcHAJlcWc) | Gamma distribution: sum of k Exponentials; Gamma function Γ(k) | 12 |
| 20 | P23 | [Functions of a Random Variable](https://www.youtube.com/watch?v=hC2idx2-GME) | Functions of a random variable; change-of-variable formula; Y = g(X) | 14 |
| 20 | P24 | [Rescaling the Normal Distribution to Mean Zero and Variance One](https://www.youtube.com/watch?v=pm4si2u-ZC4) | Rescaling Normal: Z = (X−μ)/σ derivation via change of variable | 9 |
| 20 | P25 | [The Chi Squared Distribution: The Square of the Normal Distribution](https://www.youtube.com/watch?v=h9j849vAsAA) | Chi-squared distribution: χ²(k) = sum of k squared standard Normals | 13 |
| 21 | P26 | [Joint Probability Distributions](https://www.youtube.com/watch?v=NBo5bXIX7Ac) | Joint PDF/PMF f(x,y); joint CDF; support; probability as volume under surface | 15 |
| 21 | P27 | [Joint Probability Distributions: Marginal and Conditional Densities](https://www.youtube.com/watch?v=pribJ8bUBzo) | Marginal distribution via integration/summation; conditional density f(x|y) | 10 |
| 21 | P28 | [The Expected Value (Mean) of a Probability Distribution](https://www.youtube.com/watch?v=CBgCR1kHSUI) | E[X] definition (discrete and continuous); linearity; E[aX+b] = aE[X]+b | 15 |
| 22 | P29 | [Properties of the Expected Value](https://www.youtube.com/watch?v=8rnzHE2UtoM) | Properties of expectation: linearity, E[X+Y] = E[X]+E[Y]; E[g(X)] | 10 |
| 22 | P30 | [Variance and Standard Deviation](https://www.youtube.com/watch?v=dmSRMYQsM8w) | Variance Var(X) = E[X²]−E[X]²; standard deviation; Var(aX+b) = a²Var(X) | 13 |
| 22 | P31 | [Example of Computing the Expectation and Variance of an Exponential Distribution](https://www.youtube.com/watch?v=Fz9_yqdEt-I) | Worked example: E[X] and Var(X) for Exponential distribution | 12 |
| 23 | P32 | [Two Examples of Expected Values & Functions: Temperature in C vs F, and the Kinetic Theory of Gases](https://www.youtube.com/watch?v=fB6-lCdkEdQ) | Applied E[g(X)]: temperature C↔F example; kinetic theory of gases | 15 |
| 23 | P33 | [Markov's Inequality in Probability: First Order Estimates](https://www.youtube.com/watch?v=onZSWfbTeho) | Markov's inequality: P(X≥a) ≤ E[X]/a; first-order concentration bound | 8 |
| 23 | P34 | [Chebyshev's Inequality in Probability: Second Order Estimates](https://www.youtube.com/watch?v=otCHN3s52ho) | Chebyshev's inequality: P(|X−μ|≥kσ) ≤ 1/k²; second-order bound | 10 |
| 24 | P35 | [The Law of Large Numbers](https://www.youtube.com/watch?v=0VoRWJMt6mk) | Law of Large Numbers: X̄ →^p μ as n→∞; weak vs strong LLN | 13 |
| 24 | P36 | [The Central Limit Theorem](https://www.youtube.com/watch?v=ckkrS752tjU) | Central Limit Theorem: √n(X̄−μ)/σ → N(0,1); statement and intuition | 11 |
| 24 | P37 | [The Moment Generating Function](https://www.youtube.com/watch?v=u0ku4bvp40I) | Moment Generating Function M(t) = E[e^(tX)]; generating moments M^(k)(0) = E[X^k] | 22 |
| 25 | P38 | [Example of The Moment Generating Function](https://www.youtube.com/watch?v=JjaOtHaDy9E) | MGF of Exponential worked example; using MGF to find moments | 10 |
| 25 | P39 | [The Lebesque Measure in Probability](https://www.youtube.com/watch?v=j6AD6Dm9sSs) | Lebesgue measure; Lebesgue integral vs Riemann integral; measure theory intuition | 6 |
| 25 | P40 | [Additive Property of the Moment Generating Function](https://www.youtube.com/watch?v=rn655n2JtgI) | Additive MGF property: M_{X+Y}(t) = M_X(t)·M_Y(t) for independent X,Y | 6 |
| 26 | P41 | [Covariance and Correlation in Probability](https://www.youtube.com/watch?v=QKPdk57y7Ck) | Covariance Cov(X,Y) = E[XY]−E[X]E[Y]; correlation ρ = Cov/σ_xσ_y | 20 |
| 26 | P42 | [Covariance and Correlation: Example with Gaussian Distributions](https://www.youtube.com/watch?v=upPn685IU_Q) | Covariance matrix; multivariate Gaussian example; positive semi-definite | 5 |
| 27 | P43 | [The Tail Sum Formula in Probability](https://www.youtube.com/watch?v=XQYkD_fct1A) | Tail sum formula E[X] = ∫₀^∞ P(X>t)dt; proof and applications | 9 |
| 27 | P44 | [Proof of the Central Limit Theorem](https://www.youtube.com/watch?v=nWadI0_u6QU) | Full MGF-based proof of CLT; characteristic functions; convergence in distribution | 26 |
