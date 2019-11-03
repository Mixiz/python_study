# Генерируем список, а затем формируем список без повторяющихся элементов
import random

my_list = [random.randrange(1, 20) for i in range(1, 15)]
print(my_list)

result_list = [my_list[i] for i in range(0, len(my_list) - 1) if my_list.count(my_list[i]) == 1]
print(result_list)
