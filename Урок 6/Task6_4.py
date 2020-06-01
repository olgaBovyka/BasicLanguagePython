"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = 0

    def go(self, speed):
        self.speed = speed
        print("Машина поехала со скоростью ", self.speed)

    def stop(self):
        self.speed = 0
        print("Машина остановилась")

    def turn(self, direction):
        print("Машина повернула в направлении ", direction)

    def show_speed(self):
        print("Текущая скорость ", self.speed)


class TownCar(Car):

    def __init__(self):
        self.is_police = 0

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        print("Текущая скорость ", self.speed)


class SportCar(Car):

    def __init__(self):
        self.is_police = 0


class WorkCar(Car):

    def __init__(self):
        self.is_police = 0

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        print("Текущая скорость ", self.speed)


class PoliceCar(Car):

    def __init__(self):
        self.is_police = 1


car1_car = PoliceCar()
car1_car.go(70)
car1_car.turn("направо")
car1_car.show_speed()
car1_car.stop()
car1_car.show_speed()
car2_car = WorkCar()
car2_car.go(50)
car2_car.turn("направо")
car2_car.show_speed()
car2_car.stop()
car2_car.show_speed()