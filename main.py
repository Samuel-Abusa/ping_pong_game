from main_screen import MainScreen
from paddle import Paddle
from ball import Ball

left_paddle = Paddle(-730)
right_paddle = Paddle(730)
screen = MainScreen(left_paddle, right_paddle)
ball = Ball(screen.screen)

screen.screen.exitonclick()
