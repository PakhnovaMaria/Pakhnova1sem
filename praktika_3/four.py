import turtle 
turtle.shape('turtle')
for i in range(50, 1000, 10):
    turtle.forward(i)
    turtle.left(90) 
    turtle.forward(i)
    turtle.left(90) 
    turtle.forward(i)
    turtle.left(90) 
    turtle.forward(i)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.pendown()

   
