# Preregistration — Reproducible Research Question & Analysis

## 1. Research Objective

The objective of this study is to investigate whether participation in structured programming practice is associated with programming assessment performance among college students over a predefined observation period.

The analysis plan will be established before inspecting outcome patterns in the real dataset.

---

## 2. Population

The study population will consist of college students included in the research dataset who meet the predefined eligibility criteria.

---

## 3. Exposure

The primary exposure will be the frequency of participation in structured programming practice during the observation period.

The exposure will initially be treated as a continuous variable representing the number of completed programming-practice sessions.

---

## 4. Comparator

The primary comparison will be between participants with different levels of programming-practice frequency.

Where appropriate, participants may also be categorized into predefined practice-frequency groups for sensitivity analysis.

---

## 5. Primary Outcome

The primary outcome will be programming assessment performance, measured using the final programming assessment score available in the dataset.

---

## 6. Observation Window

The primary observation window will be 12 weeks.

Only observations meeting the predefined observation-window requirements will be included in the primary analysis.

---

## 7. Research Question

Among college students, is higher participation in structured programming practice associated with better programming assessment performance over a 12-week observation period?

---

## 8. Hypotheses

### Null Hypothesis (H0)

There is no statistically significant association between programming-practice frequency and programming assessment performance over the 12-week observation period.

### Alternative Hypothesis (H1)

Higher programming-practice frequency is associated with better programming assessment performance over the 12-week observation period.

---

## 9. Inclusion Criteria

Participants will be included if they:

1. Belong to the defined study population.
2. Have a valid participant identifier.
3. Have valid information for the primary exposure.
4. Have a valid measurement of the primary outcome.
5. Fall within the predefined 12-week observation window.

---

## 10. Exclusion Criteria

Participants will be excluded if they:

1. Have duplicate participant records.
2. Have an invalid or missing participant identifier.
3. Are missing the primary exposure.
4. Are missing the primary outcome.
5. Fall outside the predefined observation window.
6. Fail predefined data-quality checks.

Participants will not be excluded solely because their outcome value is unusually high or low.

---

## 11. Data Transformations

The following transformations will be applied before the primary analysis:

* Programming-practice frequency will be represented as the number of completed practice sessions.
* Assessment scores will be represented using the recorded final assessment score.
* Numeric variables will be checked for invalid values.
* Duplicate records will be identified using the participant identifier.
* No outcome-based transformation will be introduced after inspecting the results.

Any additional transformation discovered during analysis will be documented as exploratory rather than treated as part of the preregistered primary analysis.

---

## 12. Missing Data

The amount and percentage of missing data will be reported.

Participants missing the primary exposure or primary outcome will be excluded from the primary analysis.

No outcome-based imputation will be performed for the primary analysis.

---

## 13. Primary Statistical Analysis

The primary analysis will use a regression-based approach to estimate the association between programming-practice frequency and programming assessment performance.

The general model will be:

Assessment Score ~ Practice Frequency

If predefined participant characteristics are available and meet the requirements specified in the final analysis plan, additional covariates may be included in a prespecified adjusted analysis.

---

## 14. Statistical Significance

The significance threshold will be:

α = 0.05

All statistical tests will use a 5% significance level unless otherwise specified in a documented sensitivity analysis.

---

## 15. Confidence Interval

Effect estimates will be reported with 95% confidence intervals.

---

## 16. Effect Size

The primary effect size will be the estimated regression coefficient for programming-practice frequency.

The coefficient will represent the expected change in assessment score associated with a one-unit increase in programming-practice frequency.

The effect estimate will be reported together with its 95% confidence interval and p-value.

---

## 17. Robustness Checks

The following robustness checks will be performed:

### Robustness Check 1

Repeat the primary analysis after examining the influence of extreme exposure values using a predefined method.

### Robustness Check 2

Analyze programming-practice frequency using predefined categorical groups rather than only as a continuous variable.

### Robustness Check 3

Compare the primary regression results with an appropriate non-parametric association analysis if the assumptions required for the primary analysis are not adequately satisfied.

### Robustness Check 4

Compare the unadjusted analysis with the predefined adjusted analysis when appropriate covariate information is available.

---

## 18. Sensitivity Analysis

Sensitivity analyses will evaluate whether reasonable changes to predefined analytical assumptions materially change the estimated association.

Any analysis that was not specified in this preregistration will be clearly labeled as exploratory.

---

## 19. Multiple Testing

The primary hypothesis will remain the main confirmatory hypothesis.

Secondary and exploratory analyses will not be presented as additional confirmatory findings unless separately justified and documented.

---

## 20. Data-Blind Analysis Principle

The primary research question, hypotheses, inclusion criteria, exclusion criteria, transformations, statistical approach, effect-size definition, and robustness checks will be established before inspecting outcome patterns in the real dataset.

The real outcome data will not be used to select the primary hypothesis or statistical method.

---

## 21. Synthetic Data Validation

Before analyzing the real dataset, the complete analysis pipeline will be tested using synthetic data.

The synthetic pipeline will verify:

* Data validation
* Data preprocessing
* Statistical analysis
* Effect-size calculation
* Confidence-interval generation
* Output structure
* Error handling

---

## 22. Exploratory Analysis

After the preregistered primary analysis is completed, additional exploratory analyses may be conducted.

Exploratory findings will be clearly separated from preregistered confirmatory findings.

---

## 23. Analysis Lock

This document represents the predefined analysis plan for the primary research question.

The primary analysis will not be modified based on observed outcome patterns.

If changes become necessary because of an unforeseen data or methodological issue, the change will be documented, justified, and identified as a deviation from the original preregistration.

---

## 24. Reproducibility

All analysis code will be maintained in the project repository.

The project will use a reproducible software environment with pinned dependency versions.

Synthetic test data will be included for pipeline validation.

---

## 25. Status

**Preregistration Status: Draft — Day 2**

The preregistration will be reviewed and finalized before the real outcome data are analyzed.
