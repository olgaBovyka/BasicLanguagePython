my_var_int = 0
var_input = input("Введите целое число n: ")
if var_input.isdigit():
    my_var_int = int(var_input) + int(var_input+var_input) + int(var_input+var_input+var_input)
    print("Результат n+nn+nnn=", my_var_int)
else:
    print("n - целое число. Вы ввели не число...")