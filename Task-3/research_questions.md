# Task 3 — Research Questions & Hypotheses

## Dataset

The analysis will use the `tips` dataset.

The dataset contains restaurant transaction information such as:

- Total bill
- Tip
- Gender
- Smoker status
- Day
- Time
- Party size

---

## Research Question 1 — Normality

### Question

Does the `total_bill` variable follow a normal distribution?

### Null Hypothesis (H₀)

The `total_bill` data are consistent with a normal distribution.

### Alternative Hypothesis (H₁)

The `total_bill` data are not consistent with a normal distribution.

### Tests

- Shapiro-Wilk test
- Kolmogorov-Smirnov test

---

## Research Question 2 — Two-Group Comparison

### Question

Is there a statistically significant difference in `total_bill` between smokers and non-smokers?

### Null Hypothesis (H₀)

There is no statistically significant difference in `total_bill` between smokers and non-smokers.

### Alternative Hypothesis (H₁)

There is a statistically significant difference in `total_bill` between smokers and non-smokers.

### Tests

- Independent two-sample t-test
- Mann-Whitney U test

---

## Research Question 3 — One-Way ANOVA

### Question

Does the average `total_bill` differ across different days of the week?

### Null Hypothesis (H₀)

The mean `total_bill` is equal across all day groups.

### Alternative Hypothesis (H₁)

At least one day group has a different mean `total_bill`.

### Test

One-Way ANOVA

### Post-Hoc Test

Tukey HSD

---

## Research Question 4 — Two-Way ANOVA

### Question

Do gender and meal time have an effect on `tip` amount?

### Null Hypothesis (H₀)

Gender, meal time, and their interaction have no statistically significant effect on `tip`.

### Alternative Hypothesis (H₁)

At least one factor or their interaction has a statistically significant effect on `tip`.

### Test

Two-Way ANOVA

---

## Significance Level

The significance level for all hypothesis tests will be:

α = 0.05

---

## Confidence Interval

Where applicable, results will be reported with a 95% confidence interval.

---

## Interpretation

A p-value below 0.05 will be considered statistically significant.

A p-value greater than or equal to 0.05 will not provide sufficient evidence to reject the null hypothesis.