from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Features: [hours studied, practice tests completed]
X = [
    [1, 0], [2, 0], [2, 1], [3, 1],
    [4, 1], [4, 2], [5, 2], [6, 3],
    [7, 3], [8, 4], [1, 1], [3, 2],
    [5, 3], [6, 2], [7, 4], [8, 3],
]

# Target: 0 = fail, 1 = pass
y = [
    0, 0, 0, 0, 1, 1, 1, 1,
    1, 1, 0, 0, 1, 1, 1, 1,
]

# Use the same split for both models
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

models = {
    "Decision Tree": DecisionTreeClassifier(
        max_depth=3,
        random_state=42,
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        max_depth=3,
        random_state=42,
    ),
}

print("Model Comparison")
print("================")

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"\n{name}")
    print("-" * len(name))
    print("Actual labels:    ", list(y_test))
    print("Predicted labels: ", [int(value) for value in predictions])
    print("Accuracy:         ", round(accuracy * 100, 2), "%")
