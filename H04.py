#16.10.2024 Yuna Antonenko
#Ülesanded 4
import turtle


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
"""



"""
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


"""
#1. Aia pikkus
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))
p = 2 * (a + b)
print(f"Aia kogupikkus om {p} meetrit.")
"""