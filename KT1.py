import turtle


turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.speed(2)
    
for i in range(3):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100/10)
    turtle.right(90)
    for i in range(3):
        if not i % 2 == 0:
            turtle.forward(100 - 2*(100/10))
        else:
            turtle.forward(100 - 100/10)
        turtle.left(90)
turtle.right(180)
turtle.forward(70/10)



turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(180)



turtle.right(90)
turtle.forward(100*2 - 100/2)
turtle.left(90)
turtle.forward(100/2)
turtle.left(180)






turtle.done()
