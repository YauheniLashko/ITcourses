# написать фигуру (прямоугольник, треугольник, круг), указать стороны и узнать периметр.
# не дать сломать отрицательными и строками
#rectangle = "прямоугольник"
#triangle = "треугольник"
#circle = "круг"


while True:
    try:
        figure = input("Выбери фигуру: \n1) Прямоугольник \n2) Треугольник \n3) Круг \n")
    except EOFError:
        print("Ну зачем Вы сделали мне EOF?")
        break
    except:
        print("Ну и как мне это нарисовать?")
        continue
    if figure == "прямоугольник" or figure == "треугольник" or figure == "круг":
        break


while True:
    if figure == 'прямоугольник':
        try:
            q1 = int(input("Введите длину одной стороны: "))
        except EOFError:
            print('Ну зачем Вы сделали мне EOF?')
            break
        except:
            print("Ну и как мне это нарисовать?")
            continue
        if q1 <= 0:
            print("Неверно указанная величина. Повторите ввод.")
            continue
        while True:
            try:
                q2 = int(input("Введите длину другой стороны: "))
            except EOFError:
                print('Ну зачем Вы сделали мне EOF?')
                break
            except:
                print("Ну и как мне это нарисовать?")
                continue
            break
#        q2 = int(input("Введите длину другой стороны: "))
        while True:
#            q2 = int(input("Введите длину другой стороны: "))
            if q2 <= 0: # хз куда вставить отдельный цикл на q2
                print("Неверно указанная величина. Повторите ввод.")
                try:
                    q2 = int(input("Введите длину другой стороны: "))
                except:
                    print("Ну и как мне это нарисовать?")
                    continue
            else:
                break
        print("Периметр равен: ", q1*2 + q2*2)
        break
    elif figure =='треугольник':
        try:
            a1 = int(input("Введите сторону: "))
        except EOFError:
            print('Ну зачем Вы сделали мне EOF?')
            break
        except:
            print("Ну и как мне это нарисовать?")
            continue
        if a1 <= 0:
            print("Неверно указанная величина. Повторите ввод.")
            continue
        print("Периметр равен: ", a1*3)
        break
    elif figure == "круг":
        try:
            r = int(input("Введите радиус: "))
        except EOFError:
            print('Ну зачем Вы сделали мне EOF?')
            break
        except:
            print("Ну и как мне это нарисовать?")
            continue
        if r <= 0:
            print("Неверно указанная величина. Повторите ввод.")
            continue
        print("Диаметр равен: ", r*2)
        break