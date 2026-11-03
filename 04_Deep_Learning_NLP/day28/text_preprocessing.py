import re

def preprocess_text(text):
    """Clean movie review text."""

    if not isinstance(text, str):
        raise TypeError("Review must be a string.")

    if not text.strip():
        raise ValueError("Review cannot be empty.")
    
    # Convert text to lowercase
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r"<br\s*/?>", " ", text)

    # Remove remaining HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove punctuation and special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text

def preprocess_dataset(df):
    """Apply text preprocessing to all reviews."""

    df = df.copy()
    df['cleaned_review'] = df['review'].apply(preprocess_text)

    return df
