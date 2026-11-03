import matplotlib.pyplot as plt
import seaborn as sns

def explore_dataset(df, dataset_name):
    """Perform basic exploratory data analysis."""

    print(f"\n{'=' * 45}")
    print(f"{dataset_name} DATASET")
    print(f"{'=' * 45}")

    print("\nDataset Information:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nSentiment distribution:")
    print(df['sentiment'].value_counts())

def analyze_duplicates(df, dataset_name):
    """Analyze duplicate reviews and their sentiment labels."""

    print(f"\nDuplicate analysis: {dataset_name}")

    duplicate_reviews = df[df.duplicated(subset=["review"], keep=False)]

    print("Rows involved in duplicate reviews:",len(duplicate_reviews))

    conflicting_reviews = (duplicate_reviews.groupby("review")["sentiment"].nunique())
    conflicting_reviews = conflicting_reviews[conflicting_reviews > 1]

    print("Reviews with conflicting sentiment labels:",len(conflicting_reviews))

def analyze_review_lengths(df, dataset_name):
    """Analyze the word count of the movie reviews."""
    df = df.copy()
    df['word_count'] = df['review'].str.split().str.len()
    print(f"\nReview Length Analysis: {dataset_name}")

    print("\nOverall review length statistics:")
    print(df["word_count"].describe())

    print("\nReview length by sentiment:")
    print(df.groupby("sentiment")["word_count"].agg(["mean", "median", "min", "max"]))

def visualize_review_lengths(df):
    """Visualize movie review length distribution."""

    df = df.copy()
    df["word_count"] = df["review"].str.split().str.len()

    # Histogram
    plt.figure(figsize=(10, 5))

    sns.histplot(
        data=df,
        x="word_count",
        hue="sentiment",
        bins=50,
        kde=True
    )

    plt.title("Movie Review Length Distribution")
    plt.xlabel("Number of Words")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    plt.show()

    # Boxplot
    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="sentiment",
        y="word_count"
    )

    plt.title("Review Length by Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Words")
    plt.tight_layout()
    plt.show()

