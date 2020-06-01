"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
from datetime import datetime
from datetime import timedelta


class TrafficLight:
    __color = "красный"
    __running_ts = datetime.now()

    def running(self, mode):
        if mode == "красный" and self.__color == "зелёный" and timedelta(seconds=4) < datetime.now() - self.__running_ts \
                or mode == "жёлтый" and self.__color == "красный" and timedelta(seconds=7) < datetime.now() - self.__running_ts\
                or mode == "зелёный" and self.__color == "жёлтый" and timedelta(seconds=2) < datetime.now() - self.__running_ts:
            self.__color = mode
            self.__running_ts = datetime.now()
            print(self.__color, "c ", self.__running_ts)
        else:
            print("Неверная последовательность переключения или рано переключать!")

    def state(self):
        print(self.__color, "c ", self.__running_ts)


tl = TrafficLight()
colors = {
    1: "красный",
    2: "жёлтый",
    3: "зелёный"
}
while True:
    mode_var = input("введите режим: 1 - красный, 2 - жёлтый, 3 - зелёный, 4 - состояние, другое - выход ")
    if mode_var == "1" or mode_var == "2" or mode_var == "3" or mode_var == "4":
        if mode_var != "4":
            tl.running(colors[int(mode_var)])
        else:
            tl.state()
    else:
        break
