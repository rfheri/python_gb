"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = []
        for row in self.data:
            result.append(' '.join([str(k) for k in row]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.data) == len(other.data):
            result = []
            for i, row in enumerate(self.data):
                new_list = list(map(lambda x, y: x + y, row, other.data[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return


lst_01 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst_02 = [[4, 5, 6], [7, 8, 9], [0, 1, 2]]

matr_1 = Matrix(lst_01)
matr_2 = Matrix(lst_02)
matr_3 = matr_1 + matr_2

print(matr_1, end='\n\n')
print(matr_2, end='\n\n')
print(matr_3)
