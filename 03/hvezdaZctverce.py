from turtle import forward, left, exitonclick
from turtle import shape

shape('turtle')

for i in range(2):
    for j in range(4):
        forward(50)
        left(90)
    left(-20)

exitonclick()