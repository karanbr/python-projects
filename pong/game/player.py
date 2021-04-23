from turtle import Turtle

LEFT = (-380, 0)
RIGHT = (370, 0)


class Player(Turtle):

    def __init__(self, position: str):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if position.lower() == "left":
            self.goto(LEFT)
        else:
            self.goto(RIGHT)

    def up(self):
        self.goto(self.xcor(), (self.ycor() + 20))

    def down(self):
        self.goto(self.xcor(), (self.ycor() - 20))

# from turtle import Turtle
#
# LEFT_POSITIONS = [(-470, 40), (-470, 20), (-470, 0), (-470, -20), (-470, -40)]
# RIGHT_POSITIONS = [(470, 40), (470, 20), (470, 0), (470, -20), (470, -40)]
# UP = 90
# DOWN = 270
#
#
# class Player:
#
#     def __init__(self, position):
#         self.blocks = []
#         for i in range(4):
#             block = Turtle()
#             block.shape("square")
#             block.penup()
#             block.color("white")
#             if position.lower() == "left":
#                 block.goto(LEFT_POSITIONS[i])
#             else:
#                 block.goto(RIGHT_POSITIONS[i])
#             self.blocks.append(block)
#         self.top = self.blocks[0]
#         self.bottom = self.blocks[-1]
#
#     def up(self):
#         for block in self.blocks:
#             block.setheading(UP)
#             block.forward(30)
#
#     def down(self):
#         for block in self.blocks:
#             block.setheading(DOWN)
#             block.forward(30)
