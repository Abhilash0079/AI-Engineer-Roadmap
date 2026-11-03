# Day 28 — Movie Review Sentiment Analysis: Interview Notes

## 1. Project Explanation

**Question: Explain your Movie Review Sentiment Analysis project.**

**Answer:**

I developed an NLP-based sentiment classification system using the IMDb Large Movie Review Dataset, containing 50,000 movie reviews.

I performed text preprocessing, converted reviews into numerical representations using TF-IDF, and trained a Logistic Regression classifier to predict whether a review was positive or negative.

I evaluated the model on 25,000 test reviews and achieved 89.52% accuracy. I also implemented model persistence using Joblib, reusable prediction functions, and automated tests using pytest.

## 2. NLP Fundamentals

### Q1. What is Natural Language Processing?

NLP is a branch of Artificial Intelligence that enables computers to process, understand, and analyze human language.

Examples:
- Sentiment analysis
- Text classification
- Machine translation
- Chatbots
- Text summarization

### Q2. What is sentiment analysis?

Sentiment analysis is an NLP task that identifies the opinion or emotional polarity expressed in text.

In this project, it is a binary classification problem:
- Positive
- Negative

### Q3. Why is text preprocessing important?

Raw text contains noise such as HTML tags, inconsistent capitalization, punctuation, and extra whitespace.

Preprocessing standardizes text and helps prepare it for feature extraction.

### Q4. What preprocessing did you perform?

I:
1. Converted text to lowercase.
2. Removed HTML tags.
3. Removed unnecessary special characters.
4. Normalized whitespace.
5. Preserved negation words such as "not".

## 3. TF-IDF

### Q5. What is TF-IDF?

TF-IDF stands for Term Frequency–Inverse Document Frequency.

It converts text into numerical features by considering how frequently a term appears in a document and how informative it is across the document collection.

### Q6. What is Term Frequency?

Term Frequency measures how frequently a term occurs in a document.

### Q7. What is Inverse Document Frequency?

Inverse Document Frequency reduces the importance of terms that occur in many documents and gives more weight to terms that are relatively uncommon.

### Q8. Why did you use TF-IDF?

Machine learning algorithms such as Logistic Regression require numerical input.

TF-IDF converts text reviews into numerical feature vectors that can be used for classification.

### Q9. What is a unigram?

A unigram is a single word.

Example: "movie"

### Q10. What is a bigram?

A bigram is a sequence of two consecutive words.

Example: "good movie"

### Q11. Why did you use ngram_range=(1, 2)?

It allows the vectorizer to capture both individual words and two-word phrases.

This can help identify sentiment expressions such as "not good".

### Q12. Why did you disable stop-word removal?

The built-in English stop-word list includes negation words such as "not".

Removing these words can change the meaning of sentiment expressions. I disabled stop-word filtering to preserve them.

### Q13. What is data leakage in TF-IDF?

Data leakage occurs when information from the test dataset influences training.

I used fit_transform() on training text and transform() on test text so that the vocabulary and IDF statistics were learned only from training data.

## 4. Logistic Regression

### Q14. Why did you use Logistic Regression?

Logistic Regression is a suitable baseline for binary text classification. It is computationally efficient and works well with high-dimensional sparse TF-IDF features.

### Q15. Is Logistic Regression a classification algorithm?

Yes. Despite its name, Logistic Regression is commonly used for classification tasks.

### Q16. What does max_iter=1000 mean?

It sets the maximum number of iterations allowed by the optimization algorithm to converge during training.

### Q17. What does random_state=42 do?

It provides reproducibility where the algorithm uses randomness. It does not mean every machine-learning algorithm requires a random state.

## 5. Model Evaluation

### Q18. What is accuracy?

Accuracy is the proportion of correctly classified observations among all observations.

Our test accuracy was 89.52%.

### Q19. What is precision?

Precision measures how many observations predicted as a particular class actually belong to that class.

### Q20. What is recall?

Recall measures how many actual observations of a class the model correctly identifies.

### Q21. What is the F1-score?

F1-score is the harmonic mean of precision and recall. It balances both metrics.

### Q22. What is a confusion matrix?

A confusion matrix compares actual labels with predicted labels.

Our matrix was:

```text
[[11147  1353]
 [ 1268 11232]]
```

Rows represent actual classes and columns represent predicted classes, in the order negative and positive.

- True negatives: 11,147
- False positives: 1,353
- False negatives: 1,268
- True positives: 11,232

### Q23. Why did you use a separate test dataset?

The test dataset helps measure how well the trained model performs on reviews that were not used to fit the model.

## 6. Model Persistence

### Q24. What is Joblib?

Joblib is a Python library commonly used to serialize and deserialize Python objects, including scikit-learn models.

### Q25. Why did you save the TF-IDF vectorizer?

The model expects features in the same representation used during training.

Saving the vectorizer ensures that new reviews are transformed using the original vocabulary and IDF weights.

### Q26. Why separate training and prediction?

Training can be computationally expensive. Loading saved artifacts allows the application to make predictions without retraining every time.

## 7. Python and Project Architecture

### Q27. Why did you divide the project into multiple modules?

Modular architecture separates responsibilities, improves readability, makes testing easier, and supports maintenance.

### Q28. What is the purpose of pytest?

Pytest is a Python testing framework used to write and execute automated tests.

### Q29. What is a pytest fixture?

A fixture prepares reusable objects or resources for tests. In this project, I used one to create a small trained model and vectorizer for prediction tests.

### Q30. Why did you use exception handling for invalid reviews?

Input validation prevents invalid data from reaching the model and produces clear errors for callers.

## 8. Project Results

| Item | Result |
|---|---:|
| Total reviews | 50,000 |
| Training reviews | 25,000 |
| Testing reviews | 25,000 |
| TF-IDF maximum features | 20,000 |
| N-gram range | (1, 2) |
| Classifier | Logistic Regression |
| Test accuracy | 89.52% |
| Automated tests | 10 passed |

## 9. Possible Follow-up Interview Questions

1. What are the limitations of TF-IDF?
2. How does Logistic Regression calculate class probabilities?
3. What is the difference between stemming and lemmatization?
4. What is the difference between CountVectorizer and TfidfVectorizer?
5. How would you improve the model's accuracy?
6. How would you deploy this model using FastAPI?
7. How would you monitor model performance after deployment?
8. Why might accuracy be misleading on an imbalanced dataset?
9. What is cross-validation?
10. How would you compare TF-IDF with Transformer embeddings?

## 10. Important Project Talking Points

- Used a predefined train/test split.
- Avoided fitting TF-IDF on test data.
- Preserved negation by disabling built-in English stop-word filtering.
- Evaluated with multiple classification metrics.
- Saved both model and vectorizer.
- Created a separate prediction entry point.
- Added automated tests for preprocessing, prediction, and persistence.

**Note:** The reported 89.52% is the result from this project's current test run. It is not a guarantee of performance on other datasets.