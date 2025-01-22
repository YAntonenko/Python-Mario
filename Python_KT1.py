# 07.01.2025 Yuna Antonenko
#KT1

# ÜLESANNE 3 - Einstein

# Isegi kui sa pole füüsikat (hiljuti või üldse!) õppinud, oled ilmselt kuulnud valemist E=mc², kus:

#     E tähistab energiat (mõõdetuna džaulides)
#     m tähistab massi (mõõdetuna kilogrammides)
#     c tähistab valguse kiirust (ligikaudu 300 000 000 meetrit sekundis)
# Albert Einsteini ja tema kaasautorite järgi tähendab see valem sisuliselt, et mass ja energia on ekvivalentsed.

# Failis nimega einstein.py loo programm Pythonis, mis küsib kasutajalt massi täisarvuna (kilogrammides) ja väljastab ekvivalendi energia džaulides täisarvuna. Eelda, et kasutaja sisestab alati täisarvu.
'''
def arvutada_energia(mass):
    c = 300000000  
    energia = mass * c ** 2
    return energia

def arv():
    mass = int(input("Palun sisestage mass kilogrammides: "))
    energia = arvutada_energia(mass)
    print(f"Ekvivalentenergia on {energia} joules.")
arv()
'''










# ÜLESANNE 8 - NämNaäm

# Oletame, et tavaks on süüa:
#     Hommikusööki vahemikus 7:00 – 8:00
#     Lõunasööki vahemikus 12:00 – 13:00
#     Õhtusööki vahemikus 18:00 – 19:00

# Oleks ju tore, kui sul oleks programm, mis ütleb sulle, millal on aeg süüa?
# Failis sook.py loo programm, mis küsib kasutajalt aega ja väljastab, kas on aeg hommikusöögiks, lõunasöögiks või õhtusöögiks. Kui pole söögi aeg, ei väljasta programm midagi.

# Eelda, et kasutaja sisestab aja 24-tunnises formaadis:

#     #:## või ##:##

# Ja eelda, et iga söögiaja vahemik on kaasav. Näiteks, kui aeg on 7:00, 7:01, 7:59 või 8:00, on aeg hommikusöögiks.
# Programmi struktuur peaks olema järgmine:
#     teisenda aeg (str) 24-tunnises formaadis vastavaks arvuks (float).
#     Näiteks, kui antakse aeg "7:30", tagastab funktsioon 7.5.
#     programm kontrollib aja alusel, kas on hommiku-, lõuna- või õhtusöögi aeg, ja väljastab vastava teate.
'''
from datetime import datetime

def aeg():
    now = datetime.now().strftime("%H:%M")

Hommikusööki_vahemikus_start = "7:00"
Hommikusööki_vahemikus_end = "8:00"
Lõunasööki_vahemikus_start = "12:00"
Lõunasööki_vahemikus_end = "13:00"
Ohtusööki_vahemikus_start = "18:00"
Ohtusööki_vahemikus_end = "19:00"

if Hommikusööki_vahemikus_start <= aeg < Hommikusööki_vahemikus_end:
    print("On aeg hommikusöögiks.")
elif Lõunasööki_vahemikus_start <= aeg < Lõunasööki_vahemikus_end:
    print("On aeg lõunasöögiks.")
elif Ohtusööki_vahemikus_start <= aeg < Ohtusööki_vahemikus_end:
    print("On aeg õhtusöögiks.")
aeg()
'''

# ÜLESANNE 11 - Kütusenäidik

# Kütusenäidikud näitavad sageli murdarvude abil, kui palju kütust on paagis. Näiteks:
#     1/4 näitab, et paak on 25% täis.
#     1/2 näitab, et paak on 50% täis.
#     3/4 näitab, et paak on 75% täis.

# Failis kytus.py loo programm, mis:
#     Küsib kasutajalt murdosa kujul X/Y, kus X ja Y on täisarvud.
#     Arvutab ja väljastab kütusekoguse protsendina (ümardatuna lähima täisarvuni).
#     Kui kütust on 1% või vähem, väljastab E (empty – tühi).
#     Kui kütust on 99% või rohkem, väljastab F (full – täis).
#     Kui kasutaja sisestus ei ole korrektne:
#         X või Y ei ole täisarv
#         X on suurem kui Y
#         Y on 0
#         – küsib programm sisestust uuesti.
# Programmis tuleb kasutada try-except veapüüdmist, et vältida programmi krahhi vigase sisendi korral.

def kytuse_naydik():
    while True:
        try:
            sisend = input("Sisestage kütuse kogus murdosa kujul X/Y: ")
            x, y = map(int, sisend.split('/'))

            if y == 0:
                raise ValueError("Y ei tohi olla 0.")
            if x > y:
                raise ValueError("X ei tohi olla suurem kui Y.")

            protsent = round((x / y) * 100)

            if protsent <= 1:
                print("E")
            elif protsent >= 99:
                print("F")
            else:
                print(protsent)

            break

        except ValueError:
            print("Vale sisend. Palun proovige uuesti.")

kytuse_naydik()



