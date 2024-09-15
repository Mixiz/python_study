# Класс для работы с датами


class Date:
    MONTHS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # Парсим строку с датой и возвращаем словарь {'day': xx, 'month': xx, 'year': xxxx}
    @classmethod
    def parse_date(cls, date_str):
        try:
            str_tmp = date_str.split('-')
            date_dict = {'day': int(str_tmp[0]), 'month': int(str_tmp[1]), 'year': int(str_tmp[2])}
            Date.check_date(date_dict)
            return date_dict
        except Exception:
            raise Exception(f'Неверный формат даты {date_str}')

    @staticmethod
    def is_leap_year(year):
        is_leap = False
        # Год должен 1) делиться на 400 или 2) делиться на 4 и не делиться на 100
        if not (year % 400) or not (year % 4) and (year % 100):
            is_leap = True
        return is_leap

    # Проверяем дату, год должен быть положительным числом, дни и месяце - в диапазоне
    @staticmethod
    def check_date(date_dict):
        # Для февраля учтем високосность
        shift = 0
        if date_dict['month'] == 1 and Date.is_leap_year(date_dict['year']):
            shift = 1

        if date_dict['year'] < 0:
            raise Exception(f'Год отрицательный')

        if date_dict['month'] < 0 or date_dict['month'] > 11:
            raise Exception(f'Месяц выходит за границы (от 1 до 12)')

        if date_dict['day'] < 1 or date_dict['day'] > Date.MONTHS[date_dict['month']] + shift:
            raise Exception(f'День выходит за границы месяца (день - {date_dict["day"]}, '
                            f'дней в месяце {Date.MONTHS[date_dict["month"]] + shift})')

    def __init__(self, date_str):
        self.__date_dict = Date.parse_date(date_str)

    @property
    def day(self):
        return self.__date_dict['day']

    @property
    def month(self):
        return self.__date_dict['month']

    @property
    def year(self):
        return self.__date_dict['year']


if __name__ == '__main__':
    assert Date.is_leap_year(2000)
    assert not Date.is_leap_year(2100)
    assert Date.is_leap_year(2004)
    assert not Date.is_leap_year(2002)

    my_date = Date('12-11-2018')
    assert my_date.day == 12
    assert my_date.month == 11
    assert my_date.year == 2018

    my_date = Date('31-11-2018')
