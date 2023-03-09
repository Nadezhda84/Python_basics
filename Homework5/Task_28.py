"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
неотрицательных чисел. Из всех арифметических операций допускаются только +1 и
-1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""

from timeit import timeit


def summa(a):
    if a == 1:
        return 1
    return 1 + summa(a - 1)


try:
    a = int(input('Введите натуральное число а: '))
    b = int(input('Введите натуральное число b: '))
    print(f'{a} + {b} = {summa(a) + summa(b)}')
except Exception:
    print('Вы ввели не натуральное число!')

print(timeit("summa(a)", setup="from __main__ import summa, a", number=100000))
