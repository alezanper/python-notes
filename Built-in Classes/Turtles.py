# Using turtle 
import turtle

# Draw a pentagone
y = 5
for i in range(y):
    turtle.forward(100)
    turtle.right(360/y)

# Adding a star
for i in range(y) :
    turtle.forward(100)
    turtle.right(360/y)
    for j in range(y):
        turtle.forward(50)
        turtle.right(360/y)