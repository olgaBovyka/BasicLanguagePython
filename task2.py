time_second_int = 0
time_minute_int = 0
time_hour_int = 0
var_input = input("Введите время в секундах: ")
if var_input.isdigit():
    time_second_int = int(var_input)
    time_minute_int = time_second_int % 3600 // 60
    time_hour_int = time_second_int // 3600
    time_second_int = time_second_int % 60
    print("Форматированное время: {:02d}:{:02d}:{:02d}".format(time_hour_int, time_minute_int, time_second_int))
else:
    print("Время в секундах - это целое число")
