"""
3. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""
source_list = [3, 2, 5, 7, 5, 1, 49, 4, 3, 2, 0, 7, 2, 77]
destination_list = [el for el in source_list if source_list.count(el) == 1]
print(f"Исходный список: {source_list}")
print(f"Новый список: {destination_list}")
