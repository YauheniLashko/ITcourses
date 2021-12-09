with open('test.txt') as f:
    k = 0
    l = f.readlines(1)
    for n in l:
        n = n.replace('_', ' ')
        n = n.replace('\n', '')
        m = n.split(' ')
        for c in m:
            if c.isdigit():
                k += int(c)
        print(k)
# with open('test.txt') as f:
#     s = f.readlines(1)
#     print(s)
# for i in s:
#     i = i.replace('_', ' ')
#     i = i.replace('\n', '')
#     l = i.split(' ')
#
# print(l)
# sum = 0
# for i in l:
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)