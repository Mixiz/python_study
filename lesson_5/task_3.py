# В файле содержатся фамилии сотрудников и их оклады.
# Нужно вывести тех, у кого оклады меньше 20к и сумму среднего оклада среди всех

CRIT_SALARY = 20000

avg_salary = 0
records = []

# Ввод данных
with open('task_3_file.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        record = line.rstrip('\n').split(' ')
        records.append(record)

# Вычисления

for rec in records:
    salary = float(rec[1])
    avg_salary += salary
    if salary >= CRIT_SALARY:
        print(f'{rec[0]} получает {salary}')

avg_salary /= len(records)

print(f'Средняя зарплата {avg_salary}')