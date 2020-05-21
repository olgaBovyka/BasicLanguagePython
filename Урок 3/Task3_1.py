"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_func(argument1, argument2):
    return argument1/argument2


input_var = input("Введите числитель ")
if input_var.isdigit():
    arg1_int = int(input_var)
    input_var = input("Введите знаменатель ")
    if input_var.isdigit():
        arg2_int = int(input_var)
        try:
            result_var = division_func(arg1_int, arg2_int)
            print(result_var)
        except ZeroDivisionError:
            print("Деление на 0.")
    else:
        print("Ошибка ввода. Нужно вводить целое число.")

else:
    print("Ошибка ввода. Нужно вводить целое число.")
