my_var_int = 0
var_input = input("Введите целое положительное число: ")
if var_input.isdigit():
    my_var_int = int(var_input)
    max_int = 0
    while my_var_int > 0:
        if (my_var_int % 10) > max_int:
            max_int = my_var_int % 10
        my_var_int = (my_var_int - my_var_int % 10) // 10
    print("Самая большая цифра в числе ", max_int)
else:
    print(var_input, " - не целое число. Вы ошиблись при вводе")