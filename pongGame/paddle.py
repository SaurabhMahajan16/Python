from turtle import Turtle
TOP=255
BOTTOM=-255
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')
        self.goto(x,y)
    #paddle.goto(378,0)


    def paddleUp(self):
        if self.ycor()<TOP:
            newyCord=self.ycor()+20
            self.goto(self.xcor(), newyCord)

    def paddleDown(self):
        if self.ycor()>BOTTOM:
            newyCord=self.ycor()-20
            self.goto(self.xcor(), newyCord)