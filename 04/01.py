"""
 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
 необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета
 для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, work_hours, payment, plus = argv


def calc_func(a, b, c):
    return (int(a) * int(b) + int(c))


print(calc_func(work_hours, payment, plus))
