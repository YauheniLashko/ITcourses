class Tomato:
    states = {1: 'посадили', 2: 'выросло'}

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[1]

    def grow(self):
        self._state = Tomato.states[2]

    def is_ripe(self):
        if self._state == Tomato.states[2]:
            print("Созрел")
        else:
            return False


class TomatoBush(Tomato):

    def __init__(self, tomatoes):
        super().__init__(tomatoes)
        my_tomatoes = []
        self.tomatoes = my_tomatoes.append(tomatoes)
        print(my_tomatoes)


    def grow_all(self):
        print("Томат растет!")


    def all_are_ripe(self):
        Tomato.grow(self)
        if self.tomatoes == Tomato.states[2]:
            return True
        else:
            return False


class Gardener:
    def __init__(self, name):
        self.name = name
        self._plant = Tomato

    def work(self):
        TomatoBush(1).grow_all()

    def harvest(self):
        TomatoBush(Tomato).all_are_ripe()
        if TomatoBush(Tomato).all_are_ripe():
            print("Все выросло")
        else:
            print("Не все выросло")


t = Tomato(1)
tb = TomatoBush('pomidor')
g = Gardener('Ivan')
t.grow()
t.is_ripe()
g.harvest()
tb.grow_all()
g.harvest()
g.harvest()