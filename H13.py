#15.11.2024 Yuna Antonenko
#Ülesane 13
import turtle
import random


screen = turtle.Screen()
t = turtle.Turtle()
turtle.speed(0)

nr = int(screen.textinput("Vanuse sisestamine", "mis on sinu vanus?", default=20, minval=0, maxval=100))
nr = 10
for i in range(nr*10):
    t.lt(90)
    t.fd(3)

    t.lt(180)
    t.fd(3)   
    t.lt(90)
    t.fd(4)
t.goto(0,0)


# Küsi kasutajalt tekstilist sisendit



nr = 10
for i in range(nr+1):
    t.lt(90)
    t.fd(5)
    t.write(i, font=("Arial", 10, "normal"))
    t.lt(180)
    t.fd(5)   
    t.lt(90)
    t.fd(10*4)
    
 




turtle.done()































