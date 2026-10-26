# Day 24: Deep Learning Interview Notes

## 1. What is data leakage?
Data leakage occurs when information unavailable at prediction time influences model training. It can make evaluation results overly optimistic.

## 2. Why fit a scaler only on training data?
The scaler learns statistics from the training data. Validation and test data must use the same fitted scaler without influencing those statistics.

## 3. What is the purpose of a validation set?
It helps monitor generalization during development, compare model settings, and support decisions such as early stopping.

## 4. Why keep a test set separate?
The test set estimates final performance on data that was not used to fit the model or select training settings.

## 5. What is a DataLoader?
A PyTorch `DataLoader` batches samples from a dataset and can shuffle training examples between epochs.

## 6. What is a batch?
A batch is a group of samples processed together in one training step.

## 7. What is an epoch?
An epoch is one complete pass through the training dataset.

## 8. What does MSE measure?
Mean Squared Error averages the squared differences between predictions and targets. Larger errors receive disproportionately more weight.

## 9. What does RMSE measure?
Root Mean Squared Error is the square root of MSE. It is expressed in the same units as the target.

## 10. What does MAE measure?
Mean Absolute Error averages the absolute differences between predictions and targets. It is also expressed in the target's units.

## 11. What is early stopping?
Early stopping ends training when the monitored validation metric has not improved for a configured number of epochs.

## 12. Why save the best model checkpoint?
The final epoch is not necessarily the best one. Saving and restoring the state with the best validation performance preserves the selected model.

## 13. Why use `model.eval()` and `torch.no_grad()` during evaluation?
`model.eval()` switches modules such as dropout and batch normalization into evaluation behavior. `torch.no_grad()` disables gradient tracking to reduce unnecessary memory and computation.

## 14. Why use `float32` tensors?
Neural-network layers and common loss functions generally expect floating-point inputs and targets for regression.

## 15. How do you interpret this run's metrics?
- Test MSE: 3966.72
- Test RMSE: 62.98
- Test MAE: 50.32

The metrics quantify prediction error; comparison with a simple baseline is needed to judge whether the model provides useful improvement.
