from main_screen import MainScreen
from paddle import Paddle

left_paddle = Paddle(-730)
right_paddle = Paddle(730)
screen = MainScreen(left_paddle, right_paddle)

screen.screen.exitonclick()
