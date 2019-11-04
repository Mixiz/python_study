# Класс клеток

STANDART_SIZE = 5


class Cell:
    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, cells):
        if cells <= 0:
            raise Exception('У клетки будет меньше 1 ячейки!')
        else:
            self.__cells = cells

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(abs(self.cells - other.cells))

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(max(self.cells, other.cells) // min(self.cells, other.cells))

    # Формируем "изображение" клетки, выстраиваем в ряд по size ячеек
    def make_order(self, size):
        result = '\n'.join('*' * size for i in range(self.cells // size))
        if self.cells % size > 0:
            result = result + '\n' + ('*' * (self.cells % size))
        return result


if __name__ == '__main__':
    cell_1 = Cell(12)
    cell_2 = Cell(5)
    new_cell = cell_1 + cell_2
    new_cell_2 = cell_2 - cell_1
    new_cell_3 = cell_1 * cell_2
    new_cell_4 = cell_1 / cell_2
    print(new_cell.make_order(STANDART_SIZE) + '\n')
    print(new_cell_2.make_order(STANDART_SIZE) + '\n')
    print(new_cell_3.make_order(STANDART_SIZE * 2) + '\n')
    print(new_cell_4.make_order(STANDART_SIZE) + '\n')
