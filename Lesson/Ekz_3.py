# Задача 3
from random import randint
import copy

k = 0  # сколько раз введенные оказались больше рандомных
l = 0  # сколько раз бот победил
arr = []
bot = []
iter_4 = []

for i in range(9):
    num1 = int(input('Введите первое число от 1 до 20: '))
    arr.append(num1)
    num2 = int(input('Введите второе число от 1 до 20: '))
    arr.append(num2)
    bot1 = randint(1, 20)
    bot.append(bot1)
    bot2 = randint(1, 20)
    bot.append(bot2)
    print(arr, bot)  # чтобы не было скучно тупо вводить циферки
    if arr[0] + arr[1] > bot[0] + bot[1]:
        k += 1
    else:
        l += 1
    if k + l == 4:
        iter_4 = copy.deepcopy(bot)
    arr.clear()
    bot.clear()

print(f'Сумма цифр пользователя была больше рэндома {k} раз')
if k == l:
    print(f'Вау, да ты бот! вот какая была 4-ая итерация у рэндома: {iter_4}')
