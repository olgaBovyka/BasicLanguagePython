"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(argument_word):
    return argument_word.title()


input_string = input("Введите строку на латинице ")
input_list = input_string.split()
output_list = []
for word_string in input_list:
    output_list.append(int_func(word_string))
print(' '.join(output_list))

