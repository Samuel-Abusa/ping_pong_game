from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.score = 0

    def reset_position(self, x_axis):
        self.goto(x_axis, 0)
