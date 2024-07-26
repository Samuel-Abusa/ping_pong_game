from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_axis):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(x_axis, 0)
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_len=4, stretch_wid=1)
