from main_screen import MainScreen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep


left_paddle = Paddle()
right_paddle = Paddle()
scoreboard = ScoreBoard()
screen = MainScreen(left_paddle, right_paddle)
ball = Ball(screen.screen)


def set_up():
    ball.reset_position()
    left_paddle.reset_position(-380)
    right_paddle.reset_position(380)
    screen.screen.update()


set_up()


while left_paddle.score < 10 and right_paddle.score < 10:
    sleep(2)

    while abs(ball.xcor()) < int(screen.screen.window_width() / 2):
        ball.move(left_paddle, right_paddle, screen.screen)

    if ball.xcor() > right_paddle.xcor():
        left_paddle.score += 1
    else:
        right_paddle.score += 1

    scoreboard.write_score(left_paddle.score, right_paddle.score)

    sleep(1)
    set_up()

scoreboard.game_over(left_paddle.score, right_paddle.score)
screen.screen.exitonclick()
