"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, cell_count):
        self.__cell_count = cell_count

    @property
    def cell_count(self):
        return self.__cell_count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count - other.cell_count > 0:
            return Cell(self.cell_count - other.cell_count)
        else:
            print("Разница не должна быть больше нуля")
            return Cell(0)

    def __truediv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def make_order(self, raw_cell_count):
        make_order_string = ''
        count_raw_int = self.cell_count // raw_cell_count
        for i in range(0, count_raw_int):
            for j in range(0, raw_cell_count):
                make_order_string = make_order_string + "*"
            make_order_string = make_order_string + "\n"
        raw_cell_count = self.cell_count % raw_cell_count
        for j in range(0, raw_cell_count):
            make_order_string = make_order_string + "*"
        return make_order_string


my_cell_1 = Cell(2)
my_cell_2 = Cell(5)
my_cell_3 = my_cell_1 + my_cell_2
print("Результат +")
print(my_cell_3.cell_count)
my_cell_4 = my_cell_1 - my_cell_2
print("Результат M1-M2")
print(my_cell_4.cell_count)
my_cell_4 = my_cell_2 - my_cell_1
print("Результат M2-M1")
print(my_cell_4.cell_count)
my_cell_4 = my_cell_2 / my_cell_1
print("Результат /")
print(my_cell_4.cell_count)
my_cell_4 = my_cell_1 * my_cell_2
print("Результат *")
print(my_cell_4.cell_count)
print("Результат make_order")
print(my_cell_4.make_order(3))
