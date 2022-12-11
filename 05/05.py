"""
 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

with open('dz_5.txt', 'w') as file:
    for i in range(10):
        file.write(f'{random.randrange(10, 300)} ')

with open('dz_5.txt', 'r') as file:
    for item in file:
        lst = list(item.split())
        print(lst)
        print(sum([int(x) for x in lst]))
