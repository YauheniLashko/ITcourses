

def calc(num1, num2):
    def oper(par):
        if par == '+':
            return num1+num2
        elif par == '-':
            return num1-num2
        elif par == '*':
           return num1*num2
        else:
            try:
                return num1/num2
            except ZeroDivisionError:
                exit("Пока")
    return oper(par)


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
par = input('Укажите операцию (+-*/): ')
print(calc(num1, num2))