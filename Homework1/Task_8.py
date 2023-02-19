"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k
долек, если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).

Пример:

3 2 4 -> yes 3 2 1 -> no
"""

n = int(input("Введите длину шоколадки (количество долек): "))
m = int(input("Введите ширину шоколадки (количество долек): "))
k = int(input("Введите количество долек, которые хотите отломить: "))
if (k % n == 0 or k % m == 0) and k < n * m:
    print('yes')
else:
    print('no')
