# Получаем х и y, делаем х ** у без встроенного возведения в степень


def calc_exponent(x, y):
    result = None
    try:
        x = float(x)
        y = int(y)
        # Возведение в отрицательную степень - умножение на обратное число
        if y < 0:
            x = 1 / x
            y = -y
        result = 1
        for i in range(0, y):
            result *= x
    except ValueError:
        print("Входные данные не числа")
    finally:
        return result


x = input("Число\n")
y = input("Степень\n")
print(calc_exponent(x, y))
print(f'Проверка {float(x) ** int(y)}')
