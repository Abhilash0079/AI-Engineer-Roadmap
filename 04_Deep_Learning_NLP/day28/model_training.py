from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def create_tfidf_features(train_texts, test_texts):
    """Convert text reviews into TF-IDF numerical features."""

    vectorizer = TfidfVectorizer(
        max_features=20000,
        ngram_range=(1, 2)
    )

    X_train = vectorizer.fit_transform(train_texts)

    X_test = vectorizer.transform(test_texts)

    return vectorizer, X_train, X_test

def train_sentiment_model(X_train, y_train):
    """Train a Logistic Regression sntiment classifier."""
    model = LogisticRegression(
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model

