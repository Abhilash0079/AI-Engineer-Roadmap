from sklearn.linear_model import LinearRegression

# 1. Training Data: Hours studied and Exam score
X = [[1], [2], [3], [4], [5]]
y = [40, 50, 60, 70, 80]

# 2. Create the model
model = LinearRegression()

# 3. Train the model
model.fit(X, y)

# 4. Predict the score for a student who studies 6 hours
prediction = model.predict([[6]])
print(f"Predicted Exam Score: {prediction}")