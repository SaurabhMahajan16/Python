from turtle import Turtle, Screen
import random

screen=Screen()
#Saurabh=Turtle(shape='turtle')
#Saurabh.penup()
#Saurabh.goto(x=-450,y=350)
#sonali=Turtle(shape='turtle')
#sonali.penup()
#sonali.goto(x=-450,y=300)
#rama=Turtle(shape='turtle')
#rama.penup()
#rama.goto(x=-450,y=250)
#rajesh=Turtle(shape='turtle')
#rajesh.penup()
#rajesh.goto(x=-450,y=200)
#yuvan=Turtle(shape='turtle')
#yuvan.penup()
#yuvan.goto(x=-450,y=150)
#Saurabh.color('yellow')
#sonali.color('green')
#rama.color('coral')
#rajesh.color('red')
#yuvan.color('brown')
colors=['yellow', 'green', 'red', 'blue', 'coral', 'brown']
startPosition=[350,300,250,200,150,100]
allTurtles=[]
for turtleIndex in range(0,6):
    newTurtle=Turtle(shape='turtle')
    newTurtle.penup()
    newTurtle.color(colors[turtleIndex])
    newTurtle.goto(x=-450,y=startPosition[turtleIndex])
    #startPosition=-50
    allTurtles.append(newTurtle)
    
    
    
    

#print(sonali)
#print(Saurabh)
#print(rama)
#print(rajesh)
#print(yuvan)
speed=[0,3,5,10]
screen.setup(width=1000,height=800)
yourBet=screen.textinput(title= "BET", prompt="which color you want to bet on? red, green, blue, coral, brown, yellow")

startRace=False

if yourBet is not None:
    startRace=True
    
#def turtleRace():
#    Saurabh.speed(random.choice(speed))
#    sonali.speed(random.choice(speed))
#    rajesh.speed(random.choice(speed))
#    rama.speed(random.choice(speed))
#    yuvan.speed(random.choice(speed))
# 
#turtleRace()    
while startRace:
    for turtle in allTurtles:
        if turtle.xcor()>700:
            startRace=False
            winningColor=turtle.pencolor()
            
            if winningColor==yourBet:
                print("Your turtle won the race")
                print(f"the winning turtle color is {winningColor}")
                
            else:
                print("Your turtle lost the race")
                print(f"the winning turtle color is {winningColor}")
        randomDistance=random.randint(0,10)
        turtle.forward(randomDistance)


screen.exitonclick()

