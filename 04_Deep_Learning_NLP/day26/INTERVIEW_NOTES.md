# Day 26: Text Representation and Embeddings — Interview Notes

## 1. Why Do We Need Text Representation?

Machine-learning algorithms generally work with numerical data. Text must therefore be converted into numerical features before it can be used by most traditional ML models.

Text representation converts words, sentences, or documents into numerical vectors.

## 2. Bag of Words (BoW)

Bag of Words represents a document using the frequency of words in a vocabulary.

### Important points
- Each unique word becomes a feature.
- Each document becomes a numerical vector.
- Word order is ignored.
- The resulting matrix is usually sparse.

### CountVectorizer

`CountVectorizer` from scikit-learn creates a vocabulary and converts text into word-count vectors.

```python
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "Python is easy to learn",
    "Python is powerful"
]

vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(matrix.toarray())
```

## 3. N-grams

N-grams are consecutive sequences of words.

- Unigram: one word, such as `machine`.
- Bigram: two consecutive words, such as `machine learning`.
- Trigram: three consecutive words, such as `machine learning model`.

In scikit-learn:

```python
CountVectorizer(ngram_range=(1, 2))
```

This generates both unigrams and bigrams.

N-grams preserve some local word-order information that ordinary BoW ignores.

## 4. TF-IDF

TF-IDF stands for Term Frequency–Inverse Document Frequency.

It gives greater importance to terms that are frequent in a particular document but less common across the document collection.

- **Term Frequency (TF):** Measures how often a term appears in a document.
- **Inverse Document Frequency (IDF):** Reduces the importance of terms appearing in many documents.

`TfidfVectorizer` converts text into TF-IDF feature vectors.

Unlike raw word counts, TF-IDF weights reflect how informative a term is within the collection.

## 5. Sparse and Dense Vectors

### Sparse vector
A vector in which most values are zero.

BoW and TF-IDF commonly produce sparse representations because each document contains only a small portion of the complete vocabulary.

### Dense vector
A vector in which most or all dimensions contain numerical values.

Word embeddings generally use dense vectors to represent semantic information.

## 6. Word Embeddings

Word embeddings represent words as dense numerical vectors. They can capture relationships and similarities between words based on their usage and context.

### Common embedding techniques

- **Word2Vec:** Learns word vectors from surrounding-word context. Common approaches include CBOW and Skip-gram.
- **GloVe:** Learns word vectors using global word co-occurrence statistics.
- **FastText:** Represents words using character n-grams, helping it handle word structure and some unseen words.

These techniques were covered conceptually in Day 26; they were not implemented in the practical script.

## 7. Cosine Similarity

Cosine similarity measures the similarity between two vectors by comparing the angle between them.

- A value near 1 indicates similar directions.
- A value near 0 indicates little directional similarity.
- A value near -1 indicates opposite directions.

For ordinary non-negative BoW and TF-IDF vectors, values are generally between 0 and 1.

It is useful for comparing documents, search results, and text representations.

## 8. Data Leakage in Text Vectorization

Data leakage occurs when information from test data influences model training.

Incorrect approach:

```python
vectorizer.fit_transform(all_documents)
```

This learns the vocabulary and statistics using both training and test documents before evaluation.

Correct approach:

```python
X_train = vectorizer.fit_transform(train_documents)
X_test = vectorizer.transform(test_documents)
```

- `fit()` learns the vocabulary or statistics.
- `transform()` applies the learned representation.
- `fit_transform()` learns and transforms the supplied data.

The vectorizer must be fitted on training data only. Test data must use the already-fitted vectorizer.

## 9. Common Interview Questions

**Q1. What is Bag of Words?**  
BoW represents text using word frequencies from a vocabulary. It ignores word order.

**Q2. What is the limitation of Bag of Words?**  
It does not capture semantic meaning and generally ignores word order.

**Q3. What is TF-IDF?**  
TF-IDF weights terms based on their frequency in a document and their rarity across the document collection.

**Q4. What is an N-gram?**  
An N-gram is a sequence of N consecutive tokens.

**Q5. What is the difference between sparse and dense vectors?**  
Sparse vectors contain mostly zeros, while dense vectors have values in most or all dimensions.

**Q6. What are Word2Vec, GloVe, and FastText?**  
They are word-embedding techniques that learn dense numerical representations of words using different approaches.

**Q7. What is cosine similarity?**  
It measures the directional similarity between two vectors.

**Q8. Why should a vectorizer be fitted only on training data?**  
To prevent test-data information from leaking into the training process and producing an overly optimistic evaluation.

**Q9. What is the difference between `fit_transform()` and `transform()`?**  
`fit_transform()` learns from data and transforms it. `transform()` applies previously learned information to new data.

## 10. Practical File

The `text_representation.py` script demonstrates:

- Bag of Words with CountVectorizer
- Unigram and bigram features
- TF-IDF with TfidfVectorizer
- BoW and TF-IDF comparison
- Cosine similarity
- Train/test splitting
- Correct vectorizer fitting to prevent data leakage

**Note:** Word2Vec, GloVe, and FastText are conceptual topics in this project, not implemented features.