def func(user):
    if type(user) == tuple:
        for i in user:
            print(len(i))
    elif type(user) == list:
        for i in user:
            a = 0
            b = 0
            for l in i:
                if l.isdigit():
                    a += 1
                else:
                    b += 1
            print(a, b)
    elif type(user) is int:
        f = 0
        for i in str(user):
            i = int(i)
            if i % 2 != 0:
                f += 1
        print(f)
    elif type(user) is str:
        s = 0
        for i in user:
            s += 1
        print(s)





func('sss')