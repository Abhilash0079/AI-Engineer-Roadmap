from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt

# 1. Sample data: Study_Hours and Exam Scores
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [35, 40, 50, 55, 60, 65, 75, 80, 85, 95]

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train the Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Train the baseline model
baseline = DummyRegressor(strategy='mean')
baseline.fit(X_train, y_train)

# 5. Predict on test data
model_predictions = model.predict(X_test)
baseline_predictions = baseline.predict(X_test)

# 6. Calculate the evaluation metrices
model_mae = mean_absolute_error(y_test, model_predictions)
model_mse = mean_squared_error(y_test, model_predictions)
model_rmse = sqrt(model_mse)

baseline_mae = mean_absolute_error(y_test, baseline_predictions)
baseline_mse = mean_squared_error(y_test, baseline_predictions)
baseline_rmse = sqrt(baseline_mse)

# 7. Display the results
print("Training examples:", len(X_train))
print("Testing examples:", len(X_test))
print("Actual test scores:", y_test)

print("\nLinear Regression Results")
print("Predictions:", model_predictions)
print("MAE:", round(model_mae, 2))
print("MSE:", round(model_mse, 2))
print("RMSE:", round(model_rmse, 2))

print("\nBaseline Results")
print("Predictions:", baseline_predictions)
print("MAE:", round(baseline_mae, 2))
print("MSE:", round(baseline_mse, 2))
print("RMSE:", round(baseline_rmse, 2))