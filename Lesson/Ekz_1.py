# Задача 1

num = [1, 2, 3, 4, 5, 6, 7]
k = 0
c = 0
for i in num:
    if i % 2 == 0:
        k += 1
    else:
        c += 1

for a in num:
    if k > c:
        print(sum(a))
    else:
        print(num[0] * num[2] * num[-2])

