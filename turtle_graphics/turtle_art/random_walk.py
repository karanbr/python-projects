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


def direction():
    moves = [0, 90, 180, 270]
    return random.choice(moves)


def make_move():
    timmy.pensize(20)
    timmy.speed("fast")
    for _ in range(1000):
        r, g, b = random_color()
        timmy.pencolor(r, g, b)
        move = direction()
        timmy.setheading(move)
        timmy.forward(50)


screen = Screen()
screen.colormode(255)
make_move()


screen.exitonclick()


# if move == "left":
#         #     timmy.left(90)
#         #     timmy.forward(50)
#         # else:
#         #     timmy.right(90)
#         #     timmy.forward(50)
