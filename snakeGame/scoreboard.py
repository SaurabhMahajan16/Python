from turtle import Turtle
FONT=('Arial',24,'normal')
ALIGNMENT="center"
STOP="GAMEOVER"

class Scoreboard(Turtle):
    
    
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        #self.write((0,-290), False)
        self.createScoreboard()
        
        
    def createScoreboard(self):
        self.write(f"Score :{self.score}", move=False, align=ALIGNMENT, font=FONT) 
        
    def refresh(self):
        self.score+=1
        self.clear()
        self.createScoreboard()
        
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"{STOP} \n Final Score {self.score} ", move=False, align=ALIGNMENT, font=FONT)
        
        
        