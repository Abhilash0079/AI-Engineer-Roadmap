# Day 16 — Classification Metrics

## 1. Learning Objectives

- Understand the confusion matrix and its four outcomes.
- Calculate accuracy, precision, recall, and F1-score.
- Evaluate a classification model using scikit-learn.
- Understand false positives, false negatives, and the limitations of small test sets.

## 2. Classification Basics

Classification is a supervised machine learning task that predicts a category or class.

In our spam classification example:

- `0` = legitimate email
- `1` = spam email

`y_true` contains the actual labels, while `y_pred` contains the model's predicted labels.

## 3. Confusion Matrix

A confusion matrix compares actual labels with predicted labels.

| Actual / Predicted | Predicted 0 | Predicted 1 |
|---|---:|---:|
| Actual 0 | True Negative (TN) | False Positive (FP) |
| Actual 1 | False Negative (FN) | True Positive (TP) |

- **True Positive (TP):** An actual spam email correctly classified as spam.
- **True Negative (TN):** A legitimate email correctly classified as legitimate.
- **False Positive (FP):** A legitimate email incorrectly classified as spam.
- **False Negative (FN):** A spam email incorrectly classified as legitimate.

Remember: rows represent actual labels and columns represent predicted labels in our scikit-learn examples.

## 4. Classification Metrics and Formulas

### Accuracy

Accuracy measures the proportion of all predictions that are correct.

Formula: `(TP + TN) / (TP + TN + FP + FN)`

For the predefined example:

- TP = 2, TN = 6, FP = 1, FN = 1
- Accuracy = (2 + 6) / 10 = 80%

### Precision

Precision measures the proportion of predicted positive cases that are actually positive.

Formula: `TP / (TP + FP)`

For the predefined example:

- Precision = 2 / (2 + 1) = 66.67%

Precision is particularly useful when false positives are costly. In spam filtering, a false positive means a legitimate email is incorrectly sent to spam.

### Recall

Recall measures the proportion of actual positive cases correctly identified.

Formula: `TP / (TP + FN)`

For the predefined example:

- Recall = 2 / (2 + 1) = 66.67%

Recall is particularly useful when false negatives are costly. In spam filtering, a false negative means an actual spam email is missed.

### F1-score

F1-score is the harmonic mean of precision and recall.

Formula: `2 * (Precision * Recall) / (Precision + Recall)`

For the predefined example, precision and recall are both 66.67%, so F1-score is also 66.67%.

## 5. Checkpoint 2.1 — Theory Questions and Verified Answers

### Question 1
A legitimate email is incorrectly classified as spam. Which confusion-matrix outcome is this?

**Answer: False Positive (FP).**

The model predicts spam, but the actual class is legitimate.

### Question 2
Out of 20 emails predicted as spam, 15 really are spam. What is precision?

**Answer: 75%.**

Calculation: 15 / 20 × 100 = 75%.

### Question 3
A spam classifier misses many actual spam emails. Which metric should we especially examine?

**Answer: Recall.**

Missed spam emails are false negatives. Recall measures how many actual spam emails the model successfully identifies.

## 6. Checkpoint 3.2 — Model Understanding Questions

### Question 1
Why is accuracy 80% while precision and recall are 66.67%?

**Answer:**

Accuracy measures all correct predictions: 8 correct predictions out of 10 emails gives 80%.

Precision is 2 / 3 = 66.67%, because 2 of the 3 emails predicted as spam were actually spam.

Recall is 2 / 3 = 66.67%, because the model identified 2 of the 3 actual spam emails.

### Question 2
Which metric helps reduce the risk of legitimate emails being marked as spam?

**Answer: Precision.**

A legitimate email incorrectly marked as spam is a false positive. Precision measures how reliable positive predictions are.

### Question 3
What happens to recall when more actual spam emails are missed, while the number of actual spam emails stays fixed?

**Answer: Recall decreases.**

The number of false negatives increases while the total number of actual spam emails stays constant.

## 7. Predefined-Prediction Evaluation

File: `classification_metrics.py`

Actual labels:

`[0, 0, 0, 0, 0, 0, 0, 1, 1, 1]`

Predicted labels:

`[0, 0, 0, 0, 0, 0, 1, 0, 1, 1]`

Expected confusion matrix:

```text
[[6 1]
 [1 2]]
```

Expected metrics:

- Accuracy: 80.00%
- Precision: 66.67%
- Recall: 66.67%
- F1-score: 66.67%

This script evaluates predefined predictions. It does not train a classifier.

## 8. Trained Classification Model

File: `train_classifier.py`

The script uses:

- `train_test_split` to create training and testing sets.
- `LogisticRegression` to train a classification model.
- `predict()` to generate predictions on held-out test samples.
- `accuracy_score`, `precision_score`, `recall_score`, and `f1_score` to evaluate the predictions.
- `confusion_matrix` to show classification outcomes.

### Observed results

- Training samples: 16
- Testing samples: 4
- Actual test labels: `[0, 0, 1, 1]`
- Predicted test labels: `[0, 0, 1, 1]`

Confusion matrix:

```text
[[2 0]
 [0 2]]
```

Observed metrics:

- Accuracy: 100.00%
- Precision: 100.00%
- Recall: 100.00%
- F1-score: 100.00%

### Important limitation

The test set contains only four samples, and the dataset is synthetic. Perfect results on four samples do not establish reliable real-world spam-filter performance. A larger, representative test dataset is needed for a stronger assessment.

## 9. Checkpoint 3.3 — Verified Answers

### Question 1
If the model incorrectly marks a legitimate email as spam, which confusion-matrix value increases?

**Answer: False Positive (FP).**

### Question 2
Why should we be cautious about a 100% score on just four test samples?

**Answer: The test set is too small to establish reliable real-world performance.**

## 10. Common AI/ML Interview Questions

### Q1. What is classification?
Classification is a supervised learning task that predicts a discrete class or category.

### Q2. What is a confusion matrix?
A confusion matrix compares actual classes with predicted classes and summarizes true positives, true negatives, false positives, and false negatives.

### Q3. What is the difference between precision and recall?
Precision measures how reliable positive predictions are. Recall measures how many actual positive cases the model identifies.

### Q4. When is precision important?
Precision matters when false positives are costly, such as when legitimate emails must not be incorrectly marked as spam.

### Q5. When is recall important?
Recall matters when false negatives are costly, such as when missing an important positive case has serious consequences.

### Q6. What is the F1-score?
The F1-score is the harmonic mean of precision and recall. It is useful when both metrics matter.

### Q7. Can accuracy be misleading?
Yes. Accuracy can be misleading with imbalanced datasets, particularly when a model performs poorly on a minority class.

### Q8. Why split data into training and testing sets?
Training data is used to fit the model. Test data evaluates its performance on samples not used for training.

### Q9. Does a 100% test score guarantee a good model?
No. The test set may be too small or unrepresentative, and the model may not generalize to new real-world data.

### Q10. What is the difference between evaluating predefined predictions and evaluating a trained model?
Predefined-prediction evaluation calculates metrics from supplied labels and predictions. Trained-model evaluation fits an algorithm on training data and measures its predictions on held-out data.

### Q11. What is logistic regression used for?
Logistic regression is a classification algorithm that estimates class probabilities and predicts classes using a decision threshold.

### Q12. What is a false negative in spam classification?
A false negative occurs when an actual spam email is classified as legitimate.

## 11. Key Takeaways

- Accuracy measures overall correctness.
- Precision focuses on the reliability of positive predictions.
- Recall focuses on finding actual positive cases.
- F1-score balances precision and recall.
- FP means a negative case was incorrectly predicted positive.
- FN means a positive case was incorrectly predicted negative.
- Always interpret evaluation metrics in the context of dataset size, class balance, and the cost of errors.
