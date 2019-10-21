# Запросим у пользователя данные и передадим их в функцию как именованные аргументы. Вывод в одну строку


def print_user_data(name, surname, birth_place, birth_date, email, phone_number):
    print(f'Пользователь {name} {surname} родился {birth_date} в населенном пункте {birth_place}. '
          f'Вы можете написать ему письмо на {email} или позвонить по номеру {phone_number}')


name = input("Введите имя\n")
surname = input("Введите фамилию\n")
birth_place = input("Введите место рождения\n")
birth_date = input("Введите дату рождения\n")
email = input("Введите email\n")
phone_number = input("Введите номер телефона\n")
print_user_data(name=name,
                surname=surname,
                birth_place=birth_place,
                birth_date=birth_date,
                email=email,
                phone_number=phone_number)
