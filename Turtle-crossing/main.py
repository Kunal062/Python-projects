import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.move, "Up")
car = CarManager()
score = Scoreboard()

count = 0
game_is_on = True
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_speed()

    # Detect collision with car
    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect successful crossing
    if player.is_at_finish():
        player.move_to_start()
        car.level_up()
        score.level_up()


screen.exitonclick()

