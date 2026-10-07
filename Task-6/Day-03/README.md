# Task 6 — Day 3: Predictive Modeling & Model Evaluation

## Objective

The objective of Day 3 was to develop, evaluate, and compare statistical time-series and machine learning models for daily demand forecasting.

## Work Completed

### 1. ARIMA Model Selection
Tested multiple ARIMA configurations:

- ARIMA(0,1,0)
- ARIMA(0,1,1)
- ARIMA(1,1,0)
- ARIMA(1,1,1)
- ARIMA(2,1,0)
- ARIMA(2,1,1)

Models were compared using:

- MAE
- RMSE
- MAPE

The model with the lowest test-set RMSE was selected.

### 2. Selected ARIMA Validation

The selected ARIMA configuration was independently evaluated on the held-out test data.

### 3. SARIMA Modeling

A seasonal SARIMA model was developed using weekly seasonality:

- ARIMA order: (1,1,0)
- Seasonal order: (1,0,0,7)

### 4. Statistical Model Comparison

ARIMA and SARIMA were compared using MAE, RMSE, and MAPE.

### 5. Complete Model Comparison

The following approaches were compared:

- Naive Baseline
- ARIMA
- SARIMA
- Random Forest
- Gradient Boosting

The primary selection criterion was the lowest test-set RMSE.

### 6. Visualization

Created visualizations for:

- Overall model RMSE comparison
- Actual vs predicted demand
- Final model forecast

### 7. Final Model Selection

The best-performing model was selected based on the lowest test-set RMSE.

The selected model's:

- MAE
- RMSE
- MAPE

were recorded for the final research report.

### 8. Reproducible Results

Saved:

- ARIMA hyperparameter comparison
- Statistical model comparison
- Complete model comparison
- Final model predictions
- Day 3 modeling findings
- Final model forecast visualization

## Key Outputs

### Results

```text
results/
├── task6_arima_hyperparameter_comparison.csv
├── task6_statistical_model_comparison.csv
├── task6_complete_model_comparison.csv
├── task6_final_model_predictions.csv
└── task6_day03_modeling_findings.txt