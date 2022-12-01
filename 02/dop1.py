# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = input('введите число: ')
a = a.replace('.', '')
a = a.replace(',', '')
temp = 0
for i in a:
    temp = temp + int(i)
print(temp)
