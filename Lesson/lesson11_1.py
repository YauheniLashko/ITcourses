import random

dic = {'name1': [random.randint(0, 10) for i in range(1)],
       'name2': [random.randint(0, 10) for k in range(1)],
       'name3': [random.randint(0, 10) for l in range(1)],
       'name4': [random.randint(0, 10) for n in range(1)]}
print(dic)
small = min(dic.values())
print(small)
x = 0
for k in dic.values():
    x += 1

a = sum(sum(value) for value in dic.values())
print(a)

a = 'asdasdad'