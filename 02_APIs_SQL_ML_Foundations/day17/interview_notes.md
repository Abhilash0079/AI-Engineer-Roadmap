
# Day 17: Tree-Based Models — Interview Notes

## 1. What is a Decision Tree?

A Decision Tree is a supervised machine learning algorithm that makes predictions using a sequence of learned decision rules.

For classification, it predicts a class such as `0` or `1`.

### Important Terms
- **Root node:** The starting point of the tree.
- **Decision node:** A node that splits data based on a feature and condition.
- **Leaf node:** A terminal node that produces a prediction.
- **Depth:** The number of edges along a path from the root to a node.

## 2. What is Gini Impurity?

Gini impurity measures how mixed the classes are within a node.

- `0` means the node contains only one class.
- Higher values indicate a more mixed class distribution.
- A Decision Tree can use Gini impurity to evaluate candidate splits.

For a binary classification problem, a node with equal proportions of both classes has Gini impurity `0.5`.

## 3. What is Random Forest?

Random Forest is an ensemble learning algorithm that combines multiple decision trees.

It introduces diversity through techniques such as bootstrap sampling and random feature selection. For classification, the trees' predictions are combined, typically by voting.

### Advantages
- Can reduce variance compared with an individual tree.
- Can model nonlinear relationships.
- Often works well with relatively little feature preprocessing.

### Limitations
- Usually requires more computation than a single tree.
- Is less straightforward to interpret as a whole.
- Can still overfit or generalize poorly depending on the data and settings.

## 4. Decision Tree vs. Random Forest

| Aspect | Decision Tree | Random Forest |
|---|---|---|
| Number of trees | One | Multiple |
| Interpretability | Generally easier | Generally harder |
| Variance | Can be high | Often reduced |
| Computation | Usually lower | Usually higher |
| Prediction | Follows one tree | Combines tree predictions |

A Random Forest is not guaranteed to outperform a Decision Tree on every dataset.

## 5. What does `max_depth` do?

`max_depth` limits the maximum depth of a tree.

For example:

```python
DecisionTreeClassifier(max_depth=3, random_state=42)
```

This limits the tree to a maximum root-to-leaf path length of three edges. It controls model complexity; it does not specify the number of target classes.

## 6. What does `n_estimators` mean?

In a Random Forest:

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42,
)
```

`n_estimators=100` means the forest contains 100 decision trees.

Increasing the number of trees can improve stability, but it also increases computation and does not guarantee better predictive performance.

## 7. What is Feature Importance?

Feature importance estimates how much each feature contributes according to a model-specific importance measure.

In scikit-learn, `feature_importances_` for these tree models reports normalized impurity-based importance.

Important limitations:
- It does not prove causation.
- Correlated features can affect how importance is distributed.
- It should not automatically be interpreted as a percentage of the target explained.

In this project:
- Hours studied: `0.6342`
- Practice tests completed: `0.3658`

Hours studied had the higher impurity-based importance score in this fitted Random Forest.

## 8. Why use `random_state`?

Setting `random_state` makes randomized operations reproducible under the same data, configuration, and software environment.

The value `42` is an arbitrary seed, not a special value that guarantees better results.

## 9. Why split data into training and testing sets?

The training set is used to fit the model. The test set estimates how well the fitted model performs on unseen examples.

Evaluating on the training data alone can give an overly optimistic impression of performance.

## 10. Is 100% accuracy always good?

No. Accuracy depends on the dataset and evaluation design.

In this project, only four synthetic samples were used for testing. Both models correctly predicted all four, but this is not enough evidence of reliable real-world performance.

Better evaluation may require:
- Representative real-world data.
- A larger, appropriate test set.
- Cross-validation where suitable.
- Metrics such as precision, recall, and F1-score.
- Checks for data leakage and overfitting.

## 11. Why use the same train/test split to compare models?

Using the same split makes the comparison fairer because both models are evaluated on the same examples.

In this project, both models used `random_state=42`, `test_size=0.25`, and `stratify=y`.

## 12. Interview Answers

### Q1. What is the difference between a Decision Tree and a Random Forest?

A Decision Tree uses one tree to make predictions, whereas a Random Forest combines predictions from multiple decision trees. Random Forest often reduces variance, but it is not always more accurate.

### Q2. What does `max_depth=3` mean?

It limits the maximum depth of the tree to three edges along a root-to-leaf path.

### Q3. What does `n_estimators=100` mean?

It specifies that the Random Forest contains 100 decision trees.

### Q4. Does feature importance prove causation?

No. It measures a model-specific contribution to its decisions and does not establish a causal relationship.

### Q5. Why use `random_state=42`?

It makes randomized operations reproducible when the data and other settings remain the same.

### Q6. Why is 100% accuracy on four test samples insufficient?

Four samples provide very limited evidence about performance on unseen real-world data. The model should be evaluated with representative data and an appropriate validation strategy.

## Day 17 Summary

Implemented and compared Decision Tree and Random Forest classifiers, examined feature importance, and reviewed model evaluation limitations.
