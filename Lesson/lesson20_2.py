class Human:
    default_name = "Name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Money: {self.__money}\n'
              f'House: {self.__house}')

    @staticmethod
    def default_info():
        print(f'default name: {Human.default_name}\n'
              f'default age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Amount money increase on {amount}. Current value is {self.__money}')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Not enough money!")



class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price is {final_price}')
        return final_price

class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


h = Human("LEO", 27)
print(h.default_name)
h.info()
h.earn_money(10000)
h.earn_money(100000)
h.info()

small = SmallHouse(8500)
h.buy_house(small, 20)