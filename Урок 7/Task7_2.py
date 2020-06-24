"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Wear(ABC):

    @property
    @abstractmethod
    def consumption(self) -> float:
        pass


    @property
    @abstractmethod
    def params(self) -> float:
        pass

class Suit(Wear):

    def __init__(self, name: str, height: float):
        self.__height = height
        self.__name = name

    @property
    def consumption(self) -> float:
        return 2*self.__height+0.3

    @property
    def params(self) -> float:
        return self.__height


class Coat(Wear):

    def __init__(self, name: str, size: float):
        self.__name = name
        self.__size = size

    @property
    def consumption(self) -> float:
        return self.__size / 6.5 + 0.5

    @property
    def params(self) -> float:
        return self.__size

while True:
    coat_h_var = input("Введите размер пальто ")
    if coat_h_var.isdigit():
        coat_h_int = int(coat_h_var)
        break
my_coat = Coat("burberry", coat_h_int)
print("Расход ткани на 1 пальто", my_coat.consumption)
while True:
    coat_c_var = input("Введите количество пальто ")
    if coat_c_var.isdigit():
        coat_c_int = int(coat_c_var)
        break
while True:
    suit_s_var = input("Введите размер костюма ")
    if suit_s_var.isdigit():
        suit_s_int = int(suit_s_var)
        break
my_suit = Coat("prada", suit_s_int)
print("Расход ткани на 1 костюм", my_suit.consumption)
while True:
    suit_c_var = input("Введите количество костюмов ")
    if suit_c_var.isdigit():
        suit_c_int = int(suit_c_var)
        break
print("Общий расход ткани", my_suit.consumption * suit_c_int + my_coat.consumption * coat_c_int)
