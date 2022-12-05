"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

name = input('введите имя: ')
soname = input('введите фамилию: ')
birthday = input('введите дату рождения: ')
town = input('введите город рождения: ')
email = input('введите email: ')
phone = input('введите телефон: ')


def info(name, soname, birthday, town, email, phone):
    print(
        f"Имя: {name}, фамилия:{soname}, датa рождения:{birthday}, город рождения: {town}, email:{email}, телефон:{phone}")

info(name=name, soname=soname, birthday=birthday, town=town, email=email, phone=phone)