
## Function that extracts the words from text and arranges them by frequency
# The function needs a text file as it's only input

def word_frequency(text_file_name):
    import re

    oText = open(text_file_name, 'r')
    rFile = oText.read()

    get_words = re.findall(r'\w+', rFile)

    set_words = set(get_words)

    list_words = list(set_words)

    word_frequency_list = []

    for word in list_words:    
        count_words = get_words.count(word)
        word_frequency_list.append([count_words, word])

    sortedWFL = sorted(word_frequency_list)

    sortedWFL.reverse()

    word_frequency_text = sortedWFL

    print(word_frequency_text)

# Call the function
word_frequency('text_file_name.txt')
