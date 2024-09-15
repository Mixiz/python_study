# Класс проверяет элементы списка на допустимость


class ExceptionList(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    my_list = [1, 4.2, "какая-то строка", False, [1, 2, 3], ('a', 'z'), {"Проверка", "данных"}, set([1,2,4,9]), frozenset(['a', 'e', 'u', 'i', 'o'])]
    try:
        for i in my_list:
            if isinstance(i, bool):
                raise ExceptionList('В списке есть булевое значение')
            elif isinstance(i, str):
                raise ExceptionList('В списке есть строковое значение')
    except ExceptionList as err:
        print(err)

    my_list = [1, 4.2, False, [1, 2, 3], ('a', 'z'), {"Проверка", "данных"}, set([1, 2, 4, 9]),
               frozenset(['a', 'e', 'u', 'i', 'o'])]
    try:
        for i in my_list:
            if isinstance(i, bool):
                raise ExceptionList('В списке есть булевое значение')
            elif isinstance(i, str):
                raise ExceptionList('В списке есть строковое значение')
    except ExceptionList as err:
        print(err)
