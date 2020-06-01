"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
(карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы
должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для
 каждого экземпляра.
"""


class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):

    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):

    def draw(self):
        print("Рисуем маркером")


pen1 = Pen()
pen1.draw()

pencil1 = Pencil()
pencil1.draw()

handle1 = Handle()
handle1.draw()

something = Stationery()
something.draw()