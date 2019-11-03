# Расчитывает зарплату как (ставка_в_час * кол-во_часов) + премия
# Аргументы принимает из параметров запуска
import sys


if __name__ == '__main__':
    try:
        salary_per_hour = sys.argv[1]
        working_hours = sys.argv[2]
        bonus = sys.argv[3]

        salary = float(salary_per_hour) * float(working_hours) + float(bonus)

        print(f'Зарплата будет равна {salary} y.e.')
    except IndexError:
        print("Переданы не все параметры")
    except ValueError:
        print("Переданы некорректные параметры")
    except Exception:
        print("Произошла ошибка")
