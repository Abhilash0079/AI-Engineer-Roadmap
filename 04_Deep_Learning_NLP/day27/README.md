# Day 27: NLP Modeling and Transformer Fundamentals

## Project Overview

This project demonstrates sentiment analysis using a pretrained Transformer model from Hugging Face.

The model classifies text into two sentiment categories:

- **POSITIVE**
- **NEGATIVE**

The project uses the DistilBERT model fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset.

## Learning Objectives

- Understand text classification.
- Understand RNNs and Transformers.
- Learn the fundamentals of attention and self-attention.
- Understand Query, Key, and Value (Q, K, V).
- Understand pretrained models and transfer learning.
- Perform sentiment analysis using a pretrained model.
- Implement input validation and prediction functions.

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- DistilBERT
- VS Code

## Project Structure

```text
day27/
│
├── sentiment_analysis.py
├── README.md
└── INTERVIEW_NOTES.md
```

## Model Information

**Model:** `distilbert/distilbert-base-uncased-finetuned-sst-2-english`

This is a pretrained DistilBERT model fine-tuned for binary sentiment classification.

The model returns:
- A sentiment label.
- A confidence score reported by the model.

Note: The confidence score should not automatically be interpreted as a calibrated probability of correctness.

## Implementation

The Python script contains three main functions:

### 1. `create_sentiment_classifier()`

Creates a sentiment-analysis pipeline using the pretrained DistilBERT model.

### 2. `predict_sentiment(classifier, text)`

- Validates the input type.
- Rejects empty or whitespace-only text.
- Returns the predicted sentiment and score.

### 3. `test_input_validation(classifier)`

Tests invalid inputs and verifies the expected exceptions.

## How to Run

Activate the project's virtual environment and navigate to the Day 27 folder.

Install the dependencies if they are not already installed:

```powershell
python -m pip install torch transformers accelerate
```

Run the script:

```powershell
python sentiment_analysis.py
```

Compile-check the script:

```powershell
python -m py_compile sentiment_analysis.py
```

The pretrained model is downloaded from Hugging Face when needed. An internet connection is required for the initial download.

## Sample Results

| Input | Predicted sentiment |
|---|---|
| I love learning Python and machine learning. | POSITIVE |
| This product is absolutely amazing. | POSITIVE |
| I am very disappointed with this service. | NEGATIVE |
| The movie was terrible and boring. | NEGATIVE |
| The experience was wonderful and enjoyable. | POSITIVE |

All five sample predictions produced the expected sentiment labels.

## Input Validation Results

| Input | Expected exception | Result |
|---|---|---|
| Empty string | ValueError | Passed |
| Whitespace-only string | ValueError | Passed |
| Integer input | TypeError | Passed |

## Hardware

The project was executed using CPU-based inference.

CUDA was unavailable in the current environment, but the model ran successfully on CPU.

## Important Note

This project uses a pretrained model for inference. It does not implement model fine-tuning or training from scratch.

## Key Takeaway

This project demonstrates how to integrate a pretrained Transformer model into a Python application and use it for practical NLP inference with input validation.