coin = 0
guess = int(input("Введите стоимость услуги: "))

while guess > 0:
    if guess >= 25:
        coin += 1
        guess -= 25
    elif guess >= 10:
        coin += 1
        guess -= 10
    elif guess >= 5:
        coin += 1
        guess -= 5
    elif guess >= 1:
        coin += 1
        guess -= 1
print(coin)