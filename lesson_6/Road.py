# Класс Дорога. Можем рассчитать массу дороги

class Road:
    _length = 0
    _width = 0
    _depth = 1
    __UNIT_WEIGHT = 125

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def set_params(self, length=0, width=0, depth=0):
        if length > 0:
            self._length = length
        if width > 0:
            self._width = width
        if depth > 0:
            self._depth = depth

    def get_weight(self):
        return self._length * self._width * self._depth * self.__UNIT_WEIGHT


if __name__ == '__main__':
    road = Road(12, 10)
    road.set_params(100, depth=5)

    print(f'Масса дорожного полотна {road.get_weight()}')
