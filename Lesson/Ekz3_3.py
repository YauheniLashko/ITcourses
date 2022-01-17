class Tomato:
    states = {1: 'посадили', 2: 'выросло'}

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[1]

    def grow(self):
        self._state = Tomato.states[2]
        print("Растет!")

    def is_ripe(self):
        return "Созрел" if self._state == Tomato.states[2] else "Не созрел"

    def __getstate__(self):
        return self._state


class TomatoBush:

    def __init__(self, tomatoes):
        self.tomatoes = tomatoes

    def grow_all(self):
        for tomato in self.tomatoes:
            if tomato.__getstate__() != Tomato.states[2]:
                tomato.grow()
            print("Томат растет!")

    def all_are_ripe(self):
        return len(tuple(filter(lambda x: x.is_ripe(), self.tomatoes))) == len(self.tomatoes)

class Gardener:
    def __init__(self, name):
        self.name = name
        self._plant = TomatoBush(1)

    def work(self):
        TomatoBush(self).grow_all()

    def harvest(self):
        TomatoBush(self).all_are_ripe()
        if TomatoBush(self).all_are_ripe():
            print("Все выросло")
        else:
            print("Не все выросло")


t = Tomato(1)
t1 = Tomato(2)
t2 = Tomato(3)
tb = TomatoBush([t, t1, t2])
g = Gardener('Ivan')

t.grow()
print(t.is_ripe())
print(tb.all_are_ripe())
tb.grow_all()
