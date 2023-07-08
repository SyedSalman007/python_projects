import random
from turtle import Turtle, Screen
import turtle as t

my_screen = Screen()

my_screen.setup(width=500, height=450)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "green", "blue", "purple", "yellow", "orange"]
y_coords = [-100, -50, 0, 50, 100, 150]
all_turtles = []


for index in range(0, 6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(colors[index])
    my_turtle.goto(x=-230, y= y_coords[index])
    all_turtles.append(my_turtle)

if user_bet:
    game_on_hai = True

while game_on_hai:

    for race_turtle in all_turtles:
        if race_turtle.xcor() > 225:
            game_on_hai = False
            winner = race_turtle.fillcolor()
            break

        rand_num = random.randint(1, 10)
        race_turtle.forward(rand_num)

if user_bet == winner:
    print("You win !!.\nCongragulations")
else:
    print(f"You lose. {winner.title()} win the race")

# # etch a shetch app
#
# def move_forward():
#     my_turtle.forward(10)
#
#
# def move_backward():
#     my_turtle.backward(10)
#
#
# def rotate_right():
#     my_turtle.right(10)
#
#
# def rotate_left():
#     my_turtle.left(10)
#
# def clear_screen():
#     # my_turtle.reset()
#     my_turtle.clear()
#     my_turtle.penup()
#     my_turtle.home()
#     my_turtle.pendown()
#
# my_screen.listen()
# my_screen.onkey(key="w", fun=move_forward)
# my_screen.onkey(key="s", fun=move_backward)
# my_screen.onkey(key="a", fun=rotate_left)
# my_screen.onkey(key="d", fun=rotate_right)
# my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()
