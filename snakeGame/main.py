from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from snakemusic import SnakeMusic


screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(n=0)
screen.title('SNAKE GAME')

snakeMusic=SnakeMusic()

score=Scoreboard()
food=Food()    
screen.update()  
game_on=True
snake=Snake()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
snakeMusic.gameGoing()

while game_on:
    
    
    screen.update() 
    
    time.sleep(0.2)
    snake.move()
    
    if snake.head.distance(food)<15:
        food.refresh()
        score.refresh()
        #snakeMusic.gotFood()
        snake.extendSnake()
    
        
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        game_on=False
        #food.hideturtle()
        score.gameover()
        snakeMusic.gameOver()
    
    for segment in snake.segments[2:]:
        if snake.head.distance(segment)<15:
            score.gameover()
            game_on=False
            snakeMusic.gameOver()
    
            
        
    
          
    
           



screen.exitonclick()