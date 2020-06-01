"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

only_dict = {}
sum_profit = 0
count_int = 0
with open("firms_file.txt") as file_object:
    for subject_var in file_object:
        word_list = subject_var.split(" ")
        this_profit = int(word_list[2]) - int(word_list[3])
        new_dict = {word_list[0]: this_profit}
        if this_profit > 0:
            sum_profit += this_profit
            count_int += 1
        only_dict.update(new_dict)
average_profit_dict = {'average_profit':sum_profit/count_int}
some_list = [only_dict, average_profit_dict]
print(some_list)
with open("firms_file.json", "w") as write_f:
    json.dump(some_list, write_f)
#print(some_list)
