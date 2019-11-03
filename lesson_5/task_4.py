# Считываем файл и подменяем англ числительные на русские

num_dict = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'zero': 'ноль',}

new_file = open('task_4_file_output.txt', 'w', encoding='UTF-8')

with open('task_4_file.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        num = line.split(' ', 1)
        try:
            new_line = f'{num_dict[num[0].lower()].capitalize()} {num[1]}'
            new_file.write(new_line)
        except KeyError:
            # Первое слово в строке не числительное, просто запишем строку обратно в файл
            new_file.write(line)

new_file.close()