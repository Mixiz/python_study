# Для введенной строки возвращаем строку, где каждая первая буква слова - заглавная


def int_func(word: str):
    if word.lower() != word:
        print("Есть заглавные буквы. Строка не соответствует описанию")
    return word.capitalize()


user_string = input("Введите строку")
# Разбивает строку на слова, каждое слово делает с заглавной и возвращает пробелы на место
result = ''.join(int_func(x)+' ' for x in user_string.split(' '))
print(result)
