from pathlib import Path

import joblib
from sklearn.linear_model import LinearRegression

# 1. Training data: hours studied and exam scores
X = [[1], [2], [3], [4], [5]]
y = [40, 50, 60, 70, 80]

# 2. Create and train the model
model = LinearRegression()
model.fit(X, y)

# 3. Save the trained model in day14 folder
model_path = Path(__file__).parent / "exam_score_model.joblib"
joblib.dump(model, model_path)

print("Model trained successfully.")
print(f"Model saved to : {model_path}")
print(f"Prediction for 6 hours studies: {model.predict([[6]])[0]:.2f}")