from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 \
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset_snake()
    # Detect collision with tail
    # for block in snake.snake_blocks:
    #     if block == snake.head:
    #         pass
    #     elif snake.head.distance(block) < 10:
    #         game_is_on = False
    #         score.game_over()
    # Same but with slicing
    for block in snake.snake_blocks[1::]:
        if snake.head.distance(block) < 10:
            score.reset()
            snake.reset_snake()
screen.exitonclick()
