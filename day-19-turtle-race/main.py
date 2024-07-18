import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def spawn_turtles():
    position = -70
    for i in colors:
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.color(i)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=position)
        position += 30
        all_turtles.append(new_turtle)


def move_turtle():
    pass


spawn_turtles()

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"you've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
