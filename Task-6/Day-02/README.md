# Task 6 — Day 2

## Statistical Analysis and Time-Series Investigation

### Work Completed

Day 2 focused on deeper statistical analysis of the daily demand dataset and investigation of its time-series characteristics.

## Time-Series Decomposition

Performed additive time-series decomposition using a 7-day seasonal period.

The decomposition examined:

- Observed demand
- Trend
- Weekly seasonality
- Residual component

## Stationarity Testing

Performed the Augmented Dickey-Fuller (ADF) test on the original demand series.

### Hypotheses

- H0: The time series is non-stationary.
- H1: The time series is stationary.

First-order differencing was then applied and the ADF test was repeated.

This helped determine whether differencing was required for statistical forecasting models.

## Weekly Seasonality Analysis

Analyzed average demand by day of the week to investigate potential weekly demand patterns.

A visualization was created to compare average demand across the seven days.

## Correlation Analysis

Created a correlation matrix to examine relationships between demand and numerical predictive features, including:

- Day of week
- Day of month
- Month
- Week of year
- Previous-day demand
- Previous-week demand
- Rolling mean
- Rolling standard deviation

## Statistical Findings

Generated a statistical findings summary containing:

- Stationarity conclusions
- Highest average demand day
- Lowest average demand day
- Strongest numerical relationship with demand

## Results Generated

The following files were saved:

- `task6_adf_stationarity_results.csv`
- `task6_weekly_seasonality.csv`
- `task6_correlation_matrix.csv`

## Status

**Day 2 completed successfully.**