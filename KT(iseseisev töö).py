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
porgandite_arv=0
while i <= ringide_arv:
    if i%2==0:
        porgandite_arv+=1
        print(i)
    i += 1
print(f"porgandite koguarv on: {porgandite_arv}")
'''


#
'''
taring = 5
taringute_arv = int(input("Taringute arv: "))
for i in range(taringute_arv):
    taring = random.randint(1,6)
print(taring)

#
taisarv = 10
nisureta = 0
korda = taisarv 

if taisarv > 64:
    print("Nii palju ruut ei ole")

if taisarv >= 1:
    nisureta +- 1
    taisarv-=1

while korda >= 1:
    nisureta *=2
    korda -=1
print(nisureta)
'''

#
ounu = 14
poise = 3
for i in range(poise):
    ounu -= random.randint(1,2)
print(ounu)



#Iseseisev töö 3
'''
#
fail = open("rebsed.txt",encoding="UTF-8")
vastuvõetud =[]

for rida in fail:
    vastuvõetud.append(int(rida))
print(vastuvõetud)
fail.close()

a = int(input("Palun sissetege, millise aasta andmeid vajate?: "))
print(vastuvõetud[int(a[3])-1])
'''

#
fail = open("konto.txt", encoding="UTF-8")

for rida in fail:
    if float(rida) > 0:
        print(rida,end="")





