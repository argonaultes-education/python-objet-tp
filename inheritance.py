class Furniture(object):
    def __init__(self):
        print(f'init Furniture')
        super().__init__()

class Table(object):
    def __init__(self):
        print(f'init Table')
        super().__init__()

class Desk(Furniture, Table):
    def __init__(self):
        super().__init__()

desk = Desk()
