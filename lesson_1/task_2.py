# получаем число n, выводим n + nn + nnn
n = input("Введите число n")
if n.isdigit():
    print(int(n) + int(n+n) + int(n+n+n))
    # аналогичный вариант, через конкатенацию
    # n = int(n)
    # print("%d%d%d" % (n, n*2, n*3))
else:
    print("Вы ввели некорректное число")