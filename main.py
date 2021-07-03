import turtle
import pandas as pd

FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.title("India State Game")
image = "india_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_list = pd.read_csv("india_states.csv")
guessed_states = []
all_states = state_list["state"].to_list()

# def get_mouse_click_coor(x, y):
#     # turtle.onscreenclick(None)
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

while len(guessed_states) < len(all_states):
    screen.update()
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/{len(all_states)}", prompt="What's another state's name?")

    if answer_state is None:
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        state = state_list[state_list["state"] == answer_state]
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state, font=FONT)
    else:
        print("not found")
