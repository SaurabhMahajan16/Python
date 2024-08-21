import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from music import Music

screen = Screen()
screen.setup(width=600, height=600)
music=Music()
screen.listen()
screen.tracer(0)
cars=CarManager()
player=Player()
scoreBoard=Scoreboard()
screen.onkey(fun=player.moveTurtle, key="Up")

music.gameGoing()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.createCars()
    cars.move()
    for car in cars.allCars:
        if player.distance(car)<10:
            game_is_on=False
            print("gameover")
            music.gameOver()
            scoreBoard.gameover()
        if player.ycor()==280:
            player.goto(0,-280)
            cars.increaseSpeed()
            music.reachGoal()
            scoreBoard.refresh()
    
screen.exitonclick()