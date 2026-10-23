from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

# Features: [hours studied, practice tests completed]
X = [
    [1, 0],
    [2, 0],
    [2, 1],
    [3, 1],
    [4, 1],
    [4, 2],
    [5, 2],
    [6, 3],
    [7, 3],
    [8, 4],
    [1, 1],
    [3, 2],
    [5, 3],
    [6, 2],
    [7, 4],
    [8, 3],
]

# Target: 0 = fail, 1 = pass
y = [
    0, 0, 0, 0, 1, 1, 1, 1,
    1, 1, 0, 0, 1, 1, 1, 1,
]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2, stratify=y
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Decision Tree Evaluation")
print("-"*30)
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Actual labels:", list(y_test))
print("Predicted labels:", list(y_pred))
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))