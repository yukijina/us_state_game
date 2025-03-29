import turtle
import pandas as pd
import time

screen = turtle.Screen()
screen.title("U.S. State Game")
image_path = "blank_states_img.gif"

screen.addshape(image_path)
turtle.shape(image_path)
screen.title("U.S. State Game🇺🇸")

guess_states = []


while len(guess_states) < 50: #50 states
  time.sleep(0.3) #delay textinput popup
  answer = (screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another state name?")).title()


  data = pd.read_csv("50_states.csv")
  matched_state = data[data.state == answer]

  try:
    guess_states.append(answer)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(matched_state.x.item(), matched_state.y.item())  
    t.pencolor('blue')
    t.pendown()
    t.write(answer, font=("Courier",12, "bold"))

  except ValueError:
    t.goto(-150, 50)
    t.pencolor('red')
    t.write('Type error. Try agin',  font=("Courier",24, "bold"))
    time.sleep(0.5) #keep text in the screen for 5 sec
    t.clear()


"""another way. If we use list"""
#all_states = data.state.to_list()
# if answer in all_states:
#   t = turtle.Turtle()
#   t.hideturtle()
#   t.penup()
#   matched_data = data[data.state == answer]
#   t.goto(matched_data.x.item(), matched_data.y.item())
#   t.pendown()
#   t.pencolor("blue")
#   t.write(answer)

screen.exitonclick()


