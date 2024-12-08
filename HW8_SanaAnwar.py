# PROBLEM 1
def initialLetterCount(wordList):
    count_dict = {}
    for word in wordList:
        initial = word[0]
        count_dict[initial] = count_dict.get(initial, 0) + 1
    return count_dict

# PROBLEM 2
def initialLetters(wordList):
    letter_dict = {}
    for word in wordList:
        initial = word[0]
        if initial not in letter_dict:
            letter_dict[initial] = []
        if word not in letter_dict[initial]:
            letter_dict[initial].append(word)
    return letter_dict


# PROBLEM 3
def shareOneLetter(wordList):
    share_dict = {}
    for word in wordList:
        shared_words = []
        for other_word in wordList:
            if any(letter in word for letter in other_word):  
                if other_word not in shared_words:
                    shared_words.append(other_word)
        share_dict[word] = shared_words
    return share_dict
