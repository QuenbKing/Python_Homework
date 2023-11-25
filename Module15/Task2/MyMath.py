import math


class MyMath:
    @classmethod
    def circle_len(cls, radius: float) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, edge_length: float) -> float:
        return edge_length ** 3

    @classmethod
    def sphere_surface_sq(cls, radius: float) -> float:
        return 4 * math.pi * radius ** 2
