"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""

replace_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
newfile = open('dz_4_ru.txt', 'w')

with open('dz_4.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.rstrip()
        for key, value in replace_dict.items():
            line = line.replace(key, value)
        print(line)
        print(line, file=newfile)

newfile.close()
