# words frequencies

def word_usage(text_file_name):
    import re

    oText = open(text_file_name, 'r')
    rFile = oText.read()
    rFile = rFile.lower()

    get_words = re.findall(r'\w+', rFile)

    most_pop_100 = ['the', 'i', 'a', 'of', 'and', 'to', 'it', 'that', 'in', 'was', 's', 'as', 'he', 'you', 'my', 'his', 'is', 'for', 'what', 'up', 'manuel', 'lin', 'just', 'think', 'musical', 'me', 'like', 'writing', 'with', 'who', 'this', 'so', 'school', 're', 'from', 'time', 'm', 'hamilton', 'best', 'because', 'at', 'about', 'when', 'were', 'we', 'under', 'kid', 'island', 'hop', 'hip', 'him', 'do', 'all', 'writer', 'very', 'there', 'them', 'start', 'she', 'remember', 'pseudonym', 'parents', 'out', 'one', 'on', 'miranda', 'life', 'if', 'get', 'be', 'an', '11', 'would', 've', 'thought', 'things', 'they', 'than', 'starts', 'show', 'scared', 'people', 'part', 'old', 'not', 'myself', 'musicals', 'most', 'more', 'into', 'home', 'have', 'got', 'going', 'ever', 'early', 'discs', 'desert', 'could', 'but']
    
    word_frequency_list = []

    for word in most_pop_100:    
        count_words = get_words.count(word)
        word_frequency_list.append([count_words, word])

    # print(word_frequency_list)

    # sortedWFL = sorted(word_frequency_list)

    # sortedWFL.reverse()

    # word_frequency_text = sortedWFL
    # most_pop = [item[1] for item in word_frequency_text]
    # most_pop_100 = sortedWFL

    # print(most_pop_100)
    return word_frequency_list
    
# word_usage('text_2.txt')

def word_percent(text_file_name):
    import re

    oText = open(text_file_name, 'r')
    rFile = oText.read()
    rFile = rFile.lower()

    get_words = re.findall(r'\w+', rFile)

    most_pop_100 = ['the', 'i', 'a', 'of', 'and', 'to', 'it', 'that', 'in', 'was', 's', 'as', 'he', 'you', 'my', 'his', 'is', 'for', 'what', 'up', 'manuel', 'lin', 'just', 'think', 'musical', 'me', 'like', 'writing', 'with', 'who', 'this', 'so', 'school', 're', 'from', 'time', 'm', 'hamilton', 'best', 'because', 'at', 'about', 'when', 'were', 'we', 'under', 'kid', 'island', 'hop', 'hip', 'him', 'do', 'all', 'writer', 'very', 'there', 'them', 'start', 'she', 'remember', 'pseudonym', 'parents', 'out', 'one', 'on', 'miranda', 'life', 'if', 'get', 'be', 'an', '11', 'would', 've', 'thought', 'things', 'they', 'than', 'starts', 'show', 'scared', 'people', 'part', 'old', 'not', 'myself', 'musicals', 'most', 'more', 'into', 'home', 'have', 'got', 'going', 'ever', 'early', 'discs', 'desert', 'could', 'but']
    
    word_percent_list = []

    for word in most_pop_100:    
        count_words = get_words.count(word)
        word_percent_list.append([count_words/len(get_words)*100, word])

    # print(word_percent_list)

    return word_percent_list
    
# word_percent('today\'s_articles/text.txt')








