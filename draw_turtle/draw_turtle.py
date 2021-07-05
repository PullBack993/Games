from turtle import Turtle, Screen

mt = Turtle()
screen = Screen()

def move_forwards():
    mt.forward(10)

def move_backwards():
    mt.backward(10)

def turn_left():
    # or mt.left(45)
    heading = mt.heading() + 10
    mt.setheading(heading)

def turn_right():
    mt.right(45)
    # heading = mt.heading() - 10
    # mt.setheading(heading)

def clear():
    mt.clear()
    mt.penup()
    mt.home()
    mt.pendown()


screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()