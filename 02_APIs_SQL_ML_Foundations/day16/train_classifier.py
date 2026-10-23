from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Features: number of suspicious words in each email
X = [[0], [1], [2], [3], [4], [5], [1], [2], [4], [5],
     [0], [3], [2], [4], [1], [5], [3], [0], [4], [2]]

# Labels: 0 = legitimate, 1 = spam
y = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1,
     0, 1, 0, 1, 0, 1, 1, 0, 1, 0]

# Split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train the classifier
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict labels for unseen test data
y_pred = model.predict(X_test)

# Evaluation predictions
print("Classification Model Evaluation")
print("-"*30)
print(f"Training Samples: {len(X_train)}")
print(f"Testing Samples: {len(X_test)}")
print(f"Actual Labels: {y_test}")
print(f"Predicted Labels: {y_pred}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=[0,1]))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print(f"Precision: {precision_score(y_test, y_pred, zero_division=0):.2%}")
print(f"Recall: {recall_score(y_test, y_pred, zero_division=0):.2%}")
print(f"F1-score: {f1_score(y_test, y_pred, zero_division=0):.2%}")
