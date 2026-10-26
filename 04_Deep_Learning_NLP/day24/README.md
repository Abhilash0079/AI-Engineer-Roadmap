# Day 24: Deep Learning with Real Data

## Objective
Build a complete PyTorch regression pipeline using a real dataset from scikit-learn.

## Dataset
- **Source:** scikit-learn Diabetes dataset
- **Samples:** 442
- **Input features:** 10
- **Task:** Regression — predict a quantitative diabetes progression target.

## Data Preparation
- Split the data into training, validation, and test sets.
- Training set: 309 samples
- Validation set: 66 samples
- Test set: 67 samples
- Standardize features using `StandardScaler`.
- Fit the scaler on the training data only to prevent data leakage.
- Convert features and targets into PyTorch tensors with `float32` data types.
- Use `TensorDataset` and `DataLoader` to organize data into batches.

## Model
A fully connected neural network with:
- Input layer: 10 features
- Hidden layer 1: 32 neurons with ReLU
- Hidden layer 2: 16 neurons with ReLU
- Output layer: 1 regression value

## Training
- Loss function: Mean Squared Error (`MSELoss`)
- Optimizer: Adam
- Learning rate: 0.001
- Maximum epochs: 100
- Batch size: 32
- Validation loss is monitored to track model performance.
- The best validation checkpoint is restored if implemented by the training script.
- Early stopping is configured, but it did not activate during this run.

## Test Results

| Metric | Result |
|---|---:|
| Test MSE | 3966.72 |
| Test RMSE | 62.98 |
| Test MAE | 50.32 |

These metrics provide an initial evaluation of the neural network. A simple baseline model and further experiments would help determine whether the network improves predictive performance.

## Key Learnings
- Preparing real data for PyTorch.
- Splitting datasets into training, validation, and test sets.
- Preventing preprocessing data leakage.
- Creating tensors, datasets, and data loaders.
- Training a neural network for regression.
- Evaluating predictions with MSE, RMSE, and MAE.
- Monitoring validation loss and understanding early stopping.

## Run the Project

Activate the repository's existing virtual environment and run:

```powershell
python .\real_data_pipeline.py
```
