from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan2")


def random_color():
    rc = random.randint(1, 255)
    gc = random.randint(1, 255)
    bc = random.randint(1, 255)
    return rc, gc, bc


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        timmy.forward(100)
        timmy.right(angle)


screen = Screen()
screen.colormode(255)

for shape_side_n in range(3, 11):
    r, g, b = random_color()
    timmy.pencolor(r, g, b)
    draw_shape(shape_side_n)

screen.exitonclick()
