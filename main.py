import turtle
import pandas as pd
import time

screen = turtle.Screen()
screen.title("U.S. State Game🇺🇸👏 (Type 'Exit' when you want to leave the game.)")
image_path = "blank_states_img.gif"

screen.addshape(image_path)
turtle.shape(image_path)


data = pd.read_csv("50_states.csv")

guess_states = []
all_states = data.state.to_list()
guess_states = []


while len(guess_states) < 50: #50 states
  time.sleep(0.3) #delay textinput popup
  answer = (screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another state name?")).title()
  
  if answer == "Exit":
    missing_states = []
    for state in all_states:
      if state not in guess_states:
        missing_states.append(state)
        
        #save the missing sates to csv file
        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states")
    screen.title("Good job! A list of missing states is avaibale in missing_states.csv file👩‍🏫")
    break
    
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


screen.exitonclick()



