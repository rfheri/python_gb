# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input("введите количество секунд"))

seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(f"{hour}:{minutes}:{seconds}")
