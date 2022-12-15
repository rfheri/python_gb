from timeit import timeit
import random

def slow_func():
    """
    вместо list comprehension заполняем один массив, ищем в нем объеты, удовлетворяющие условию,
    заполняем второй массив
    скорость выполнения lc - 0.018228
    скорость выполнения кода функции - 7.968835800000001
    разница в скорости выполнения - 437 раз
    :return:
    """
    new_lst = []
    lst = []
    for i in range(20, 240):
        lst.append(i)
    for j in lst:
        if j % 20 == 0 or j % 21 == 0:
            new_lst.append(j)


print(timeit('[i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]', globals=globals(), number=1000))  # 0.018228

print(timeit('slow_func()', globals=globals(), number=1000))  # 7.968835800000001

