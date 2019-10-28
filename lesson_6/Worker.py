# Классы Работника и Должность

class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_info(self):
        return f'{self.get_full_name()} зарабатывает {self.get_total_income()} на должности "{self.position}"'


if __name__ == '__main__':
    worker_1 = Position("Василий", "Пупкин", "Курьер", 1200, 700)
    worker_2 = Position("Аркадий", "Головин", "Начальник курьерской службы", 3000, 900)

    print(worker_1.get_info())
    print(worker_2.get_info())
