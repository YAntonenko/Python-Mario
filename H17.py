#29.11.2024 Yuna Antonenko
#Ülesane 17
import optparse


'''
fail = open("pangakonto.txt")

print(fail.readlines())

loend = fail.readlines()


print(f"Tehinguid kokku {tehingute_arv}")
print("Pos tehinguid kokku: {pos_tehinguvad}")
print("Tehingute summa: {pos_tehingute_summa}")

for i in loend:
    print(i)


'''



#Palgatõendid

with open("palgad.txt") as fail:
    loend = fail.readlines()
    print(loend)



fail = open("palgad.txt")

loend = fail.readlines()
tehingute_arv = len(loend)

mehed =[]
naised = []
palk= []


for i in loend:
    andmed = i.strip()
    
    nimi = float(andmed[2])
    isikukod = float(andmed[3])
    sugu = float(andmed[4])
    töötunnid = float(andmed[5])
    tunnitasu = float(andmed[6],"€")
    palk = float(andmed[7])


for i in loend:
    print(i.split(","))
    mehed.append(float(palk))
    naised.append(float(palk))

print([nimi], [isikukod], [sugu], [töötunnid], [tunnitasu], [palk])

fail.close()













