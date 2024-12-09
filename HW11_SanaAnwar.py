# Sana Anwar
# CS 100 H FALL 2023
# Homework 11 - Math & Turtle Modules

"""
Problem 1: Write code that uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon, each with side length 100.

Problem 2: Write code that uses turtle graphics to draw four concentric circles of radius 50, 100, 150 and 200.

Problem 3: Write code that uses the Python math module to compute and print out the values of:
    Part A: 100!
    Part B: the log (base 2) of 1,000,000
    Part C: the greatest common divisor of 63 and 49

Problem 4: Write a program that asks the user for a color, a line width, a line length and a shape. 
Assume that the user will specify a shape that is either a line, a triangle, or a square. 
Use turtle graphics to draw the shape that the user requests of the size, color, line width and line length that the user requests.
"""

# Problem 1:
import turtle

def draw_polygon(sides, side_length):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.right(angle)

# triangle
draw_polygon(3, 100)

turtle.penup()
turtle.forward(150)
turtle.pendown()

# square
draw_polygon(4, 100)

turtle.penup()
turtle.forward(150)
turtle.pendown()

# hexagon
draw_polygon(5, 100)

turtle.done()

# Problem 2:
import turtle

def concentric():
    turtle.penup()
    turtle.goto(0, -50) 
    turtle.pendown()
    
    for radius in [50, 100, 150, 200]:
        turtle.circle(radius)
        turtle.penup()
        turtle.goto(0, -(radius + 50)) 
        turtle.pendown()

turtle.speed(1)
concentric()

turtle.done()

# Problem 3: Part A
import math

factorial = math.factorial(100)
print("100! = ", factorial)

# Problem 3: Part B
log = math.log2(1000000)
print("log base 2 of 1,000,000 = ", log)

# Problem 3: Part C
gcd = math.gcd(63, 49)
print("greatest common denominator of 63 and 49 = ", gcd)

# Problem 4:
import turtle

def draw_line(length):
    turtle.forward(length)

def draw_triangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.right(120)

def draw_square(length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_shape():
    color = input("what color? ")
    line_width = int(input("what line width? "))
    line_length = int(input("what line length? "))
    shape = input("line, triangle or square? ").lower()
    
    turtle.color(color)
    turtle.width(line_width)
    
    if shape == "line":
        draw_line(line_length)
    elif shape == "triangle":
        draw_triangle(line_length)
    elif shape == "square":
        draw_square(line_length)
    else:
        print("invalid shape")

    turtle.done()

draw_shape()
