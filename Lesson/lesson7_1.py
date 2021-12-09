import time

products = ['Апельсин', 'Банан', 'Киви']
price = [5, 7, 10]
criterion = ['Сочный', 'Медовый', 'Не ГМО']
factor = [2, 3, 4]
cart = []

print("Welcome to HELL!")
print("Please, select a product!")
while True:
    choise = input('1 - Сделайте заказ\n0 - Выйти')
    if choise == '0':
        print('До свидания!')
        break
    else:
        print("Категории товаров:")
        for crit in enumerate(criterion):
            print(f"{crit[0] + 1} - {crit[1]}")
        crit_choise = input(" Введите цифру категории, которая вас интересует: ")
        if int(crit_choise) <= len(criterion):
            if crit_choise == 1:
                price *= factor[0]
            elif crit_choise == 2:
                price *= factor[1]
            else:
                price *= factor[2]
            print("Каталог: ")
        for product in enumerate(products):
            print(f'{product[0]+1} - {product[1]} {price[product[0]]}$')
        good_choice = input("Выберите один из товаров по цифре:")
        cart.append(good_choice)
        while True:
            smth = input('Хотите добавить что-то еще? Да = 1 / нет = 0')
            if smth == '0':
                break
            else:
                for product in enumerate(products):
                    print(f'{product[0] + 1} - {product[1]} {price[product[0]]}$')
        time.sleep(2)
        print('Ваш заказ отправлен на рассмотрение!')
        if int(good_choice) <= len(products):
            time.sleep(2)
            print("Ваш заказ принят!")
            print(f"Вы приобрели {products[int(good_choice)-1]}\nС Вас {price[int(good_choice)-1]}$")
        else:
            print("Неправильный товар!")