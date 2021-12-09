repeat_num = [1, 2, 3, 1, 5, 2, 7, 3, 1, 7, 2, 6, 7]
num = []
a = 2
for i in repeat_num:
    if a < repeat_num.count(i):
        num.append(i)
print(set(num))

'''
repeat_num = [1, 2, 3, 1, 5, 2, 7, 3, 1, 7, 2, 6, 7]
num = [i for i in repeat_num if repeat_num.count(i) > 2]
print(set(num))
'''