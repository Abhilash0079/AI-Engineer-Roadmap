import pytest

from model_persistence import save_model, load_model
from model_training import create_tfidf_features, train_sentiment_model

@pytest.fixture
def trained_components():
    reviews = [
        "excellent amazing wonderful movie",
        "great enjoyable fantastic film",
        "terrible boring awful movie",
        "bad disappointing horrible film",
    ]

    labels = ["positive", "positive", "negative", "negative"]

    vectorizer, X_train, _ = create_tfidf_features(reviews, reviews)
    model = train_sentiment_model(X_train, labels)

    return vectorizer, model


def test_save_and_load_model(trained_components, tmp_path, monkeypatch):
    vectorizer, model = trained_components

    monkeypatch.setattr(
        "model_persistence.MODEL_DIR",
        tmp_path
    )

    save_model(model, vectorizer)

    loaded_model, loaded_vectorizer = load_model()

    assert loaded_model is not None
    assert loaded_vectorizer is not None

    assert loaded_model.predict(
        loaded_vectorizer.transform(["excellent amazing movie"])
    )[0] == "positive"