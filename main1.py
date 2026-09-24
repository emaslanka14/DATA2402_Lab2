import string

def remove_stopwords(filename: str, stopwords: set) -> list:
    """
    Reads a textFile into a string and then removes 
    all the stopwords present in the given stopwords set in that string
    :param filename: The filename of the textfile
    :param stopwords: a set containting all of the strings you wish to remove
    :return: a list of strings without stopwords
    """
    try:
        with open(filename, "r") as f:
            text = f.read().lower()
    except FileNotFoundError:
        print(f"Error: file not found: {filename}")
        return []
    translator = str.maketrans('', '', string.punctuation)
    cleanedText = str(text).translate(translator)
    newList = cleanedText.strip().split()

    good_words = [w for w in newList if w not in stopwords and w != '']
    return good_words

def load_stopwords(filename: str) -> set:
    try:
        with open(filename, "r") as f:
            text = f.read().lower()
    except FileNotFoundError:
        print(f"Error: file not found: {filename}")
        return set()

    return set(text.split())


def get_term_freq(words: list) -> dict:
    occurrences = {}
    for w in words:
        if w in occurrences:
            occurrences[w] = occurrences[w] + 1
        else:
            occurrences[w] = 1

    frequency = {}
    total = sum(occurrences.values())
    for w in occurrences:
        frequency[w] = occurrences[w] / total
    return frequency
        

def main():
    stopwords = load_stopwords("stopwords.txt")   # returns a set

    words_a = remove_stopwords("textA.txt", stopwords)
    words_b = remove_stopwords("textB.txt", stopwords)         


    print(words_a)
    print(words_b)


    freq_A = get_term_freq(words_a)
    freq_B = get_term_freq(words_b)

    print(freq_A)
    print(freq_B)

    common = freq_A.keys() & freq_B.keys() 
    print(common)

    for w in common:
        freq_A.pop(w)
        freq_B.pop(w)

    print(list(freq_A.keys()))
    print(list(freq_B.keys()))


if __name__ == "__main__":
    main()
