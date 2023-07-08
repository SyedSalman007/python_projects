from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.back(50)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(50)
# timmy.back(100)
#
# my_screen = Screen()
# # print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
