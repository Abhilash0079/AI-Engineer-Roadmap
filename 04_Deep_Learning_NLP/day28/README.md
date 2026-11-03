# Movie Review Sentiment Analysis

## Project Overview

This project is an NLP-based Movie Review Sentiment Analysis System that classifies movie reviews as **Positive** or **Negative**.

It uses TF-IDF for text feature extraction and Logistic Regression for sentiment classification.

The project also includes model persistence, reusable prediction functions, and automated testing with pytest.

## Dataset

- Dataset: IMDb Large Movie Review Dataset
- Total reviews: 50,000
- Training reviews: 25,000
- Testing reviews: 25,000
- Positive reviews: 25,000
- Negative reviews: 25,000

The dataset is organized into predefined training and testing folders, each containing positive and negative reviews.

Expected dataset structure:

```text
large_movie_review_dataset/
├── train/
│   ├── pos/
│   └── neg/
└── test/
    ├── pos/
    └── neg/
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Joblib
- Pytest

## Project Structure

```text
day28/
├── large_movie_review_dataset/
├── saved_models/
├── tests/
│   ├── test_text_preprocessing.py
│   ├── test_prediction.py
│   └── test_model_persistence.py
├── data_loader.py
├── data_analysis.py
├── text_preprocessing.py
├── model_training.py
├── model_evaluation.py
├── prediction.py
├── model_persistence.py
├── sentiment_analysis.py
├── run_prediction.py
├── README.md
└── INTERVIEW_NOTES.md
```

## Project Workflow

1. Load training and testing reviews.
2. Explore dataset structure, missing values, duplicates, and review lengths.
3. Clean text by converting it to lowercase and removing HTML tags and unnecessary characters.
4. Convert text into numerical features using TF-IDF.
5. Train a Logistic Regression classifier.
6. Evaluate the model using accuracy, precision, recall, F1-score, and a confusion matrix.
7. Save the trained model and vectorizer using Joblib.
8. Load saved artifacts to predict sentiment for new reviews.
9. Run automated tests using pytest.

## Model Configuration

**TF-IDF**
- Maximum features: 20,000
- N-gram range: (1, 2)
- Stop-word filtering: Disabled to preserve negation-related words.

**Logistic Regression**
- Maximum iterations: 1,000
- Random state: 42

## Model Performance

Evaluation on the 25,000-review test dataset:

| Metric | Result |
|---|---:|
| Accuracy | 89.52% |
| Negative precision | 0.90 |
| Negative recall | 0.89 |
| Negative F1-score | 0.89 |
| Positive precision | 0.89 |
| Positive recall | 0.90 |
| Positive F1-score | 0.90 |

Confusion matrix:

```text
[[11147  1353]
 [ 1268 11232]]
```

## Running the Project

Activate the project's virtual environment and navigate to the Day 28 directory.

### Train and evaluate the model

```powershell
python sentiment_analysis.py
```

This runs the training and evaluation workflow and saves the model artifacts.

### Predict sentiment for a new review

```powershell
python run_prediction.py
```

Enter a movie review when prompted. The application returns its predicted sentiment and confidence.

## Running Automated Tests

```powershell
python -m pytest tests -v
```

Current test coverage includes:
- Text preprocessing
- Invalid input validation
- Positive and negative predictions
- Model saving and loading

Current result: **10 tests passed**.

## Saved Model Artifacts

The trained artifacts are stored in:

```text
saved_models/
├── sentiment_model.pkl
└── tfidf_vectorizer.pkl
```

## Key Learning Outcomes

- Understanding NLP preprocessing.
- Converting text into numerical features using TF-IDF.
- Understanding unigrams and bigrams.
- Training a text classification model.
- Evaluating binary classification performance.
- Preserving negation during text processing.
- Saving and loading machine learning models.
- Building reusable prediction functions.
- Writing automated tests using pytest.

## Limitations

- Logistic Regression may not capture all contextual and semantic relationships in natural language.
- Confidence scores are model estimates, not guaranteed probabilities of correctness.
- Performance depends on the dataset and preprocessing configuration.
- The model is trained for binary positive/negative sentiment classification.

## Future Improvements

- Compare Logistic Regression with Naive Bayes and other classifiers.
- Experiment with alternative text representations.
- Perform hyperparameter tuning.
- Explore Transformer-based sentiment classification.

## Author

Abhilash Kumar

GitHub: https://github.com/Abhilash0079