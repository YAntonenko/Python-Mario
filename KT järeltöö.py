# 07.01.2025 Yuna Antonenko
#KT1

# ÜLESANNE 3 - Einstein

# Isegi kui sa pole füüsikat (hiljuti või üldse!) õppinud, oled ilmselt kuulnud valemist E=mc², kus:

#     E tähistab energiat (mõõdetuna džaulides)
#     m tähistab massi (mõõdetuna kilogrammides)
#     c tähistab valguse kiirust (ligikaudu 300 000 000 meetrit sekundis)
# Albert Einsteini ja tema kaasautorite järgi tähendab see valem sisuliselt, et mass ja energia on ekvivalentsed.

# Failis nimega einstein.py loo programm Pythonis, mis küsib kasutajalt massi täisarvuna (kilogrammides) ja väljastab ekvivalendi energia džaulides täisarvuna. Eelda, et kasutaja sisestab alati täisarvu.


c = 300000000 
mass = int(input("Sisesta mass kilogrammides: "))
energy = mass * c**2
print(f"Massile {mass} kg vastav energia on {energy} džauli.")


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

aeg = input("Sisesta aeg: ")
tunnid, minutid = map(int, aeg.split(":"))
t = tunnid + minutid / 60

if 7 <= t <= 8:
    print("On aeg hommikusöögiks!")
elif 12 <= t <= 13:
    print("On aeg lõunasöögiks!")
elif 18 <= t <= 19:
    print("On aeg õhtusöögiks!")



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

x, y = map(int, input("Sisesta kütus (X/Y): ").split("/"))
if y == 0 or x > y:
    print("Viga.")
else:
    p = round((x / y) * 100)
    print("E" if p <= 1 else "F" if p >= 99 else f"{p}%")
'''