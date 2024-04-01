import turtle
from turtle import Screen, Turtle
import pandas


def write_state(name, x, y):
    t = Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(name, align="center", font=("Arial", 15, "bold"))


screen = Screen()
screen.setup(width=750, height=520)
screen.bgpic("blank_states_img.gif")
screen.title("Guess the States")
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
states = data["state"].str.lower()

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(f"Welcome to the Guessing Game! {len(guessed_states)}/50", "Write the state's name:").lower()

    if answer == 'exit':
        missing_states = [state for state in states if state not in guessed_states]
        print("Missing states:", missing_states)
        left_learn = pandas.DataFrame(missing_states)
        left_learn.to_csv("left_to_learn.csv")
        break

    if answer in states.values and answer not in guessed_states:
        state_data = data[data.state.str.lower() == answer]
        xcor = int(state_data.x)
        ycor = int(state_data.y)
        write_state(state_data.state.item(), xcor, ycor)
        guessed_states.append(answer)




turtle.mainloop()
