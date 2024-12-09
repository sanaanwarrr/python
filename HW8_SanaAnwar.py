# Sana Anwar
# CS 100 H FALL 2023
# Homework 8 - Dictionaries

"""
Problem 1: Write a function named initialLetterCount that takes one parameter, wordList — a list of words. 
Create and return a dictionary in which each initial letter of a word in wordList is a key and the corresponding value is the number 
of words in wordList that begin with that letter. The keys in the dictionary should be case-sensitive, which means 'a' and 'A' are two different keys.

Problem 2: Write a function named initialLetters that takes one parameter, wordList – a list of words. 
Create and return a dictionary in which each initial letter of a word in wordList is a key and the corresponding value is a list of the 
words in wordList that begin with that letter. There should be no duplicate words in any value in the dictionary.


Problem 3: Write a function named shareOneLetter that takes one parameter, wordList – a list of words. 
Create and return a dictionary in which each word in wordList is a key and the corresponding value is a list of all the words
in wordList that share at least one letter with that word. There should be no duplicate words in any value in the dictionary.
"""

# Problem 1
def initialLetterCount(wordList):
    count_dict = {}
    for word in wordList:
        initial = word[0]
        count_dict[initial] = count_dict.get(initial, 0) + 1
    return count_dict

# Problem 2
def initialLetters(wordList):
    letter_dict = {}
    for word in wordList:
        initial = word[0]
        if initial not in letter_dict:
            letter_dict[initial] = []
        if word not in letter_dict[initial]:
            letter_dict[initial].append(word)
    return letter_dict


# Problem 3
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
