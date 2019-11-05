# Класс с комплексными числами


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        coef_a = (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)
        coef_b = (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)
        return Complex(coef_a, coef_b)


if __name__ == '__main__':
    a = Complex(12, 3)
    b = Complex(-3, -1)
    print(a + b)
    print(a - b)
    print(a * b)
    c = a / b
    print(c)
    print(c * b)
