# Day 16 — Classification Metrics

## Overview

This project demonstrates how to evaluate a classification model using scikit-learn. It covers the confusion matrix, accuracy, precision, recall, and F1-score.

## Learning Objectives

- Understand TP, TN, FP, and FN.
- Calculate and interpret classification metrics.
- Train a logistic regression classifier.
- Evaluate predictions on a held-out test set.
- Recognize the limitations of small test datasets.

## Project Files

| File | Description |
|---|---|
| `classification_metrics.py` | Calculates metrics from predefined predictions. |
| `train_classifier.py` | Trains and evaluates a logistic regression classifier. |
| `interview_notes.md` | Theory, formulas, checkpoint answers, and interview questions. |
| `README.md` | Project overview and execution instructions. |

## Requirements

- Python
- scikit-learn

The project uses the existing virtual environment and installed dependencies from the AI Engineer roadmap.

## How to Run

From the `day16` folder, activate the project's virtual environment if it is not already active.

Run the predefined-prediction evaluation:

```powershell
python .\classification_metrics.py
```

Run the trained classifier evaluation:

```powershell
python .\train_classifier.py
```

## Concepts Covered

- Confusion matrix
- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)
- Accuracy
- Precision
- Recall
- F1-score
- Training and testing data
- Logistic regression
- Limitations of small test sets

## Results

### Predefined predictions

The predefined-prediction script produced:

- Accuracy: 80.00%
- Precision: 66.67%
- Recall: 66.67%
- F1-score: 66.67%

### Trained classification model

The logistic regression script produced:

- Training samples: 16
- Testing samples: 4
- Accuracy: 100.00%
- Precision: 100.00%
- Recall: 100.00%
- F1-score: 100.00%

The trained model correctly classified all four test samples in this run.

## Important Limitation

The trained model uses a small synthetic dataset and only four test samples. The perfect test score is a learning result, not evidence of real-world spam-filter performance. A larger, representative dataset is needed to assess generalization reliably.

## Interview Preparation

See `interview_notes.md` for definitions, formulas, worked calculations, verified checkpoint answers, and common AI/ML interview questions.

## Status

Day 16 classification metrics practice and evaluation completed, pending final file verification and Git commit/push.
