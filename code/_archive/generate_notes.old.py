import os

base = r"C:\Users\aakas\OneDrive\Desktop\memory\claude_memory\wiki\notes"

days = [
    # (date_str, day_num, day_of_week, phase, topic, videos, playlist, vid_topics, next_file)
    ("2026-05-10", "ps-1",  "Saturday",  "Prob/Stats Week 1", "Intro to Statistics: Data Types & Visualizations",
     [("Stats #1", "Intro to statistics, course overview, why statistics matters"),
      ("Stats #2", "Types of data — nominal, ordinal, interval, ratio"),
      ("Stats #3", "Data visualization — histograms, bar charts, scatter plots")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-11-ps-2"),

    ("2026-05-11", "ps-2",  "Sunday",    "Prob/Stats Week 1", "Descriptive Statistics — Mean, Median, Mode, Variance",
     [("Stats #4", "Measures of central tendency — mean, median, mode"),
      ("Stats #5", "Measures of spread — range, variance, standard deviation"),
      ("Stats #6", "IQR, box plots, outliers")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-12-ps-3"),

    ("2026-05-12", "ps-3",  "Monday",    "Prob/Stats Week 1", "Standard Deviation, Z-Scores, Distributions",
     [("Stats #7", "Standard deviation deep dive, population vs sample"),
      ("Stats #8", "Z-scores, standardization, standard normal"),
      ("Stats #9", "Intro to probability distributions")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-13-ps-4"),

    ("2026-05-13", "ps-4",  "Tuesday",   "Prob/Stats Week 1", "Normal Distribution, Empirical Rule, CLT",
     [("Stats #10", "Normal distribution — shape, properties, bell curve"),
      ("Stats #11", "Empirical rule (68-95-99.7), normal probabilities"),
      ("Stats #12", "Central Limit Theorem — statement and intuition")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-14-ps-5"),

    ("2026-05-14", "ps-5",  "Wednesday", "Prob/Stats Week 1", "Sampling, Confidence Intervals",
     [("Stats #13", "Sampling methods — random, stratified, cluster"),
      ("Stats #14", "Sampling distributions, standard error"),
      ("Stats #15", "Confidence intervals — construction and interpretation")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-15-ps-6"),

    ("2026-05-15", "ps-6",  "Thursday",  "Prob/Stats Week 1", "Hypothesis Testing, p-values, t-tests",
     [("Stats #16", "Hypothesis testing framework — null vs alternative"),
      ("Stats #17", "p-values — definition, interpretation, common misuse"),
      ("Stats #18", "t-tests — one sample, two sample, paired")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-16-ps-7"),

    ("2026-05-16", "ps-7",  "Friday",    "Prob/Stats Week 1", "Type I/II Errors, ANOVA, Week Review",
     [("Stats #19", "Type I and Type II errors, significance level, power"),
      ("Stats #20", "Chi-square test, goodness of fit"),
      ("Stats #21", "ANOVA intro — comparing multiple groups")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-17-ps-8"),

    ("2026-05-17", "ps-8",  "Saturday",  "Prob/Stats Week 2", "Regression Intro, Correlation vs Causation",
     [("Stats #22", "Correlation — Pearson r, scatter plots, direction/strength"),
      ("Stats #23", "Correlation vs causation — examples and pitfalls"),
      ("Stats #24", "Simple linear regression — line of best fit")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-18-ps-9"),

    ("2026-05-18", "ps-9",  "Sunday",    "Prob/Stats Week 2", "Linear Regression, Residuals, R²",
     [("Stats #25", "Least squares method — derivation and intuition"),
      ("Stats #26", "Residuals, residual plots, checking assumptions"),
      ("Stats #27", "R² — coefficient of determination, model fit")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-19-ps-10"),

    ("2026-05-19", "ps-10", "Monday",    "Prob/Stats Week 2", "Multiple Regression, Model Evaluation",
     [("Stats #28", "Multiple linear regression — adding predictors"),
      ("Stats #29", "Model evaluation — adjusted R², AIC, overfitting"),
      ("Stats #30", "Multicollinearity, feature selection basics")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-20-ps-11"),

    ("2026-05-20", "ps-11", "Tuesday",   "Prob/Stats Week 2", "Data Analysis, Outliers, Non-parametric Tests",
     [("Stats #31", "Identifying and handling outliers"),
      ("Stats #32", "Non-parametric tests — Mann-Whitney, Wilcoxon"),
      ("Stats #33", "Spearman correlation, rank-based methods")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-21-ps-12"),

    ("2026-05-21", "ps-12", "Wednesday", "Prob/Stats Week 2", "Stats Wrap-up + Review",
     [("Stats #34", "Data analysis workflow end to end"),
      ("Stats #35", "Course review — key concepts, common mistakes")],
     "Introduction to Statistics and Data Analysis",
     "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx",
     "may-22-ps-13"),

    ("2026-05-22", "ps-13", "Thursday",  "Prob/Stats Week 2", "Probability: Sample Spaces, Events, Set Notation",
     [("Prob #1", "Intro to probability — sample spaces, outcomes, events"),
      ("Prob #2", "Set notation — union, intersection, complement"),
      ("Prob #3", "Venn diagrams, De Morgan's laws")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-23-ps-14"),

    ("2026-05-23", "ps-14", "Friday",    "Prob/Stats Week 2", "Axioms of Probability, Counting, Permutations/Combinations",
     [("Prob #4", "Axioms of probability — Kolmogorov axioms"),
      ("Prob #5", "Counting — multiplication rule, addition rule"),
      ("Prob #6", "Permutations — ordered arrangements"),
      ("Prob #7", "Combinations — unordered selections, binomial coefficient")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-24-ps-15"),

    ("2026-05-24", "ps-15", "Saturday",  "Prob/Stats Week 3", "Conditional Probability, Multiplication Rule",
     [("Prob #8",  "Conditional probability — P(A|B) definition and intuition"),
      ("Prob #9",  "Multiplication rule — P(A∩B) = P(A)·P(B|A)"),
      ("Prob #10", "Tree diagrams for multi-step experiments")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-25-ps-16"),

    ("2026-05-25", "ps-16", "Sunday",    "Prob/Stats Week 3", "Bayes' Theorem",
     [("Prob #11", "Bayes' theorem — derivation from conditional probability"),
      ("Prob #12", "Bayes' theorem — examples (medical tests, spam filter)"),
      ("Prob #13", "Prior, likelihood, posterior — Bayesian reasoning")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-26-ps-17"),

    ("2026-05-26", "ps-17", "Monday",    "Prob/Stats Week 3", "Independence, Law of Total Probability",
     [("Prob #14", "Independence — P(A∩B) = P(A)·P(B), checking independence"),
      ("Prob #15", "Law of total probability — partitioning sample space"),
      ("Prob #16", "Combining Bayes + total probability — full examples")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-27-ps-18"),

    ("2026-05-27", "ps-18", "Tuesday",   "Prob/Stats Week 3", "Random Variables, PMF, PDF",
     [("Prob #17", "Random variables — discrete vs continuous"),
      ("Prob #18", "PMF — probability mass function for discrete RVs"),
      ("Prob #19", "PDF — probability density function for continuous RVs")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-28-ps-19"),

    ("2026-05-28", "ps-19", "Wednesday", "Prob/Stats Week 3", "Expectation, Variance, Moments",
     [("Prob #20", "Expected value E[X] — definition, linearity of expectation"),
      ("Prob #21", "Variance Var(X) = E[X²] - (E[X])² — derivation"),
      ("Prob #22", "Moments, moment generating functions, skewness")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-29-ps-20"),

    ("2026-05-29", "ps-20", "Thursday",  "Prob/Stats Week 3", "Binomial, Poisson, Geometric Distributions",
     [("Prob #23", "Binomial distribution — n trials, p success, PMF, E, Var"),
      ("Prob #24", "Poisson distribution — rare events, λ parameter, E=Var=λ"),
      ("Prob #25", "Geometric distribution — trials until first success")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-30-ps-21"),

    ("2026-05-30", "ps-21", "Friday",    "Prob/Stats Week 3", "Uniform, Normal, Exponential Distributions",
     [("Prob #26", "Uniform distribution — discrete and continuous"),
      ("Prob #27", "Normal distribution — PDF, CDF, standardizing"),
      ("Prob #28", "Exponential distribution — memoryless property, relation to Poisson")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "may-31-ps-22"),

    ("2026-05-31", "ps-22", "Saturday",  "Prob/Stats Week 4", "Joint Distributions, Marginal, Conditional",
     [("Prob #29", "Joint distributions — joint PMF/PDF for two RVs"),
      ("Prob #30", "Marginal distributions — summing/integrating out a variable"),
      ("Prob #31", "Conditional distributions from joint — P(X|Y)")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "jun-01-ps-23"),

    ("2026-06-01", "ps-23", "Sunday",    "Prob/Stats Week 4", "Covariance, Correlation, Independence of RVs",
     [("Prob #32", "Covariance — Cov(X,Y) definition, formula, sign interpretation"),
      ("Prob #33", "Correlation coefficient ρ from covariance"),
      ("Prob #34", "Independence of RVs vs uncorrelated — important distinction")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "jun-02-ps-24"),

    ("2026-06-02", "ps-24", "Monday",    "Prob/Stats Week 4", "Law of Large Numbers, CLT Revisited",
     [("Prob #35", "Law of Large Numbers — weak and strong LLN"),
      ("Prob #36", "Central Limit Theorem — formal statement, why it works"),
      ("Prob #37", "CLT applications — approximating distributions, sampling")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "jun-03-ps-25"),

    ("2026-06-03", "ps-25", "Tuesday",   "Prob/Stats Week 4", "MLE — Maximum Likelihood Estimation",
     [("Prob #38", "MLE — likelihood function, log-likelihood"),
      ("Prob #39", "MLE for common distributions — Gaussian, Bernoulli"),
      ("Prob #40", "MLE vs MAP — adding a prior (Bayesian connection)")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "jun-04-ps-26"),

    ("2026-06-04", "ps-26", "Wednesday", "Prob/Stats Week 4", "Bayesian Inference, Prior/Posterior",
     [("Prob #41", "Bayesian inference — updating beliefs with data"),
      ("Prob #42", "Conjugate priors — Beta-Binomial, Gaussian-Gaussian")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "jun-05-ps-27"),

    ("2026-06-05", "ps-27", "Thursday",  "Prob/Stats Week 4", "Probability Bootcamp Wrap-up",
     [("Prob #43", "Wrap-up — connecting all probability concepts"),
      ("Prob #44", "Final summary — key formulas, distributions, theorems")],
     "Probability Bootcamp",
     "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V",
     "jun-06-ps-28"),

    ("2026-06-06", "ps-28", "Friday",    "Prob/Stats Week 4", "Full Review — Re-watch + Key Formulas",
     [],  # review day, no new videos
     "",
     "",
     "jun-07-ps-29"),

    ("2026-06-07", "ps-29", "Saturday",  "Prob/Stats Week 4", "Consolidation — Formula Sheet",
     [],  # consolidation day
     "",
     "",
     ""),
]

playlist1_link = "https://www.youtube.com/watch?v=QIXUTsdj_oA&list=PLMrJAkhIeNNT14qn1c5qdL29A1UaHamjx"
playlist2_link = "https://www.youtube.com/watch?v=sQqniayndb4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V"

for (date, slug, dow, phase, topic, videos, playlist, playlist_link, next_slug) in days:
    day_num = slug.replace("ps-", "")
    filename = f"{date[:7].replace('-','')}-{date[8:10]}-{slug}.md"
    # e.g. 202605-10-ps-1.md → better: may-10-ps-1.md
    month_map = {"05": "may", "06": "jun"}
    month_str = month_map.get(date[5:7], date[5:7])
    day_str = date[8:10]
    filename = f"{month_str}-{day_str}-{slug}.md"
    filepath = os.path.join(base, filename)

    lines = []
    lines.append("---")
    lines.append(f"type: note")
    lines.append(f"date: {date}")
    lines.append(f"day: ps-{day_num}")
    lines.append(f"phase: {phase}")
    lines.append(f"topic: {topic}")
    lines.append(f"tags: [probability, statistics, math, ml, coding]")
    lines.append("---")
    lines.append("")
    lines.append(f"# Prob/Stats Day {day_num} — {topic}")
    lines.append(f"**Date:** {dow}, {date}")
    lines.append(f"**Phase:** {phase}")
    if playlist:
        lines.append(f"**Playlist:** {playlist}")
        lines.append(f"**Playlist link:** {playlist_link}")
    lines.append("")
    lines.append("---")
    lines.append("")

    if videos:
        lines.append("## Videos")
        lines.append("")
        for (vid_label, concepts) in videos:
            lines.append(f"### {vid_label}")
            lines.append(f"**Concepts covered:** {concepts}")
            lines.append("**Notes:**")
            lines.append("```")
            lines.append("")
            lines.append("```")
            lines.append("**Key formulas / definitions:**")
            lines.append("```")
            lines.append("")
            lines.append("```")
            lines.append("**What was surprising or hard:**")
            lines.append("-")
            lines.append("")
    else:
        lines.append("## Review / Consolidation Day")
        lines.append("")
        if "Review" in topic:
            lines.append("**Task:** Re-watch the 3–5 videos you found hardest. Write a 1-page summary of all key formulas.")
            lines.append("")
            lines.append("### Videos to Re-watch")
            lines.append("- ")
            lines.append("- ")
            lines.append("- ")
            lines.append("")
            lines.append("### Key Formula Sheet (fill in from memory first, then check)")
            lines.append("| Concept | Formula |")
            lines.append("|---------|---------|")
            lines.append("| E[X] discrete | |")
            lines.append("| Var(X) | |")
            lines.append("| Bayes' theorem | |")
            lines.append("| Binomial PMF | |")
            lines.append("| Normal PDF | |")
            lines.append("| MLE objective | |")
        else:
            lines.append("**Task:** Write a 1-page summary of all key probability + stats formulas from memory.")
            lines.append("")
            lines.append("### My Formula Sheet")
            lines.append("*(write entirely from memory — no notes)*")
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
    lines.append("## What Was Hard")
    lines.append("-")
    lines.append("")
    lines.append("## What to Revisit")
    lines.append("-")
    lines.append("")
    lines.append("---")
    lines.append("")
    if next_slug:
        lines.append(f"_Next: [[{month_str}-{day_str}-{next_slug}]]_")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Created: {filename}")

print(f"\nDone! Created {len(days)} notes files.")
