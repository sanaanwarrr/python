# Sana Anwar
# CS 100 H FALL 2023
# Homework 4 - Functions

"""
Problem 1:
    Part A: Write a function named hasFinalLetter that takes two parameters:
    - strList, a list of non-empty strings
    - letters, a string of upper and/or lower case letters

    The function hasFinalLetter should create and return a list of all the strings in strList that end with a letter in letters.

    Part B: Create three test cases, each consisting of a list of non-empty strings and a string of upper and/or lower case letters,
    for your function in Problem 1a. One of these tests should return the empty list. For each test case write two assignment statements 
    and a function call that passes the test arguments to your function.

Problem 2:
    Part A: Write a function named isDivisible that takes two parameters:
    - maxInt, an integer
    - twoInts, a tuple of two integers

    The function isDivisible should create and return a list of all the ints in the 
    range from 1 to maxInt (not including maxInt) that are divisible of both ints in twoInts.

    Part B: Create three test cases, each consisting of a value for maxInt and a value for twoInts, for your
    function in Problem 2a. One of these tests should return the empty list. For each test case 
    write two assignment statements and a function call that passes the test arguments to your function.
"""

# Problem 1: Part A

def hasFinalLetter(strList,letters):
    result = []
    letters = set(letters.lower())
    for word in strList:
        if word[-1].lower() in letters:
            result.append(word)
    return result

# Question 1: Part B

strList1 = ["anna", "bella", "carmen", "david"]
letters1 = "abc"
result1 = hasFinalLetter(strList1, letters1)
print(result1) 

strList2 = ["ox","yay","zebra","jazz"]
letters2 = "xyz"
result2 = hasFinalLetter(strList2,letters2)
print(result2)

strList3 = ["dog","elephant","flamingo","gorilla"]
letters3 = "def"
result3 = hasFinalLetter(strList3,letters3)
print(result3)

# Question 2: Part A

def isDivisible(maxInt, twoInts):
    result = []
    for num in range(1, maxInt):
        if num % twoInts[0] == 0 and num % twoInts[1] == 0:
            result.append(num)
    return result

# Question 2: Part B

maxInt1 = 20
twoInts1 =(2,3)
result1 = isDivisible(maxInt1, twoInts1)
print(result1)

maxInt2 = 50
twoInts2 = (4,6)
result2 = isDivisible(maxInt2, twoInts2)
print(result2)

maxInt3 = 10
twoInts3 = (3,7)
result3 = isDivisible(maxInt3, twoInts3)
print(result3)
