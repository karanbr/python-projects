import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)
screen.onkey(key="Down", fun=player.move_back)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.drive()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            level.game_over()
            game_is_on = False

    if player.reached_finish_line():
        level.level_up()
        player.back_to_start()
        car_manager.level_up()

screen.exitonclick()
