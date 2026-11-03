import joblib
from pathlib import Path

MODEL_DIR = Path("saved_models")

def save_model(model, vectorizer):
    """Save trained model and TF-IDF vectorizer."""

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_DIR / "sentiment_model.pkl")
    joblib.dump(vectorizer, MODEL_DIR / "tfidf_vectorizer.pkl")

    print("\nModel and vectorizer saved successfully!")

def load_model():
    """Load saved model and TF-IDF vectorizer."""

    model = joblib.load(MODEL_DIR / "sentiment_model.pkl")
    vectorizer = joblib.load(
        MODEL_DIR / "tfidf_vectorizer.pkl"
    )

    return model, vectorizer