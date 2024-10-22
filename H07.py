#22.10.2024 Yuna Antonenko
#Ülesanded 7 Loendid 
import datetime 

# Tänane kuu number
x = datetime.datetime.now()
tana = int(x.strftime('%m')) -1


#12 kuud
kuud = [["jaanuar",-2,11,-11,-5,-20,-12,26,15,9,30,12,-3,-10,23,-14,5,-11,-1,-2,6,1,-7,-9,-18,21,-20,-4,-18,23,-10,-11],
["veebruar",4,27,22,5,4,24,17,-18,4,-5,22,-10,20,0,24,-7,-15,10,25,8,20,6,17,-15,14,-17,-18,14],
["marts",17,4,1,-16,12,-1,-2,-8,30,3,1,16,18,-2,10,18,7,19,-20,-7,6,13,17,-9,11,12,2,0,14,16,-14],
["aprill",24,-11,-3,10,25,-18,15,9,-14,-6,30,-20,-15,2,13,25,29,15,-18,7,-10,23,8,5,-3,-10,-20,1,0,-2],
["mai",-6,-8,6,-9,21,15,-18,-19,-3,15,13,6,8,-18,1,5,27,20,-5,21,-12,6,29,-4,8,19,10,25,-11,12,20],
["juuni",9,15,25,-3,27,19,-6,23,24,19,1,10,-2,3,-20,-12,-17,-12,-13,-18,16,-11,23,16,7,-7,7,-9,-16,19],
["juuli",-8,21,4,-6,27,22,11,-6,-4,-8,-15,-3,-9,4,16,10,6,-7,9,16,8,26,2,6,15,27,5,-20,-16,27,23],
["august",19,3,-3,-17,-3,26,-5,-4,-8,0,-18,22,21,10,-9,-8,-12,9,-20,21,14,13,-4,-2,9,-15,19,20,-5,10,-9],
["september",8,0,2,5,20,16,-15,6,29,27,-16,27,13,-13,5,3,17,26,-3,-10,14,-14,19,-16,6,17,12,29,2,12],
["oktoober",0,19,-12,-7,-18,18,18,-20,28,4,-8,16,-6,-14,-9,28,16,2,25,10,11,26,1,-5,-10,19,15,-8,-12,-5,17],
["november",-16,24,-5,-14,4,10,24,-16,-16,19,14,17,-17,9,-13,18,-6,25,13,-5,0,-1,25,-1,29,16,7,7,4,21],
["detsember",-4,12,30,24,-20,22,-14,9,23,10,-7,2,16,-5,29,25,17,-6,-16,-16,15,-3,28,11,9,22,-17,-5,9,18,-2]]


#ülesanded
print(kuud[tana][0])
print(f"Viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
ajutine = []
for i in range(len(kuud[tana])-1):
    ajutine.append(kuud[tana][i+1])
    print(kuud[tana][i+1], end=", ")
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")

print(f"-20 esineb {ajutine.count(-20)} korda")


ajutine.pop(5)
print(ajutine)




"""
# 1. Loo lugudest loend
muusika = ['ALIKA – "Bridges"','Anett x Fredi – "Read Between The Lines"','villemdrillem – "leekiv armastus"','Clicherik & Mäx – "PAKSUD"','nublu – "ära ärata"','NOËP – "Move Your Feet"','Trad.Attack! – "Bring It On"','Bedwetters – "It Is What It Is"','Reket – "Panama paberid"','Grete Paia – "Võluväel"']

for i in range(len(muusika)):
    print(i+1". "+muusika[i])

try:
    valik = int(input("Vali laul: "))
    print(f"Mängin lugu {muusika[valik-1]}")
except:
    print("Midagi läks katki. Taevita adminni")
"""

    








