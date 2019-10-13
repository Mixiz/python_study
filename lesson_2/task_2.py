# Ввод элементов списка продолжается, пока не введена пустая строка
# А затем соседние элементы меняются местами (0 и 1, 2 и 3 и т.д.)

print("Завершение ввода окончится при вводе пустой строки (нажатие Enter)")
element = input("Введите элемент списка")
my_list = []
while element:
    my_list.append(element)
    element = input("Введите следующий элемент")
print("Полученный список")
print(my_list)

# Меняем элементы списка местами
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print("Результат")
print(my_list)
