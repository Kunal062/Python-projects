import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race. Make your bet.")
colors = ["red", "green", "yellow", "purple", "blue", "orange",]
positions = [75, 45, 15, -15, -45, -75]
is_game_on = False
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_game_on = True


while is_game_on:
    for i in all_turtles:
        if i.xcor() > 230:
            winning_turtle = i.pencolor()
            is_game_on = False
            if user_bet == winning_turtle:
                print(f"You've won. The {winning_turtle} color turtle has won the race.")
            else:
                print(f"You've lost. The {winning_turtle} color turtle has won the race.")
        random_position = random.randint(0, 20)
        i.forward(random_position)


screen.exitonclick()
