"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

salary_amount = 0
count = 0
persons = []
with open("file_3.txt", "r", encoding='utf-8') as file_obj:
    for line in file_obj:
        print(line, end="")
        current_line = line.split()
        if int(current_line[1]) < 20000:
            persons.append(current_line[0])
            salary_amount += int(current_line[1])
            count += 1
result = round(salary_amount / count, 2)
print(f"Сотрудники с окладом менее 20000: {persons}")
print(f"Средний доход этих сотрудников: {result}")
