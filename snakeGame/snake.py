from turtle import Turtle
class Snake:

    STARTINGPOSITION=[(0,0),(-18,0),(-38,0)]
    SNAKEMOVEDISTANCE=20
    UP=90
    DOWN=270
    RIGHT=0
    LEFT=180
    def __init__(self) -> None:
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0]
    
    def createSnake(self):
        for position in self.STARTINGPOSITION:
            self.addSegment(position)
    
    def addSegment(self,position):
        newSegment=Turtle(shape='square')
        newSegment.penup()
        newSegment.goto(position)
        newSegment.color('white')
        self.segments.append(newSegment)
    
    def extendSnake(self):
        self.addSegment(self.segments[-1].position())  
    

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
            #if snakeSegment[seg].xcor()>280:
            #    snakeSegment[seg].goto(x=-300, y=0)
        self.segments[0].forward(self.SNAKEMOVEDISTANCE)
        #self.segments[0].left(90)
        #self.segments[0].right(90)

        #if self.segments[len(self.segments)-1].xcor()>280:
        #    self.segments[0].goto(x=-300, y=0)
    
    
    def up(self):
        if self.head.heading()!=self.DOWN:
            self.head.setheading(self.UP)
        #    newHeading=self.head.heading()+90
        #    self.head.setheading(newHeading)
        #    self.move()
        
    def down(self):
        if self.head.heading()!=self.UP:
            self.head.setheading(self.DOWN)
        #newHeading=self.segments[0].heading()+270
        #self.segments[0].setheading(newHeading)
        #self.move()
        #self.head.setheading(270)
        
    def right(self):
        #self.segments[0].right(90)
        #self.move()
        if self.head.heading()!=self.LEFT:
            self.head.setheading(self.RIGHT)
    
    def left(self):
        #self.segments[0].left(90)
        #self.head.setheading(90)self.move()
        if self.head.heading()!=self.RIGHT:
            self.head.setheading(self.LEFT)
        