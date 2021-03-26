import turtle
from turtle import Turtle, Screen
import random

colors = ['red', 'yellow', 'orange', 'green', 'purple', 'brown']
tim = Turtle()
tim.shape('turtle')
tim.backward(100)


def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for i in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape_sides in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_sides)


my_screen = turtle.Screen()
my_screen.bgcolor('black')
my_screen.exitonclick()

