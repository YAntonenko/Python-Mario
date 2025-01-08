# 08.01.2025 Yuna Antonenko

# Покажите, сколько команд приняло участие, и откройте список (пунктуация должна быть указана правильно, пропустите первую строку)
# Найдите, сколько игр было у каждой команды (используйте словарь, если команда уже есть в словаре, вы увеличиваете ее значение на +1)
# Найдите победы и поражения каждой команды и запишите результаты в новый CSV-файл, удобный для Excel.

# Date,Team 1,Team 2,Score 1,Score 2
# 20.02.24,Tallinna Kalev,KK Viimsi/Sportland,83,86

import csv

EstonianBasketballGames = 'EstonianBasketballGames.csv'
with open(EstonianBasketballGames, mode='r', encoding='utf-8') as fail:
    dict_reader = csv.DictReader(fail)
   
    for rida in dict_reader:
        print(rida['Team 1'], rida['Team 2'], rida['Score 1'], rida['Score 2'])




         




























