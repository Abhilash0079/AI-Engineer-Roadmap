
# Day 23: Neural Network Training and Evaluation — Interview Notes

## 1. What is the difference between training, validation, and test data?

- **Training data:** Used to learn model parameters such as weights and biases.
- **Validation data:** Used during development to compare models, tune hyperparameters, and monitor overfitting.
- **Test data:** Used for final evaluation after model choices have been made.

The test set should not be repeatedly used to tune the model because that can make the evaluation overly optimistic.

## 2. What is a model parameter?

A model parameter is a value learned automatically from training data.

Examples:
- Weights
- Biases

## 3. What is a hyperparameter?

A hyperparameter is a setting chosen before or during model development rather than learned directly as a model weight.

Examples:
- Learning rate
- Batch size
- Number of layers
- Number of training epochs
- Early-stopping patience

## 4. What is overfitting?

Overfitting occurs when a model learns the training data too closely, including noise or accidental patterns, and performs poorly on unseen data.

A common warning sign is training loss decreasing while validation loss starts increasing.

## 5. What is underfitting?

Underfitting occurs when a model cannot learn the important patterns in the data.

Possible signs include high training loss and high validation loss.

## 6. How can we detect overfitting?

Monitor training and validation losses or other appropriate metrics across epochs.

- Training loss decreases and validation loss decreases: learning may be improving.
- Training loss decreases but validation loss increases: possible overfitting.
- Both losses remain high: possible underfitting.

These patterns are useful clues, not absolute rules.

## 7. What is early stopping?

Early stopping stops training when a monitored validation metric stops improving according to a specified rule.

For example, with a patience of five epochs, training stops after five consecutive epochs without improvement in validation loss.

It can reduce unnecessary training and help limit overfitting.

## 8. What does optimizer.zero_grad() do?

PyTorch accumulates gradients by default. optimizer.zero_grad() clears previously stored gradients before the next backward pass.

## 9. What does loss.backward() do?

It calculates gradients of the loss with respect to the model's trainable parameters using backpropagation.

## 10. What does optimizer.step() do?

It updates model parameters using the gradients and the optimizer's update rule.

For example, the Adam optimizer uses adaptive parameter updates based on gradient information.

## 11. Why do we use model.train()?

model.train() switches the model into training mode. This matters for layers such as Dropout and Batch Normalization, whose behavior differs between training and evaluation.

It does not itself perform a parameter update.

## 12. Why do we use model.eval()?

model.eval() switches the model into evaluation mode. For example, Dropout is disabled and Batch Normalization uses its stored running statistics.

It does not automatically disable gradient tracking.

## 13. What does torch.no_grad() do?

torch.no_grad() disables gradient tracking for operations inside its context. It reduces unnecessary computation and memory use during ordinary evaluation.

## 14. What is a batch?

A batch is a subset of training samples processed together during one forward and backward pass.

Batch training divides a dataset into smaller groups instead of processing the entire dataset at once.

## 15. What is a DataLoader?

PyTorch's DataLoader provides batches of data and supports options such as shuffling and batch size.

It helps make training and evaluation loops easier to implement.

## 16. What is binary cross-entropy loss?

Binary cross-entropy measures the difference between predicted probabilities and binary target labels.

In the Day 23 example, nn.BCELoss() is used with a model whose final layer is Sigmoid.

For numerically stable training, another common approach is nn.BCEWithLogitsLoss() without a separate final Sigmoid layer.

## 17. What is classification accuracy?

Accuracy is the proportion of predictions that are correct.

Accuracy can be misleading on imbalanced datasets. A model may predict the majority class frequently and still miss most minority-class examples.

## 18. What metrics are useful for imbalanced classification?

- **Precision:** Of the examples predicted positive, how many were actually positive?
- **Recall:** Of the actual positive examples, how many did the model identify?
- **F1-score:** Harmonic mean of precision and recall.
- **PR-AUC:** Summarizes the precision-recall trade-off across thresholds and is often useful for rare positive classes.

The appropriate metric depends on the business objective and the cost of false positives and false negatives.

## 19. What is the difference between MAE and MSE?

Both are regression metrics.

- **MAE (Mean Absolute Error):** Averages the absolute differences between actual and predicted values.
- **MSE (Mean Squared Error):** Averages the squared differences between actual and predicted values.

MSE gives larger errors disproportionately more influence than MAE.

Example: If absolute errors are 2 and 4:

- MAE = (2 + 4) / 2 = 3
- MSE = (2² + 4²) / 2 = 10

## 20. Why restore the best validation checkpoint?

The final epoch is not always the epoch with the best validation performance. Restoring the model state with the lowest validation loss ensures that the final test evaluation uses the selected best checkpoint.

## 21. Why can 100% test accuracy be misleading?

A perfect result on a small, simple synthetic dataset does not guarantee real-world performance.

The dataset may be easy to separate and may not represent the complexity, noise, or class imbalance of production data.

Real-world models need representative held-out data and appropriate evaluation metrics.

## 22. Describe the Day 23 project.

I implemented a binary-classification neural network using PyTorch. I generated synthetic data, split it into training, validation, and test sets, trained the model in mini-batches, monitored validation loss, saved the best model state, implemented early stopping, and evaluated the selected model on the test set.

In my recorded run, training completed for 50 epochs, validation and test accuracy reached 100%, and test loss was 0.0038. Early stopping did not activate because validation loss continued to improve.

## Key Training Sequence

1. Clear previous gradients with optimizer.zero_grad().
2. Run the forward pass to obtain predictions.
3. Calculate the loss.
4. Call loss.backward() to calculate gradients.
5. Call optimizer.step() to update model parameters.
6. Evaluate on validation data without gradient tracking.
7. Restore the best validation checkpoint and evaluate on test data.
