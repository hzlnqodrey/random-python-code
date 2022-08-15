txt = "Here are man%y examp@les of short stories for you to read online. Online has become another leg in our life. WE have to take that into account so that we will go along the growth of the science and technology. Computer has revolutionalised our world. The people have started to see another world. What we were has become history. The twentieth century has become remote@ history. The IT companies and other computer-based companies have outperformed other traditional companies which have been there for a long time. Accuracy has become the most used word among the people. Telecommunication has become very very cheap affair all over the world. All these achievements are possible because of Computer and the Internet. Reading short stories online has become our favorite pastime."

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


def cleaning_punc(txt, punctuations):
    for character in punctuations:
        txt = txt.replace(character, '')
    return txt


def cleaning_uninteresting_words(txt, uninteresting_words):
    txt_list = txt.split()
    for word in uninteresting_words:
        if word in txt_list:
            txt_list.remove(word)
    clean_txt = " ".join(txt_list)
    return clean_txt


# Remove Punc
txt = cleaning_punc(txt, punctuations)
# Cleaning uninteresting_words
clean_txt = cleaning_uninteresting_words(txt, uninteresting_words)
# Characters lowered
txt = clean_txt.lower()


def counting_word(txt):
    counting_word = {}
    list_txt = txt.split()
    # iterating through the txt
    for word in list_txt:
        # Check if word is not a key in counting_word dict
        if word not in counting_word:
            counting_word[word] = 0
        counting_word[word] += 1
    return counting_word


result = counting_word(txt)
print(result)
