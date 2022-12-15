from memory_profiler import profile


@profile
def fact_slow(x):
    """
    потребление памяти 18.4 Mib
    :param x:
    :return:
    """
    cnt = 1
    for i in range(1, x + 1):
        cnt *= i
        return cnt

fact_slow(500)



def fact(x):
    """
    та же логика, но с генератором - потребление памяти 18.4 Mib
    :param x:
    :return:
    """
    cnt = 1
    for i in range(1, x + 1):
        cnt *= i
        yield cnt

fact(500)