"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
input_string = input("Введите несколько слов через пробел ")
input_list = input_string.split()
for splitted_string in input_list:
    print(splitted_string[0:10])