# Sana Anwar
# CS 100 H FALL 2023
# Homework 2 - Conditional Statement and List Datatypes

"""
Problem 1: Write Python code that does the following:
    Part A:
    Assigns the values 3, 4 and 5 to the variables a, b and c, respectively.

    Part B:
    Write an if statement that prints “OK” if a is less than b

    Part C:
    Write an if statement that prints “OK” if c is less than b

    Part D:
    Write an if statement that prints “OK” if the sum of a and b is equal to c

    Part E:
    Write an if statement that prints “OK” if the sum of a squared and b squared equals c squared.

Problem 2: Repeat the previous problem with the additional requirement that “NOT OK”
is printed if the condition is false.

Problem 3: Assign to the variable grades a list of 10 letter grades from among 'A', 'B', 'C', 'D', and 'F'. For example:
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']

Write a Python expression that creates a list named frequency,
in which the elements are the number of times each of the letters A, B, C, D and F appear in grades. 
For example, for the above value of grades, the following would be correct output:
frequency = [4, 2, 2, 0, 2]

Problem 4:
    Part A:  Write a Python statement that creates a list named dog_breeds that contains the elements 
    'collie', 'sheepdog', 'Chow', and 'Chihuahua' in the order given.

    Part B: Write a Python statement that uses list slicing to create a list herding_dogs 
    that is made up of the first two elements of dog_breeds.

    Part C: Write a Python statement that uses list indexing to create a list tiny_dogs
    that is made up of the last element of dog_breeds.

    Part D: Write a Python statement that tests whether 'Persian' is in the list dog_breeds
    and prints either True or False depending on the answer.
"""

# Problem 1: Part A
a = 3
b = 4
c = 5

# Problem 1: Part B
if a < b:
    print("OK")

# Problem 1: Part C
if c < b:
    print("OK")

# Problem 1: Part D
if a + b == c:
    print("OK")

# Problem 1: Part E
if a**2 + b**2 == c**2:
    print("OK")

# Problem 2
if a**2 + b**2 == c**2:
    print("OK")
else:
    print("NOT OK")

# Problem 3
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print(frequency)

# Problem 4: Part A
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

# Problem 4: Part B
herding_dogs = dog_breeds[:2]
print(herding_dogs)

#Problem 4: Part C
tiny_dogs = [dog_breeds[-1]]
print(tiny_dogs)

# Problem 4: Part D
print('Persian' in dog_breeds)