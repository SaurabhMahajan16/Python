import turtle
import pandas as pd
from write import Write

FONT = ("Ariel", 10, "normal")
#stateName=Write()
screen=turtle.Screen()
screen.title("US States Quiz")
IMAGE="blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

#def addingPosition(self,coord):
#    #location=[]
#    self.location.append(coord)
#    print(len(self.location))

#def mouseClickCoordinates(x,y):
#    xcor=x
#    ycor=y
#    position=(x,y)
#    #self.addingPosition(position)
#    print(position)
#    #print(location)
#
#turtle.onscreenclick(mouseClickCoordinates)
#print(location)
data=pd.read_csv("50_states.csv")
allStates=data.state.to_list()

screen.bgpic("blank_states_img.gif")
gameOn=True
guessedStates=[]

def statesNotFound(inputStates):
    #allStates=allStates.sort()
    #userStates=inputStates.sort
    #missingStates=[]
    #for state in allStates:
    #    if state not in inputStates:
    #        missingStates.append(state)
    #return missingStates
    return [x for x in allStates if x not in inputStates]

while len(guessedStates)<=50:
    userInput=(screen.textinput(title=f" {len(guessedStates)}/50 States Correct",prompt="Whats is the name of other state?")).title()
    print(userInput)
    
    if userInput in allStates:
        stateName=Write()
        guessedStates.append(userInput)
        
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pencolor('black')
        
        lineData=data[data["state"]==userInput]
        #t.goto(lineData.x.item(),lineData.y.item())
        #t.write(f"{userInput}", move=False, align="center", font=FONT)
        stateName.writeState(userInput,lineData.x.item(),lineData.y.item())
    
    if userInput == "Exit":
        notFound=statesNotFound(guessedStates)
        df=pd.DataFrame(notFound, columns=['missing_states'])
        df.to_csv("states_not_input.csv")
        break
    
    #
    ##print(lineData)
    #if lineData is not None:
    #    print(lineData.x)
    #    print(lineData.y)
        
    #    print(True)

turtle.mainloop()
#screen.exitonclick()