import time
import shop_file


def print_goods():
    goods = shop_file.get_all_goods()
    for key, value in goods.items():
        print('------------------------')
        print(f'id: {key}\nНазвание: {value["good"]}\nКатегория: {value["category"]}\n'
              f'Цена: {value["price"]}\nКоличество: {value["count"]}')


def buy_cart(cart):
    goods = shop_file.get_all_goods()
    print("Ваша корзина:")
    total_price = 0
    for good_id in cart:
        print('------------------------')
        print(f'id: {good_id}\nНазвание: {goods[good_id]["good"]}\nКатегория: {goods[good_id]["category"]}\n'
              f'Цена: {goods[good_id]["price"]}\nКоличество: {goods[good_id]["count"]}')
        total_price += float(goods[good_id]["price"])
    print('------------------------')
    print(f"Общая сумма: {total_price}")


def menu():
    print("Добрый вечер, вас приветсвует магазин спорт-товаров, сделайте, пожалуйста, заказ")
    cart = []
    while True:
        user_choice = input("Меню\n1-Сделать заказ\n2-Посоветоваться\n3-Оформить заказ\n4 - Показать корзину"
                            "0-Выйти\nВаш выбор: ")
        if user_choice == '1':
            print_goods()
            good_choice = input("Введите id: ")
            cart.append(good_choice)
        elif user_choice == '2':
            money = float(input('Введите количество денег: '))

        elif user_choice == '3':
            buy_cart(cart)
            cart.clear()
        elif user_choice == '0':
            exit("До свидания")

def advise(money):
    goods = shop_file.get_all_goods()
    for key,value in goods.items():
        if money >= float(value['price']):
            print_good(key, value)




def print_cart():
    goods = shop_file.get_all_goods()
    print("Ваша корзина:")
    total_price = 0
    for good_id in cart:
        print('------------------------')
        print(f'id: {good_id}\nНазвание: {goods[good_id]["good"]}\nКатегория: {goods[good_id]["category"]}\n'
              f'Цена: {goods[good_id]["price"]}\nКоличество: {goods[good_id]["count"]}')
        total_price += float(goods[good_id]["price"])
    print('------------------------')
    print(f"Общая сумма: {total_price}")
    return total_price

if __name__ == "__main__":
        menu()


# print("Добрый вечер, вас приветсвует магазин спорт-товаров, сделайте, пожалуйста, заказ")
# while True:
#     user_choice = input("Меню\n1-Сделать заказ\n2-Посоветоваться\n0-Выйти\nВаш выбор: ")
#     user_cart = []
#     if user_choice == '0':
#         print("До свидания")
#         break
#     elif user_choice == "2":
#         user_money = float(input("Введите количество ваших денег: "))
#         if user_money < PRICES[0]*MAXIMIZE[0]:
#             exit("К сожалению, вы ничего не можете купить")
#         else:
#             for price in enumerate(PRICES):
#                 for m in enumerate(MAXIMIZE):
#                     if price[1]*m[1] < user_money:
#                         print(f"Вы можете купить {GOODS[price[0]]} {CHAR[m[0]]}")
#     else:
#         while True:
#             print("Категории товаров:")
#             for ch in enumerate(CHAR):
#                 print(f'{ch[0]+1} - {ch[1]}')
#             char_choice = input("Введите цифру категории, которая вас интересует: ")
#             if int(char_choice) <= len(CHAR):
#                 print("Каталог: ")
#                 for good in enumerate(GOODS):
#                     print(f'{good[0]+1} - {good[1]} {PRICES[good[0]]*MAXIMIZE[int(char_choice)-1]}$')
#                 good_choice = input("Выберите один из товаров по цифре: ")
#                 time.sleep(2)
#                 print("Ваш заказ отправлен на рассмотрение")
#                 if int(good_choice) <= len(GOODS):
#                     time.sleep(2)
#                     print('Ваш заказ принят')
#                     user_cart.append([f'{CHAR[int(char_choice)-1]} {GOODS[int(good_choice)-1]}', PRICES[int(good_choice)-1]
#                                       *MAXIMIZE[int(char_choice)-1]])
#                     question = input('1-Продолжить покупки\n2-Купить всё, что в корзине\n3-Посмотреть корзину')
#                     if question == '1':
#                         continue
#                     elif question == '2':
#                         for i in user_cart:
#                             print(f'''Вы приобрели {i[0]} за {i[1]}$''')
#                         print(f"Общая сумма {sum([i[1] for i in user_cart])}")
#                         print("Спасибо за покупку")
#                         break
#                     elif question == '3':
#                         for i in user_cart:
#                             print(f'''Вы приобрели {i[0]} за {i[1]}$''')
#                     else:
#                         print("Такого выбора нет продолжаем")
#                 else:
#                     print("Такого товара нет")
#             else:
#                 print("Такой категории нет")