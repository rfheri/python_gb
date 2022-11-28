#  Запросите у пользователя значения выручки и издержек фирмы.
#  Определите, с каким финансовым результатом работает фирма
#  (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#  Выведите соответствующее сообщение. Если фирма отработала с прибылью,
#  вычислите рентабельность выручки (соотношение прибыли к выручке).
#  Далее запросите численность сотрудников фирмы и определите прибыль фирмы
#  в расчете на одного сотрудника.

money = int(input("значение выручки: "))
loss = int(input("значение издержек: "))

if money > loss:
    print("фирма работает с прибылью")
    print(f"рентабельность выручки: {(money - loss) / money}")
    people = int(input("численность сотрудников фирмы: "))
    print(f"прибыль фирмы в расчете на одного сотрудника: {(money - loss) / people}")
elif money < loss:
    print("фирма работает с убытком")
else:
    print("фирма работает в ноль")
