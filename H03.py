#16.10.2024 Yuna Antonenko
#Ülesanded 03
import turtle

#Ülesane 03.2:Ostunimekiri
toode = "porgant"
kogus = 3
hind = 5.35 
print("Soovin " + toode + "eid" +str(kogus) + ", mille tüki hind on" + str(hind) + " eurot." )









""""
#Ülesane 03.4:Lemmikraamat
raamatu_pealkiri = ("Sipsik")
raamatu_autor = ("Eno Raund")
lehekulgede_arv = 16
hindamisskoor = 9.7
print("Minu lemmikraamat on "+raamatu_pealkiri+" "+raamatu_autor+", mis on "+str(lehekulgede_arv)+" lehekülge pikk mille ma hindan "+str(hindamisskoor)+" punktiga.")
"""






"""
#Ülesane 03.5: unistuste auto
mark, mudel = "bmw", "118"
auto = mark+" "+mudel
aasta = 1997
hind = 301.60

print("Minu unistuste auto on",auto,"aastast",aasta,"mille hind on",hind,"eurot.")
"""



"""
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
"""