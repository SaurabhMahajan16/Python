from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.color("coral")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def moveTurtle(self):
        self.forward(10)
        
    def reset(self):
        self.goto(STARTING_POSITION)
        #self.bounceX()
        #self.ballSpeed*=0.1
    
    

