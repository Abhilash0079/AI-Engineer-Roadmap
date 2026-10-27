# Day 25: NLP Interview Notes

## 1. What is Natural Language Processing (NLP)?
NLP is a field of AI that enables computers to process, analyze, and work with human language.

## 2. What is text normalization?
Text normalization converts text into a consistent format. Examples include lowercasing text and removing unnecessary whitespace.

## 3. What is tokenization?
Tokenization splits text into smaller units called tokens, such as words, subwords, or sentences.

## 4. What is the difference between stemming and lemmatization?
- **Stemming:** Applies rules to reduce a word to a stem, which may not be a dictionary word.
- **Lemmatization:** Uses linguistic information to return a valid base form. The result depends on the word's part of speech.

## 5. What are stop words?
Stop words are common words that may be excluded for some NLP tasks. Their removal is optional and depends on the task.

## 6. Why should we preserve negation?
Words such as "not" can reverse meaning. Removing "not" from "not good" can change the interpretation.

## 7. Why do we convert text into numbers?
Most traditional machine-learning algorithms require numerical features rather than raw text. Techniques such as Bag of Words, TF-IDF, and embeddings can create numerical representations.

## 8. Why compare tokenizers?
Different tokenizers handle punctuation, contractions, and word boundaries differently. The tokenizer should match the intended NLP task.

## 9. What is a reusable preprocessing pipeline?
It combines preprocessing operations into a function that can be called consistently across different inputs.

## 10. Why validate input types?
Type validation catches invalid inputs early and produces a clear error instead of allowing confusing failures later.

## 11. Does preprocessing always improve an NLP model?
No. Removing punctuation, stop words, or other information can harm some tasks. Preprocessing decisions should be based on the task and validated experimentally.

## 12. What is the difference between `print()` and `return`?
- `print()` displays information.
- `return` sends a result back to the caller so it can be reused by other code.
