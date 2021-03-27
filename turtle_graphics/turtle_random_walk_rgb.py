import turtle as t
import random

t.colormode(255)


def random_color_finder():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
t.pensize(15)
t.speed('fastest')

for _ in range(200):
    t.color(random_color_finder())
    t.forward(30)
    t.setheading(random.choice(directions))

my_screen = t.Screen()
my_screen.bgcolor('black')
my_screen.exitonclick()
