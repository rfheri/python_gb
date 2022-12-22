"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class divide(Exception):
    def __init__(self, inp):
        self.inp = inp


def div():
    try:
        a = int(input('делимое: '))
        b = int(input('делитель: '))
        if b == 0:
            raise divide("деление на ноль")
        else:
            res = a / b
            return res
    except ValueError:
        return "вы ввели не число"
    except divide as err:
        return err


print(div())
