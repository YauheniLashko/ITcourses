arr = [1,2,3,4,5]
index = int(input('Index'))
b  =int(input('Меняем'))
try:
    a[index] = b
except IndexError:
    print('Такого нет')
# for i,k in enumerate(arr):
#     try:
#         a = int(input('Введите индекс: '))
#         arr[i] = a
#         print(arr[a])
#     except IndexError:
#         print('Отсутствует индекс.')
#         a = int(input('Введите индекс'))