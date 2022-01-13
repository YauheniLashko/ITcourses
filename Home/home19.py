class Func:
    b = 0
    c = 0
    k = []
    s = 0
    h = 0


    def __init__(self):
        self.a = input("enter: ")
        self.k = self.a



    def dlina(self):
        for i in self.a:
            if i in "aeuio":
                self.b += 1
            else:
                self.c += 1
        if self.b * self.c <= len(self.k):
            for l in self.k:
                if l == "a" or l == "e" or l == "u" or l == "i" or l == "o":
                    print(l)
        elif self.b * self.c > len(self.k):
            for l in self.k:
                if l not in "aeuio":
                    print(l)
        if self.k.isdigit():
            #print(self.k)
            self.h += int(self.k)
            for i in str(self.h):
                if int(i) % 2 == 0:
                    self.b += int(i)
            print(self.b * len(self.a))



f = Func()
f.dlina()
