def predict_sentiment(review, vectorizer, model):
    """Predict sentiment for a new movie review."""

    from text_preprocessing import preprocess_text

    cleaned_review = preprocess_text(review)
    review_features = vectorizer.transform([cleaned_review])

    prediction = model.predict(review_features)[0]
    probability = model.predict_proba(review_features)[0]

    class_probabilities = dict(zip(model.classes_, probability))

    confidence = class_probabilities[prediction]

    return prediction, confidence
