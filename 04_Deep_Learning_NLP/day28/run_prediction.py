from model_persistent import load_model
from prediction import predict_sentiment

def main():
    """Run sentiment prediction using the saved model."""

    model, vectorizer = load_model()
    print("Sentiment Prediction System")
    print("="*40)

    review = input("\nEnter a movie review: ")
    sentiment, confidence = predict_sentiment(
        review,
        vectorizer,
        model
    )

    print("\nPrediction Result")
    print("=" * 40)
    print("Sentiment:", sentiment.upper())
    print(f"Confidence: {confidence:.2%}")

if __name__=='__main__':
    main()