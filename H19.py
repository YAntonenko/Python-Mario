# 14.01.2025 Yuna Antonenko


#  1   Отобразить список учеников 12-го класса
#  2   Покажите, сколько учеников учатся в 10, 11 и 12 классе.
#  3   Покажите, какие упражнения посещают ученики
#  4   Отображение ведомости оценок учащегося 12 класса (имя, предметы, баллы)


import json 



with open ('haridustulemused.json', 'r', encoding='utf-8') as file:
    haridustulemused = json.load(file)



for hl in haridustulemused:
    id = hl['id']
    nimi = hl['nimi']
    klass = hl['klass'] 
    hinded = hl['hinded']
    tegevused = hl['tegevused']
    klasside_arv = []

        #1
    if klass == "12":
        print(f"12 klass: {klass} õpilast")
        print(nimi)        
        
        #3
        print(f"Tegevused: {tegevused}")

        #4
        print(f"Hinded: {hinded}")

        #2
        klasside_arv = []
        









# for hl in haridustulemused:
#     id = hl['id']
#     nimi = hl['nimi']
#     klass = hl['klass'] 
#     hinded = hl['hinded']





















