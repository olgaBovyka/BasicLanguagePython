"""
6. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо
выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(n):
    object_iterator = [el for el in range(1, n + 1)]
    fact_int = 1
    object_iterator2 = []
    for ell in object_iterator:
        fact_int *= ell
        object_iterator2.append(fact_int)
    yield object_iterator2


count_var = input("Введите целое число n: ")
if count_var.isdigit():
    print_list = [el for el in fact(int(count_var))]
    print(print_list[0])
else:
    print("Введено не целое число")
