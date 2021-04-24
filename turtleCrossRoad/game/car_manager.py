from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.color(choice(COLORS))
            random_y = choice(range(-250, 250))
            car.goto(300, random_y)
            for any_other_car in self.cars:
                if car.distance(any_other_car) < 50:
                    random_y = choice(range(-250, 250))
                    car.goto(300, random_y)
            self.cars.append(car)

    def drive(self):
        for car in self.cars:
            # car.back(STARTING_MOVE_DISTANCE)
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    # def create_cars(self):
    #     for i in range(20):
    #         car = Turtle("square")
    #         car.penup()
    #         car.shapesize(stretch_wid=1, stretch_len=2)
    #         car.setheading(180)
    #         car.color(choice(COLORS))
    #         car.goto(x=choice(range(250, 800)), y=choice(range(-250, 250)))
    #         for any_other_car in self.cars:
    #             if car.distance(any_other_car) < 20:
    #                 car.goto(x=choice(range(250, 400)), y=choice(range(-250, 250)))
    #         self.cars.append(car)
