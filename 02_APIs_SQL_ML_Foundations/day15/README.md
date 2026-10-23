# Day 15: Regression and Evaluation Metrics

## Objective
Learn how to evaluate regression models using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

## Dataset
This exercise uses sample data relating hours studied to exam scores.

- Input feature: Hours studied
- Target: Exam score
- Total examples: 10
- Training examples: 8
- Testing examples: 2

The data is split using `train_test_split` with `test_size=0.2` and `random_state=42`.

## Models
1. **Linear Regression:** Learns a relationship between study hours and exam scores.
2. **Mean Baseline:** Uses `DummyRegressor(strategy="mean")` to predict the average target value from the training data.

Both models are evaluated on the same held-out test set.

## Evaluation Results

| Metric | Linear Regression | Mean Baseline |
|---|---:|---:|
| MAE | 1.88 | 22.50 |
| MSE | 3.59 | 509.77 |
| RMSE | 1.90 | 22.58 |

Lower values indicate better performance for these metrics when comparing predictions on the same test set.

## Conclusion
Linear Regression performed better than the mean baseline on this test set because all three evaluation metrics were lower.

However, the test set contains only two examples. These results are preliminary and do not establish how well the model will perform on new, real-world data.

## How to Run
From the project root, with the virtual environment activated, run:

```powershell
python .\02_APIs_SQL_ML_Foundations\day15\regression_metrics.py
```

## Key Learning
- MAE measures the average absolute prediction error.
- MSE squares errors, giving larger errors a stronger penalty.
- RMSE is the square root of MSE and is expressed in the target's original units.
- A baseline provides a simple benchmark for evaluating a trained model.
- Evaluation should use held-out data that was not used to train the models.