from turtle import Turtle, Screen
from paddle import Paddle


screen=Screen()
rPaddle=Paddle(378,0)
lPaddle=Paddle(-378,0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('PONG GAME')



screen.listen()
screen.onkey(rPaddle.paddleUp, key="Up")
screen.onkey(rPaddle.paddleDown, key="Down")
screen.onkey(rPaddle.paddleUp, key="w")
screen.onkey(rPaddle.paddleDown, key="s")

gameOn=True
while gameOn:
    screen.update()

screen.exitonclick()