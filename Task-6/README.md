# Task 6 — Data Science Research Capstone & Whitepaper

## Research Title

**Daily Demand Forecasting Using Statistical and Machine Learning Models**

## Research Question

How effectively can statistical time-series and machine learning models predict future daily demand, and which approach provides the most reliable predictive performance?

## Objective

The objective of this research is to develop, evaluate, and compare statistical and machine learning approaches for daily demand forecasting and identify a reliable predictive model.

## Dataset

The project uses a historical daily demand dataset containing:

- Date
- Demand
- Marketing Event
- Holiday

The dataset contains 30 daily observations.

## Methodology

The complete research workflow includes:

1. Data quality assessment
2. Exploratory Data Analysis
3. Time-series decomposition
4. Stationarity testing
5. Feature engineering
6. Naive baseline forecasting
7. ARIMA modeling
8. SARIMA modeling
9. Random Forest modeling
10. Gradient Boosting modeling
11. Model evaluation
12. Model comparison
13. Future demand forecasting
14. Business interpretation
15. Research report and whitepaper preparation

## Evaluation Metrics

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

RMSE was used as the primary model-selection criterion.

## Final Model

The best-performing model on the held-out test data was:

**SARIMA**

Performance:

- **MAE:** 0.8887
- **RMSE:** 0.9622
- **MAPE:** 0.58%

## Future Forecast

The selected model was refitted using the complete historical demand series and used to generate a **30-day future demand forecast**.

## Repository Structure

```text
Task-6/
├── Day-01/
│   └── README.md
├── Day-02/
│   └── README.md
├── Day-03/
│   └── README.md
├── Day-04/
│   └── README.md
├── data/
│   └── daily-demand-series.csv
├── notebooks/
│   └── Task_6_Research_Capstone.ipynb
├── plots/
├── results/
├── report/
│   ├── Research_Report.md
│   ├── Daily_Demand_Forecasting_Research_Whitepaper.pdf
│   └── generate_whitepaper.py
├── README.md
└── requirements.txt