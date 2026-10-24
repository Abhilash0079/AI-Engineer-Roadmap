from pathlib import Path
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "breast_cancer_pipeline.joblib"

app = FastAPI(
    title="ML Prediction API",
    description="Predict breast cancer dataset classes using a saved ML pipeline.",
    version="1.0.0"
)

class PredictionRequest(BaseModel):
    features : list[float] = Field(
        ...,
        min_length=30,
        max_length=30,
        description="Exactly 30 numeric features in the dataset's expected order.",
    )

class PredictionResponse(BaseModel):
    prediction:int
    predicted_class:str

def load_pipeline():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Saved model not found at: {MODEL_PATH}. "
            "Run python -m src.train_model first."
        )

    return joblib.load(MODEL_PATH)

pipeline = load_pipeline()

@app.get('/')
def health_check():
    return {"status": "healthy", "message": "ML Prediction API is running."}

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": pipeline is not None}

@app.post("/predict", response_model = PredictionResponse)
def predict(request:PredictionRequest):
    if not np.isfinite(request.features).all():
        raise HTTPException(
            status_code=422,
            detail="All features must be finite numbers.",
        )

    prediction = int(pipeline.predict([request.features])[0])

    # The dataset maps 0 to malignant and 1 to benign.
    class_names = {0: "malignant", 1: "benign"}

    return PredictionResponse(
        prediction=prediction,
        predicted_class=class_names[prediction],
    )

