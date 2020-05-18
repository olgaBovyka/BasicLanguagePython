"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
winter_list = [1, 2, 12]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
fall_list = [9, 10, 11]
var_month = input("Введите номер месяца: ")
if var_month.isdigit():
    month_int = int(var_month)
    if winter_list.count(month_int) > 0:
        print("время года - зима")
    else:
        if spring_list.count(month_int) > 0:
            print("время года - весна")
        else:
            if summer_list.count(month_int) > 0:
                print("время года - лето")
            else:
                if fall_list.count(month_int) > 0:
                    print("время года - осень")
                else:
                    print("Номер месяца должен быть в интервале от 1 до 12")
else:
    print("Ошибка ввода. Нужно вводить целое число.")