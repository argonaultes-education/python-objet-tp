class MyClass:
    i = 19

    # def __init__(self):
    #     pass

    def display_i(self):
        print(self.i)

c1 = MyClass()
c1.i = 20
c1.autre_attribut = 'hello'
print(c1.i)
print(c1.autre_attribut)

c2 = MyClass()
print(c2.i)
print(c2.autre_attribut)
#c1.display_i()