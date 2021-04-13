from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race. Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = -300

for color in colors:
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-450, y=y)
    turtles.append(turtle)
    y += 100

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner!")
        turtle.forward(float(random.randint(1, 100)))


# red = Turtle("turtle")
# blue = Turtle("turtle")
# red.penup()
# blue.penup()
# red.color("red")
# blue.color("blue")
#
# red.goto(x=-450, y=-300)
# blue.goto(x=-450, y=-200)


screen.exitonclick()
