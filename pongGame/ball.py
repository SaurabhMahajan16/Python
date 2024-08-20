from turtle import Turtle
HOME=(0,0)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xMove=10
        self.yMove=10
        self.ballSpeed=0.1
    
    def move(self):
        newx=self.xcor()+self.xMove
        newy=self.ycor()+self.yMove
        self.goto(newx,newy)
    
    def bounce(self):
        
            self.yMove*=-1
            #newx=self.xcor()-10
    def bounceX(self):
        
            self.xMove*=-1
            self.ballSpeed*=0.5
    
    def reset(self):
        self.goto(0,0)
        self.bounceX()
        self.ballSpeed*=0.1
        
            
            
        