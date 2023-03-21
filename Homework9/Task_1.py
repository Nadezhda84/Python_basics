"""
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
str str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.

Реализовать дескрипторы для любых двух классов
"""


class NonStr:

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError("Должно иметь строковый тип!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = NonStr()
    surname = NonStr()
    position = NonStr()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def __str__(self):
        return f'{self.surname} {self.name} должность {self.position} '


class Position(Worker):
    def get_full_name(self):
        return f'Работник: {self.surname} {self.name}'

    def get_total_income(self):
        return f'Доход: {sum(self._income.values())}'


worker_1 = Worker(5, 'Иванов', 'Тестировщик', 40000, 15000)
# worker_2 = Worker('Петр', 'Петров', 6 , 140000, 30000)
print(Worker(worker_1))
print(Worker(worker_2))
print(Position.get_full_name(worker_1))
print(Position.get_total_income(worker_1))
print(Position.get_full_name(worker_2))
print(Position.get_total_income(worker_2))
