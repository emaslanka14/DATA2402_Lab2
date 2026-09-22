def read_text(text: str, stopwords: set) -> list:
    new_list = text.strip().split()
    good_words = [w for w in new_list if w not in stopwords]
    return good_words

def load_stopwords(filename: str) -> set:
    with open(filename, "r") as f:
        text = f.read().lower()
    return set(text.split())

def get_occurrences(words: list) -> dict:
    occurrences = {}
    for w in words:
        if w in occurrences:
            occurrences[w] = occurrences[w] + 1
        else:
            occurrences[w] = 1
    return occurrences

def term_freq(occurrences: dict) -> dict:
    frequency = {}
    for w in occurrences:
        frequency[w] = occurrences[w] / sum(occurrences.values())
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

    occurrences_A = get_occurrences(words_a)
    occurrences_B = get_occurrences(words_b)

    print(occurrences_A)
    print(occurrences_B)

    freq_A = term_freq(occurrences_A)
    freq_B = term_freq(occurrences_B)

    print(freq_A)
    print(freq_B)


    
    

    


main()
