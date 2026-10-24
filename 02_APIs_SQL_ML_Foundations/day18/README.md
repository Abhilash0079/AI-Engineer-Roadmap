# Day 18 — Data Preprocessing Pipelines

## Objective
Build reusable preprocessing pipelines using scikit-learn to handle missing values, scale numerical features, encode categorical features, and integrate preprocessing with model training.

## Concepts Covered
- SimpleImputer for missing-value imputation
- StandardScaler for numerical feature scaling
- OneHotEncoder for categorical encoding
- ColumnTransformer for applying different transformations to column groups
- Pipeline for connecting preprocessing and model training
- Train/test splitting and prevention of data leakage

## Project Files

| File | Purpose |
|---|---|
| `notes.txt` | Notes on preprocessing concepts and data leakage |
| `preprocessing_pipeline.py` | Demonstrates imputation, scaling, encoding, and column transformations |
| `train_preprocessing_pipeline.py` | Connects preprocessing with Logistic Regression and evaluates predictions |
| `README.md` | Project overview and execution instructions |
| `interview_notes.md` | Interview concepts and questions |

## Dataset
The examples use a small synthetic dataset with eight records.

**Input features**
- `Age` — numerical
- `Salary` — numerical
- `City` — categorical

**Target**
- `Purchased` — binary target (0 or 1)

The dataset intentionally contains missing values in numerical and categorical features.

## Preprocessing Design

### Numerical pipeline
1. Fill missing values using the median.
2. Scale features using `StandardScaler`.

### Categorical pipeline
1. Fill missing values using the most frequent category.
2. Encode categories using `OneHotEncoder(handle_unknown="ignore")`.

### Combined pipeline
`ColumnTransformer` applies the appropriate preprocessing to each feature group. A scikit-learn `Pipeline` then connects the preprocessor to a Logistic Regression classifier.

## Execution

Activate the project's virtual environment and run these commands from this folder:

```powershell
python .\preprocessing_pipeline.py
python .\train_preprocessing_pipeline.py
```

## Evaluation Results
The training script uses a 75% training split and a 25% test split.

- Training samples: 6
- Testing samples: 2
- Test accuracy in this run: 50%

The test set is extremely small, so this score is only a demonstration and does not provide a reliable estimate of real-world performance.

## Preventing Data Leakage
The model pipeline is fitted on training data only. Its learned imputation values, scaling statistics, and encoding categories are reused when predicting on test or new data.

This avoids fitting preprocessing steps on the test set.

**Note:** `preprocessing_pipeline.py` uses `fit_transform()` on the