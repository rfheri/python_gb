"""
 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
 разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
 к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
  программы завершается. Если специальный символ введен после нескольких чисел, то вначале
   нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

summ = 0
while True:
    numbers = input('введите числа, или введите * для выхода: ').split()
    for i in numbers:
        try:
            if i == '*':
                break
            else:
                summ += int(i)
        except ValueError:
            print('введите число или *')
    print(summ)

#выход из цикла не работает