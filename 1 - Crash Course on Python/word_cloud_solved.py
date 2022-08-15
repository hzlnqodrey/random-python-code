file_contents = "Here are many examples of short stories for you to read online. Online has become another leg in our life. WE have to take that into account so that we will go along the growth of the science and technology. Computer has revolutionalised our world. The people have started to see another world. What we were has become history. The twentieth century has become remote@ history. The IT companies and other computer-based companies have outperformed other traditional companies which have been there for a long time. Accuracy has become the most used word among the people. Telecommunication has become very very cheap affair all over the world. All these achievements are possible because of Computer and the Internet. Reading short stories online has become our favorite pastime."
# Here is a list of punctuations and uninteresting words you can use to process your text
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                          "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

# LEARNER CODE START HERE
# Cleaning Word (Puntuations and Uninteresting Words)
# 1. Cleaning Punctuations
def cleaning_punctuation(file_contents, punctuations):
    for character in punctuations:
        file_contents = file_contents.replace(character, '')
    txt = file_contents
    return txt

# 2. Cleaning Unused Word
def cleaning_uninteresting_words(txt, uninteresting_words):
    lowered_txt = txt.lower()
    list_txt = lowered_txt.split()
    new_list = []
    for word in list_txt:
        if word not in uninteresting_words:
            new_list.append(word)
    return new_list

# Removing Punc
txt = cleaning_punctuation(file_contents, punctuations)
# Removing Unused Word
txt = cleaning_uninteresting_words(txt, uninteresting_words)

# Counting Frequencies of Word
def count_frequencies(txt):
    counting_word = {}
    # iterating through the txt
    for word in txt:
        # Check if word is not a key in counting_word dict
        if word not in counting_word:
            counting_word[word] = 0
        counting_word[word] += 1
    return counting_word

result = count_frequencies(txt)
print(result)
