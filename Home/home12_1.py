while True:
    a = input('Введите первую строку: ')
    b = input('Введите вторую строку: ')
    for i in a:
        for k in b:
            if i == k:
                print(set(i), end='')