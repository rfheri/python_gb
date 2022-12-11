"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

staff = {}

with open('dz_3.txt', 'r', encoding='utf-8') as file:
    for i in file:
        staff = dict(i.split(':') for i in file)

staff = dict((key, int(value)) for key, value in staff.items())

for key, value in staff.items():
    if value >= 20000:
        print(key, value)

avg = (sum(staff.values())) / (len(staff) + 1)
print(f'')
print(f'средняя величина дохода: {avg}')
