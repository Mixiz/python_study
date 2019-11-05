# Класс с пользовательским исключением


class ExceptionDivision(Exception):
    TEXT = 'Произошло деление на 0'

    def __init__(self, a, b):
        self.txt = f'{self.TEXT} при операции {a} / {b}'


def func(a, b):
    if not b:
        raise ExceptionDivision(a, b)
    else:
        return a / b


if __name__ == '__main__':
    a = 12
    b = 0
    try:
        result = func(a, b)
    except ExceptionDivision as err:
        print(err.txt)
    else:
        print(result)

    a = 12
    b = 12
    try:
        result = func(a, b)
    except ExceptionDivision as err:
        print(err.txt)
    else:
        print(result)
