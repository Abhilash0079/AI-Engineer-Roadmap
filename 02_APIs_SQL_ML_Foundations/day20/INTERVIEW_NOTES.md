# Day 20 — Interview Notes: Model Persistence and Reproducibility

## 1. What is model persistence?
Model persistence is saving a trained model so it can be loaded and reused later without training it from scratch.

## 2. What is serialization?
Serialization converts an object into a representation that can be stored and later reconstructed.

## 3. Why use Joblib?
Joblib is commonly used to serialize scikit-learn models and pipelines, including objects containing NumPy arrays.

## 4. Why save the complete pipeline?
A pipeline keeps preprocessing and prediction steps together. Saving the scaler and classifier together helps ensure new data receives the same transformations used during training.

## 5. What do `joblib.dump()` and `joblib.load()` do?
- `joblib.dump(object, path)` saves an object.
- `joblib.load(path)` restores a saved object.

## 6. Does loading a saved model retrain it?
No. Loading restores the fitted model state. Predictions can then be made using `predict()` without calling `fit()` again.

## 7. What is reproducibility?
Reproducibility means being able to repeat an experiment under documented conditions and obtain consistent results. It benefits from fixed random seeds and recorded dataset, code, and library versions.

## 8. Why split data before fitting preprocessing?
Preprocessing should learn its statistics from training data only. Fitting a scaler on the full dataset before evaluation leaks information from the test set.

## 9. What does a test accuracy of 0.9825 mean?
The pipeline correctly classified 98.25% of the 114 held-out test samples in this run. It does not guarantee the same accuracy on future data.

## 10. Is Joblib safe for files from unknown sources?
No. Loading an untrusted serialized file can execute malicious code. Only load files from trusted sources.

## 11. How can you verify that a saved model works?
Load it in a separate script, make predictions on the same test features, compare predictions against a reference pipeline, and evaluate performance using appropriate metrics.

## Summary
Model persistence enables reuse of trained pipelines. Reliable model deployment also requires consistent preprocessing, reproducible experiments, version tracking, appropriate evaluation, and safe handling of serialized files.
