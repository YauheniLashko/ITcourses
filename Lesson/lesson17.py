def func1(a,b):
    def func2(c):
        return c**3
    return func2(a) + func2(b)
print(func1(2,3))