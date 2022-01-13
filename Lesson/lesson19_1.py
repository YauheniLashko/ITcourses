class Example:
    weight = 1300
    potato = 200

    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def back(self):
        return self.weight + self.potato

    def mult(self):
        return self.model ** self.speed


e1 = Example(2, 300)
e2 = Example(3, 2)
print(e1.model, e1.speed)
print(e2.model, e2.speed)
print(e2.mult())

print(dir(e2))