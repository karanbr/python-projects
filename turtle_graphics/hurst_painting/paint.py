import turtle as t
import random
import colorgram

color_list = [(131, 165, 206), (225, 151, 100),
              (32, 41, 59), (200, 134, 147), (235, 212, 87), (166, 56, 46), (39, 104, 153), (141, 184, 161),
              (153, 58, 65),
              (170, 29, 33), (217, 80, 69), (158, 32, 29), (15, 96, 71), (236, 165, 156), (50, 111, 90), (58, 50, 47),
              (50, 42, 46), (228, 164, 168), (34, 61, 56), (170, 188, 222), (190, 99, 108), (32, 59, 108),
              (103, 127, 163),
              (34, 151, 210), (175, 200, 188), (66, 66, 56)]

timmy = t.Turtle()
screen = t.Screen()
screen.colormode(255)

timmy.penup()
timmy.setx(-500.0)
timmy.sety(-400.0)
y_start = timmy.ycor()
x_start = timmy.xcor()
timmy.pensize(50)


def draw():
    timmy.pencolor(random.choice(color_list))
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(100)


for _ in range(10):
    for _ in range(10):
        draw()

    y_start += 100
    timmy.sety(y_start)
    timmy.setx(x_start)


# timmy.sety(y_start)

screen.exitonclick()

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
