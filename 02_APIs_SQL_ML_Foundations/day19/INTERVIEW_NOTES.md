# Day 19 — Interview Notes

## 1. What is cross-validation?

Cross-validation evaluates a model using multiple train-validation splits. It provides a more stable performance estimate than relying on a single split.

## 2. What is StratifiedKFold?

`StratifiedKFold` attempts to preserve the proportion of each class across the folds. This is useful for classification tasks, especially with imbalanced classes.

## 3. What is data leakage?

Data leakage occurs when information that should be unavailable during training influences model fitting or evaluation. For example, fitting a scaler on all data before cross-validation allows validation-fold statistics to influence preprocessing.

## 4. Why use a Pipeline?

A scikit-learn `Pipeline` combines preprocessing and a model. During cross-validation, it allows preprocessing to be fitted separately within each training fold.

## 5. What is GridSearchCV?

`GridSearchCV` evaluates every specified hyperparameter combination using cross-validation and selects the best combination according to the chosen scoring metric.

## 6. What is RandomizedSearchCV?

`RandomizedSearchCV` samples a specified number of hyperparameter combinations. It is useful when the search space is large and exhaustive search is expensive.

## 7. What does C control in Logistic Regression?

`C` is the inverse of regularization strength. Smaller values mean stronger regularization; larger values mean weaker regularization.

## 8. Why use precision, recall, and F1?

Accuracy measures overall correctness. Precision measures the reliability of positive predictions, recall measures how many actual positives are detected, and F1 combines precision and recall using their harmonic mean.

## 9. Does the highest cross-validation score guarantee the best real-world model?

No. Scores are estimates and can vary across data samples. A final evaluation on an untouched test set helps assess generalization after model selection.

## 10. Why can RandomizedSearchCV be faster?

It evaluates a specified number of sampled combinations instead of testing every combination in a large grid.

## Day 19 Summary

This day covered stratified cross-validation, classification metrics, preprocessing pipelines, GridSearchCV, RandomizedSearchCV, and experiment documentation.
