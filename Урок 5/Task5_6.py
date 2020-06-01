"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
 были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
 Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
file_object = open("subjects_file.txt")
content = file_object.read()
strings_var = content.split("\n")
only_dict = {}
for subject_var in strings_var:
    word_list = subject_var.split(":")
    hours_list = word_list[1].split(" ")
    sum_hours = 0
    for el in hours_list:
        if el.count("(") > 0:
            literal_list = el.split("(")
            sum_hours += int(literal_list[0])
    new_dict = {word_list[0]:sum_hours}
    only_dict.update(new_dict)
print(only_dict)
file_object.close()
