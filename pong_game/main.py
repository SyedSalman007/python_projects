from turtle import Screen
from paddle_class import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# TIME = 0.1

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((420, 0))
l_paddle = Paddle((-420, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    # time.sleep(TIME)
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # bounce from the wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
        # TIME *= 0.9

    # bounce from right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 390 or ball.distance(l_paddle) < 50 and ball.xcor() < -390:
        ball.bounce_x()
        # TIME *= 0.9

    if ball.xcor() > 450:
        ball.ball_reset()
        score.r_point()
        # TIME = 0.1

    if  ball.xcor() < -450:
        ball.ball_reset()
        score.l_points()
        # TIME = 0.1

    if score.l_score == 10:
        score.l_win()
        ball.game_end()

    if score.r_score == 10:
        score.r_win()
        ball.game_end()

screen.exitonclick()