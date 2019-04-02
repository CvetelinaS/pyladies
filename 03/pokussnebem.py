from turtle import forward, backward, left,right, penup, pendown, up, down, goto, exitonclick
from turtle import shape
from random import randint

shape('turtle')
#hvězda na vrsku stromu
def nebe(): 
    for i in range(5):
        forward(25)
        left(145)
hvezdy = 0
while hvezdy < 50:
    x = randint(-300, 300)
    y = randint(-300, 300)
    nebe()
    penup()
    up()
    goto(x,y)
    down()
    pendown()
    hvezdy = hvezdy + 1
    continue

    exitonclick ()