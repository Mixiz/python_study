# получим время в секундах и переведем в hh:mm:ss
seconds = input("Введите время в секундах")
try:
    seconds = int(seconds)
    hours = seconds // 60 // 60
    minutes = seconds // 60 % 60
    seconds %= 60
    print("Ваше время %d:%02d:%02d" % (hours, minutes, seconds))
except Exception:
    print("Вы ввели некорректное число")