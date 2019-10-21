# Вводятся числа через пробел, пока не введен специальный символ

cont_sum = True
spec_symbol = 'q'


def sum_numbers(string: str):
    numbers = string.split(' ')
    # На всякий случай проверяем длину, чтобы после сплита не было пустых значений
    try:
        return sum(float(x) if len(x) > 0 else 0 for x in numbers)
    except ValueError:
        print("Не удалось разобрать строку")
        return 0


total = 0
while cont_sum:
    user_string = input("Введите числа. Ввод окончится после 'q'\n")
    if user_string.find(spec_symbol) > -1:
        cont_sum = False
    # Передаем строку до спецсимвола
    total += sum_numbers(user_string.split(spec_symbol)[0])
    print(total)

print(f'Результат {total}')
