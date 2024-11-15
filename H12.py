#15.11.2024 Yuna Antonenko
#Ülesane 12
import turtle
import random
"""
#1
def teemperatuur(temp,yhik):
    
    if yhik=="c":
        v = temp * 5/9 + 32
    else:
        v = (temp - 32) * 5/9
    return round(v,2)

print(teemperatuur(3,"c"))
print(teemperatuur(3,"f"))
print(teemperatuur.__doc__)

"""
#2

kytusKulu = lambda x, y: (x / 100) * y
print

#3
pangakonto = 15

def konto_haldur(saldo, toiming, summa):
    """
    Eriti oluline dokumentatsioon, et kõik aru saaaks
    """
    global pangakonto
    if toiming=="deposiit":
        summa = summa + saldo 
    else:
        summa = summa - saldo

    pangakonto = summa
    return summa

print(konto_haldur(20,"deposiit", pangakonto))
print(konto_haldur(40,"deposiit", pangakonto))
print(konto_haldur(40,"valjavote", pangakonto))












