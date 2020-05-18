"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
"""
var_list = []
var_counter = input("Введите количество элементов в списке: ")
if var_counter.isdigit():
    counter_int = int(var_counter)
    counter_int2 = 0
    while counter_int > 0:
        var_list.append(input("Введите элемент списка "))
        if counter_int2 % 2 == 0:
            var_element = var_list[counter_int2]
        else:
            var_list.append(var_element)
            var_list.pop(counter_int2 - 1)
        counter_int -= 1
        counter_int2 += 1
    print(var_list)
else:
    print("Ошибка ввода. Нужно вводить целое число.")
