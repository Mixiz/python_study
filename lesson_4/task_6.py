# Два генератора. 1-ый генерирует целые числа, начиная с указанного
# 2-й повторяет элементы списка, определенного заранее

from itertools import (count,
                       cycle)

iterator = count(10)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator_list = cycle([4, 8, 15, 16, 23, 42])
print(next(iterator_list))
print(next(iterator_list))
print(next(iterator_list))
print(next(iterator_list))
print(next(iterator_list))
print(next(iterator_list))
print(next(iterator_list))
print(next(iterator_list))
print(next(iterator_list))
