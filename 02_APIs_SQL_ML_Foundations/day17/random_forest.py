from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
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
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42,
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Random Forest Evaluation")
print("------------------------")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Actual labels:", list(y_test))
print("Predicted labels:", [int(value) for value in y_pred])
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nFeature Importance")
print("------------------")
print("Hours studied:", round(float(model.feature_importances_[0]), 4))
print("Practice tests completed:", round(float(model.feature_importances_[1]), 4))
