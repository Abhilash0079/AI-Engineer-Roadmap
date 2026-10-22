# Day 12 — Supervised Learning Fundamentals

## Objective
Learn the fundamentals of supervised machine learning by building one regression model and one classification model using scikit-learn.

## Concepts Covered
- Features (`X`) and labels (`y`)
- Training a model using `model.fit(X, y)`
- Generating predictions using `model.predict()`
- Regression versus classification

## 1. Regression Model
**File:** `regression_model.py`

Uses `LinearRegression` to predict an exam score from the number of hours studied.

- Feature: hours studied
- Label: exam score
- Example prediction: 6 hours of study → 90.0 predicted score

The dataset is artificial and intended only for learning.

## 2. Classification Model
**File:** `classification_model.py`

Uses `LogisticRegression` to classify an email as spam or not spam based on the number of suspicious words.

- Feature: number of suspicious words
- Label: `0` = not spam, `1` = spam
- Example prediction: 4 suspicious words → `1` (spam)

The dataset is artificial and does not represent a production spam detector.

## How to Run

Run these commands from the project root with the virtual environment activated:

```powershell
python .\02_APIs_SQL_ML_Foundations\day12\regression_model.py
python .\