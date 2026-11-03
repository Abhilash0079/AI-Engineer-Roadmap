from pathlib import Path
import pandas as pd

DATASET_DIR = Path("large_movie_review_dataset")

def load_reviews_from_folder(folder_path, sentiment):
    """Load movie reviews from a sentiment folder."""

    reviews = []

    for file_path in folder_path.glob("*.txt"):
        review_text = file_path.read_text(encoding="utf-8")

        reviews.append({
            "review": review_text,
            "sentiment": sentiment
        })

    return reviews

def load_dataset(split):
    """Load positive and negative reviews for a dataset split."""

    split_path = DATASET_DIR / split

    positive_reviews = load_reviews_from_folder(
        split_path / "pos",
        "positive"
    )

    negative_reviews = load_reviews_from_folder(
        split_path / "neg",
        "negative"
    )

    all_reviews = positive_reviews + negative_reviews

    return pd.DataFrame(all_reviews)
