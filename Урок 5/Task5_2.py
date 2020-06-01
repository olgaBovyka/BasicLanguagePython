"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
file_object = open("my_python_file.txt")
content = file_object.read()
strings_var = content.split("\n")
print(len(strings_var), "строки в текстовом файле")
for string_el in strings_var:
    word_war = string_el.split(" ")
    print(string_el,  ": слов в строке :", len(word_war))
file_object.close()
