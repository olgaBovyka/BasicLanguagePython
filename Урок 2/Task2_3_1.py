"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
month_dict = {1: 'зима', 2: 'зима', 12: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень'}
var_month = input("Введите номер месяца: ")
if var_month.isdigit():
    month_int = int(var_month)
    if month_dict.get(month_int) is not None:
        print(month_dict.get(month_int))
    else:
        print("Номер месяца должен быть в интервале от 1 до 12")
else:
    print("Ошибка ввода. Нужно вводить целое число.")