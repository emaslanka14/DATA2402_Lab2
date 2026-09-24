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
    translator = str.maketrans('', '', string.punctuation) #Thanks to https://www.geeksforgeeks.org/python/python-remove-punctuation-from-string/#google_vignette
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
        try:
            frequency[w] = occurrences[w] / total
        except ValueError:
            print(f"Value error for key: f{w}")
            frequency[w] = None


    return frequency

def remove_common_words(dictA: dict, dictB: dict) -> None:
    common = dictA.keys() & dictB.keys() 
    print(f'common words set: {common}')

    for w in common:
        dictA.pop(w)
        dictB.pop(w)
    return None

def word_freq_from_text_file(fileNameA:str, fileNameB:str=None) -> None:
    stopwords = load_stopwords("stopwords.txt")   # returns a set
    words_a = remove_stopwords(fileNameA, stopwords)
    freq_A = get_term_freq(words_a)

    if fileNameB: 
        words_b = remove_stopwords(fileNameB, stopwords)         
        freq_B = get_term_freq(words_b)

        remove_common_words(freq_A, freq_B)

    print_dict(freq_A)
    if fileNameB:
        print_dict(freq_B)

def print_dict(myDict: dict):
    for key, value in myDict.items():
        print(f"Word: {key} Frequency {value}")
    


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

    remove_common_words(freq_A, freq_B)

    print_dict(freq_A)
    print_dict(freq_B)


if __name__ == "__main__": #Only run this if we are running this file itself
    main()
