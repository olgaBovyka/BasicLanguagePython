"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
out_f = open("my_python_file.txt", "w")
while True:
    user_string = input("Введите что-нибудь для записи в файл: ")
    if user_string == "":
        break
    out_f.write(user_string + "\n")
out_f.close()
