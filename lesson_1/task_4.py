# Получаем значение выручки и издержек, определяем прибыльность
# Если компания прибыльная, определяем рентабельность и прибыль на одного сотрудника
try:
    income = input("Введите размер доходов")
    expense = input("Введите размер издержек")
    expense = float(expense)
    profit = float(income) - expense

    if profit > 0:
        print("Выручка больше издержек")
        efficiency = profit / expense * 100
        print("Рентабельность", efficiency, '%')
        workers_cnt = input("Введите количество сотрудников")
        print("Прибыль на одного сотрудника", profit / int(workers_cnt), "y.e.")
    else:
        print("Издержки больше выручки")
except Exception:
    print("Вы ввели некорректные числа")