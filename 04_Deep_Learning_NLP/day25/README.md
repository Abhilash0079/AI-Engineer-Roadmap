# Day 25: NLP Fundamentals and Text Preprocessing

## Objective
Learn fundamental NLP preprocessing techniques and implement a reusable text preprocessing pipeline in Python.

## Environment
- Python 3.14.3
- NLTK 3.10.4
- scikit-learn 1.9.1
- PyTorch 2.14.1+cpu

## Features
- Text normalization: lowercase conversion and whitespace cleanup
- Regex-based tokenization
- NLTK word and punctuation tokenization
- Optional stop-word removal
- Negation preservation, including the word `not`
- Porter stemming
- WordNet noun lemmatization
- Input validation for non-string values
- Reusable preprocessing function

## Functions
- `normalize_text()`: normalizes case and whitespace.
- `tokenize_text()`: extracts word-like tokens using a regular expression.
- `remove_stopwords()`: removes selected common words while preserving negation.
- `stem_tokens()`: applies the Porter stemming algorithm.
- `lemmatize_tokens()`: lemmatizes tokens as nouns.
- `preprocess_text()`: combines normalization, tokenization, and optional stop-word removal.

## Important Notes
- Stemming can produce forms that are not dictionary words.
- Lemmatization depends on linguistic information, including part of speech.
- Stop-word removal is optional and depends on the task.
- Removing negation can change sentiment and meaning.
- The regex tokenizer is a basic educational implementation, not a universal tokenizer.
- NLTK's WordNet corpus is required for the lemmatization example.

## Run
From the repository's activated virtual environment:

```powershell
python .\text_preprocessing.py
```

## Key Learnings
This project demonstrates basic NLP preprocessing and how to combine small user-defined functions into a reusable pipeline.
