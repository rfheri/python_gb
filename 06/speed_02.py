from timeit import timeit

def fact_slow(x):
    """
    реализованная функция, время выполнения 0.4992413
    :param x:
    :return:
    """
    cnt = 1
    for i in range(1, x + 1):
        cnt *= i
        return cnt

def fact(x):
    """
    та же логика, но с генератором - время выполнения 0.2265896. Сокращение времени выполнения в 2 раза.
    :param x:
    :return:
    """
    cnt = 1
    for i in range(1, x + 1):
        cnt *= i
        yield cnt

print(timeit('fact(500)', globals=globals(), number=1000000))
print(timeit('fact_slow(500)', globals=globals(), number=1000000))