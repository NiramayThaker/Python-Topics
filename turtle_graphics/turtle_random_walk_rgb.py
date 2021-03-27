import turtle as t
import random

t.colormode(255)


def random_color_finder():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim = t.Turtle()
tim.shape('turtle')

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')

for _ in range(200):
    tim.color(random_color_finder())
    tim.forward(30)
    tim.setheading(random.choice(directions))

my_screen = t.Screen()
my_screen.bgcolor('black')
my_screen.exitonclick()
