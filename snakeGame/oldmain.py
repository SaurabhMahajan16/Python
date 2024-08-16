from turtle import Screen, Turtle
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')

position=[0,-18,-38]
#snakeSegment=[]
screen.tracer(n=0)
#for snakeindex in range (0,3):
#    snake=Turtle(shape='square')
#    snake.penup()
#    snake.goto(x=position[snakeindex], y=0)
#    snake.color('white')
#    snakeSegment.append(snake)
    
screen.update()  
game_on=True

while game_on:
    
    
    screen.update() 
    #for seg in range(len(snakeSegment)-1,0,-1):
    #    new_x=snakeSegment[seg-1].xcor()
    #    new_y=snakeSegment[seg-1].ycor()
    #    snakeSegment[seg].goto(new_x,new_y)
    #    #if snakeSegment[seg].xcor()>280:
    #    #    snakeSegment[seg].goto(x=-300, y=0)
    #snakeSegment[0].forward(20)
    #snakeSegment[0].left(90)
    #snakeSegment[0].right(90)
    #
    #if snakeSegment[len(snakeSegment)-1].xcor()>280:
    #    snakeSegment[0].goto(x=-300, y=0)
    time.sleep(0.02)
         
    #game_on=-1
          
    
           



screen.exitonclick()