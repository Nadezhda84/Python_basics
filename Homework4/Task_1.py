"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются
в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

from timeit import timeit


def list_completion(count):
    my_list = []
    for i in range(count):
        elem = int(input(f'Введите целое число {i + 1}: '))
        my_list.append(elem)
    return my_list


n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
print('Введите элементы первого множества')
my_list_n = list_completion(n)
my_list_n.sort()
print('Введите элементы второго множества')
my_list_m = list_completion(m)
my_list_m.sort()
print(my_list_n)
print(my_list_m)

set_1 = set(my_list_n)
set_2 = set(my_list_m)
set_res = set_1.intersection(set_2)
print(f'Числа, встречающиеся в обоих множествах,: {set_res}')

print(timeit("list_completion(n)",
             setup="from __main__ import list_completion, n", number=4))
