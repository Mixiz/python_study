# Создаем структуру
# subjects = [{'Subject': {'lectures': number, 'practice': number, 'labs': number} }, and so on]
# и заполняем ее из файла

# Типы занятий
LESSON_WORDS = ['лекции', 'практика', 'лабораторные']

# Структура занятий
subjects = {}

# Считываем данные из файла
with open('task_6_file.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        tmp = line.split(':')
        subject_name = tmp[0]
        lessons = tmp[1].split(', ')
        subject = {}
        sum_lessons = 0
        for lesson in lessons:
            tmp = lesson.strip(' ').split(' - ')
            # Считаем только определенные типы занятий
            if LESSON_WORDS.count(tmp[0]):
                subject[tmp[0]] = int(tmp[1])
                sum_lessons += int(tmp[1])
            else:
                print(f'Такого типа занятий нет "{tmp[0]}"')
            # Добавляем поле с общим количеством занятий
            subject['Всего'] = sum_lessons
        subjects[subject_name] = subject

# Вывод результата
print(subjects)

