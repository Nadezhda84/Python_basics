"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open('file_2.txt',encoding='utf-8')
content = my_file.read()
print(f'Содержимое файла:')
print(content)

my_file = open('file_2.txt',encoding='utf-8')
content = my_file.readlines()
print(f'Количество строк в файле: {len(content)}')
for string in content:
    print(f'Количество слов в строке: {len(string.split())}')
my_file.close()
