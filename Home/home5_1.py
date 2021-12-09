wins = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7]]
player_x = []
player_o = []
count = 9
x = int()
wins.sort()

while count > 0:
    x = int(input('Введите число от 1 до 9: '))
    while x not in range(1, 10):
        x = int(input('Введите число от 1 до 9: '))
    while x in player_x or x in player_o:
        x = int(input('Введите число от 1 до 9: '))
    else:
        player_x.append(x)
    print("Ваши ходы:", player_x)
    count -= 1
    if count == 0:
        print('Ничья!')
        break
    player_x.sort()
    if [i for i in player_x] == [j for j in wins[0]] or \
            [i for i in player_x] == [j for j in wins[1]] or \
            [i for i in player_x] == [j for j in wins[2]] or \
            [i for i in player_x] == [j for j in wins[3]] or \
            [i for i in player_x] == [j for j in wins[4]] or \
            [i for i in player_x] == [j for j in wins[5]] or \
            [i for i in player_x] == [j for j in wins[6]] or \
            [i for i in player_x] == [j for j in wins[7]]:
        print("CROSSES WIN")
        break
    for win in wins:
        index = 0
        for i in win:
            if i in player_x:
                index += 1
        if index == 3:
            print("CROSSES WIN")
            break  # не брейкает, а дальше требует ввод чисел ?!
    x = int(input('Введите число от 1 до 9: '))
    while x not in range(1, 10):
        x = int(input('Введите число от 1 до 9: '))
    while x in player_x or x in player_o:
        x = int(input('Введите число от 1 до 9: '))
    else:
        player_o.append(x)
    print("Ходы соперника:", player_o)
    count -= 1
    player_o.sort()
    if [i for i in player_o] == [j for j in wins[0]] or \
            [i for i in player_o] == [j for j in wins[1]] or \
            [i for i in player_o] == [j for j in wins[2]] or \
            [i for i in player_o] == [j for j in wins[3]] or \
            [i for i in player_o] == [j for j in wins[4]] or \
            [i for i in player_o] == [j for j in wins[5]] or \
            [i for i in player_o] == [j for j in wins[6]] or \
            [i for i in player_o] == [j for j in wins[7]]:
        print("ZEROES WIN")
        break
    for win in wins:
        index = 0
        for i in win:
            if i in player_o:
                index += 1
        if index == 3:
            print("ZEROES WIN")
            count = 0
            break
