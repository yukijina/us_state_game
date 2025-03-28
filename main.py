import turtle

screen = turtle.Screen()
screen.title("U.S. State Game")
image_path = "blank_states_img.gif"

screen.addshape(image_path)
turtle.shape(image_path)

user_answer = (screen.textinput(title="Guess the state", prompt="What's another state name?")).title()
print(user_answer)




screen.exitonclick()


