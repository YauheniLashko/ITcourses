import math

choise = input("Введите фигуру, площадь которой ищем: ")
PI = math.pi


def square_circle():
    diametr = float(input("Введите диаметр круга: "))
    return PI * diametr


def square_rectangle():
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    return length * width


def square_triangle():
    a1 = float(input("Введите длину первой стороны треугольника: "))
    a2 = float(input("Введите длину второй стороны треугольника: "))
    a3 = float(input("Введите длину третьей стороны треугольника: "))
    p = (a1 + a2 + a3) / 2

    return math.sqrt(p * ((p - a1) * (p - a2) * (p - a3)))


if choise == "круг":
    print(square_circle())
elif choise == "прямоугольник":
    print(square_rectangle())
else:
    print(square_triangle())
