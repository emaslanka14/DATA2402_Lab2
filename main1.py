def read_text(text: str, stopwords: set) -> list:
    new_list = text.strip().split()
    good_words = [w for w in new_list if w not in stopwords]
    return good_words

def load_stopwords(filename: str) -> set:
    with open(filename, "r") as f:
        text = f.read().lower()
    return set(text.split())

def get_term_freq(words: list) -> dict:
    occurrences = {}
    for w in words:
        if w in occurrences:
            occurrences[w] = occurrences[w] + 1
        else:
            occurrences[w] = 1
    print(occurrences)

    frequency = {}
    total = sum(occurrences.values())
    for w in occurrences:
        frequency[w] = occurrences[w] / total
    return frequency
        

def main():
    stopwords = load_stopwords("stopwords.txt")   # returns a set

    with open("textA.txt", "r") as f:
        text_a = f.read().lower()
    words_a = read_text(text_a, stopwords)         

    with open("textB.txt", "r") as f:
        text_b = f.read().lower()
    words_b = read_text(text_b, stopwords)

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


main()
