from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title("Turtle Road Crossing")
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 265:
        score.score_update()
        player.position_reset()
        car_manager.car_speed_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            game_is_on = False
            score.game_end()

screen.exitonclick()