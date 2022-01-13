def card():
    user_card = input('введите номер кредитной карты: ')
    return '*'*(len(user_card)-4) + user_card[-4:]

print(card())