# Day 14 — ML Model Serving with FastAPI

## Objective
Serve a trained machine-learning regression model through a REST API using FastAPI.

## Project Files
- `train_model.py` — trains and saves the regression model.
- `exam_score_model.joblib` — saved trained model.
- `main.py` — FastAPI application and prediction endpoint.
- `README.md` — project documentation.

## Model
The model uses hours studied to predict an exam score.

Training data:
- Hours studied: 1, 2, 3, 4, 5
- Exam scores: 40, 50, 60, 70, 80

The model predicts a score of 90 for 6 hours of study.

## Run the Project

From the `day14` directory, activate the project's virtual environment if it is not already active, then run:

```powershell
python train_model.py
python -m uvicorn main:app --reload
```

Open the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Endpoint

### `GET /`
Confirms that the API is running.

### `POST /predict`
Accepts JSON:

```json
{
  "hours_studied": 6
}
```

Example response:

```json
{
  "hours_studied": 6.0,
  "predicted_exam_score": 90.0
}
```

## Input Validation
- `hours_studied` is required.
- Values from 0 through 24 are allowed.
- Negative values, values greater than 24, and missing fields return HTTP 422.

## What I Learned
- Saving and loading a trained model with joblib.
- Connecting a machine-learning model to FastAPI.
- Creating a POST prediction endpoint.
- Validating request data with Pydantic.
- Testing successful and invalid requests through Swagger UI.

## Limitation
This model was trained on only five examples for learning purposes. Its predictions should not be treated as reliable real-world exam-score estimates.
