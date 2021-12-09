a = float(input("сумма на карте "))
i = float(input('расходы '))
s = 0
while i < a:
    a -= i
    s += 1
    i = float(input("расходы "))
print(f'Остаток на карте {a}, совершено покупок {s}')