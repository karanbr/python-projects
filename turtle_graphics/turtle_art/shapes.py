from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan2")

starting_pos = timmy.pos()


def random_color():
    rc = random.randint(1, 255)
    gc = random.randint(1, 255)
    bc = random.randint(1, 255)
    return rc, gc, bc


def triangle():
    r, g, b = random_color()
    timmy.pencolor((r, g, b))
    timmy.forward(100)
    timmy.right(120)
    timmy.forward(100)
    timmy.right(120)
    timmy.forward(100)
    timmy.right(120)


def square():
    r, g, b = random_color()
    timmy.pencolor((r, g, b))
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


def pentagon():
    r, g, b = random_color()
    timmy.pencolor((r, g, b))
    for _ in range(5):
        timmy.forward(100)
        timmy.right(72)


def hexagon():
    r, g, b = random_color()
    timmy.pencolor((r, g, b))
    for _ in range(6):
        timmy.forward(100)
        timmy.right(60)


def heptagon():
    r, g, b = random_color()
    timmy.pencolor((r, g, b))
    for _ in range(7):
        timmy.forward(100)
        timmy.right(51.42)


def octagon():
    r, g, b = random_color()
    timmy.pencolor((r, g, b))
    for _ in range(8):
        timmy.forward(100)
        timmy.right(45)


def polygon():
    r, g, b = random_color()
    timmy.pencolor((r, g, b))
    for _ in range(9):
        timmy.forward(100)
        timmy.right(40)


def draw():
    triangle()
    square()
    pentagon()
    hexagon()
    heptagon()
    octagon()
    polygon()


# r, g, b = random_color()
screen = Screen()
screen.colormode(255)
# timmy.pencolor((r, g, b))
draw()
screen.exitonclick()
