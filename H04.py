#16.10.2024 Yuna Antonenko
#Ülesanded 4
<<<<<<< HEAD
<<<<<<< HEAD
import turtle 

#5. Ringi pindala ja Turtle
try:
    r = int(input("Lisa ringi raadius: "))
    pi = 3.14
    s = pi*r**2 #astendamine
    p = 2*pi*r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f} ")
    turtle.circle(r, 360)
except:
    print("Tegid sisestamisel vea!")



"""
#4. Kingituste pakkimine
try:
    kingitused = int(input("Lisa kinkide arv: "))
    maht = 5
    pakid = kingitused // maht
    yle = kingitused % maht
    print(f"Saad teha {pakid} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print("Tegid sisestamisel vea!")
"""


"""
#3. Faili allalaadimine
try:
    failiSuurus = int(input("Siseta faili suurus kiirus (MB): "))
    downKiirus = int(input("Siseta allalaadimise kiirus (MB/s): "))
    aeg = failiSuurus / downKiirus
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundi")
except:
    print("Tegid sisestamisel vea!")
=======
import turtle


=======
import turtle


>>>>>>> 431736d48c9bfeeaf17fd0a4e6bfcb6f51bdde28
#Ringi pindala ja Turtle 
try:
    r = int(input("Ssseta ringi raadius:"))
    s = 3.14 * r ** 2
    p = 2 * 3.14 * r
    print(f"Programm väljastab konsoolis: Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r*2,360)
    turtle.done()

except:
    print("Sissetus vale!")



"""
#Kingituste pakkimine
try:
    kast = 5
    kingitusteArv = int(input("Lisa kingituste arv:"))
    komplektid = kingitusteArv // kast # täisarvu saamine
    yle = kingitusteArv % kast #jäägi saamine
    print(f"Saad teha {komlektid} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print("Lisasid koguse valesti")
<<<<<<< HEAD
>>>>>>> 431736d48c9bfeeaf17fd0a4e6bfcb6f51bdde28
=======
>>>>>>> 431736d48c9bfeeaf17fd0a4e6bfcb6f51bdde28
"""



"""
<<<<<<< HEAD
<<<<<<< HEAD
#2. Raamatute allahindus
ale = 0.3
kogus = 3
hind = 12.53
summa = hind - (hind * ale) * kogus
print(f"{kogus} raamatu hind soodustusega on {summa:0.2}€")
"""



=======
=======
>>>>>>> 431736d48c9bfeeaf17fd0a4e6bfcb6f51bdde28
#Faili allalaadimine
try: 
    failiSuurus = int(input("Sisesta faili suurus: "))
    downlKiirus = int(input("Sisesta allalaadimise kiirus: "))
    aeg = failiSuurus/downlKiirus
    prind(f"Allalaadimiseks kulub {aeg} sekundit")
except:
    print("Sa ei sisestanud täisarvu!")
"""


"""
#Raamatute allahindlus
ale = 0.3
hind = 12.5
kogus = int(input("Lisa raamatute kogus:"))
summa = (hind-(hind*ale))*kogus
print(f" {kogus} raamatu hind soodustusega on {summa:0.2f}€.")
"""


<<<<<<< HEAD
>>>>>>> 431736d48c9bfeeaf17fd0a4e6bfcb6f51bdde28
=======
>>>>>>> 431736d48c9bfeeaf17fd0a4e6bfcb6f51bdde28
"""
#1. Aia pikkus
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))
p = 2 * (a + b)
print(f"Aia kogupikkus om {p} meetrit.")
<<<<<<< HEAD
<<<<<<< HEAD
"""


=======
"""
>>>>>>> 431736d48c9bfeeaf17fd0a4e6bfcb6f51bdde28
=======
"""
>>>>>>> 431736d48c9bfeeaf17fd0a4e6bfcb6f51bdde28
