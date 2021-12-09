import random

l = 0  # считаем сколько раз встретиламсь цифра
count = int(input('Сколько сгенерировать чисел?'))
num = int(input('Какую цифру будем искать?'))
arr = []
for i in range(count):
    c = random.randint(1, 100)
    arr.append(c)
    print(c)
for k in arr:
    for b in str(k):
        if str(num) == b:

            l += 1
print(f'Цифра {num} встертилась {l} раз')

