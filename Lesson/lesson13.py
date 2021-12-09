f = open('poem.txt')
l = f.readlines()

k = 0
for i in l:
    i = i.split()
    for n in i:
        if n.isdigit():
            k += int(n)
print(k)

f.close()
