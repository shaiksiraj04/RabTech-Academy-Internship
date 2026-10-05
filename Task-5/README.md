# Task 5 — Time-Series Forecasting

## Objective

Perform time-series analysis and forecasting on daily demand data using statistical forecasting techniques.

## Dataset

**File:** `daily-demand-series.csv`

The dataset contains:

- `date` — Daily observation date
- `demand` — Daily demand value
- `marketing_event` — Marketing event indicator
- `holiday` — Holiday indicator

## Analysis Performed

### 1. Data Exploration
- Loaded and inspected the dataset
- Converted the date column to datetime format
- Checked chronological ordering
- Examined descriptive statistics
- Checked for missing values

### 2. Time-Series Decomposition
Performed additive decomposition using a **7-day seasonal period** to analyze:

- Observed series
- Trend
- Seasonality
- Residuals

### 3. Stationarity Testing
Applied the **Augmented Dickey-Fuller (ADF) test** to:

- Original demand series
- First-order differenced demand series

### 4. ARIMA Forecasting
Evaluated multiple ARIMA configurations:

- ARIMA(0,1,0)
- ARIMA(0,1,1)
- ARIMA(1,1,0)
- ARIMA(1,1,1)
- ARIMA(2,1,0)
- ARIMA(2,1,1)

The best model was selected using validation **RMSE**.

### 5. SARIMA Forecasting
A SARIMA model with weekly seasonality was evaluated:

```text
Order: (1,1,0)
Seasonal Order: (1,0,0,7)