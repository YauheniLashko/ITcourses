#  Русская рулетка
import random
import time

members_name = []

while True:
    members = int(input("Введите количество игроков: "))
    alive = members
    for name in range(1, members + 1):
        names = input(f'Введите имя игрока {name}: ')
        members_name.append(names)
    while alive != 1:
        bullet = random.randint(1, 6)
#        print(bullet)
        for member in members_name:
            if member == '0':
                continue
            luck = int(input(f'{member} крутит барабан: ')) #  Игрок выбирает число от 1 до 6
            if luck != bullet:
                print('3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(2)
                print(f"Не в этот раз, {member}!")
            else:
                time.sleep(2)
                print(f'Кажется, {member} совсем потерял голову')
                members_name[members_name.index(member)] = '0' # Обнуляем застрелившегося, чтобы не терять индекс
                alive -= 1
                bullet = random.randint(1, 6)
#                print(bullet)
                if alive == 1:
                    members_name.sort()
                    for i in members_name:
                        if i == '0':
                            del members_name[members_name.index(i)] # Удаляем обнулившихся
                    print(f"А вот и наш победитель! это {members_name[-1]}")
                    break