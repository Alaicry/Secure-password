#Подключение библиотек
import random
from string import digits
from string import punctuation
from string import ascii_letters
#Цикл генерации 5ти паролей
for i in range(5): 
#Генерация безопасного пароля
    symbols = ((ascii_letters + digits + punctuation)
               + (ascii_letters + digits + punctuation)
               + (ascii_letters + digits + punctuation)) 
    sec_pass = random.SystemRandom()
    password = "". join(sec_pass.choice(symbols) for i in range(36))
#Запись в текстовый документ
    file = open(r'C:\\Users\Раиль\Desktop\F3%ui(f5@petTN-zncaJ9R,L3US8B\password.txt', 'a')
    file.write(password)
    file.write('\n')
    file.write('\n')
    file.close()
#Чтение(необязательно)
    file = open(r'C:\\Users\Раиль\Desktop\F3%ui(f5@petTN-zncaJ9R,L3US8B\password.txt', 'r')
    text = file.read()
    file.close()
    print(text)
