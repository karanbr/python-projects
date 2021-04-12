import turtle
import random

turtle.colormode(255)

color_list = [(131, 165, 206), (225, 151, 100),
              (32, 41, 59), (200, 134, 147), (235, 212, 87), (166, 56, 46), (39, 104, 153), (141, 184, 161),
              (153, 58, 65),
              (170, 29, 33), (217, 80, 69), (158, 32, 29), (15, 96, 71), (236, 165, 156), (50, 111, 90), (58, 50, 47),
              (50, 42, 46), (228, 164, 168), (34, 61, 56), (170, 188, 222), (190, 99, 108), (32, 59, 108),
              (103, 127, 163),
              (34, 151, 210), (175, 200, 188), (66, 66, 56)]

tim = turtle.Turtle()
screen = turtle.Screen()
# tim.penup()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
