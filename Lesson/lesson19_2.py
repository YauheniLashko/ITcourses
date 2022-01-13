class Calc:

    def __init__(self):
        self.a = int(input("First"))
        self.b = int(input("Second"))
        self.d = input("operator")


    def plus(self):
        print(self.a + self.b)

    def minus(self):
        print(self.a - self.b)

    def mult(self):
        print(self.a * self.b)

    def delen(self):
        print(self.a / self.b)


c = Calc()
if c.d == "+":
    c.plus()
elif c.d == "-":
    c.minus()
elif c.d == "*":
    c.mult()
elif c.d == "/":
    c.delen()

# class TheExample:
#     def __init__(self):
#         self.a = int(input("1"))
#         self.b = int(input("2"))
#
#     def func(self):
#         return self.a + self.b
#
#     def func1(self):
#         return self.a - self.b
#
#     def fun2(self):
#         return self.a * self.b
#
#     def func3(self):
#         return self.a / self.b
#
#
# while True:
#     x = input("symb")
#     print("Numb")
#     example = TheExample()
#     if x == '6':
#         break
#     elif x == '+':
#         print(example.func())
#     elif x == '-':
#         print(example.func1())
#     elif x == '*':
#         print(example.fun2())
#     elif x == '/':
#         print(example.func3())
