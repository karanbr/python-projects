from turtle import Screen
from marker import Marker
from player import Player
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

marker = Marker()
left_player = Player("left")
right_player = Player("right")
ball = Ball()

screen.listen()
screen.onkey(left_player.up, "w")
screen.onkey(left_player.down, "s")
screen.onkey(right_player.up, "Up")
screen.onkey(right_player.down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.distance(left_player) < 50:
        ball.bounce_x()

    if ball.distance(right_player) < 50 and ball.xcor() > 340 \
            or ball.distance(left_player) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

screen.exitonclick()
