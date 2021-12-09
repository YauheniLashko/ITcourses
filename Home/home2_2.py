num1 = int(input("Enter 1 number: "))
num2 = int(input("Enter 2 number: "))
num3 = int(input("Enter 3 number: "))


if sum([num1, num2]) == num3:
    print(num1, "+", num2, '=', num3)
elif sum([num1, num3]) == num2:
    print(num1, "+", num3, '=', num2)
elif sum([num2, num3]) == num1:
    print(num3, "+", num2, '=', num1)
else:
    print("Wrong numbers")