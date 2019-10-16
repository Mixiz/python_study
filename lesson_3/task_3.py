# Функция принимает три аргумента и возвращает сумму двух наибольших


def sum_two_of_three(a, b, c):
    result = None
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        my_list = [a, b, c]
        my_list.sort()
        result = my_list[1] + my_list[2]
    except ValueError:
        print("Входные данные не числа")
    finally:
        return result


a = input("1-ое число\n")
b = input("2-ое число\n")
c = input("3-е число\n")

print(sum_two_of_three(a, b, c))
