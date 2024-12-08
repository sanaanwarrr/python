# PROBLEM ONE
def twoWords(length, letter):
    while True:
        word1 = input(f"enter a {length}-letter word please: ")
        if len(word1) == length:
            break
        else:
            print(f"the word must be exactly {length} letters long.")

    while True:
        word2 = input(f"enter a word beginning with {letter} please: ")
        if word2.lower().startswith(letter.lower()):
            break

    return [word1, word2]

print(twoWords(6, 'a'))

# PROBLEM TWO
def twoWordsV2(length, letter1):
    first_word_valid = False
    while not first_word_valid:
        first_word = input(f"enter a {length}-letter word please: ")
        if len(word1) == length:
            first_word_valid = True
        else:
            print(f"the word must be exactly {length} letters long.")
    
    second_word_valid = False
    while not second_word_valid:
        word2 = input(f"enter a word beginning with {letter1} please: ")
        if second_word.lower().startswith(letter1.lower()):
            second_word_valid = True
        else:
            print(f"the word must begin with '{letter1}'.")

    return [word1, word2]

# PROBLEM THREE
def enterNewPassword():
    while True:
        password = input("enter a password (8-15 characters with at least one digit): ")
        if 8 <= len(password) <= 15 and any(char.isdigit() for char in password):
            print("password is valid.")
            break
        else:
            if len(password) < 8 or len(password) > 15:
                print("password must be between 8 and 15 characters.")
            if not any(char.isdigit() for char in password):
                print("password must contain at least one digit.")

# PROBLEM FOUR
import random

def guessNumber():
    number = random.randint(0, 50)
    print("i'm thinking of a number in the range 0-50. you have five tries to guess it.")

    for attempt in range(1, 6): 
        guess = int(input(f"guess {attempt}? "))
        if guess == number:
            print(f"you are right! i was thinking of {number}!")
            return
        elif guess > number:
            print(f"{guess} is too high")
        else:
            print(f"{guess} is too low")

    print(f"sorry, you've used all your guesses. the number was {number}.")