from turtle import Turtle
GAME_FONT = ('Courier', 18, 'normal')
WINNER_FONT = ('Courier', 30, 'normal')
STARTING_POSITION = (-240, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.levels = 1
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.write(f"Level: {self.levels}", align="center", font=GAME_FONT)

    def score_update(self):
        self.clear()
        self.levels += 1
        self.goto(STARTING_POSITION)
        self.write(f"Level: {self.levels}", align="center", font=GAME_FONT)

    def game_end(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=WINNER_FONT)
