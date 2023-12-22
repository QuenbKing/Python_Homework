from Shapes import *

print('Задача 6. Абстрактный класс\n')

circle = Circle(radius=3)
triangle = Triangle(first_side=4, second_side=3, angle=30)
rectangle = Rectangle(width=12, length=5)
#shape = Shape()

print(f'Площадь круга: {circle.get_area()}')
print(f'Площадь треуголника: {triangle.get_area()}')
print(f'Площадь квадрата: {rectangle.get_area()}')
