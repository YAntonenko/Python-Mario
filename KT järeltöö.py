# 07.01.2025 Yuna Antonenko
#KT1

# ÜLESANNE 3 - Einstein

c = 300000000 
mass = int(input("Sisesta mass kilogrammides: "))
energy = mass * c**2
print(f"Massile {mass} kg vastav energia on {energy} džauli.")



# ÜLESANNE 8 - NämNaäm

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

x, y = map(int, input("Sisesta kütus (X/Y): ").split("/"))
if y == 0 or x > y:
    print("Viga.")
else:
    p = round((x / y) * 100)
    print("E" if p <= 1 else "F" if p >= 99 else f"{p}%")
