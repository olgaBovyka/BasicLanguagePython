"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
file_object = open("english_numeric.txt")
out_f = open("russian_numeric.txt", "w")
content = file_object.read()
strings_var = content.split("\n")
russian_numbers = {
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    0: 'ноль'
}
for string_el in strings_var:
    word_war = string_el.split(" ")
    if word_war[len(word_war)-1].isdigit() and len(word_war[len(word_war)-1]) == 1:
        word_war[0] = russian_numbers[int(word_war[len(word_war)-1])]
        whole_string = " ".join(word_war)
        out_f.write(whole_string + "\n")
    else:
        print("Нарушена структура файла!")
        file_corrupt = True
        break
file_object.close()
out_f.close()
