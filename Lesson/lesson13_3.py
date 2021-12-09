with open('test3.txt', 'w', encoding='utf-8') as f:
    while True:
        user = input('Введите текст: ')
        f.write(user + '\n')
        if user == '':
            break