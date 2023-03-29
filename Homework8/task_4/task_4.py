"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
translater = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('file_4.txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        line = line.split(' ', 1)
        new_file.append(translater[line[0]] + '  ' + line[1])
    print(new_file)

with open('file_4_new.txt', 'w',encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)