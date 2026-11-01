from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

def main() -> None:
    documents = [
        "Python is easy to learn",
        "Python is powerful",
        "Machine Learning is interesting"
    ]

    # Creates the BoW vectorizer
    vectorizer = CountVectorizer()

    # Learns the vocabulary and converts documents into vectors. fit_transform() both learns the vocabulary and creates the document vectors.
    document_vectors = vectorizer.fit_transform(documents)

    # Returns the vocabulary
    feature_names = vectorizer.get_feature_names_out()

    print("Vocabulary:")
    print(feature_names)

    print("\nBag of Words Matrix:")
    print(document_vectors.toarray())

    print("\nDocument Shape:")
    print(document_vectors.shape)


    # Implement N-grams
    bigram_vectorizer = CountVectorizer(ngram_range=(1,2))

    """ngram_range=(1, 2) means:
        - Include individual words (unigrams).
        - Include two-word combinations (bigrams).
    """
    bigram_vectors = bigram_vectorizer.fit_transform(documents)

    print("\nUnigrams and Bigrams:")
    print(bigram_vectorizer.get_feature_names_out())

    print("\nUnigrams and Bigrams Matrix:")
    print(bigram_vectors.toarray())

    print("\nN-gram Matrix Shape:")
    print(bigram_vectors.shape)


    # Implementation of TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    print("\nTF-IDF Vocabulary:")
    print(tfidf_vectorizer.get_feature_names_out())

    print("\nTF-IDF Matrix:")
    print(tfidf_matrix.toarray())

    print("\nTF-IDF Matrix Shape:")
    print(tfidf_matrix.shape)

    # Compare BOW and TF-IDF
    print("\nBoW vs TF-IDF Comparison:")

    print("\nDocument 1:")
    print(documents[0])

    print("\nBoW Vector:")
    print(document_vectors.toarray()[0])

    print("\nTF-IDF Vector:")
    print(tfidf_matrix.toarray()[0])

    print("\nVocabulary Mapping:")

    for index, word in enumerate(feature_names):
        print(
            f"{word}: "
            f"BoW={document_vectors.toarray()[0][index]}, "
            f"TF-IDF={tfidf_matrix.toarray()[0][index]:.4f}"
        )
    

    # Implementing cosine similarity
    print("\nCosine Similarity using TF-IDF:")

    similarity_matrix = cosine_similarity(tfidf_matrix)

    print(similarity_matrix)

    print("\nDocument 1 vs Document 2:")
    print(similarity_matrix[0][1])

    print("\nDocument 1 vs Document 3:")
    print(similarity_matrix[0][2])

    # Implement Data Leakage
    print("\nData Leakage Prevention:")

    train_documents, test_documents = train_test_split(
        documents,
        test_size=0.33,
        random_state=42,
    )

    leakage_safe_vectorizer = TfidfVectorizer()

    train_vectors = leakage_safe_vectorizer.fit_transform(train_documents)
    test_vectors = leakage_safe_vectorizer.transform(test_documents)

    print("Training documents:", len(train_documents))
    print("Testing documents:", len(test_documents))

    print("Training matrix shape:", train_vectors.shape)
    print("Testing matrix shape:", test_vectors.shape)

    print(
        "Training vocabulary:",
        leakage_safe_vectorizer.get_feature_names_out(),
    )

if __name__=="__main__":
    main()