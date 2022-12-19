"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name, speed, color, is_police=True):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение \n'

    def stop(self):
        return f'{self.name} остановилась \n'

    def turn(self, direction):
        return f'{self.name} повернула {direction} \n'

    def show_speed(self):
        return f'скорость {self.speed} \n'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'превышении скорости! {self.speed} \n'
        else:
            return f'скорость в норме: {self.speed} \n'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'превышении скорости! {self.speed} \n'
        else:
            return f'скорость в норме: {self.speed} \n'


class PoliceCar(Car):
    pass


town = TownCar('Nissan', 80, 'желтая', False)
print(f'{town.name}')
print(f'полицейская: {town.is_police}')
print(f'цвет: {town.color}')
print(town.go(), town.show_speed(), town.turn('направо'), town.turn('налево'), town.stop() + '\n')

sport = SportCar('Mustang', 120, 'красная', False)
print(f'{sport.name}')
print(f'полицейская: {sport.is_police}')
print(f'цвет: {sport.color}')
print(sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop() + '\n')

work = WorkCar('Volkswagen', 40, 'синяя', False)
print(f'{work.name}')
print(f'полицейская: {work.is_police}')
print(f'цвет: {work.color}')
print(work.go(), work.show_speed(), work.turn('налево'), work.turn('направо'), work.stop() + '\n')

police = PoliceCar('Skoda', 110, 'белая', True)
print(f'{police.name}')
print(f'полицейская: {police.is_police}')
print(f'цвет: {police.color}')
print(police.go(), police.show_speed(), police.turn('направо'), police.stop() + '\n')
