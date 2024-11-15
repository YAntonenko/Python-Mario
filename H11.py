#08.11.2024 Yuna Antonenko
#Ülesane 11
import turtle
import random
'''
#1
def pikim_sona(*sonad):
    pikim = 0
    for i in sonad:
        if len(i)>pikim:
            pikim=len(i)
    print(f"Pikkim sõna on {pikim} märki!")


pikim_sona("üks", "kaks", "kolmkümmend", "kaheksa", "vjfgdlfökvlkjnpoegrvlkös")


#2
def kolm_pikit_sona(a):
    sonastik = {}
    for i in a:
        sonastik[i] = len(i)
    sorteeritud = sorted(sonastik.items(), key = lambda x:x[1], reverse = True)
    for i in range(3):
        print(sorteeritud[j][0])

sonad = ("üks", "kaks", "kolmkümmend", "kaheksa", "viis")



#3
def sarnased_esitahed(nimi):
    tykk = nimi.slice(" ")
    if tykk [0][0] == tykk [1][0]:
        return True
    else:
        return False



print(sarnased_esitahed['Vapper Vares'])
print(sarnased_esitahed['Lahe Känguru'])
'''

#4



def viisnurk():
    print("Joonistan viisnurga")

def ring():
    print("Joonistan ringi")

def ruut(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.rt(random.randint(0,90))
        for i in range(4):
            turtle.fd(100)
            turtle.lt(90)

def suvaline(k):
    for i in range(k):
        random.choice([viisnurk(1),  ring(1), ruut(1)])

print("--------------Minu fancy program----------------")
valik = int(input("1 - viisnurk\n2 - ring\n3 - ruut\n4 - suvaline\nLisa valik (1-4): "))
kujunditeArv = int(input("Mitu kujundit soovid joonistada: "))

if valik == 1:
    viisnurk()
elif valik == 2:
    ring()
elif valik == 3:
    ruut()
else:
    suvaline()













