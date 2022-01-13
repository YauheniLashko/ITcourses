class A:
    def hi(self):
        print("I'm class A")


class B:
    def hi(self):
        print("I'm class B")


class C:
    def hi(self):
        print("I'm class C")


class D(B):
    def say_hi(self):
        print("I'm class D")


class E(B):
    def say_hi(self):
        print("I'm class E")


class F(B):
    def say_hi(self):
        print("I'm class F")


class G(D, A):
    def say_hi(self):
        print("I'm class G")


class H(C, G):
    def say_hi(self):
        print("I'm class H")


class I(D):
    def say(self):
        print("I'm class I")


class J(E, F, G):
    def say(self):
        print("I'm class J")


class K(I):
    def hello(self):
        print("I'm class K")

class L(I):
    def hello(self):
        print("I'm class L")


class M(J):
    def hello(self):
        print("I'm class M")



class N(H):
    def hello(self):
        print("I'm class K")

