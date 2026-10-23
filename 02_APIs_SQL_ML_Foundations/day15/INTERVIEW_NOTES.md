# Day 15: Regression Interview Notes

## 1. What is regression?
Regression is a supervised machine learning task used to predict a numerical value, such as an exam score, house price, or temperature.

## 2. What is MAE?
Mean Absolute Error is the average of the absolute differences between actual and predicted values.

- Easy to interpret.
- Expressed in the target's original units.
- Treats errors linearly.

## 3. What is MSE?
Mean Squared Error is the average of squared differences between actual and predicted values.

- Penalizes large errors more strongly.
- Is expressed in squared target units.
- Can be sensitive to outliers.

## 4. What is RMSE?
Root Mean Squared Error is the square root of MSE.

- Expressed in the target's original units.
- Penalizes large errors more strongly than MAE.
- Is useful when larger errors deserve extra attention.

## 5. Why use a baseline model?
A baseline provides a simple benchmark. A more complex model should demonstrate value by outperforming a reasonable baseline on data that was not used for training.

## 6. Why split data into training and test sets?
The training set is used to fit the model. The test set estimates performance on unseen examples. Using test targets to train the model or make modeling decisions can cause data leakage.

## 7. What does `DummyRegressor(strategy="mean")` do?
It predicts the mean target value calculated from the training data for every input, regardless of the input features.

## 8. What do lower MAE, MSE, and RMSE values mean?
When comparing models on the same target and test set, lower values indicate smaller prediction errors according to those metrics.

## 9. What is a limitation of our Day 15 experiment?
The test set contains only two examples. The metrics can therefore be unstable and may not represent performance on real-world data.

## 10. Day 15 Results

| Metric | Linear Regression | Mean Baseline |
|---|---:|---:|
| MAE | 1.88 | 22.50 |
| MSE | 3.59 | 509.77 |
| RMSE | 1.90 | 22.58 |

Linear Regression performed better on this particular test set. More representative data and further validation are needed before making strong generalization claims.