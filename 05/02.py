"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

row = 0
words = 0

with open('dz_2.txt', 'r') as file:
    for i in file:
        words = len(i.split())
        row += 1
        print(f'строка {row}: количество слов: {words}')

print(f'всего строк: {row}')
