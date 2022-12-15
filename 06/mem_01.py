from memory_profiler import profile
import random

@profile
def slow_func():
    """
    вместо list comprehension заполняем один массив, ищем в нем объеты, удовлетворяющие условию,
    заполняем второй массив
    потребление памяти lc - 18.5
    потребление памяти функции slow_func() - 18.5
    по замерам разницы нет, что выглядит странно
    :return:
    """
    new_lst = []
    lst = []
    for i in range(20, 2400):
        lst.append(i)
    for j in lst:
        if j % 20 == 0 or j % 21 == 0:
            new_lst.append(j)


slow_func()

@profile
def fast_func():
    [i for i in range(20, 2400) if i % 20 == 0 or i % 21 == 0]

fast_func()