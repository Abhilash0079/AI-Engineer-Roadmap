from pathlib import Path
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "breast_cancer_pipeline.joblib"
REPORT_PATH = PROJECT_ROOT / "reports" / "model_evaluation.txt"

def train_and_save_model():
    # Load the dataset
    dataset = load_breast_cancer()
    X = dataset.data
    y = dataset.target

    # Split data before fitting preprocessing steps
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Keep preprocessing and classifier in one pipeline
    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=5000))
        ]
    )

    # Train the pipeline
    pipeline.fit(X_train, y_train)

    # Evaluate using held-out test data
    predictions = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(
        y_test, predictions,target_names=dataset.target_names, zero_division=0
    )

    # Save the fitted pipeline
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)

    # Save the evaluation report
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        f"Dataset: Breast Cancer Wisconsin\n"
        f"Training samples: {len(X_train)}\n"
        f"Test samples: {len(X_test)}\n"
        f"Test accuracy: {accuracy:.4f}\n\n"
        f"Classification report:\n{report}",
        encoding="utf-8",
    )

    print("Training completed successfully.")
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    print(f"Test accuracy: {accuracy:.4f}")
    print(f"Saved model: {MODEL_PATH}")
    print(f"Saved evaluation report: {REPORT_PATH}")

if __name__=="__main__":
    train_and_save_model()