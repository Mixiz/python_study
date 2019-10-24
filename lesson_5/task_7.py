# Считать файл с данными о фирме
# Сформировать список с общими данными, преобразовать в json и вывести в новый файл
import json

avg_profit = 0
profit_cnt = 0
companies = {'companies': {}}

# Считываем данные
with open('task_7_file.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        tmp = line.split(': ')
        data = tmp[1].split(' ')
        profit = float(data[1]) - float(data[2])
        companies['companies'][tmp[0]] = profit
        if profit > 0:
            profit_cnt += 1
            avg_profit += profit

companies['average_profit'] = avg_profit / profit_cnt

# Вывод структуры и запись json в файл
print(companies)
with open('task_7_file_output.txt', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(companies, ensure_ascii=False, sort_keys=True, indent=4))
