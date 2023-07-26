import turtle, pandas
import time
FONT = ('Sans-Serif', 10, 'normal')


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")

game_is_on = True
correct = 0
all_correct_states = []
states_to_learn = {
    "states": [],
}

while game_is_on:
    screen.update()
    answer_state = screen.textinput(title=f"{correct}/50, States Correct", prompt="Guess the State.").title()
    if answer_state in data['state'].to_list():
        correct += 1
        check_data = data[data.state == answer_state]
        x_axis = int(check_data['x'].iloc[0])
        y_axis = int(check_data['y'].iloc[0])
        time.sleep(0.1)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        screen.update()
        new_turtle.penup()
        new_turtle.goto(x_axis, y_axis)
        new_turtle.write(f"{answer_state}", align="center", font=FONT)
        all_correct_states.append(answer_state)
    elif answer_state == "Exit":
        game_is_on = False
        print("You lose")
        for state in data["state"].to_list():
            if state not in all_correct_states:
                states_to_learn["states"].append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
    elif correct == 50:
        print("Quiz Complete")
        game_is_on = False

