"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
 передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    wage = 0
    bonus = 0
    _income = {"wage": wage, "bonus": bonus}
    total_income = 0


class Position(Worker):

    def set_full_name(self):
        self.surname = input("Введите фамилию: ")
        self.name = input("Введите имя: ")

    def get_full_name(self):
        print("Полное имя:", self.surname, self.name)

    def set_total_income(self):
        wage_var = input("Введите оклад: ")
        bonus_var = input("Введите премию: ")
        try:
            self.wage = int(wage_var)
            self.bonus = int(bonus_var)
        except ValueError:
            print("Вы ввели не числа!")

    def get_total_income(self):
        self._income = {"wage": self.wage, "bonus": self.bonus}
        self.total_income = self.wage + self.bonus


position_my = Position()
position_my.set_full_name()
position_my.get_full_name()
position_my.set_total_income()
position_my.get_total_income()
print("доход с учетом премии ", position_my.total_income)
