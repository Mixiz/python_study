# Структура данных Товары
# Пользователь вводит допустимые поля для ввода
# Затем заполняет саму структуру
# После строится аналитика

fields = []


# Возвращает int float string в зависимости от входных данных
def get_value(value):
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            return value
    return value


str = input("Введите поля товара. Ввод оканчивается пустой строкой\n")
while str:
    fields.append(str)
    str = input("Введите следующее поле\n")

# Вводим товар
goods = []
cont_input = True
while cont_input:
    cont_input = False
    # Ввод единицы товара
    tmp_dict = {}
    for elem in fields:
        value = input(f'Введите {elem}\n')
        value = get_value(value)
        if value:
            cont_input = True
        tmp_dict[elem] = value
    # Если ввели хоть что-то, добавим в товары
    if cont_input:
        goods.append((len(goods)+1, tmp_dict))

print("Полученная структура")
print(goods)

# Соберем аналитику
analytic = {}
for elem in fields:
    tmp_field_values = []
    for good in goods:
        tmp_field_values.append(good[1][elem])
    analytic[elem] = tmp_field_values

print("Полученная аналитика")
print(analytic)
