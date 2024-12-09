# Sana Anwar
# CS 100 H FALL 2023
# Homework 6 - While Loops

"""
Problem 1: Write a function named twoWords that gets and returns two words from a user. The first word is 
of a specified length, and the second word begins with a specified letter.

The function twoWords takes two parameters:
    - an integer, length, that is the length of the first word and
    - a character, firstLetter, that is the first letter of the second word. The second word 
    may begin with either an upper or lowercase instance of firstLetter.

    The function twoWords should return the two words in a list. Use a while True loop and a break statement in the implementation of twoWords.

Problem 2: Write a function named twoWordsV2 that has the same specification as Problem 1, but implement it using 
while and not using break. (Hint: provide a different boolean condition for while.)
Since only the implementation has changed, and not the specification, for a given input the output should be identical to the output in Problem 1.

Problem 3: Write a function named enterNewPassword. This function takes no parameters. It prompts the user to enter a password until the entered password has 8-15 characters, including at least one digit. Tell the user whenever a password fails one or both of these tests.

Problem 4: Implement the GuessNumber game. In this game, the computer:
    - Think of a random number in the range 0-50. (Hint: use the random module.)
    - Repeatedly prompt the user to guess the mystery number.
    - If the guess is correct, congratulate the user for winning. If the guess is incorrect, let the user know if the guess is too high or too low.
    - After 5 incorrect guesses, tell the user the right answer.

The following is an example of correct input and output.
"""

# Problem 1:
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

# Problem 2:
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

# Problem 3:
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

# Problem 4:
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