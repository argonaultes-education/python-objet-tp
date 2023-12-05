class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.__tricks = []
    
    def add_trick(self, trick):
        self.__tricks.append(trick)

    def print_tricks(self):
        print(self.__tricks)

if __name__ == '__main__':
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')

    print(f'{d.name} is {d.kind}')
    d.print_tricks()
    d.add_trick('cry')

    d.print_tricks()

    print(f'{e.name} is {e.kind}')

    e.print_tricks()