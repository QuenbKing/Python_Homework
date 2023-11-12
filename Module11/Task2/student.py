import random


class Student:
    def __init__(self, name, surname, group, estimations_count=5):
        self.name_and_surname = ' '.join([name, surname])
        self.group = group
        self.estimations = [random.randint(0, 100) for _ in range(estimations_count)]

    def print_info(self):
        print(f'ФИ: {self.name_and_surname}, '
              f'Группа: {self.group}, '
              f'Средняя успеваемость: {sum(self.estimations)/len(self.estimations)}')
