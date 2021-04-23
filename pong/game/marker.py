from turtle import Turtle


class Marker(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, -300)
        self.setheading(90)
        for _ in range(11):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
