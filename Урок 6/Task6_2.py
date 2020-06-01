"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = 1
    _width = 1
    mass = 0

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def calculate(self, norma_mass, thickness):
        self.mass = self._length * self._width * norma_mass * thickness


length_var = input("Введите длину дороги: ")
width_var = input("Введите ширину дороги: ")
try:
    rd = Road(int(length_var), int(width_var))
    norma_mass_var = input("масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: ")
    thickness_var = input("число см толщины полотна: ")
    try:
        rd.calculate(int(norma_mass_var), int(thickness_var))
        print(rd.mass, "т")
    except ValueError:
        print("Вы ввели не числа!")
except ValueError:
    print("Вы ввели не числа!")



