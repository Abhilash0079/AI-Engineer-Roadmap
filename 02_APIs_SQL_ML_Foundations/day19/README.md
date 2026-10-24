# Day 19 — Cross-Validation and Hyperparameter Tuning

## Objective

Learn to evaluate classification models with cross-validation, compare evaluation metrics, and tune hyperparameters using scikit-learn.

## Dataset

- Dataset: Breast Cancer Wisconsin dataset built into scikit-learn
- Samples: 569
- Features: 30
- Task: Binary classification

## Files

- `cross_validation.py` — evaluates Logistic Regression with five-fold stratified cross-validation.
- `hyperparameter_tuning.py` — uses `GridSearchCV` to tune the Logistic Regression `C` parameter.
- `randomized_search.py` — uses `RandomizedSearchCV` to sample candidate values of `C`.
- `tuning_comparison.py` — compares the recorded best mean F1 scores.

## Cross-Validation Results

Five-fold cross-validation produced these mean scores:

| Metric | Mean score |
|---|---:|
| Accuracy | 0.9737 |
| Precision | 0.9683 |
| Recall | 0.9916 |
| F1 score | 0.9794 |

These values are validation estimates, not guaranteed future performance.

## Hyperparameter Tuning Results

### GridSearchCV

- Best `C`: 0.1
- Best mean cross-validation F1: 0.9795
- Candidate values: 0.01, 0.1, 1, 10, 100

### RandomizedSearchCV

- Best sampled `C`: approximately 0.9847
- Best mean cross-validation F1: 0.9794
- Candidates evaluated: 10
- Cross-validation folds: 5

The two methods produced very similar scores in this experiment. The tiny difference does not establish that one method is generally superior.

## Key Concepts Learned

1. Cross-validation estimates model performance across different data splits.
2. Stratified folds help preserve class proportions in classification tasks.
3. Precision, recall, and F1 complement accuracy.
4. `GridSearchCV` tests all specified parameter combinations.
5. `RandomizedSearchCV` samples a limited number of parameter combinations.
6. A scikit-learn `Pipeline` helps prevent preprocessing leakage during cross-validation.
7. A separate untouched test set is needed for a final, less biased evaluation after model selection.

## Important Limitation

This exercise tuned and evaluated candidates using cross-validation on the complete dataset. It did not reserve a separate final test set, so the best cross-validation score should not be treated as an unbiased final performance estimate.

## Status

- [x] Cross-validation implemented
- [x] Evaluation metrics compared
- [x] GridSearchCV implemented
- [x] RandomizedSearchCV implemented
- [x] Tuning results compared
- [x] Results documented
- [x] Git verification and push