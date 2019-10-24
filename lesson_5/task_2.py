# Считывает данные из файла построчно и считает, сколько слов в строке

lines_cnt = 0

with open('task_2_file.txt', 'r') as file:
    for line in file:
        lines_cnt += 1
        # Учитываем, что может стоять два пробела или быть пробел в конце, тогда слово не считаем
        words_cnt = len([i for i in line.split(' ') if len(i) > 0])
        print(f'{line}Количество слов в строке {words_cnt}')
