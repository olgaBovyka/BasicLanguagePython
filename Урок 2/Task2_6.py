"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
— номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
number_var = input("Введите количество товаров ")
if number_var.isdigit():
    number_int = int(number_var)
    counter_int = 0
    goods_list = []
    while counter_int < number_int:
        good_list = []
        print("Введите параметры товара ", counter_int + 1)
        input_var = input("Введите название товара ")
        while True:
            input_var2 = input("Введите цену товара ")
            if input_var2.isdigit():
                break
        while True:
            input_var3 = input("Введите количество товара ")
            if input_var3.isdigit():
                break
        input_var4 = input("Введите единицу измерения товара ")
        parameters_dict = dict(название=input_var, цена=input_var2, количество=input_var3, ед=input_var4)
        good_list.insert(0, counter_int)
        good_list.insert(1, parameters_dict)
        goods_list.append(tuple(good_list))
        counter_int += 1
    print("Структура данных ТОВАРЫ")
    print(goods_list)
    name_list = []
    price_list = []
    count_list = []
    metric_list = []
    for name_var in goods_list:
        name_list.append(name_var[1].get('название'))
        price_list.append(name_var[1].get('цена'))
        count_list.append(name_var[1].get('количество'))
        metric_list.append(name_var[1].get('ед'))
    analytic_dict = dict(название=list(set(name_list)), цена=list(set(price_list)), количество=list(set(count_list)), ед=list(set(metric_list)))
    print("Структура данных АНАЛИТИКА")
    print(analytic_dict)
else:
    print("Ошибка ввода. Нужно вводить целое число.")





