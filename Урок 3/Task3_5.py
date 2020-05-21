"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_func(list_parameter):
    number_list = list(list_parameter)
    sum_int = 0
    for some_int in number_list:
        sum_int += int(some_int)
    return sum_int


print("Вы будете вводить числа через пробелы до тех пор, пока не введете специальный символ #")
sum_int2 = 0
while True:
    input_var = input("введите числа через пробелы: ")
    input_list = []
    input_list = input_var.split()
    if input_list.count("#"):
        input_list.pop(input_list.index("#"))
        try:
            sum_int2 += sum_func(input_list)
            print(sum_int2)
        except ValueError:
            print("Введены не числа!")
        print("Ввод окончен. Спасибо!")
        break
    try:
        sum_int2 += sum_func(input_list)
        print(sum_int2)
    except ValueError:
        print("Введены не числа!")
