# Day 14 — Interview Notes

## 1. Why serve an ML model through an API?
An API lets another application send input data to a trained model and receive predictions without directly running the training code.

## 2. Why save a trained model?
Saving a trained model lets an application load and reuse it without retraining for every prediction request.

## 3. What is joblib?
`joblib` can serialize Python objects, including many scikit-learn models, so they can be saved to disk and loaded later. Only load model files from trusted sources.

## 4. What is FastAPI?
FastAPI is a Python framework for building APIs. It supports request validation and generates interactive API documentation.

## 5. Why use POST for `/predict`?
POST allows the client to send prediction input in the request body, commonly as JSON.

## 6. What does HTTP 422 mean in this project?
FastAPI returns 422 when the request body fails validation, such as when `hours_studied` is missing or outside the allowed range.

## 7. What is Pydantic doing?
Pydantic validates request data against the `PredictionRequest` model before the prediction function runs.

## 8. Why load the model when the API module starts?
Loading the model when the application starts avoids loading it separately for each prediction request.

## 9. What is a limitation of this model?
It was trained on only five examples, so it is suitable for demonstrating the API workflow, not for making reliable real-world exam predictions.
