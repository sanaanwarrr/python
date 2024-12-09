# Sana Anwar
# CS 100 H FALL 2023
# Homework 3 - For Loops + Turtle Commands

"""
Problem 1: Create a list named months of the months of the year. Write a for loop that iterates 
over the elements of months and prints out each one that begins with letter 'J', one month per line.

Problem 2: Write a for loop that iterates over all of the integers in the range 0 through 99, 
inclusive, and prints out all of those numbers that are divisible by both 2 and 5.

Problem 3: Consider the strings created by these assignment statements:
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

Write a for loop that prints out all the vowels in horton in the order they appear in horton.

Problem 4: Write code that uses the Python math module to compute and print out the values of:
    Part A: 100!
    Part B: the log (base 2) of 1,000,000
    Part C: the greatest common divisor of 63 and 49

Problem 5:
    Part A: Write code that uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon, each with side length 100.
    Part B: Write code that uses turtle graphics to draw four concentric circles of radius 50, 100, 150 and 200.
"""

# Problem 1
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

for month in months:
    if month.startswith("J"):
        print(month)

# Problem 2
for num in range(99):
    if num % 2 == 0 and num % 5 == 0:
        print(num)

# Problem 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for char in horton:
    if char in vowels:
        print(char, end=" ")

# Problem 4: Part A
import math

factorial = math.factorial(100)
print("100! =", factorial)

# Problem 4: Part B
logarithm = math.log2(1000000)
print("Log base 2 of 1,000,000 = ", logarithm)

# Problem 4: Part C
gcd = math.gcd(63,49)
print("GCD of 63 and 49 = ", gcd)

# Problem 5: Part A
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

def draw_polygon(sides, side_length):
    angle = 360 / sides
    for i in range(sides):
        pen.forward(side_length)
        pen.left(angle)

# Problem 5A: Equilateral Triangle
pen.penup()
pen.goto(-200, 100) 
pen.pendown()
draw_polygon(3, 100)

# Problem 5A: Square
pen.penup()
pen.goto(0, 100) 
pen.pendown()
draw_polygon(4, 100)

# Problem 5A: Pentagon
pen.penup()
pen.goto(200, 100)  
pen.pendown()
draw_polygon(5, 100)

pen.penup()
pen.goto(0, -50)
pen.pendown()

# Problem 5: Part B (Concentric Circles)
radii = [50, 100, 150, 200]
for radius in radii:
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.circle(radius)

screen.mainloop()
