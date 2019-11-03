# Формирует список из исходного списка, значения которых больше предыдущего элемента
import random


my_list = [random.randrange(1, 100) for i in range(1, 15)]
print(my_list)

# Вернет значения, которые больше предыдущего
result_list = [my_list[i+1] for i in range(0, len(my_list)-1) if my_list[i] < my_list[i+1]]
print(result_list)
