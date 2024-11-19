#19.11.2024 Yuna Antonenko
#Ülesane 14
import turtle
import random 

ekraan = turtle.Screen()
 
def muuda_varvi_red():
    print("punane")
    turtle.color("red")

def muuda_varvi_green():
    print("rohaline")
    turtle.color("green")

def muuda_varvi_blue():
    print("sinine")
    turtle.color("blue")

ekraan.listen()



def ruut(x, y):
    turtle.speed()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.fd(50)
        turtle.lt(90)
 

def puhasta_ekraan():
    turtle.clear()
 
ekraan.onscreenclick(ruut, 1) # Vasak klõps
#ekraan.onscreenclick(paremKlikk, 3) # Parem klõps
ekraan.onscreenclick(puhasta_ekraan, 3)
ekraan.onkey(muuda_varvi_red"r")
ekraan.onkey(muuda_varvi_green"g")
ekraan.onkey(muuda_varvi_blue"b")
 
turtle.mainloop()
























