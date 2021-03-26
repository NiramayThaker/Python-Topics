# Drawing sun pattern with turtle graphics

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


my_screen = turtle.Screen()
my_screen.bgcolor('black')
my_screen.title("Turtle_graphics")
my_screen.exitonclick()
