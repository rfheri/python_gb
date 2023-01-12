class Validation:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значение не может быть меньше 0')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    wage = Validation()
    bonus = Validation()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.wage + self.bonus


p = Position('Иван', 'Петров', 'менеджер', -100000, 20000)
print(p.get_full_name())
print(p.get_total_income())
print(p.position)
