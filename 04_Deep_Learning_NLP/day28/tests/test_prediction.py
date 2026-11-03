import pytest
from prediction import predict_sentiment
from model_training import create_tfidf_features, train_sentiment_model

@pytest.fixture
def trained_components():
    reviews = [
        "this movie was excellent and amazing",
        "this film was wonderful and enjoyable",
        "this movie was terrible and boring",
        "this film was awful and disappointing",
    ]

    labels = ["positive", "positive", "negative", "negative"]

    vectorizer, X_train, _ = create_tfidf_features(reviews, reviews)

    model = train_sentiment_model(X_train, labels)

    return vectorizer, model

def test_predict_positive_sentiment(trained_components):
    vectorizer, model = trained_components

    sentiment, confidence = predict_sentiment(
        "this movie was excellent and amazing",
        vectorizer,
        model
    )

    assert sentiment == "positive"
    assert 0 <= confidence <= 1

def test_predict_negative_sentiment(trained_components):
    vectorizer, model = trained_components

    sentiment, confidence = predict_sentiment(
        "this movie was terrible and boring",
        vectorizer,
        model
    )

    assert sentiment == "negative"
    assert 0 <= confidence <= 1

def test_predict_empty_review(trained_components):
    vectorizer, model = trained_components

    with pytest.raises(ValueError, match="Review cannot be empty."):
        predict_sentiment("", vectorizer, model)