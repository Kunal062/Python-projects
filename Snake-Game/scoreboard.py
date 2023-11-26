from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 17, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.count}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.count += 1
        self.update_score()


