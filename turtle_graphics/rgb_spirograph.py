import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
tim = Turtle()
tim.shape('turtle')
tim.speed('fastest')


def random_color_finder():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gaps):
    for _ in range(int(360/size_of_gaps)):
        tim.color(random_color_finder())
        tim.circle(100)
        # tim.left(size_of_gaps)
        #         or
        tim.setheading(tim.heading() + size_of_gaps)


draw_spirograph(5)

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.exitonclick()
