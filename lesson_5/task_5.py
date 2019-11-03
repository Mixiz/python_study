# Генерируем числа, записываем в файл
# Считываем файл и подсчитываем сумму

import random
from functools import reduce

FILE_NAME = 'task_5_file.txt'

# Создаем файл
with open(FILE_NAME, 'w') as file:
    # Создаем 20 чисел
    numbers = [str(random.randrange(1, 1000)) for i in range(20)]
    file.write(' '.join(numbers))

# Читаем файл и считаем
with open(FILE_NAME, 'r') as file:
    sum = 0
    for line in file:
        sum = reduce(lambda x, y: float(x) + float(y), line.split(' '))

    print(f'Сумма чисел {sum}')
