"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых
больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
from random import randint

source_list = [randint(10, 2000) for i in range(15)]
destination_list = [el for el in source_list if el > source_list[source_list.index(el)-1] and source_list.index(el) != 0]
source2_list = [el for el in range(20, 241)]
destination2_list = [el for el in source2_list if el % 20 == 0 or el % 21 == 0]
print(f"Исходный список: {source_list}")
print(f"Новый список: {destination_list}")
print(f"Исходный список 2: {source2_list}")
print(f"Новый список 2: {destination2_list}")