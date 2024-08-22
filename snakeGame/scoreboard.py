from turtle import Turtle
FONT=('Arial',24,'normal')
ALIGNMENT="center"
STOP="GAMEOVER"
POSITION=(0,265)

class Scoreboard(Turtle):
    
    
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        with open('score.txt','r') as file:
            value=file.read()
            if value is None:
                self.highScore=0
            else:
                self.highScore=int(value)
           
        #self.write((0,-290), False)
        self.createScoreboard()
        self.speed=0.2
        
        
    def createScoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Score :{self.score} High Score : {self.highScore}", move=False, align=ALIGNMENT, font=FONT) 
        
    def refresh(self):
        self.score+=1
        self.createScoreboard()
        self.speed*=0.9
        
    def reset(self):
        if self.score>self.highScore:
            self.highScore=self.score
            with open ('score.txt', "w") as file:
                file.write(f"{self.highScore}")
        self.score=0
        self.createScoreboard()
        self.speed=0.2
        
    #def gameover(self):
    #    self.goto(0,0)
    #    self.write(f"{STOP} \n Final Score {self.score} | High Score {self.highScore} ", move=False, align=ALIGNMENT, font=FONT)
    #    self.score=0
    #    self.createScoreboard()
        
        
        