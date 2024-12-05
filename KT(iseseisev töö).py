#05.12.2024 Yuna Antonenko
#KT
import random

#Iseseisev töö 1
'''
#
print("Tere, maailm!")

#
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = "aasta liblikas on: "

def lause():
    print(aasta,lause_keskosa,liblikas)
lause()

#
kõrgus = int(input("Pilve kõrgus: "))

if kõrgus >= 6:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")
    

#
inimesed = 60
inimekohad = 40

bussid = inimesed//inimekohad
vimases_bussis = inimesed&inimekohad
if vimases_bussis==0:
    print(f"Selle arvu inimeste jaoks on vaja {bussid} buss, vimases bussion {inimekohad}")
else:
    print(f"Selle arvu inimeste jaoks on vaja {bussid+1} buss, vimases bussion {vimases_bussis}")

'''


#Iseseisev töö 2
'''
#
kordade_arv = int(input("Sisseta mitu korda äratada: "))
for i in range(kordade_arv):
    print("Tõuse ja säru!")

#
ringide_arv = int(input("Sisseta ringide arv: "))
koguarv = 0
ring = 1
while ring <= ringide_arv:
    if ring % 2 == 0:
        koguarv +- ring 
    ring +- 1
print(f"Porgandite koguarv on {koguarv}.")

ringide_arv=6
i = 1
while i < ringide_arv:
    print(i)
    i += 1
'''


#
taringute_arv = int(input("Taringute arv: "))
for i in range(taringute_arv):
    taring = random.randint(1,6)
print(taring)





