from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def clockwise():
    current_heading = tim.heading()
    head = current_heading + 5
    tim.setheading(head)

def counter_clockwise():
    current_heading = tim.heading()
    head = current_heading - 5
    tim.setheading(head)

def clear():
    screen.reset()

screen.listen()
screen.onkey(key = "w", fun =move_forward)
screen.onkey(key = "s", fun =move_backward)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = clear)
screen.exitonclick()