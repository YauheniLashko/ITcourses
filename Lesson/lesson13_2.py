with open('test2.txt') as f:
    l = f.readlines()
    num = []
    word = []
    for sen in l:
        k = sen.replace('\n', '')
        if k.isdigit():
            num.append(int(k))
            num.sort()
        else:
            word.append(k)
            word.sort(key=len)

print(num)
print(word)


# f = open('test2.txt')
# b = []
# n = []
# s = f.readlines()
# print(s)
# for i in s:
#     i = i[:-1]
#     if i.isalpha():
#         i = str(i)
#         b.append(i)
#     elif i.isdigit():
#         i = int(i)
#         n.append(i)
# print(b)
# print(n)
# n.sort()
# b.sort()
# mas = n + b
# print(mas)