from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 1. Sample Data: Hours studied and exam scores
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [35, 40, 50, 55, 60, 65, 75, 80, 85, 95]

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the actual regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Train a baseline model
baseline = DummyRegressor(strategy='mean')
baseline.fit(X_train, y_train)

# 5. Generate predictions on unseen test data
model_predictions = model.predict(X_test)
baseline_predictions = baseline.predict(X_test)

# 6. Evaluate both models using mean absolute error
model_mae = mean_absolute_error(y_test, model_predictions)
baseline_mae = mean_absolute_error(y_test, baseline_predictions)

print("Training examples:", len(X_train))
print("Testing examples:", len(X_test))
print("Actual test scores:", y_test)
print("Model predictions:", model_predictions)
print("Baseline predictions:", baseline_predictions)
print("Model MAE:", round(model_mae, 2))
print("Baseline MAE:", round(baseline_mae, 2))

# 7. Demonstrate data leakage in a baseline

# Correct: use training labels only
correct_baseline_value = sum(y_train) / len(y_train)

# Incorrect: uses test labels to calculate the prediction
leaky_baseline_value = sum(y) / len(y)

print("\nCorrect baseline value:", round(correct_baseline_value, 2))
print("Leaky baseline value:", round(leaky_baseline_value, 2))
print("Training mean uses training labels only:", correct_baseline_value)
print("Leaky mean includes test labels:", leaky_baseline_value)