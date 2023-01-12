class Validation:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значение не может быть меньше 0')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    _length = Validation()
    _width = Validation()

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass = 25
        self.height = 5

    def a_mass(self):
        mass = self._length * self._width * self.mass * self.height / 1000
        print(f'масса асфальта, необходимого для покрытия всего дорожного полотна: {round(mass)} т')


r = Road(5000, -10)
r.a_mass()
