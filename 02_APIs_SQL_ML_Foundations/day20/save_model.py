from pathlib import Path
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def train_and_save_model():
    # Load the dataset
    dataset = load_breast_cancer()
    X = dataset.data
    y = dataset.target

    # Split the data before fitting preprocessing steps
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.2, random_state = 42, stratify=y
    )

    # Keep preprocessing and model together
    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ('classifier', LogisticRegression(max_iter=5000))
        ]
    )

    # Train the complete Pipeline
    pipeline.fit(X_train, y_train)

    # Evaluate on the held-out test data
    test_accuracy = pipeline.score(X_test, y_test)

    # Create the model directory and save the fitted pipeline
    model_directory = Path("models")
    model_directory.mkdir(parents=True, exist_ok=True)
    model_path = model_directory / "breast_cancer_pipeline.joblib"
    joblib.dump(pipeline, model_path)

    print("Model training completed.")
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    print(f"Test accuracy: {test_accuracy:.4f}")
    print(f"Saved pipeline to: {model_path}")

if __name__ == '__main__':
    train_and_save_model()

