from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')
GAME_END_FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_end(self):
        self.goto(0, 0)
        self.write(f"Game End", align=ALIGNMENT, font=GAME_END_FONT)

