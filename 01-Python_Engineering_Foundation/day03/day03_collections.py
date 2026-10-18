sentence = "python is easy and python is powerful"
words = sentence.split()

# print(words)
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word]+=1
    else:
        word_counts[word] = 1

print(word_counts)