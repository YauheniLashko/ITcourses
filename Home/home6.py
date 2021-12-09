list = [15, 48, 'hello', 6, 19, 'world']
v = 0  # счетчик гласных
q = 0  # счетчик букв
for i in list:
    if type(i) is int:
        if i % 2 == 0:
            k = 0
            if i // 10 > 0:  # проверка на наличие десятичных
                k = i // 10 + i % 10
                print(k)  # печатает сумму цифр четных чисел
        else:
            list[list.index(i)] = 1  # меняем нечетные значения на 1
#print(list)


    elif type(i) is str:
        for a in i:
            if a in 'aeiouy':
                v += 1
            elif a.isalpha():
                q += 1

print("Количество гласных в списке:", v)
print("Количество согласных в списке:", q)
# делаем лист гласных букв
# vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#
# for vowel in vowels:
#     for string in list:
#         if type(string) is str:
#             if vowel in string:
#                 v += 1
#
# for k in list:
#     if type(k) is str:
#         for l in k:
#             q += 1
# print("Количество гласных в списке:", v)
# print("Количество согласных в списке:", q - v)
