mas = [1, 'table', 15, 'pen', 3, 'environment']
num = []
word = []
with open('home13.txt', 'a') as f:
    for value in mas:
        if type(value) == int:
            value = int(value)
            num.append(value)
        else:
            word.append(value)
    word.sort(key=len)
    num.sort()
    for el in word:
        f.write(el)
        f.write('\n')
    for elem in num:
        f.write(str(elem))
        f.write('\n')
