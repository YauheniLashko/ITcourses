print("Здравствуйте, Вас приветствует Банк!")
print("Выберите номер лицевого счета для работы.")
choise_money = int(input("Нажмите '1' для работы со счетом №1\nНажмите '2' для работы со счетом №2: "))
money = 0 # первый лицевой счет
money_2 = 0 # второй лицевой счет пользователя
while True:
    if choise_money == 1:
        print(f"Вы выбрали счет №{choise_money}!")
    elif choise_money == 2:
        print(f"Вы выбрали счет №{choise_money}!")
    print("Выберите категорию:\n1 - Открыть счет\n2 - Перевести деньги\n3 - Пополнить счет\n4 - Посмотреть баланс\n5 - Сменить лицевой счет\n6 - Выйти")
    cat = int(input('Введите номер категории: '))
    if cat == 1:
        print('В какой валюте Вы желаете открыть счет?\n1 - USD\n2 - Euro')
        val = int(input("Укажите валюту: "))
        if val == 1:
            print("USD счет открыт!")
        else:
            print("Euro счет открыт!")
    elif cat == 2:
        print("Вы желаете перевести деньги\n1 - на иной свой лицевой счет\n2 - в пользу третьего лица?")
        ls = int(input('Выберите категорию: '))
        if ls == 1:
            print("Какую сумму вы хотите перевести?")
            mon = int(input("Введите сумму: "))
            if choise_money == 1:
                if mon > money:
                    print('Недостаточно средств для перевода!')
                else:
                    print("Деньги успешно переведены!")
                    money -= mon
                    money_2 += mon
            elif choise_money == 2:
                if mon > money:
                    print('Недостаточно средств для перевода!')
                else:
                    print("Деньги успешно переведены!")
                    money += mon
                    money_2 -= mon
        elif ls == 2:
            ls = int(input("Введите номер лицевого счета: "))
            print("Какую сумму вы хотите перевести?")
            mon = int(input("Введите сумму: "))
            if choise_money == 1:
                if mon > money:
                    print("Недостаточно средств для перевода")
                else:
                    print(f'Деньги в количестве {mon} переведены на счет {ls}')
                    money -= mon
                    money_2 += mon
            else:
                if mon > money_2:
                    print("Недостаточно средств для перевода")
                else:
                    print(f'Деньги в количестве {mon} переведены на счет {ls}')
                    money_2 -= mon
                    money += mon
    elif cat == 3:
        print('На какую сумму желаете пополнить счет?')
        choise = float(input("Введите сумму для зачисления: "))
        if choise_money == 1:
            money += choise
            print(f'Вы успешено пополните баланс на {choise}')
        else:
            money_2 += choise
            print(f'Вы успешено пополните баланс на {choise}')
    elif cat == 4:
        if choise_money == 1:
            print(f'Ваш баланс составляет {money}')
        else:
            print(f'Ваш баланс составляет {money_2}')
    elif cat == 5:
        print("Выберите номер лицевого счета для работы.")
        choise_money = int(input("Нажмите '1' для работы со счетом №1\nНажмите '2' для работы со счетом №2: "))
    else:
        exit("Всего хорошего!")