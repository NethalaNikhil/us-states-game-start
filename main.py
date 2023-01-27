# import csv
import turtle
import pandas

# def mouse_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(mouse_cor)

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
area = data["state"].tolist()
guessed_items = []
learn =[]
count =0
while len(guessed_items) < 50:
    guess = screen.textinput(title=f"{count}/50 States correct", prompt="Whats other state name?r").title()
    x = data[data.state == guess]
    if guess == "Exit":
        break
    if guess in area:
        count = count+1
        guessed_items.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_cor = x.x
        y_cor = x.y
        t.goto(int(x_cor), int(y_cor))
        t.write(guess, True)


# states to learn.csv
for i in area:
    if i in guessed_items:
        continue
    else:
        learn.append(i)


pandas.DataFrame(learn).to_csv("learn_states.csv")



