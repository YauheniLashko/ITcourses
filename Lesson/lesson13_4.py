with open('test3.txt') as f:
    i = 0
    for sen in f:
        i += 1
        l = sen.replace('\n', '')
        print(len(l))
print(i)