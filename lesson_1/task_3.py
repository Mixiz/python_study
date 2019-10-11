# Получаем от пользователя число и выводим самую большую цифру
number = input("Введите положительное число")
if number.isdigit():
    max = 0
    number = int(number)
    while number > 0:
        digit = number % 10
        if digit > max:
            max = digit
        number //= 10
    print("Самая большая цифра", max)
else:
    print("Вы ввели некорректное число")