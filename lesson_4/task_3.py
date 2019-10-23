# Получить список из элементов от 20 до 240 кратных 20 или 21

result_list = [i for i in range(20, 241) if not i % 20 or not i % 21]

print(result_list)
