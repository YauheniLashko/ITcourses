a = [1, 2, 3, 4, 4, 2, 7, 1, 5, 4, 4] # 1, 2, 4, 4 - повторы
# for i in a:
#     if a.count(i) == 2:
#         print(i, 'образовала пару') # да, некрасиво. да, повторяются. но тут важнее скорость

# b = int(input(' числа '))
couples = dict.fromkeys(set(a), 0)
for i in enumerate(a):
    for j in a[i[0]+1:]:
        if j == i[1]:
            couples[i[1]] += 1
print(couples)


for key, value in couples.items():
    if value != 0:
        print(f'{key} - {value} пар')