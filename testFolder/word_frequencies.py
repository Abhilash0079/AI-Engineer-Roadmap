def count_word_frequencies(sentence:str) -> dict[str, int]:
    words = sentence.split()

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word]+=1
        else:
            word_counts[word]=1

    return word_counts

sentence = "python is easy and python is powerful"
result = count_word_frequencies(sentence)
print(result)