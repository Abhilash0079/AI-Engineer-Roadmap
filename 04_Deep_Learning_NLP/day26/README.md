# Day 26: Text Representation and Embeddings

## Objective
Understand how text is converted into numerical representations for machine-learning models.

## Environment
- Python 3.14.3
- scikit-learn 1.9.1
- NumPy 2.5.4

## Topics Covered
- Bag of Words (BoW)
- CountVectorizer
- Unigrams and Bigrams
- N-gram representation
- TF-IDF
- TfidfVectorizer
- Sparse and dense vectors
- Word embeddings fundamentals
- Word2Vec, GloVe, and FastText fundamentals
- Cosine similarity
- Data leakage prevention in text vectorization

## Implementation

The `text_representation.py` script demonstrates:

1. Creating a vocabulary and document-term matrix using CountVectorizer.
2. Generating unigram and bigram features.
3. Converting documents into TF-IDF representations.
4. Comparing BoW counts with TF-IDF weights.
5. Calculating document similarity using cosine similarity.
6. Splitting documents into training and testing sets.
7. Fitting the vectorizer only on training documents and transforming test documents.

## Key Results

| Technique | Output shape |
|---|---|
| Bag of Words | (3, 9) |
| Unigrams and Bigrams | (3, 17) |
| TF-IDF | (3, 9) |
| Training TF-IDF | (2, 6) |
| Testing TF-IDF | (1, 6) |

## Important Learnings

- BoW represents documents using word counts.
- TF-IDF assigns weights using term and inverse document frequency.
- N-grams capture combinations of consecutive words.
- Word embeddings represent words or text using dense numerical vectors.
- Cosine similarity measures the direction-based similarity between vectors.
- Vectorizers must be fitted on training data only to prevent data leakage.

## Run the Project

Activate the existing virtual environment and execute:

```powershell
python .\text_representation.py
```

## Project Structure

```text
day26/
    text_representation.py
    README.md
    INTERVIEW_NOTES.md
```

## Note
Word2Vec, GloVe, and FastText were studied conceptually in this project. The practical implementation focuses on BoW, N-grams, TF-IDF, and cosine similarity.
