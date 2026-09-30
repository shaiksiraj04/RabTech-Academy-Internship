# Task 4 — Dimensionality Reduction & Unsupervised Clustering

## Overview

This task applies dimensionality reduction and unsupervised clustering techniques to identify patterns in high-dimensional numerical data.

## Dataset

Scikit-learn Wine Dataset

- 178 observations
- 13 numerical features
- No missing values

## Techniques Applied

### Dimensionality Reduction
- Feature Standardization
- Principal Component Analysis (PCA)
- Explained Variance Ratio
- PCA Scree Plot

### Clustering
- K-Means Clustering
- Elbow Method
- Silhouette Score
- DBSCAN
- Hierarchical Clustering

### Visualization
- PCA 2D cluster visualization
- PCA 3D cluster visualization
- Elbow plot
- Silhouette score plot
- DBSCAN visualization
- Hierarchical clustering visualization

## Results

PCA was used to reduce the dimensionality of the standardized dataset while retaining at least 95% of the variance.

K-Means cluster selection was evaluated using both the Elbow Method and Silhouette Score.

DBSCAN was used to identify density-based clusters and potential noise points.

Hierarchical clustering was performed using Agglomerative Clustering with Ward linkage.

## Project Structure

```text
Task-4/
├── Day-01/
├── notebooks/
│   └── Task_4_PCA_Clustering.ipynb
├── plots/
├── results/
├── README.md
└── requirements.txt