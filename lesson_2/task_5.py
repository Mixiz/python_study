# Формирует рейтинг - невозрастающая последовательность натуральных чисел
# Пользователь вводит значения, которые добавляются в рейтинг

rating = [108, 42, 23, 16, 15, 8, 4]


# Бинарным поиском находим позицию для вставки элемента
def bin_search(value):
    right = len(rating)
    left = 0
    pos = right // 2
    while right != left:
        if rating[pos] > value:
            left = pos + 1
        else:
            right = pos
        pos = (left + right) // 2
    return pos

print("Стартовый рейтинг")
print(rating)

number = input("Добавить в рейтинг ")
try:
    while number:
        number = int(number)
        if number < 1:
            print("Некорректное число")
        else:
            pos = bin_search(number)
            rating.insert(pos, number)
        print("Текущий рейтинг")
        print(rating)
        number = input("Следующее число")
except Exception:
    print("Некорректный ввод")

print("Финальный рейтинг")
print(rating)
