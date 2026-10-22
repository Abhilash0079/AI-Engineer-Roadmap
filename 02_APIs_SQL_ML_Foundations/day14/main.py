from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

# 1. Create an Application
app = FastAPI(title="Exam Score Prediction API")

# 2. Load the save model
model_path = Path(__file__).parent / "exam_score_model.joblib"
model = joblib.load(model_path)

# 3. Define and validate the request data
class PredictionRequest(BaseModel):
    hours_studied: float = Field(ge=0, le=24)


# 4. Define the home endpoint
@app.get('/')
def home():
    return {"message": "Exam Score Prediction API is running"}

# 5. Define the prediction endpoint
@app.post('/predict')
def predict_exam_score(request: PredictionRequest):
    prediction  = model.predict([[request.hours_studied]])[0]

    return {
        "hours_studied": request.hours_studied,
        "predicted_exam_score": round(float(prediction), 2),
    }