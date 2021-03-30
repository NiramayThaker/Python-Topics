from turtle import Turtle, Screen
import random

is_race_on = False

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


def ending_line():
    tim = Turtle()
    tim.hideturtle()
    tim.color("white")
    tim.penup()
    tim.goto(x=230, y=0)
    tim.pendown()
    for number_to_multi in range(1, 3):
        tim.right(90*number_to_multi)
        tim.forward(100*number_to_multi)


ending_line()
while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()
