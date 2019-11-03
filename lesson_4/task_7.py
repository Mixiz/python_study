# Реализуем генератор факториала


def fact_gen(number):
    multiply = 1
    for i in range(0, number):
        if i:
            multiply = multiply * i
        yield multiply

fact_iter = fact_gen(15)
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
