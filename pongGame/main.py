from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreBoard import Scoreboard
from music import Music

screen=Screen()
rPaddle=Paddle(378,0)
lPaddle=Paddle(-378,0)
ball=Ball()
music=Music()
scoreboard=Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('PONG GAME')


music.gameGoing()
screen.listen()
screen.onkey(fun=rPaddle.paddleUp, key="Up")
screen.onkey(fun=rPaddle.paddleDown, key="Down")
screen.onkey(fun=lPaddle.paddleUp, key="w")
screen.onkey(fun=lPaddle.paddleDown, key="s")

gameOn=True
while gameOn:
    screen.update()
    time.sleep(ball.ballSpeed)
    ball.move()
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce()
    
    if ball.distance(rPaddle)<50 and ball.xcor()>340:
        
        ball.bounceX()
        scoreboard.refreshRight()
    if ball.xcor()>380:
        ball.reset()
    
    if ball.distance(lPaddle)<50 and ball.xcor()<-340:
        
        ball.bounceX()
        scoreboard.refreshLeft()
    if ball.xcor()<-380:
        ball.reset()
        
    if scoreboard.scoreRight==5 and scoreboard.scoreRight>scoreboard.scoreLeft :
        scoreboard.gameover()
        gameOn=False
        music.gameOver()
    elif  scoreboard.scoreLeft==5 and scoreboard.scoreLeft>scoreboard.scoreRight:
        scoreboard.gameover()
        gameOn=False
        music.gameOver()

screen.exitonclick()