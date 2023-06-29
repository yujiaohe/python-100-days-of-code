import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("50_states.csv")
number_of_states = len(states.state)
guessed = []
label = turtle.Turtle()

while len(guessed) < 50:
  answer_state = screen.textinput(
    title=f"{len(guessed)}/{number_of_states} Guess the State",
    prompt="What's another state name?")
  answer_state_format = answer_state.title()
  if answer_state_format == "Exit":
    # not_guessed = states[~states.state.isin(guessed)]
    # not_guessed.state.to_csv("states_to_learn.csv")
    # conditional list comprehesion
    not_guessed = [
      item for item in states.state.to_list() if item not in guessed
    ]
    new_data = pd.DataFrame(not_guessed)
    new_data.to_csv("states_to_learn.csv")
    break
  if answer_state_format in states.state.to_list():
    guessed.append(answer_state_format)
    state = states[states.state == answer_state_format]
    label.hideturtle()
    label.penup()
    label.goto(int(state.x), int(state.y))
    label.write(answer_state_format)

# def get_mouse_click_coor(x, y):
#     """Print x, y of the state"""
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
