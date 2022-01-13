class Animal:
    def __init__(self, name, food, location):
        self.food = food
        self.location = location
        self.name = name

    def makeNoise(self):
        return "Такое-то животное спит"

    def eat(self):
        return "Такое-то животное ест"

    def sleep(self):
        return "Животное спит"


class Dog(Animal):
    sing = "RRrrrrr"

    def makeNoise(self):
        return "Собака спит"

    def eat(self):
        print(f"Dog eating {self.food}")


class Cat(Animal):
    sing = "Mrr"

    def makeNoise(self):
        return "Кот спит"

    def eat(self):
        print(f"Cat eating {self.food}")


class Hourse(Animal):
    sing = "Igo-go"

    def makeNoise(self):
        return "Лошадь спит"

    def eat(self):
        print(f"Horse eating {self.food}")


class Veterinar:
    def void_treat_animal(self, animal: Animal):
        animal.eat()


a = Animal('Name', 'food', 'location')
d = Dog('Dog', "bone", "home")
c = Cat('Cat', 'chicken', 'home')
h = Hourse('Horse', 'grass', 'stable')
v = Veterinar()
print(h.makeNoise())

print(v.void_treat_animal(animal=d))
