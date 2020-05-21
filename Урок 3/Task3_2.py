"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def single_string_func(name, surname, birth_year, city, email, phone):
    return f"Данные о пользователе: {name} {surname} {birth_year} года рождения, проживает в городе {city} email: {email} телефон: {phone}"


name_str = input("Введите Ваше имя: ")
surname_str = input("Введите Вашу фамилию: ")
birth_year_str = input("Введите Ваш год рождения: ")
city_str = input("Введите Ваш город проживания: ")
email_str = input("Введите Ваш адрес электронной почты: ")
phone_str = input("Введите Ваш телефон: ")
print(single_string_func(name_str, surname_str, birth_year_str, city_str, email_str, phone_str))