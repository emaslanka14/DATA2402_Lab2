def load_stopwords(filename):
    stopwords = set()

    file = open(filename, "r")

    for line in file:
        word = line.strip()
        stopwords.add(word)

    file.close()

    return stopwords


def load_words(filename, stopwords):
    words = []

    file = open(filename, "r")

    for line in file:
        line = line.lower()
        line = line.strip()

        line_words = line.split()

        for word in line_words:
            if word not in stopwords:
                words.append(word)

    file.close()

    return words


def count_words(words):
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1

    return word_counts


def calculate_tf(word_counts, total_words):
    tf = {}

    for word in word_counts:
        tf[word] = word_counts[word] / total_words

    return tf


# Main program

stopwords = load_stopwords("kai_Lab2/test/stopwords4T1.txt")

words1 = load_words("kai_Lab2/test/textA4T1.txt", stopwords)
words2 = load_words("kai_Lab2/test/textB4T1.txt", stopwords)

print("Remaining words in text A:")
print(words1)

print("\nRemaining words in text B:")
print(words2)


# Count words

counts1 = count_words(words1)
counts2 = count_words(words2)

print("\nWord counts for text A:")
print(counts1)

print("\nWord counts for text B:")
print(counts2)


# Calculate term frequencies

tf1 = calculate_tf(counts1, len(words1))
tf2 = calculate_tf(counts2, len(words2))

print("\nTerm frequencies for text A:")
print(tf1)

print("\nTerm frequencies for text B:")
print(tf2)


# Find common words

common_words = set(counts1.keys()) & set(counts2.keys())

print("\nWords common to both documents:")
print(common_words)


# Remove common words

for word in common_words:
    del tf1[word]

for word in common_words:
    del tf2[word]


print("\nUnique words in text A:")
print(tf1)

print("\nUnique words in text B:")
print(tf2)
