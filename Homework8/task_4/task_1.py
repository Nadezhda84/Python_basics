"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
my_list = []
while True:
    string = input("Введите строку (пустая строка - окончание ввода): ")
    if string == '':
        print(my_list)
        exit()
    else:
        new_string = string + '\n'
        my_list.append(new_string)

    with open("file_1.txt", "w", encoding='utf-8') as file_obj:
        file_obj.writelines(my_list)
