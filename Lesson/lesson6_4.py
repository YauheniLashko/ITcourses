# сделать список с пересечениями
a = [5, [1,2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)

print(c)

for q in a:
    if q in b:
        c.append(q)

print(c)