"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''(без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

import re


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


my_list = ['attribute', 'класс', 'функция', 'type']
my_list_bytes = []
my_list_error = []
for line in my_list:
    if has_cyrillic(line) == True:
        my_list_error.append(line)
    else:
        my_list_bytes.append(bytes(line, 'utf-8'))

print(
    f"Данные слова можно записать в байтовом типе с помощью маркировки b'': "
    f"{my_list_bytes}")
print(
    f"Данные слова невозможно записать в байтовом типе с помощью маркировки b'': "
    f"{my_list_error}")
