ball = 0

with open('ekz.txt', encoding='utf-8') as f:
    a = f.readlines()
    for i in a:
        i = i.replace('\n', '')
        i = i.split()
        for n in i:
            if n.isdigit():
                ball += int(n)
                if n == '2' or n == '1' or n == '0':
                    print('а вот и этот лузер, написавший меньше, чем на 3: ', i)






print('Средний балл: ', ball / len(a))



