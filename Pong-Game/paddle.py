from turtle import Turtle

MOVE = 20


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setposition(pos)

    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), new_y)
