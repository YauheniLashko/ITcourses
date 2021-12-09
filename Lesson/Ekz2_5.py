# можно реализовать корзину, чтобы не покупать по 1 товару, предусмотреть исключения и прочее, но в ТЗ такого нет :)

tovar = {'Торт': ['мука, яйцо, сахар, сливочное масло, вишня', 100, 1000],
         'Пирожное': ['молоко, сахар, какао, сгущеное молоко', 30, 750],
         'Маффин': ['яйцо, молоко, сахар, разрыхлитель, какао', 20, 500]}
price = []
print('Вас приветствует магазин "Обожраться!".')
while True:
    choise = input('Выберите категорию:\n1 - Посмотреть всю информацию о товаре\n2 - Посмотреть описание\n'
                   '3 - Посмотреть цену\n4 - Посмотреть количество\n5 - Приступить к покупке\n6 - До свидания! ')
    if choise == '1':
        for key, value in tovar.items():
            print(f'Наименование: {key}\nСостав: {tovar[key][0]}\nСтоимость за кг: {tovar[key][1]}$\n'
                  f'Количество: {tovar[key][2]} грамм')
            print('---------------')
    elif choise == '2':
        for key, value in tovar.items():
            print(f'Наименование: {key}\nСостав: {tovar[key][0]}')
            print('---------------')
    elif choise == '3':
        for key, value in tovar.items():
            print(f'Наименование: {key}\nЦена за кг: {tovar[key][1]}$')
            print('---------------')
    elif choise == '4':
        for key, value in tovar.items():
            print(f'Наименование: {key}\nКоличество: {tovar[key][2]} грамм.')
            print('---------------')
    elif choise == '5':  # и вот тут началось веселье
        user = input('Введите наименование товара или выберете "n" для выхода: ')
        if user == 'Торт' or user == 'Пирожное' or user == 'Маффин':
            kolvo = int(input("Введите количество: "))
            for key, value in tovar.items():
                if kolvo > tovar[user][2]:
                    print('Извините, столько товара нет')
                    break
            else:
                print('Выбранной Вами категории осталось всего', tovar[user][2] - kolvo, 'грамм!')
                print(f'С вас {(tovar[user][1] / tovar[user][2]) * kolvo}$')
                tovar[user][2] = tovar[user][2] - kolvo
        else:
            exit("До встречи!")
    else:
        exit('Давай, досвиданъя!')
