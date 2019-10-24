# Создаем файл, записываем все, что введет пользователь. При вводе пустой строки заканчиваем

with open("task_1_file.txt", 'w', encoding='UTF-8') as file:
    text = input("Начинайте ввод\n")
    while text:
        file.write(text)
        file.write('\n')
        text = input()

print("Конец")
