# Yuna Antonenko
# 04.10.24
# Harjutus02

# 9. Arvusüsteem
arv = int(input("Lisa 10nd arv: "))
print(bin(arv))
print(hex(arv))

# 10. Kütusekulu arvutamine
liiter = int(input("Lisa kütusekulu: "))
km = int(input("Lisa läbitud kilometriid: "))
kytusekulu = liiter/(km/100)
print("Sinu keskmine kütusekulu on: ", kytusekulu)



import turtle

#muudan asukohta
turtle.penup()
turtle.goto(-400,200)
turtle.pendown()


#kolmnurk
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)




#muudan asukohta
turtle.penup()
turtle.goto(-100,200)
turtle.pendown()


#
turtle.left(180)
turtle.circle(100,360)

turtle.done()
