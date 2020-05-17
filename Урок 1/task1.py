my_var_int = 0
my_var_int2 = 0
var_input = input("Введите целочисленную переменную: ")
var_input2 = input("Введите целочисленную переменную: ")
var_input3 = input("Введите свое имя ")
if var_input.isdigit() and var_input2.isdigit():
    my_var_int = int(var_input)
    my_var_int2 = int(var_input2)
    my_var_int3 = my_var_int + my_var_int2
    print(var_input3, ", сумма целочисленных переменных ", my_var_int3)
else:
    print(var_input3, ", мы ждем ввода целых чисел ")
