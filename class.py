class MyClass:
    i = 89

    def __init__(self, param2 = 'none', param3 = 'none'):
        self.__param2 = param2
        self.__param3 = param3

    def __str__(self):
        return str(self.__param2) + ' ' + str(self.__param3) + ' ' + self.newval

test = MyClass(12)
print(test._MyClass__param2)

test2 = MyClass(13, 14)
print(test2._MyClass__param2, test2._MyClass__param3)

test2.newval = '122'

print(test2)

print(test2.i)

print(MyClass.i)

class Parent:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Child(Parent):
    def __init__(self, name):
        super(Child, self).__init__(name)

john = Child('toto')
print(john.get_name())
