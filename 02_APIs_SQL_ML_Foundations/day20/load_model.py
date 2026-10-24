
from pathlib import Path

import joblib
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def verify_saved_model():
    model_path = Path("models") / "breast_cancer_pipeline.joblib"

    # Load the saved pipeline
    loaded_pipeline = joblib.load(model_path)

    # Recreate the same data split
    dataset = load_breast_cancer()
    X = dataset.data
    y = dataset.target

    _, X_test, _, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # Recreate and train a reference pipeline for comparison
    reference_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=5000)),
        ]
    )

    X_train, _, y_train, _ = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )
    reference_pipeline.fit(X_train, y_train)

    # Compare predictions on the full test set
    saved_predictions = loaded_pipeline.predict(X_test)
    reference_predictions = reference_pipeline.predict(X_test)

    predictions_match = np.array_equal(
        saved_predictions,
        reference_predictions,
    )
    test_accuracy = loaded_pipeline.score(X_test, y_test)

    print("Saved pipeline loaded successfully.")
    print("Total test samples:", len(X_test))
    print("Saved pipeline test accuracy:", round(test_accuracy, 4))
    print("Predictions match reference pipeline:", predictions_match)
    print("All predictions identical:", predictions_match)


if __name__ == "__main__":
    verify_saved_model()
