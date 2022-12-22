"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.

Необходимо создать класс Клетка (Cell).

В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).

Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
"""


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other

    def __sub__(self, other):
        return self.quantity - other

    def __mul__(self, other):
        return self.quantity * other

    def __truediv__(self, other):
        return round(self.quantity / other)

    def make_cell(self, cell_in_row):
        self.cell_fall = ""
        while self.quantity > 0:
            self.quantity -= cell_in_row
            if self.quantity < 0:
                self.cell_fall += ("*" * (cell_in_row + self.quantity) + "\n")
            else:
                self.cell_fall += ("*" * cell_in_row + "\n")
        return self.cell_fall

    def __call__(self, new_quantity):
        self.quantity = new_quantity


c = Cell(73)
print(c.make_cell(13))
print(c.quantity)
print(c + 33)
c(345)
print(c / 3)
