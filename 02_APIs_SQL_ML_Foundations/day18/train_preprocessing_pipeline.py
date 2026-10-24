import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

data = {
    "Age": [25, 35, None, 45, 30, 40, 28, 50],
    "Salary": [30000, None, 60000, 50000, 45000, 70000, 35000, 80000],
    "City": ["Delhi", "Mumbai", "Delhi", None, "Mumbai", "Delhi", "Kolkata", "Mumbai"],
    "Purchased": [0, 1, 1, 0, 1, 1, 0, 1],
}

df = pd.DataFrame(data)

X = df.drop(columns=["Purchased"])
y = df["Purchased"]

numeric_features = ["Age", "Salary"]
categorical_features = ["City"]

numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ]
)

model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y,
)

model_pipeline.fit(X_train, y_train)
y_pred = model_pipeline.predict(X_test)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Actual labels:", y_test.tolist())
print("Predicted labels:", y_pred.tolist())
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nPipeline steps:")
print(model_pipeline.named_steps.keys())