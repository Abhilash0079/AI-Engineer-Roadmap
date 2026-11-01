from transformers import pipeline

def create_sentiment_classifier():
    """Create a pretrained sentiment-analysis classifier"""
    classifier = pipeline(
        task="sentiment-analysis",
        model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        device = -1
    )

    return classifier

def predict_sentiment(classifier, text):
    """Predict the sentiment of the supplied text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    if not text.strip():
        raise ValueError("Input text cannot be empty.")

    result = classifier(text)
    return result[0]

def test_input_validation(classifier):
    """Test sentiment prediction input validation."""

    test_inputs = [
        "",
        "   ",
        123
    ]

    for text in test_inputs:
        try:
            predict_sentiment(classifier, text)

        except (TypeError, ValueError) as error:
            print(f"Input: {repr(text)}")
            print(f"Exception: {type(error).__name__}")
            print(f"Message: {error}")
            print("-" * 40)

def main():
    classifier = create_sentiment_classifier()

    test_sentences = [
        "I love learning Python and machine learning.",
        "This product is absolutely amazing.",
        "I am very disappointed with this service.",
        "The movie was terrible and boring.",
        "The experience was wonderful and enjoyable."
    ]

    for text in test_sentences:
        prediction = predict_sentiment(classifier, text)

        print("\nInput text:", text)
        print("Predicted sentiment:", prediction["label"])
        print("Confidence score:", round(prediction["score"], 4))

    print("\nTesting input validation:")
    test_input_validation(classifier)

if __name__=='__main__':
    main()