# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('введите номер месяца: '))

# вариант со списком
month_list = ['зима', 'весна', 'лето', 'осень']
if month <= 2 or month == 12:
    print(month_list[0])
elif 3 <= month <= 5:
    print(month_list[1])
elif 6 <= month <= 8:
    print(month_list[2])
elif 9 <= month <= 11:
    print(month_list[3])
else:
    print('что-то пошло не так')

# вариант со словарем
month_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for key, value in month_dict.items():
    if month in value:
        print(key)
