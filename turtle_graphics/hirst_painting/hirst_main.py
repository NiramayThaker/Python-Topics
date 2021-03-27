import turtle
from turtle import Turtle, Screen
import random

colors = [(240, 235, 238), (240, 237, 233), (235, 237, 244), (231, 241, 235), (29, 105, 164), (227, 157, 67),
          (231, 214, 92), (188, 42, 84), (219, 138, 172), (140, 105, 57), (113, 185, 211), (217, 72, 98),
          (200, 168, 33), (157, 25, 65), (116, 191, 155), (24, 54, 129), (15, 182, 150), (106, 108, 192), (237, 89, 50),
          (140, 209, 226), (21, 141, 89), (19, 165, 204), (229, 165, 187), (83, 43, 29), (99, 49, 36), (23, 42, 80),
          (21, 90, 83), (237, 209, 7), (27, 85, 90), (102, 13, 47)]

turtle.colormode(255)
tim = Turtle()
tim.shape('turtle')

space_between_dots = 25
size_of_dots = 10


def change_turtle_line():
    tim.left(90)
    tim.penup()
    tim.forward(space_between_dots)
    tim.left(90)
    tim.forward(tim.heading() + space_between_dots)
    tim.right(180)
    tim.pendown()


for _ in range(10):
    for dot in range(10):
        tim.color(random.choice(colors))
        tim.dot(size_of_dots)
        tim.penup()
        tim.forward(space_between_dots)
        tim.pendown()
    change_turtle_line()


my_screen = Screen()
my_screen.bgcolor('Black')
my_screen.exitonclick()
