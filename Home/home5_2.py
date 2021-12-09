'''
комп генерирует числа от 1 до 10 и от 1 до 2 соответственно. 1-10 = номера, 1,2 = красный, черный.
5 попыток угадать номер и цвет (пример: 5 красный). в случае неудачи вывести верную комбинацию.
'''
from random import randint

num = randint(1, 10)
color = randint(1, 2)
player_num = int()
player_color = int()
count = 5

while count > 0:
    # plauer_num = player_num.split()
    player_num = int(input('Введите число от 1 до 10: '))
    player_color = int(input('Введите число от 1 до 2: '))
    if player_num == num and player_color == color:
        print('Вы  угадали!')
        break
    else:
        print('Неверно')
    count -= 1

if count == 0:
    print(num, color)
