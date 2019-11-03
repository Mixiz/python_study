# Реализуется класс матриц с перегрузкой операторов


class Matrix:

    def __init__(self, matrix):
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.matrix = []
        for line in matrix:
            if len(line) != self.width:
                raise Exception(f'Некорректная размерность матрицы, ожидалось {self.width} на {self.height}')
            self.matrix.append(line.copy())

    def __str__(self):
        result = ''
        for line in self.matrix:
            result = f'{result}{line}\n'
        return result

    def __add__(self, other):
        if self.height != other.height or self.width != other.width:
            raise Exception(f'Некорректная размерность матрицы, ожидалось {self.width} на {self.height}, на входе {other.width} на {other.height}')
        matrix = []
        for i in range(self.height):
            matrix.append([])
            for j in range(self.width):
                matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(matrix)


matrix = Matrix([[1, 2, 3, 4], [2, 3, 4, 5], [3, 2, 1, 0], [4, 4, 4, 8]])
matrix_2 = Matrix([[1, 2, 3, 4], [2, 3, 4, 5], [3, 2, 1, 0], [4, 4, 4, 8]])
new_matrix = matrix + matrix_2
print(new_matrix)
