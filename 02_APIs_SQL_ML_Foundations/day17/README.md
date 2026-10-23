
# Day 17: Tree-Based Models

## Objective
Learn and implement Decision Tree and Random Forest classifiers, understand feature importance, and compare model performance.

## Concepts Covered
- Decision Tree classification
- Root nodes, decision nodes, leaf nodes, and tree depth
- Gini impurity
- Random Forest classification
- Feature importance
- Model comparison and evaluation
- Reproducible train/test splitting

## Project Files

| File | Description |
|---|---|
| `decision_tree.py` | Trains and evaluates a Decision Tree classifier |
| `random_forest.py` | Trains and evaluates a Random Forest classifier |
| `compare_models.py` | Compares both models using the same train/test split |
| `interview_notes.md` | Key concepts and interview preparation notes |

## Dataset
A small synthetic classification dataset with 16 samples.

Features:
- Hours studied
- Practice tests completed

Target:
- `0` = Fail
- `1` = Pass

## Models Implemented

### Decision Tree
- Algorithm: `DecisionTreeClassifier`
- Maximum depth: 3
- Random state: 42

### Random Forest
- Algorithm: `RandomForestClassifier`
- Number of trees: 100
- Maximum depth per tree: 3
- Random state: 42

## Evaluation Results

Both models used the same training and testing split.

| Metric | Decision Tree | Random Forest |
|---|---:|---:|
| Training samples | 12 | 12 |
| Testing samples | 4 | 4 |
| Correct predictions | 4/4 | 4/4 |
| Accuracy | 100% | 100% |

Actual test labels:
`[0, 1, 0, 1]`

Predicted labels for both models:
`[0, 1, 0, 1]`

## Random Forest Feature Importance

| Feature | Importance |
|---|---:|
| Hours studied | 0.6342 |
| Practice tests completed | 0.3658 |

These scores represent relative, split-based feature importance. They do not prove causation.

## Key Learnings
1. A Decision Tree makes predictions using one tree.
2. A Random Forest combines predictions from multiple decision trees.
3. `max_depth` controls tree depth and helps limit model complexity.
4. `n_estimators=100` creates a forest containing 100 trees.
5. `random_state` helps make randomized operations reproducible.
6. Feature importance describes a model-based measure of feature contribution.
7. Models must be evaluated on representative, unseen data.

## Important Limitation
The dataset is small and synthetic, and the test set contains only four samples. The 100% accuracy scores do not establish real-world performance.

Further evaluation should use representative data, appropriate validation methods, and relevant metrics.

## How to Run

Activate the project's virtual environment and navigate to this folder.

```powershell
python decision_tree.py
python random_forest.py
python compare_models.py
```

## Status
- [x] Decision Tree implementation
- [x] Random Forest implementation
- [x] Feature importance analysis
- [x] Model comparison
- [x] Interview concept review
- [ ] Documentation and Git verification
