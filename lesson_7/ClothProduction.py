# Класс одежды
from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def get_fabric_amount(self):
        pass


class Costume(Cloth):
    # Высота в см
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 0.05:
            self.__height = 0.05
        elif height > 2.40:
            self.__height = 2.40
        else:
            self.__height = height

    def __init__(self, height):
        self.height = height

    # Количество ткани на изготовление костюма
    def get_fabric_amount(self):
        return 2 * self.height + 0.3


class Coat(Cloth):
    # Европейская мерка размера
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 10:
            self.__size = 10
        elif size > 66:
            self.__size = 66
        else:
            self.__size = size

    def __init__(self, size):
        self.size = size

    # Количество ткани на изготовление пальто
    def get_fabric_amount(self):
        return self.size / 6.5 + 0.5


if __name__ == '__main__':
    my_coat = Coat(52)
    print(f'Потребуется ткани для пальто {my_coat.get_fabric_amount()}')
    my_costume = Costume(1.78)
    print(f'Потребуется ткани для костюма {my_costume.get_fabric_amount()}')
