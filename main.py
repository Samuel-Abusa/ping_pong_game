from main_screen import MainScreen
from paddle import Paddle
from ball import Ball

left_paddle = Paddle(-380)
right_paddle = Paddle(380)
screen = MainScreen(left_paddle, right_paddle)
ball = Ball(screen.screen, left_paddle, right_paddle)

screen.screen.exitonclick()
