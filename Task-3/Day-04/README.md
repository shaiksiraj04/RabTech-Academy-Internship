# Task 3 — Day 04

## ANOVA & Post-Hoc Analysis

### Objective

The objective of Day 4 was to investigate group differences using One-Way ANOVA, Two-Way ANOVA, and Tukey HSD post-hoc analysis.

## One-Way ANOVA

### Research Question

Does the mean `total_bill` differ significantly across different days of the week?

### Hypotheses

**H₀:** The mean `total_bill` is equal across all days.

**H₁:** At least one day's mean `total_bill` is different.

The One-Way ANOVA was performed using:

- Thursday
- Friday
- Saturday
- Sunday

## Tukey HSD

Tukey's Honestly Significant Difference (HSD) test was performed as a post-hoc analysis to identify which pairs of days differed when interpreting the One-Way ANOVA results.

## Two-Way ANOVA

A Two-Way ANOVA was performed to examine the effects of:

- `sex`
- `time`
- `sex × time` interaction

on the `tip` variable.

### Hypotheses

**Sex effect**

H₀: Sex has no significant effect on `tip`.

**Time effect**

H₀: Meal time has no significant effect on `tip`.

**Interaction effect**

H₀: There is no significant interaction between sex and meal time.

The significance level was:

```text
α = 0.05