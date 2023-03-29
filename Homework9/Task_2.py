"""
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

Реализовать дескрипторы для любых двух классов
"""

import math


class Сhecking:
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('Должно быть числом!')
        if value < 0:
            raise ValueError('Не может быть отрицательным числом!')
        instance.__dict__[self.my_attr] = value


class Road:
    _length = Сhecking()
    _width = Сhecking()
    mass_of_asphalt = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calc(self):
        return self._length * self._width * self.mass_of_asphalt * \
            self.thickness


# obj_1 = Road(-25, 5000)
obj_2 = Road('-25', 5000)

print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна, '
      f'равна {math.ceil(obj_1.asphalt_mass_calc() / 1000)} тонн')
