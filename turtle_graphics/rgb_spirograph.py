import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)


def random_color_finder():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim = Turtle()
tim.shape('turtle')

for _ in range(80):
    tim.color(random_color_finder())
    tim.speed('fastest')
    tim.circle(100)
    tim.left(5)

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.exitonclick()
