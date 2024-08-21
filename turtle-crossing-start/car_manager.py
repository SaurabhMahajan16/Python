from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    
    def __init__(self):
        super().__init__()
        
        self.allCars=[]
        self.speed=STARTING_MOVE_DISTANCE
        
        



    def createCars(self):
            space=random.randint(1,8)
            if space==6:
                newCar=Turtle()
                newCar.penup()
                newCar.shape("square")
                newCar.shapesize(stretch_len=2, stretch_wid=1)
                newCar.color(random.choice(COLORS))
                newCar.goto(260,random.randint(-280,280) )
                #newCar.setheading(90)
                self.allCars.append(newCar)
        
    def move(self):
        for car in self.allCars:
            car.backward(self.speed)
    
    def increaseSpeed(self):
        self.speed+=MOVE_INCREMENT
