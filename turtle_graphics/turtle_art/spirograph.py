from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan2")
timmy.speed("fastest")


def random_color():
    rc = random.randint(1, 255)
    gc = random.randint(1, 255)
    bc = random.randint(1, 255)
    return rc, gc, bc


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(200)
        timmy.setheading(timmy.heading() + size_of_gap)


screen = Screen()
screen.colormode(255)

draw_spirograph(20)

screen.exitonclick()
