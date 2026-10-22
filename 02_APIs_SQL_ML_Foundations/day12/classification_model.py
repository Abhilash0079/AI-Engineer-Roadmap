from sklearn.linear_model import LogisticRegression

# 1. Training Data: number of suspicious words
X = [[0], [1], [2], [3], [4], [5]]

# 2. Label: 0 = not spam, 1 = spam
y = [0, 0, 0, 1, 1, 1]

# 3. Create the classification model
model = LogisticRegression()

# 4. Train the model
model.fit(X, y)

# 5. Predict whether an email with 4 suspicious word is spam
prediction = model.predict([[4]])

print(f"Spam Prediction: {prediction[0]}")