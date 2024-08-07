import random
from colorgram import colorgram as cg
from prettytable import *
from turtle import *
import turtle as t

sonali=Turtle()
sonali.hideturtle()
sonali.speed(15)
groundForTurtle=Screen()
#cg= colorgram()
table=PrettyTable()
table2=PrettyTable()
t.colormode(255)
color_list = cg.extract("image.jpg", 500)
color_palette = []

for coloring in color_list:

    r = coloring.rgb.r
    g = coloring.rgb.g
    b = coloring.rgb.b
    new_color = (r, g, b)
    color_palette.append(new_color)
    
#print(len(color_palette))

table.add_column("colours",color_palette)
#print(table)
new_color=[]
color_palette.reverse()
new_color=color_palette
new_color.pop()
new_color.pop()
new_color.pop()
new_color.reverse()
color_palette=new_color
#print(len(color_palette))
#print(color_palette)
table2.add_column("colours",color_palette)
sonali.penup()
sonali.setheading(225)
sonali.forward(400)
sonali.setheading(360)
#sonali.dot(5)
#sonali.forward(20)
#sonali.dot(5)
#print(table2)
numberOfLines=10
numberofDotsInaLine=10
for i in range(0,numberOfLines):
    
    for _ in range (0,numberofDotsInaLine):
        sonali.penup()
        colormode()   
        #sonali.pencolor(color)
        sonali.dot(15, random.choice(color_palette))
        sonali.forward(50)
     
    if i<numberOfLines-1:  
        sonali.setheading(90)
        sonali.forward(50)
        sonali.setheading(180)
        sonali.forward(500)
        sonali.setheading(360)
   
    
groundForTurtle.exitonclick()

