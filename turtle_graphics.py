# Drawing sun kind of pattern using turtle graphics

import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")

i = 1
while i <= 30:
    timmy.forward(100)
    timmy.color("yellow")
    timmy.right(165)
    timmy.color("blue")
    timmy.forward(100)
    timmy.color("red")
    i += 1
