#PROBLEM ONE
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



#PROBLEM TWO
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

#PROBLEM THREE
import math

# PROBLEM 3A
factorial = math.factorial(100)
print("100! = ", factorial)

# PROBLEM 3B
log = math.log2(1000000)
print("log base 2 of 1,000,000 = ", log)

# PROBLEM 3C
gcd = math.gcd(63, 49)
print("greatest common denominator of 63 and 49 = ", gcd)



# PROBLEM FOUR
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
