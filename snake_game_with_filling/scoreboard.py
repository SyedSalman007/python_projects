from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')
GAME_END_FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score_data.txt") as file:
            data = file.read()
        self.high_score = int(data)
        print(type(self.high_score))
        self.color('white')
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score_data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
