# ML Prediction API

A machine learning prediction API built with Python, scikit-learn, FastAPI, and Uvicorn. The project trains a Logistic Regression pipeline on the Breast Cancer Wisconsin dataset, saves the trained pipeline, and exposes endpoints for health checks and predictions.

## Features

- Train and evaluate a machine learning pipeline.
- Scale input features using `StandardScaler`.
- Save and load the trained pipeline using Joblib.
- Expose REST API endpoints with FastAPI.
- Validate prediction requests using Pydantic.
- Test API behavior using Pytest and FastAPI TestClient.

## Project Structure

```text
03_ML_Prediction_API/
├── models/
│   └── breast_cancer_pipeline.joblib
├── reports/
│   └── model_evaluation.txt
├── src/
│   ├── __init__.py
│   ├── train_model.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_api.py
└── README.md
```

## Requirements

Activate the shared virtual environment and install the dependencies from the repository root if needed:

```powershell
cd D:\AI-Engineer-Roadmap
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Train the Model

From the project directory, run:

```powershell
cd D:\AI-Engineer-Roadmap\03_ML_Prediction_API
python -m src.train_model
```

The training script saves the fitted pipeline to `models/breast_cancer_pipeline.joblib` and the evaluation report to `reports/model_evaluation.txt`.

## Run the API

From the project directory, run:

```powershell
python -m uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Basic application status |
| GET | `/health` | Health check and model status |
| POST | `/predict` | Generate a prediction |

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

### Prediction Request

Send exactly 30 numeric features in the expected dataset order:

```json
{
  "features": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

### Prediction Response

```json
{
  "prediction": 1,
  "predicted_class": "benign"
}
```

Class mapping: `0` = malignant; `1` = benign. This is a learning project, not a medical diagnostic tool. Example inputs do not establish a real patient's condition.

Invalid requests, including incorrect feature counts and non-numeric values, return HTTP `422`.

## Run Automated Tests

Run the API tests from the project directory:

```powershell
python -m pytest tests/test_api.py -v
```

The current test suite checks the health endpoint, a valid prediction request, incorrect feature counts, and non-numeric input.

## Model Evaluation

The initial training run achieved test accuracy of approximately **98.25%** on a held-out test split. This is a dataset-specific result and does not establish clinical performance.

## Future Improvements

- Add input validation for finite numeric values.
- Add model metadata and versioning.
- Improve automated test coverage.
- Add containerization and deployment configuration.
