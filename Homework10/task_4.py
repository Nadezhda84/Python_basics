"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
my_list = ['разработка', 'администрирование', 'protocol', 'standard']
for line in my_list:
    var_bytes = line.encode('utf-8')
    print(var_bytes)
    var_srt = bytes.decode(var_bytes, 'utf-8')
    print(var_srt)
    print()
