"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from copy import deepcopy


class Matrix:

    def __init__(self, data: list):
        self.__data = deepcopy(data)
        self.__shape = (len(max(self.__data, key=len)), len(self.__data))
        if len(max(self.__data, key=len)) != self.shape[0]:
            self.reshape()

    @property
    def shape(self):
        return self.__shape

    def reshape(self):
        for itm in self.__data:
            tmp = self.shape[0] - len(itm)
            if tmp:
                itm.extend(0 for _ in range(tmp))

    def __getitem__(self, item):
        return self.__data[item]

    def __iter__(self):
        return deepcopy(self.__data.__iter__())

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Это у нас не матрица! Это же {type(other).__name__}")
        if self.shape != other.shape:
            raise ValueError(f"Не соответствует размерность матриц {self.shape} и {other.shape}")

        return Matrix(list(map(lambda y: list(map(sum, y)),
                               map(lambda x: list(zip(*x)), zip(self, other))
                               )
                           )
                      )

    def __str__(self):
        max_len_itm = len(str(max(map(lambda item: max(item, key=lambda x: len(str(x))), self.__data))))
        if not max_len_itm & 1:
            max_len_itm += 1

        result = ''
        for line in self.__data:
            result += ' '.join((f"{itm:<{max_len_itm}}" for itm in line)) + "\n"
        return result


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [2, 2, 2]])
print(matrix1)
matrix2 = Matrix([[5, 2, 5], [4, 0, -1], [4, 3, 0]])
print(matrix2)
matrix3 = matrix1+matrix2
print(matrix3)
