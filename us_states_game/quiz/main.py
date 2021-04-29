import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# screen.bgpic("./blank_states_img.gif")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

runner = turtle.Turtle()
runner.hideturtle()
runner.penup()

# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)

game_data = pandas.read_csv("50_states.csv")
states_list = game_data["state"].to_list()
states_dict = game_data.to_dict()
# print(states_list)
print(states_dict)
guessed_states = []
states_not_guessed_list = states_list

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's anoter states name?").title()

    if answer_state == "Exit":
        break

    if answer_state in states_list:
        print("BOOYA")
        guessed_states.append(answer_state)
        states_not_guessed_list.remove(answer_state)
        coordinates = game_data[game_data.state == answer_state]
        print(coordinates.x)
        x = int(coordinates.x)
        y = int(coordinates.y)
        runner.goto(x, y)
        runner.write(f"{answer_state}")
        # turtle.mainloop()
        # answer_state = screen.textinput(title="Guess the State", prompt="What's anoter states name?").title()

states = []
x = []
y = []
for state in states_not_guessed_list:
    row = game_data[game_data.state == state]
    states.append(row.state)
    x.append(row.x)
    y.append(row.y)

states_to_learn = {
    "state": states,
    "x": x,
    "y": y
}

series = pandas.Series(states_not_guessed_list)
series.to_csv("states_to_learn_list.csv")

dataframe = pandas.DataFrame(states_to_learn)
dataframe.to_csv("states_to_learn.csv")
