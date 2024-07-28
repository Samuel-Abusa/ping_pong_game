from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write_score(0, 0)

    def write_score(self, left_score, right_score):
        self.clear()
        self.write(
            f"{left_score} {right_score}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    def game_over(self, left_score, right_score):
        self.clear()
        self.goto(0, 0)
        self.write(
            f"   Game Over!\n{'Left' if left_score > right_score else 'Right'} player wins!",
            align="center",
            font=("Courier", 24, "normal"),
        )
