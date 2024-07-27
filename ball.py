from turtle import Turtle
from random import choice
from time import sleep

COLLISION_DISTANCE = 25


class Ball(Turtle):
    def __init__(self, screen, left_paddle, right_paddle):
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.setheading(choice((0, 180)))
        self.screen_half_height = int(screen.window_height() / 2) - COLLISION_DISTANCE
        self.move(left_paddle, right_paddle, screen)

    def move(self, paddle_1, paddle_2, screen):

        while abs(self.xcor()) < int(screen.window_width()):
            screen.update()
            sleep(0.01)
            self.forward(5)
            self.bounce_on_walls()
            self.bounce_on_paddles(paddle_1, paddle_2)

    def bounce_on_walls(self):
        if (
            self.ycor() > self.screen_half_height
            or self.ycor() < -self.screen_half_height
        ):
            self.setheading(360 - self.heading())

    def bounce_on_paddles(self, paddle1, paddle2):
        p1_x_distance = abs(self.xcor() - paddle1.xcor())
        p1_y_distance = abs(self.ycor() - paddle1.ycor())
        p2_x_distance = abs(self.xcor() - paddle2.xcor())
        p2_y_distance = abs(self.ycor() - paddle2.ycor())
        yaxis_collision_distance = 70

        if (
            p1_x_distance < COLLISION_DISTANCE
            and p1_y_distance < yaxis_collision_distance
            or p2_x_distance < COLLISION_DISTANCE
            and p2_y_distance < yaxis_collision_distance
        ):
            paddle = paddle1 if self.distance(paddle1) < 100 else paddle2
            self.setheading(180 - self.heading() + int(self.ycor() - paddle.ycor()))
            self.forward(COLLISION_DISTANCE)
