class Dog:


    def __init__(self, name):
        self.__name = name
        self.__tricks = []

    def add_trick(self, trick):
        self.__tricks.append(trick)

    def display_tricks(self):
        print(self.__tricks)

    def display_name(self):
        print(self.__name)

rex = Dog('rex')
laika = Dog('laika')

rex.add_trick('play ball')
rex.add_trick('roll over')

rex.display_tricks()

rex.add_trick('walk over the moon')

rex.display_tricks()

laika.display_tricks()