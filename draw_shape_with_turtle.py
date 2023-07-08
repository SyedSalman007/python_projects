from turtle import Turtle, Screen
import turtle as t
import random

my_turtle = Turtle()
my_turtle.shape("classic")
my_turtle.color("blue")

# drawing a circle

# my_turtle.circle(50, 220, 50)

#  drawing a square

# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)

# draw a dotted line

# for _ in range(20):
#     my_turtle.pendown()
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)

#  Drawing different shapes

color_list = ["medium blue", "cyan", "green", "red", "deep pink", "indigo", "dark orange", "rosy brown", "teal"]


def draw_shape(max_vertex):
    my_turtle.pensize(5)
    for index in range(3, max_vertex+1):
        edges = 0
        deg = 360 / index
        color = random.choice(color_list)
        my_turtle.pencolor(color)
        while edges < index:
            my_turtle.forward(80)
            my_turtle.right(deg)
            edges += 1
        edges = 0
        while edges < index:
            my_turtle.forward(80)
            my_turtle.left(deg)
            edges += 1


# draw_shape(10)

# Drawing random walk
t.colormode(255)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


def random_walk():
    check = True
    my_turtle.pensize(5)
    my_turtle.hideturtle()
    my_turtle.speed("fast")
    while check:
        num = random.randint(1, 4)
        deg = 90 * num
        color = random_color()
        my_turtle.pencolor(color)
        my_turtle.right(deg)
        my_turtle.forward(30)


# random_walk()

#  Drawing a spirograph

my_turtle.speed("fastest")
for _ in range(1, 61):
    color = random.choice(color_list)
    my_turtle.pencolor(color)
    my_turtle.circle(100)
    # my_turtle.right(6)   can do with right() and also with set heading
    current_heading = my_turtle.heading()
    my_turtle.setheading(current_heading + 6)

my_screen = Screen()
my_screen.exitonclick()
