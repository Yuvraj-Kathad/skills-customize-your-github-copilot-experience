# 📘 Assignment: Intro to Supervised ML — Binary Classification with scikit-learn

## 🎯 Objective

Build a complete supervised learning pipeline for a binary classification problem using Python and scikit-learn: load and clean data, engineer features, train models, evaluate performance, and export the trained model.

## Prerequisites

- Python 3.8+
- pandas, scikit-learn, matplotlib, joblib
- Basic familiarity with Python and the `pandas` library

## Estimated time

2–4 hours (Intermediate)

## 📝 Tasks

### 🛠️ Task 1 — Data loading & cleaning

#### Description
Load `data.csv`, inspect for missing values and basic statistics, and perform simple cleaning (fill or drop missing values). Split features and labels.

#### Requirements

- Load dataset from `data.csv`.
- Print dataset shape and class balance.
- Handle missing values with a clear strategy.

### 🛠️ Task 2 — Feature engineering & split

#### Description
Create or transform features as needed (scaling, encoding if necessary), then split into training and test sets using a reproducible random seed.

#### Requirements

- Use a train/test split (e.g., 80/20) with `random_state=42`.
- Scale numeric features when appropriate.

### 🛠️ Task 3 — Train and evaluate models

#### Description
Train at least two classifiers (a Logistic Regression and a Random Forest). Evaluate using accuracy, precision, recall, F1-score, and ROC AUC. Plot or print a confusion matrix and ROC curve.

#### Requirements

- Train `LogisticRegression` and `RandomForestClassifier` from scikit-learn.
- Report accuracy, precision, recall, F1, and ROC AUC on the test set.
- Save a simple comparison summary (console output or CSV).

### 🛠️ Task 4 — Export the best model

#### Description
Save the best-performing model to disk using `joblib` or `pickle`. Include a short script or function to load and run the model on new samples.

#### Requirements

- Save model to `model.joblib`.
- Provide a `predict()` function or script demonstrating loading the model and predicting a sample row.

### 🛠️ Optional Extension — Model serving

Integrate the exported model with the existing FastAPI assignment by creating a simple `/predict` endpoint that accepts JSON and returns predictions.

## Files in this assignment

- `starter-code.py` — starter code and helper functions
- `data.csv` — small sample dataset

## How to submit

Create a ZIP of your working folder or push a branch with your completed notebook/scripts and the exported `model.joblib`.
