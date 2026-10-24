# Day 20 — Model Persistence and Reproducibility

## Objective
Train a machine-learning pipeline, save it with Joblib, reload it without retraining, and verify that it produces consistent predictions.

## Dataset
- **Dataset:** Breast Cancer Wisconsin dataset from scikit-learn
- **Total samples:** 569
- **Features:** 30
- **Training samples:** 455
- **Test samples:** 114

## Files
- `save_model.py` — trains the pipeline, evaluates it, and saves it.
- `load_model.py` — loads the saved pipeline and verifies its predictions.
- `models/breast_cancer_pipeline.joblib` — saved preprocessing and trained classifier.

## Pipeline
1. `StandardScaler` transforms features using statistics learned during training.
2. `LogisticRegression` predicts the target class.
3. The complete fitted pipeline is saved using `joblib.dump()`.
4. The pipeline is restored using `joblib.load()`.

## Results
- **Held-out test accuracy:** 0.9825 (98.25%)
- **Test samples evaluated:** 114
- **Loaded pipeline predictions match reference pipeline:** True
- **Retraining required to use the saved pipeline:** No

## Key Lessons
- Model persistence avoids unnecessary retraining for routine inference.
- Saving preprocessing and the estimator together helps preserve the training workflow.
- Reproducibility benefits from fixed random seeds and tracking data, code, and library versions.
- A held-out test set should remain separate from model selection and tuning.

## Security Note
Only load Joblib files from trusted sources. Loading an untrusted serialized file can execute malicious code.

## Limitations
The reported accuracy comes from one train/test split. It does not guarantee performance on new data. This exercise demonstrates persistence and reproducibility, not clinical readiness.

## Status
- [x] Trained and saved the complete pipeline
- [x] Loaded the saved pipeline without retraining
- [x] Generated predictions from the loaded pipeline
- [x] Verified predictions against a reference pipeline
- [x] Documented results
- [x] Git verification and push
