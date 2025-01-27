#18.12.2024 Yuna Antonenko
#KT
#10 12 15


#10. Kaugushüpe
"""
tulemused = []

for i in range(3):
    tulemus = float(input(f"Sisestage kaugushüppe tulemus {i + 1}: "))
    tulemused.append(tulemus)

parim_tulemus = max(tulemused)
keskmine_tulemus = sum(tulemused) / len(tulemused)

print(f'Parim kaugushüppe tulemus: {parim_tulemus} m')
print(f'Keskmine kaugushüppe tulemus: {keskmine_tulemus} m')


#12. Eurokalkulaator
valik  = input("Vali suund (1: EUR -> EEK, 2: EEK -> EUR): ")
if valik == "1":
    eur = float(input("Sisesta summa EUR: "))
    eek = eur * 15.6466 
    print(f"{eur} EUR on {eek} EEK")
        
elif valik == "2":
    eek = float(input("Sisesta summa EEK: "))
    eur = eek/15.6466 
    print(f"{eek} EEK on {eur} EUR")
else:
    print("Vale valik")
"""
#15. Temperatuurid
for rida in open('temperatuurid.txt', 'r', encoding= 'UTF-8'):
    osad = rida.split()
    kuu = osad[0]
    temp = map(int, osad[1:])
    print(f"{kuu}: {max(temp)}")




