# Получить из генератора четные числа от 100 до 1000, а после их произведение
from functools import reduce

result = reduce(lambda a, b: a * b, range(100, 1001, 2))
print(result)
