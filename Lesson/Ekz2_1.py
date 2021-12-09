spisok = list('eto spisok s povtorami simvolov')
simbol = []

for i in spisok:
    if spisok.count(i) == 1:
        simbol.append(i)
print('неповторяющиеся символы: ', simbol)