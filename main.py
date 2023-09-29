import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
all_states = data["state"]
game_is_on = True

name_display = turtle.Turtle()
name_display.penup()
name_display.hideturtle()
name_display.color("black")

def write_name(state_name, x, y):
    name_display.goto(x, y)
    name_display.write(state_name, align="center", font=("Arial", 12, "normal"))

while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/{len(all_states)}",
                                    prompt="What is another state")

    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in data['state'].tolist() and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data['state'] == answer_state]
        x, y = state_data['x'].values[0], state_data['y'].values[0]
        write_name(answer_state, x, y)

# Calculate the missed states
missed_states = [state for state in all_states if state not in guessed_states]

# Print the missed states
if missed_states:
    print("Missed states:")
    for state in missed_states:
        print(state)

screen.exitonclick()
