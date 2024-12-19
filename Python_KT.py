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

with open('palk.txt', 'w') as file:
    file.write("Hubert Hunt m 2340\n")
    file.write("Siim Siil m 2570\n")
    file.write("Märt Mäger m 1960\n")
    file.write("Vilma Vihmauss n 2060\n")
    file.write("Merike Metskits n 2250\n")
    file.write("Kati Karu n 2370\n")
    file.write("Elmar Elevant m 2900\n")
    file.write("Timoteus Tigu m 2850\n")
    file.write("Reet Rebane n 2340\n")
    file.write("Kalev Kaamel m 2570\n")
    file.write("Karmen Kass n 2120\n")
    file.write("Kornelius Koer m 2250\n")


def analyze_discrimination(file_path):
    m_palk = []
    n_palk = []
    
    with open(file_path, 'r') as file:
        for line in file:
            andmed = line.strip()
    
            nimi = float(andmed[1])
            sugu = float(andmed[3])
            palk = float(andmed[4])
            
            if sugu == 'm':
                m_palk.append(palk)
            else:
                n_palk.append(palk)
        print([nimi], [sugu], [palk])

    avg_m_palk = sum(m_palk) / len(m_palk) if m_palk else 0
    avg_n_palk = sum(n_palk) / len(n_palk) if n_palk else 0

    if avg_m_palk > avg_n_palk:
        print("Discrimination detected: Mehed earn more on average.")
    elif avg_n_palk > avg_m_palk:
        print("Discrimination detected: Naised earn more on average.")
    else:
        print("No discrimination detected: Palkad are equal on average.")

analyze_discrimination('palk.txt')















sugu = m


#16




























































