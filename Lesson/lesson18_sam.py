# меню каталог корзина удаление из корзины работа с файлами регистрация вход доставка
# почему если я указываю последовательно с новой строки вызов функции в нужной последовательности - последовательность не соблюдается
print("Добро пожаловать в интернет-магазин фильмов 'ImLEO'")
action = ("Джон Уик", "Джеймс Бонд", "Веном", "Малыш на драйве")
sci_fi = ("Spider-man", "Witcher", "Justice League", "Underworld")
comedy = ("Брюс Всемогущий", "Голяк", "Sex Education", "Deadpool")
detective = ("Менталист", "Однажды ночью", "Защищая Джейкоба", "Как избежать наказания за убийство")
thriller = ("Venom 2", "Адвокат дьявола", "Сплит", "Пила")
buy = []


def registration():
    name = input("Введите Ваше имя: ")
    psw = input("Введите пароль: ")
    with open("users.txt", "w", encoding="utf-8") as f:
        f.write(name + ' ' + psw)
    print(f"Очень приятно, {name}!")


registration()


def catalog():
    while True:
        choise = input(
            "Выберите категорию:\n1 - Боевики\n2 - Фантастика\n3 - Комедия\n4 - Детективы\n5 - Триллеры\n6 - Выход ")
        if choise == '1':
            for i, n in enumerate(action):
                i = int(i)
                print(int(i) + 1, n)
            else:
                film = int(input("Выберите фильм: "))
                if film <= len(action):
                    buy.append(action[film - 1])
                    print(buy)
        elif choise == '2':
            for i, n in enumerate(sci_fi):
                i = int(i)
                print(int(i) + 1, n)
            else:
                film = int(input("Выберите фильм: "))
                if film <= len(sci_fi):
                    buy.append(sci_fi[film - 1])
                    print(buy)
        elif choise == '3':
            for i, n in enumerate(comedy):
                i = int(i)
                print(int(i) + 1, n)
            else:
                film = int(input("Выберите фильм: "))
                if film <= len(comedy):
                    buy.append(comedy[film - 1])
                    print(buy)
        elif choise == '4':
            for i, n in enumerate(detective):
                i = int(i)
                print(int(i) + 1, n)
            else:
                film = int(input("Выберите фильм: "))
                if film <= len(detective):
                    buy.append(detective[film - 1])
                    print(buy)
        elif choise == '5':
            for i, n in enumerate(thriller):
                i = int(i)
                print(int(i) + 1, n)
            else:
                film = int(input("Выберите фильм: "))
                if film <= len(thriller):
                    buy.append(thriller[film - 1])
                    print(buy)
        elif choise == '6':
            return buy


catalog()


def watch_cart():
    print(f"У Вас в корзине следующие товары: {buy}. Переходим к покупке!")
    return buy


order = watch_cart()


def transport(order):
    address = input("Введите адрес доставки: ")
    return print(
        f"Вы заказали следующие фильмы: {order}. Заказ прибудет по адресу: {address}. Спасибо, что выбрали ImLEO!")


transport(order)