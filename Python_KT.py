#18.12.2024 Yuna Antonenko
#KT


#11 Salakeel

#   ваша программа спрашивает пользователя, хочет ли он создать или перевести секретный язык — 1р
#   пользователь вводит обычное слово, которое заменяется на секретный язык - 1p
#   пользователь вводит слово на секретном языке, которое преобразуется обратно в обычный - 1р
#   код с комментариями - 1р
'''
def create_cipher(text):
    return ''.join(chr(ord(char) + 1) for char in text)

def decode_cipher(ciphered_text):
    return ''.join(chr(ord(char) - 1) for char in ciphered_text)

def main():
    choice = input("Do you want to create a cipher (1) or  take the normal word back? (2):  ")
    
    if choice == '1':
        normal_word = input("Enter a normal word to convert to cipher: ")
        ciphered_word = create_cipher(normal_word)
        print(f"Ciphered word: {ciphered_word}")
    elif choice == '2':
        ciphered_word = input("Enter a ciphered word to convert back to normal: ")
        normal_word = decode_cipher(ciphered_word)
        print(f"Normal word: {normal_word}")
    else:
        print("Invalid choice. Please select 1 or 2.")
if __name__ == "__main__":
    main()
'''

#12 Eurokalkulaator

# Создайте программу, которая рассчитывает валюту по запросу пользователя EUR->EEK или EEK->EUR.
# Важно использовать две функции!!

'''
def eur_to_eek(eur_sum):
    rate = 15.65
    return eur_sum * rate

def eek_to_eur(eek_sum):
    rate = 1 / 15.65
    return eek_sum * rate

def main():
    
    choice = input("Choose conversion: 1 (EUR->EEK) or 2 (EEK->EUR):  ")

    if choice == '1':
        eur_sum = float(input("Enter sum in EUR: "))
        print(f"{eur_sum} EUR is {eur_to_eek(eur_sum)} EEK")

    elif choice == '2':
        eek_sum = float(input("Enter sum in EEK: "))
        print(f"{eek_sum} EEK is {eek_to_eur(eek_sum)} EUR")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
'''


#13
# Напишите программу, проверяющую, является ли введенное пользователем число четным или нечетным.
#   отображаются правильные, понятные вопрос и ответ - 1п
#   предыдущая проверка, не добавил ли пользователь число или не установил его равным нулю — 2p
#   код, сообщающий о четном или нечетном числе - 2p
#   отображается название программы - 1п
'''
def check_even_odd():
    print("Hey!")
    number = int(input("Please enter a number:  "))
    
    if number % 2 == 0:
        print(f"The number {number} is even.")

    else:
        print(f"The number {number} is odd.")

check_even_odd()

'''
#14 Palkade võrdlus

# равнение зарплат. Создайте файл «зарплата.txt» с именем, полом и количеством окладов сотрудников
#  (10 сотрудников).
# Создайте программу, которая анализирует, есть ли в компании дискриминация по половому признаку. 
# Для этого сравните самые высокие зарплаты n(naised) и m(mehed). Программа должна принять решение.
'''
with open("palk.txt", "r") as file:
    for line in file:
        file.write(f"{line[0]} {line[1]} {line[2]}\n")

def analyze_pay(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    mehed_palk = []
    naised_palk = []
    for line in data:
        andmed = line.strip().split(', ')
        nimi = float(andmed[1,2])
        sugu = float(andmed[3])
        palk = float(andmed[4])
        if sugu == 'm':
            mehed_palk.append(palk)
        else:
            naised_palk.append(palk)
    mehed_avg = sum(mehed_palk) / len(mehed_palk) if mehed_palk else 0
    naised_avg = sum(naised_palk) / len(naised_palk) if naised_palk else 0
    
    print(f"Meeste keskmine palk: {mehed_avg} €")
    print(f"Naiste keskmine palk: {naised_avg} €")
    
    if mehed_avg > naised_avg:
        print("Mehed teenivad keskmiselt rohkem.")
    elif naised_avg > mehed_avg:
        print("Naised teenivad keskmiselt rohkem.")
    else:
        print("Keskmised palgad on võrdsed.")
file.close()
'''
#16 Täringud
import random

class DiceGame:
    def __init__(self):
        self.user_name = input("Enter your name: ")
        self.user_money = 500
        self.computer_money = 500
    
    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6) 
    
    def play_round(self):
        print(f"\n{self.user_name}'s money: €{self.user_money} | Computer's money: €{self.computer_money}")
        bet = int(input(f"{self.user_name}, place your bet (you have €{self.user_money}): "))
        
        if bet > self.user_money:
            print("You can´t bet more than you have!")
            return
        user_roll = self.roll_dice()
        computer_roll = self.roll_dice()
        print(f"{self.user_name} roll: {user_roll}")
        print(f"Computer roll: {computer_roll}")

        if user_roll > computer_roll:
            self.user_money += bet
            self.computer_money -= bet
            print(f"{self.user_name} win!")
        elif user_roll < computer_roll:
            self.user_money -= bet
            self.computer_money += bet
            print("Computer win!")
        else:
            print("It's tie!")
    
    def play_game(self):
        while self.user_money > 0 and self.computer_money > 0:
            self.play_round()
        
        if self.user_money <= 0:
            print("You have run out of money! Game over.")
        else:
            print("Computer has run out of money! You win!")

if __name__ == "__main__":
    game = DiceGame()
    game.play_game()























































