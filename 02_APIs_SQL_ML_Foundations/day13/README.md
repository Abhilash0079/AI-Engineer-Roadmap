# Day 13 — Train/Test Split, Baselines, and Data Leakage

## Objective
Learn how to evaluate a regression model on unseen data, compare it with a baseline, and recognize data leakage.

## Concepts Covered
- Splitting data into training and testing sets
- Using `train_test_split` with a fixed `random_state`
- Training Linear Regression and a `DummyRegressor` baseline
- Evaluating predictions with Mean Absolute Error (MAE)
- Demonstrating how test-label information can leak into a baseline calculation

## Implementation
**File:** `train_test_baseline.py`

The script:
1. Creates a small sample dataset of study hours and exam scores.
2. Splits the data into training and test sets using an 80/20 split.
3. Trains Linear Regression and a mean baseline using training data only.
4. Evaluates both models on the same test examples.
5. Demonstrates a flawed baseline calculation that includes test labels.

## Results
- Training examples: 8
- Testing examples: 2
- Linear Regression MAE: 1.88
- Mean baseline MAE: 22.50
- Correct training-set mean: 64.375
- Leaky full-dataset mean: 64.0

The sample is artificial and very small, so these results demonstrate the workflow rather than establish real-world model performance.

## Important Lesson
Split data before learning data-dependent preprocessing values. Fit models and preprocessing steps using training data only. Keep test data separate for final evaluation.

## How to Run
From the Day 13 directory:

```powershell
python .\train_test_baseline.py
```
