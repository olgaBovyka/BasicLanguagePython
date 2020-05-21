"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(argument1, argument2, argument3):
    argument_list = [argument1, argument2, argument3]
    argument_list.sort()
    return argument_list[1] + argument_list[2]


input_var = input("Введите аргумент 1 ")
if input_var.isdigit():
    arg1_int = int(input_var)
    input_var = input("Введите аргумент 2 ")
    if input_var.isdigit():
        arg2_int = int(input_var)
        input_var = input("Введите аргумент 3 ")
        if input_var.isdigit():
            arg3_int = int(input_var)
            result_var = my_func(arg1_int, arg2_int, arg3_int)
            print(result_var)
        else:
            print("Ошибка ввода. Нужно вводить целое число.")

    else:
        print("Ошибка ввода. Нужно вводить целое число.")

else:
    print("Ошибка ввода. Нужно вводить целое число.")

