class Bottle:
    def __init__(self, liquid):
        self.__quantity = 20
        self.liquid = liquid

    def drink(self, quantity):
        if quantity < self.__quantity:
            self.__quantity = self.__quantity - quantity
            print(f'C\'est super cool de boire.')
        else:
            print(f'Not enough quantity remaining')

class Glass(Bottle):
    def __init__(self, liquid):
        super().__init__(liquid)
        self._Bottle__quantity = 10



verre = Glass('eau')
verre.drink(10)
print(verre._material)
#verre._Bottle__quantity = 3001

verre.drink(10)

evian = Bottle('eau')
evian.drink(10)
