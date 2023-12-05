from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, area):
        self.__area = area
    
    @abstractmethod
    def get_area(self):
        pass

class BathRoom(Room):
    def __init__(self, area, nb_taps):
        super().__init__(area)
        self.__nb_taps = nb_taps

    def get_area(self):
        return super.__area

class LivingRoom(Room):
    def __init__(self, area, nb_tvs):
        super().__init__(area)
        self.__nb_tvs = nb_tvs

    def get_area(self):
        return super.__area

class House:
    def __init__(self):
        self.__rooms = []
    
    def add_room(self, room):
        self.__rooms.append(room)

    def __str__(self):
        return f'House has {len(self.__rooms)} rooms.'


if __name__ == '__main__':
    house1 = House()
    house1.add_room(BathRoom(10, 1))
    house1.add_room(LivingRoom(20, 1))
    house1.add_room(LivingRoom(30, 1))
    print(house1)
