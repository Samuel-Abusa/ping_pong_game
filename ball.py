from turtle import Turtle
from random import choice

COLLISION_DISTANCE = 15


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.setheading(choice((0, 180)))
        self.screen_half_width = int(screen.window_height() / 2) - COLLISION_DISTANCE
        self.move()

    def move(self):
        while True:
            self.forward(2)
            self.bounce_on_walls()

    def bounce_on_walls(self):
        if (
            self.ycor() > self.screen_half_width
            or self.ycor() < -self.screen_half_width
        ):
            self.setheading(360 - self.heading())

    def bounce_on_paddles(self):
        pass
