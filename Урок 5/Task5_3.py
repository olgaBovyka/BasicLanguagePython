"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
file_object = open("salary_file.txt")
content = file_object.read()
strings_var = content.split("\n")
workers_count = len(strings_var)
total_salary_int = 0
file_corrupt = False
for string_el in strings_var:
    word_war = string_el.split(" ")
    if word_war[1].isdigit():
        if int(word_war[1]) < 20000:
            print(word_war[0])
    else:
        print("Нарушена структура файла!")
        file_corrupt = True
        break
    total_salary_int += int(word_war[1])
if not file_corrupt:
    print("Средняя величина дохода сотрудников ", total_salary_int/workers_count)
else:
    print("Не удается расчитать среднюю величину дохода")
file_object.close()
