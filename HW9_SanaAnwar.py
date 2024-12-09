# Sana Anwar
# CS 100 H FALL 2023
# Homework 9 - Exceptions

"""
Problem 1: Recall that when the built-in function open() is called to open a file for reading, but it doesn’t exist, an exception is raised. 
However, if the file exists, a reference to the opened file object is returned. Write a function safeOpen() that takes one parameter, filename — a string 
giving the pathname of the file to be opened for reading. When safeOpen() is used to open a file, a reference to the opened file object should be 
returned if no exception is raised, just like for the open() function. If an exception is raised while trying to open the file, safeOpen() should return the value None.


Problem 2: Recall that when the built-in function float() is called it returns a floating point number constructed from a number or string. 
However, if the string doesn’t represent a valid floating point value, an exception is raised. Write a function safeFloat() that takes one 
parameter, x — a number or string that needs to be converted to floating point number. When safeFloat() is used to convert a number or string, 
an equivalent floating point number is returned if no exception is raised, just like for the float() function. If an exception is raised while trying to 
convert a number or string, safeFloat() should return 0.0 floating point value.

Problem 3: A radar speed gun is a device used in law-enforcement to measure the speed of moving vehicles in miles per hour. 
The measured speeds are supposed to be stored in a file, one number per line. Unfortunately, due to an intermittent fault, occasionally 
multiple numbers are written on a single line instead. Furthermore, occasionally the radar gun outputs a single stray character 
such as: 67.9z, 6$4.9, or a3.9, to illustrate just a few. Given a file that has radar speed gun readings, write a function averageSpeed() 
to calculate the average of the numbers in the file. Your code must adhere to the following specifications:
    - Prompt the user for the name of the input file to process. When the user enters a nonexistent file name, 
    give the user a second chance. After two wrong entries in a row, quit the program with an appropriate message.
    - Ignore numbers containing stray characters.
    - Ignore any reading for slow vehicles moving at 2 miles per hour or less.
    - Print the final average to the console.
    - Make use of the functions safeOpen() and safeFloat().
"""

# Problem 1
def safeOpen(filename):
    try:
        return open(filename, 'r')
    except FileNotFoundError:
        return None

# Problem 2
def safeFloat(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return 0.0

# Problem 3
def averageSpeed():
    attempts = 0
    file = None

    while attempts < 2:
        filename = input("enter file name: ")
        file = safeOpen(filename)
        if file:
            break
        else:
            attempts += 1
            if attempts < 2:
                print("file not found. please try again.")
            else:
                print("file not found. yet another human error. goodbye.")
                return

    valid_speeds = []
    for line in file:
        readings = line.split()
        for reading in readings:
            speed = safeFloat(reading) 
            if speed > 2: 
                valid_speeds.append(speed)

    file.close()

    if valid_speeds:
        average = sum(valid_speeds) / len(valid_speeds)
        print(f"average speed is {average:.2f} miles per hour.")
    else:
        print("no valid speeds found in the file.")