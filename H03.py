#16.10.2024 Yuna Antonenko
#Ülesanded 03
import turtle

#Ülesanded 03.6: Python turtle kolmnurk
kylje_pikkus = 200
nurk = 120
kujundi_varv = "red"

turtle.color(kujundi_varv)

for i in range(3):
    for i in range(3):
        turtle.forward(kylje_pikkus) 
        turtle.left(nurk)
        
    turtle.penup()
    turtle.forward(kylje_pikkus*1.5)
    turtle.pendown()


turtle.done()


