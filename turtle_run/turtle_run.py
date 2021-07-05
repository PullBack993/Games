import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Entre a color: ')
colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']
positions_y = [-80, -40, 0, 40, 80, 120]
all_turtle = []

for t_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[t_index])
    new_turtle.goto(x=-230, y=positions_y[t_index])
    all_turtle.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.title(f"You've won! The {winning_color} turtle is the winner!")
            else:
                screen.title(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
