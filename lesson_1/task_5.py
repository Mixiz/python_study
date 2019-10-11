# В первый день спортсмен пробегает a км, определить, когда сможет пробежать b км, прибавляя по 10% в день
a = input("Введите количество км в первый день")
b = input("Введите желаемый результат в км")
try:
    a = float(a)
    b = float(b)
    if a <= 0 or b <= 0:
        raise Exception("числа должны быть положительные")
    days = 0
    current_km = a
    while current_km < b:
        days += 1
        current_km *= 1.1
    print("Желаемая дистанция будет достигнута через", days, "дней")
except Exception as error:
    print("Вы ввели некорректные числа, ", error)