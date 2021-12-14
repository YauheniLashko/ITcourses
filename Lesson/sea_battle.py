letters = "АБВГДЕЖЗИК"
moves = [i+str(a) for i in letters for a in range(1,11)]
players_ships = {"one_cell": [], "two_cell": [], "three_cell": [], "four_cell": []}


def input_cell(message):
    cell = input(message)
    while cell.upper() not in moves:
        print("Неккоректно введена клетка")
        cell = input(message)
    return cell


def ships_coordinate():
    field = dict.fromkeys(moves, True)
    print_field(field)
    for i in range(4):
        coordinate = input_cell("Введите клетку для однопалубного корабля")
        players_ships["one_cell"].append((coordinate,))
        field[coordinate] = False
        print(players_ships)
        print_field(field)
    for i in range(3):
        two_cell_ship = []
        two_cell_ship.append(input_cell("Введите клетку для двупалубного корабля: "))
        print("Возможные клетки для продолжения: ")
        if(letters.index(two_cell_ship[0][0]) != 9):
            print(moves[moves.index(two_cell_ship[0]) + 10])
        if(letters.index(two_cell_ship[0][0]) != 0):
            print(moves[moves.index(two_cell_ship[0]) - 10])
        if (int(two_cell_ship[0][1]) != 10):
            print(moves[moves.index(two_cell_ship[0]) + 1])
        if int(two_cell_ship[0][1]) != 1:
            print(moves[moves.index(two_cell_ship[0]) -1])


def print_field(field):
    for key, value in field.items():
        if value:
            print(key, end=" ")
        else:
            print("  ", end=" ")
        if int(key[1:]) == 10:
            print()

ships_coordinate()
