from turtle import forward, backward, left,right, penup, pendown, exitonclick
from turtle import shape
from random import randint

shape('turtle')
#hvězda na vrsku stromu
for g in range(12):
    for i in range(5):
        for j in range(4):
            forward(20)
            left(120)
        left(30)
    penup()
    forward(50)
    pendown()

exitonclick ()