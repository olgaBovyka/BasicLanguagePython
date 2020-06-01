"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

out_f = open("any_numeric.txt", "w")
number_numeric_var = input("Введите количество чисел в файле ")
if number_numeric_var.isdigit():
    number_numeric_int = int(number_numeric_var)
    numeric_string = ""
    while number_numeric_int > 0:
        numeric_string += (str(random.randint(0, 20000)) + " ")
        number_numeric_int -= 1
    out_f.write(numeric_string)
    out_f.close()
    file_object = open("any_numeric.txt")
    content = file_object.read()
    strings_var = content.split(" ")
    sum_int = 0
    strings_var.pop(len(strings_var)-1)
    for el in strings_var:
        sum_int += int(el)
    print("Сумма чисел в файле ", sum_int)
else:
    print("Мы ждали ввода целого числа...")
file_object.close()
