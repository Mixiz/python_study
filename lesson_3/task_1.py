# Функция, которая принимает два числа и делит их. В случае ошибки вернет None


def division(dividend, divider) -> float:
    result = None
    try:
        result = float(dividend) / float(divider)
    except ValueError:
        print("Входные данные не числа")
    except ZeroDivisionError:
        print("Вы пробовали поделить на 0")
    finally:
        return result


dividend = input("Введите делимое\n")
divider = input("Введите делитель\n")
print(division(dividend, divider))
