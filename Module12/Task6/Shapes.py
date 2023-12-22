import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Triangle(Shape):
    def __init__(self, first_side, second_side, angle):
        self.first_side = first_side
        self.second_side = second_side
        self.angle = angle

    def get_area(self):
        return 0.5 * self.first_side * self.second_side * math.sin(math.radians(self.angle))


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2
