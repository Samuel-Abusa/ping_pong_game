from turtle import Turtle
from random import choice, randint
from time import sleep

COLLISION_DISTANCE = 20
REBOUND = 15


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.screen_half_height = int(screen.window_height() / 2) - COLLISION_DISTANCE

    def reset_position(self):
        self.goto(0, 0)
        self.setheading(choice((randint(-46, 44), randint(136, 224))))

    def move(self, paddle_1, paddle_2, screen):
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
            self.forward(REBOUND)

    def bounce_on_paddles(self, paddle1, paddle2):
        p1_x_distance = abs(self.xcor() - paddle1.xcor())
        p1_y_distance = abs(self.ycor() - paddle1.ycor())
        p2_x_distance = abs(self.xcor() - paddle2.xcor())
        p2_y_distance = abs(self.ycor() - paddle2.ycor())
        yaxis_collision_distance = 50

        if (
            p1_x_distance <= COLLISION_DISTANCE
            and p1_y_distance <= yaxis_collision_distance
            or p2_x_distance <= COLLISION_DISTANCE
            and p2_y_distance <= yaxis_collision_distance
        ):
            paddle = paddle1 if self.distance(paddle1) < 100 else paddle2
            self.setheading(180 - self.heading() + int(self.ycor() - paddle.ycor()))
            self.forward(REBOUND)
