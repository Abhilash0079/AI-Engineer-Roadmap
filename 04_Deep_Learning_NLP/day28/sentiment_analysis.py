from data_loader import load_dataset
from data_analysis import (
    explore_dataset, 
    analyze_duplicates, 
    analyze_review_lengths, 
    visualize_review_lengths
)
from text_preprocessing import preprocess_text, preprocess_dataset
from model_training import create_tfidf_features, train_sentiment_model
from model_evaluation import evaluate_model
from prediction import predict_sentiment
from model_persistent import save_model, load_model


def main():

    # ==========================================
    # STEP 1: LOAD TRAINING AND TESTING DATASETS
    # ==========================================

    train_df = load_dataset("train")
    test_df = load_dataset("test")

    print("\nTraining Dataset Shape:", train_df.shape)
    print("Testing Dataset Shape:", test_df.shape)

    # ==========================================
    # STEP 2: EXPLORE DATASETS
    # ==========================================

    explore_dataset(train_df, "Training")
    explore_dataset(test_df, "Testing")

    # ==========================================
    # STEP 3: ANALYZE DUPLICATES
    # ==========================================

    analyze_duplicates(train_df, "Training")
    analyze_duplicates(test_df, "Testing")

    # ==========================================
    # STEP 4: ANALYZE REVIEW LENGTHS
    # ==========================================

    analyze_review_lengths(train_df, "Training")
    analyze_review_lengths(test_df, "Testing")

    # ==========================================
    # STEP 5: VISUALIZE REVIEW LENGTHS
    # ==========================================

    visualize_review_lengths(train_df)

    # ==========================================
    # STEP 6: TEST TEXT PREPROCESSING
    # ==========================================

    sample_review = """
    THIS MOVIE was AMAZING!!! <br /><br />
    I really enjoyed it. The acting was great.
    I would NOT call it boring.
    """

    cleaned_review = preprocess_text(sample_review)

    print("\nOriginal Review:")
    print(sample_review)

    print("\nCleaned Review:")
    print(cleaned_review)

    # ==========================================
    # STEP 7: TEST INPUT VALIDATION
    # ==========================================

    try:
        preprocess_text("")
    except ValueError as error:
        print("\nEmpty Input Validation:", error)

    try:
        preprocess_text(123)
    except TypeError as error:
        print("\nNon-String Input Validation:", error)

    # ==========================================
    # STEP 8: PREPROCESS COMPLETE DATASETS
    # ==========================================

    train_df = preprocess_dataset(train_df)
    test_df = preprocess_dataset(test_df)

    print("\nPreprocessed Training Dataset:")
    print(train_df[["review", "cleaned_review"]].head())

    print("\nPreprocessed Testing Dataset:")
    print(test_df[["review", "cleaned_review"]].head())

    # ==========================================
    # STEP 9: VERIFY PREPROCESSED DATASETS
    # ==========================================

    print("\nPreprocessed Training Dataset Shape:")
    print(train_df.shape)

    print("\nPreprocessed Testing Dataset Shape:")
    print(test_df.shape)
    print("\nMissing Cleaned Reviews:")
    print("Training:",train_df["cleaned_review"].isnull().sum())
    print("Testing:",test_df["cleaned_review"].isnull().sum())

    # ==========================================
    # STEP 10: TF-IDF FEATURE EXTRACTION
    # ==========================================

    vectorizer, X_train, X_test = create_tfidf_features(
        train_df["cleaned_review"],
        test_df["cleaned_review"]
    )

    print("\nTF-IDF Feature Extraction Results:")

    print("Training Feature Shape:", X_train.shape)
    print("Testing Feature Shape:", X_test.shape)

    print("Vocabulary Size:", len(vectorizer.vocabulary_))

    print("\nSample Vocabulary:")
    print(list(vectorizer.vocabulary_.keys())[:20])

    # ==========================================
    # STEP 11: TRAIN LOGISTIC REGRESSION MODEL
    # ==========================================

    model = train_sentiment_model(
        X_train,
        train_df['sentiment']
    )

    print("\nModel Training Completed Successfully!")
    print("Model:", model)


    # ==========================================
    # STEP 12: EVALUATE THE MODEL
    # ==========================================

    y_pred = evaluate_model(
        model,
        X_test,
        test_df['sentiment']
    )

    # ==========================================
    # STEP 13: PREDICT NEW MOVIE REVIEWS
    # ==========================================

    sample_reviews = [
        "This movie was absolutely fantastic. I loved every moment!",
        "This movie was terrible. The story was boring and acting was poor."
    ]

    print("\nNew Movie Review Predictions:")
    print("="*40)

    for review in sample_reviews:
        sentiment, confidence = predict_sentiment(
            review,
            vectorizer,
            model
        )

        print("\nReview:", review)
        print("Predicted Sentiment:", sentiment.upper())
        print(f"Confidence: {confidence:.2%}")

    # ==========================================
    # STEP 14: SAVE TRAINED MODEL
    # ==========================================

    save_model(model, vectorizer)

    # ==========================================
    # STEP 15: LOAD SAVED MODEL
    # ==========================================

    loaded_model, loaded_vectorizer = load_model()

    print("\nSaved Model Loaded Successfully!")
    print("Loaded Model:", loaded_model)

    test_review = "The movie was wonderful and the performances were excellent."

    sentiment, confidence = predict_sentiment(
        test_review,
        loaded_vectorizer,
        loaded_model
    )

    print("\nLoaded Model Prediction:")
    print("Review:", test_review)
    print("Predicted Sentiment:", sentiment.upper())
    print(f"Confidence: {confidence:.2%}")


if __name__ == "__main__":
    main()
