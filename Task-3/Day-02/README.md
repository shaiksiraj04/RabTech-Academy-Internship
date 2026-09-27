# Task 3 — Day 02

## Normality Testing

### Objective

The objective of Day 2 was to load and inspect the dataset and perform normality analysis on the `total_bill` variable.

## Work Completed

- Loaded the Seaborn `tips` dataset.
- Inspected the dataset structure.
- Checked column names and data types.
- Checked for missing values.
- Generated descriptive statistics.
- Selected `total_bill` for normality analysis.
- Created a histogram with KDE.
- Performed the Shapiro-Wilk normality test.
- Performed the Kolmogorov-Smirnov normality test.
- Added statistical decision logic.

## Statistical Tests

### Shapiro-Wilk Test

The Shapiro-Wilk test was used to evaluate whether the `total_bill` data are consistent with a normal distribution.

Result:

```text
Statistic: 0.9197
p-value: 0.000000
Decision: Reject H₀