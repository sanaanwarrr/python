# PART ONE
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

for month in months:
    if month.startswith("J"):
        print(month)

# PART TWO
for num in range(99):
    if num % 2 == 0 and num % 5 == 0:
        print(num)

# PART THREE
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for char in horton:
    if char in vowels:
        print(char, end=" ")

# PART FOUR
import math

# PART A
factorial = math.factorial(100)
print("100! =", factorial)

# PART B
logarithm = math.log2(1000000)
print("Log base 2 of 1,000,000 = ", logarithm)

# PART C
gcd = math.gcd(63,49)
print("GCD of 63 and 49 = ", gcd)

# PART FIVE
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

def draw_polygon(sides, side_length):
    angle = 360 / sides
    for i in range(sides):
        pen.forward(side_length)
        pen.left(angle)

# equilateral triangle 
pen.penup()
pen.goto(-200, 100) 
pen.pendown()
draw_polygon(3, 100)

# square
pen.penup()
pen.goto(0, 100) 
pen.pendown()
draw_polygon(4, 100)

# pentagon
pen.penup()
pen.goto(200, 100)  
pen.pendown()
draw_polygon(5, 100)

pen.penup()
pen.goto(0, -50)
pen.pendown()

# concentric circles 
radii = [50, 100, 150, 200]
for radius in radii:
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.circle(radius)

screen.mainloop()
