a=int(input())
import turtle 
turtle.shape('turtle')
def zvezda(a):
    turtle.forward(90)
    turtle.left(a)
for i in range(0, a):
    k = 180-(180/a)
    zvezda(k)
turtle.forward(90)
     
