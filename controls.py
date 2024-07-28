SCREEN_THRESHOLD = 60


class Controls:
    def __init__(self, screen_height, paddle):
        self.screen_height = int(screen_height / 2)
        self.paddle = paddle

    def up(self):
        if self.paddle.ycor() < self.screen_height - SCREEN_THRESHOLD:
            self.paddle.forward(20)

    def down(self):
        if self.paddle.ycor() > -self.screen_height + SCREEN_THRESHOLD:
            self.paddle.backward(20)
