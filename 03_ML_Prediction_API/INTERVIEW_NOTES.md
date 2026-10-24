# Day 21 — ML Prediction API Interview Notes

## 1. What is an API?

An API (Application Programming Interface) allows different software applications to communicate with each other. In this project, a client sends feature values to a FastAPI endpoint, and the API returns a machine learning prediction.

## 2. What is FastAPI?

FastAPI is a Python framework for building APIs. It supports request validation through type hints and Pydantic models, generates interactive API documentation, and supports asynchronous endpoints.

## 3. What is Uvicorn?

Uvicorn is an ASGI server that runs the FastAPI application and handles incoming HTTP requests.

Command used:

```powershell
python -m uvicorn src.main:app --reload
```

- `src.main`: the Python module containing the application.
- `app`: the FastAPI application object.
- `--reload`: restarts the server when development code changes.

## 4. What is Pydantic validation?

Pydantic validates incoming request data against a declared model. Our `PredictionRequest` requires a list containing exactly 30 numeric features.

Invalid data is rejected before the prediction function runs. FastAPI normally returns HTTP `422` for request validation errors.

## 5. Why must the input contain exactly 30 features?

The model was trained using 30 input features. A prediction request must provide the same number of features in the expected order. Incorrect feature counts cannot be used reliably by the trained model.

## 6. What is a scikit-learn Pipeline?

A Pipeline combines preprocessing and model-estimation steps into one object. Our pipeline applies `StandardScaler` and then `LogisticRegression`.

This ensures that incoming data passes through the same preprocessing step used during training.

## 7. Why use StandardScaler?

StandardScaler transforms each feature using its training-set mean and standard deviation. Scaling can help Logistic Regression optimize its coefficients when input features have different scales.

The scaler is fitted during training and reused during prediction; it should not be fitted again on each incoming request.

## 8. Why save the trained model with Joblib?

Joblib can serialize and reload Python objects, including many scikit-learn pipelines. Saving the fitted pipeline means the API can reuse the trained model without retraining it every time the application starts.

Only load model files from trusted sources.

## 9. What is the difference between training and prediction?

- **Training:** the model learns patterns from labelled data.
- **Prediction:** the trained model receives new feature values and produces an output.

Our training script saves the fitted pipeline. The API loads that pipeline and uses its `predict()` method.

## 10. What do the API endpoints do?

- `GET /`: returns a basic status message.
- `GET /health`: reports the API health and whether the pipeline loaded.
- `POST /predict`: accepts features and returns the predicted class.

A health endpoint is useful for checking whether a service is responding. A production readiness check may need additional checks, such as dependency or model availability.

## 11. What do HTTP 200 and HTTP 422 mean?

- **200 OK:** the request succeeded.
- **422 Unprocessable Entity:** the request data failed validation.

In our tests, a valid request returned `200`, while too few features and a non-numeric feature returned `422`.

## 12. Why use Pytest and TestClient?

Pytest runs automated tests. FastAPI's `TestClient` allows requests to be made directly against the application in tests without manually starting a separate server.

Our four tests cover:
1. Health endpoint.
2. Valid prediction.
3. Too few features.
4. Non-numeric feature.

## 13. What is model persistence?

Model persistence means saving a trained model so it can be reused later. It separates the training process from the serving process and avoids retraining on every prediction request.

## 14. Why is reproducibility important?

Reproducibility makes it easier to repeat an experiment and compare results. Setting a fixed `random_state` in the train/test split helps make the split consistent across runs when the dataset and software environment remain compatible.

## 15. What does test accuracy of 98.25% mean?

It means approximately 98.25% of the samples in this particular held-out test set were classified correctly. It does not guarantee the same accuracy on other data or establish that the API is suitable for medical diagnosis.

## 16. What improvements would you make for production?

Possible improvements include:
- Stronger validation of feature order and finite numeric values.
- Model versioning and metadata.
- Logging and structured error handling.
- Authentication, rate limiting, and monitoring.
- Automated integration tests.
- Containerization and deployment.
- Evaluation on representative data before real-world use.

## Quick Revision

- Framework: FastAPI
- Server: Uvicorn
- Request validation: Pydantic
- ML library: scikit-learn
- Model persistence: Joblib
- Testing: Pytest and FastAPI TestClient
- Input size: 30 numeric features
- Successful request: HTTP 200
- Invalid request: HTTP