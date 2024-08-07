from turtle import *
from prettytable import *
import random
import turtle as t

sonali=Turtle()
groundForTurtle=Screen()
sonali.shape("turtle")
t.colormode(255)
sonali.color("coral")
sonali.shapesize(1,1,1)
#sonali.pensize(1)
sonali.speed(100)
#colours=["red", "blue", "green", "yellow", "pink", "black", "brown", "grey", "silver"]
#sonali.home(-100)

def randomColors():
    red=random.randint(0,255)
    blue=random.randint(0,255)
    green=random.randint(0,255)
    #colour=
    return (red,green,blue)

#randomColour=randomColors()
#print(randomColour)
def drawshapes():    
    for i in range(3,11):

        sonali.pencolor(randomColors())
        for _ in range (i):
            for _ in range(10):
                sonali.forward(5)
                sonali.penup()
                sonali.forward(5)
                sonali.pendown()

            sonali.right(360/i)

def drawRandomLines():
    directions=[0,90,180,270]

    for _ in range (200):
        sonali.forward(10)
        sonali.setheading(random.choice(directions))
        sonali.pencolor(randomColors())
  
def drawSpirograph(gapsize, object):
    for i in range (0,360,gapsize):
        object.circle(80)
        object.pencolor(randomColors())
        object.setheading(i)
        
    
    

def drawStar():
    while True:
        color('red')
        fillcolor('yellow')
        begin_fill()
        forward(100)
        left(155)
        if abs(pos()) < 1:
            end_fill()
            break

drawSpirograph(4, sonali)
groundForTurtle.exitonclick()

#print(groundForTurtle)


table=PrettyTable()
pokemon_names=["pickachu", "squirtel","charmander"]
type=["electric", "water", "fire"]
table.add_column("Pokemon Name", pokemon_names)
table.add_column("Type", type)
table.align="l"
print(table)
