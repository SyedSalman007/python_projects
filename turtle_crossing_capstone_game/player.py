from turtle import Turtle

STARTING_POSITION = (0, -280)
DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.color("green")

    def move(self):
        self.forward(DISTANCE)

    def position_reset(self):
        self.goto(STARTING_POSITION)