import turtle 
turtle.shape('turtle')
def cir(a): 
    for i in range(1,361):
        turtle.forward(a)
        turtle.left(1)
    for b in range(1,361): 
        turtle.forward(a)
        turtle.right(1)
for a in range (10):
    cir(a)

