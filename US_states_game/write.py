from turtle import Turtle
FONT = ("ariel", 10, "normal")
ALIGNMENT="center"
class Write(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.state=""
        self.pencolor('black')
        self.hideturtle()
        self.penup()
        
        #self.write((0,-290), False)
    def writeState(self, text,x,y):
        self.goto(x,y)
        self.write(f"{text}", move=False, align=ALIGNMENT, font=FONT)
        
    