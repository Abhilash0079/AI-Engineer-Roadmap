import re
from nltk.tokenize import wordpunct_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

def normalize_text(text: str) -> str:
    """Normalize text by lowering and cleaning whitespace"""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def tokenize_text(text:str) -> list[str]:
    """Split normalized text into word and number tokens."""
    return re.findall(r"\b\w+\b", text)

def remove_stopwords(tokens: list[str]) -> list[str]:
    """Remove selected common words while preserving negation."""
    stopwords = {
        "the", "is", "are", "a", "an", "and", "of", "to"
    }
    return [token for token in tokens if token not in stopwords]

def stem_tokens(tokens: list[str]) -> list[str]:
    """Reduce tokens using the Porter stemming algorithm."""
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]


def lemmatize_tokens(tokens: list[str]) -> list[str]:
    """Reduce noun tokens to their dictionary forms."""
    lemmatizer = WordNetLemmatizer()
    return [
        lemmatizer.lemmatize(token, pos=wordnet.NOUN)
        for token in tokens
    ]


def preprocess_text(
    text: str,
    remove_common_words: bool = False,
) -> list[str]:
    """Normalize and tokenize text, optionally removing stop words."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    normalized_text = normalize_text(text)
    tokens = tokenize_text(normalized_text)

    if remove_common_words:
        tokens = remove_stopwords(tokens)

    return tokens


def main() -> None:
    text = " The QUICK foxes are runnning! NLP is FUN.   "
    normalized_text = normalize_text(text)
    # tokens = tokenize_text(normalized_text)

    # print("Original text:", repr(text))
    # print("Normalized text:", normalized_text)
    # print("Tokens:", tokens)
    # print("Number of tokens:", len(tokens))

    # regex_tokens = tokenize_text(normalized_text)
    # punctuation_tokens = wordpunct_tokenize(normalized_text)

    # sample_tokens = tokenize_text(
    #     normalize_text("The product is not good and the service is slow.")
    # )
    # filtered_tokens = remove_stopwords(sample_tokens)

    # print("Sample tokens:", sample_tokens)
    # print("After stop-word removal:", filtered_tokens)
    # print("Normalized text:", normalized_text)
    # print("Regex tokens:", regex_tokens)
    # print("Word-punctuation tokens:", punctuation_tokens)
    # word_forms = ["studies", "cars", "running", "better"]

    # print("Word forms:", word_forms)
    # print("Stems:", stem_tokens(word_forms))
    # print("Noun lemmas:", lemmatize_tokens(word_forms))
    print("Complete pipeline:", preprocess_text("The product is NOT good!"))
    print(
        "Pipeline without common words:",
        preprocess_text("The product is NOT good!", remove_common_words=True),
    )

    try:
        preprocess_text(123)
    except TypeError as error:
        print("Input validation:", error)

    # try:
    #     nltk_tokens = word_tokenize(normalized_text)
    #     print("NLTK word tokens:", nltk_tokens)
    # except LookupError as error:
    #     print("NLTK tokenizer resource is missing.")
    #     print(error)


if __name__=="__main__":
    main()