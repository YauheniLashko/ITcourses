# Задача 2

text = input('Введите текст:')
vowels = 0
ne_vowels = 0
a = []
for i in text:
    if i.lower() in 'aeiouy':
        a.append(i)
        vowels += 1
    elif i.lower() in 'bcdfghjklmnpqrstvwxz':
        ne_vowels += 1
print(f'Глассных: {vowels}')
print(f'Согласных: {ne_vowels}')


if vowels == ne_vowels:
    print(f'Количество глассных и согласных совпадает. Глассных: {vowels},{a}')
