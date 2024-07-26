from turtle import Screen, Turtle
from controls import Controls


class MainScreen:
    def __init__(self, left_paddle, right_paddle):
        self.screen = Screen()
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=1500, height=1000)
        self.screen.listen()
        self.draw_centerline()
        self.left_paddle_controls = Controls(self.screen.window_height(), left_paddle)
        self.right_paddle_controls = Controls(self.screen.window_height(), right_paddle)
        self.screen.onkeypress(self.left_paddle_controls.up, "w")
        self.screen.onkeypress(self.left_paddle_controls.down, "s")
        self.screen.onkeypress(self.right_paddle_controls.up, "Up")
        self.screen.onkeypress(self.right_paddle_controls.down, "Down")

    def draw_centerline(self):
        marker = Turtle()
        marker.speed("fastest")
        marker.color("white")
        marker.hideturtle()
        marker.penup()
        marker.goto(0, self.screen.window_height())
        marker.setheading(-90)
        marker.pensize(5)
        while marker.ycor() >= -self.screen.window_height() / 2:
            marker.forward(20)
            marker.penup()
            marker.forward(20)
            marker.pendown()
