first_day_int = 0
total_int = 0
counter_int = 2
var_input = input("В первый день результат спортсмена составил a километров: ")
var_input2 = input("Суммарный результат пробежек не менее b километров: ")
if var_input.isdigit() and var_input2.isdigit():
    first_day_int = int(var_input)
    total_int = int(var_input2)
    if first_day_int < total_int:
        print("1-й день: %d" % (first_day_int))
        while first_day_int < total_int:
            print("%d-й день: %0.2f" % (counter_int, first_day_int + first_day_int * 0.1))
            first_day_int = first_day_int + first_day_int * 0.1
            counter_int += 1
        print("Ответ: на %d-й день спортсмен достиг результата — не менее %d км." % (counter_int - 1, total_int))
    else:
        print("Спортсмен достиг результата в первый день.")
else:
    print("Нужно вводить целые числа. Мы работаем с ними. Все остальное мимо.")