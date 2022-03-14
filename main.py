from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('white')
    circle(i)
    color('orange')
    circle(i*1.8)
    right(3)
    forward(4)
    done()