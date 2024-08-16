from turtle import Turtle, Screen

saurabh=Turtle(shape='turtle')
screen=Screen()
saurabh.color("coral")

def moveForward():
    saurabh.forward(5)

def moveBackward():
    saurabh.backward(5)

def moveCounterClock():
    newHeading=saurabh.heading()+20
    saurabh.setheading(newHeading)

def moveClock():
    newHeading=saurabh.heading()-20
    saurabh.setheading(newHeading)




screen.listen()
screen.onkey(key="w",fun=moveForward)
screen.onkey(key="s",fun=moveBackward)
screen.onkey(key="a",fun=moveCounterClock)
screen.onkey(key="d",fun=moveClock)
screen.onkey(key="c",fun=saurabh.clear)




screen.exitonclick()
