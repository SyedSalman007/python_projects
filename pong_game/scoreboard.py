from turtle import Turtle
ALIGNMENT = 'center'
GAME_FONT = ('Courier', 80, 'normal')
WINNER_FONT = ('Courier', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=GAME_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=GAME_FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=GAME_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=GAME_FONT)

    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def r_win(self):
        self.clear()
        self.goto(0, 0)
        self.write('Right Player Wins', align=ALIGNMENT, font=WINNER_FONT)

    def l_win(self):
        self.clear()
        self.goto(0, 0)
        self.write('Left Player Wins', align=ALIGNMENT, font=WINNER_FONT)
