# Класс склада и класс различной оргтехники


class Warehouse:
    __equipments = []

    def __init__(self, **kwargs):
        for key, value in kwargs:
            self.key = value

    def push(self, itm):
        self.__equipments.append(itm)

    def __str__(self):
        return '\n'.join(str(equip) for equip in self.__equipments)


class OfficeEquipment:

    # Название
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Стоимость
    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    # Вес
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self):
        return f'{self.__class__} {self.name}'

class Printer(OfficeEquipment):
    # Скорость печати (лист в минуту)
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    # Сетевое имя
    @property
    def network_name(self):
        return self.__network_name

    @network_name.setter
    def network_name(self, value):
        self.__network_name = value

    # Режим печати
    @property
    def colored(self):
        return self.__colored

    @colored.setter
    def colored(self, value):
        self.__colored = value


class Scanner(OfficeEquipment):
    # Скорость сканирования (лист в минуту)
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value


class Phone(OfficeEquipment):
    # Номер телефона
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


if __name__ == '__main__':
    my_warehouse = Warehouse()
    data = {'name': 'У секретарши',
            'cost': 4300,
            'weight': 2.7,
            'number': '222-323-22'}
    my_warehouse.push(Phone(**data))

    data = {'name': 'У секретарши',
            'cost': 5900,
            'weight': 3.5,
            'speed': 12}
    my_warehouse.push(Scanner(**data))

    data = {'name': 'В холле',
            'cost': 2005,
            'weight': 1.7,
            'speed': 4}
    my_warehouse.push(Scanner(**data))

    data = {'name': 'Новый принтер',
            'cost': 12500,
            'weight': 7.3,
            'speed': 24,
            'network_name': None,
            'colored': True}
    my_warehouse.push(Printer(**data))

    data = {'name': 'В холле',
            'cost': 4500,
            'weight': 4.3,
            'speed': 12,
            'network_name': '192.168.1.12',
            'colored': False}
    my_warehouse.push(Printer(**data))

    print(my_warehouse)
