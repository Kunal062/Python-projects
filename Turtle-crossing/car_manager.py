import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def move_speed(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setposition(400, random.randint(-250, 250))
            self.all_cars.append(new_car)


    def game_over(self):
        self.clear()
        self.create_car()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
