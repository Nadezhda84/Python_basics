"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
числу X. Пользователь в первой строке вводит натуральное число N – количество
элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""


def find_number(list_1, number):
    list_dif = []
    for i in range(len(list_1)):
        list_dif.append(abs(number - list_1[i]))
    min_index = list_dif.index(min(list_dif))
    return list_1[min_index]


try:
    n = int(input('Введите количество элементов в списке: '))
    my_list = []
    for i in range(n):
        num = int(input('Введите натуральное число: '))
        my_list.append(num)
    for elem in my_list:
        print(elem, end=' ')
    print()
    item = int(input('Введите натуральное число: '))

    res = find_number(my_list, item)
    print(res)
except ValueError:
    print('Введите натуральное число!')
