from MyMath import MyMath

print('Задача 2. Математический модуль\n')

circle_len = MyMath.circle_len(radius=5)
circle_sq = MyMath.circle_sq(radius=6)
cube_volume = MyMath.cube_volume(edge_length=3)
sphere_surface_sq = MyMath.sphere_surface_sq(radius=2)
print(f'Длина окружности: {circle_len}')
print(f'Площадь окружности: {circle_sq}')
print(f'Объём куба: {cube_volume}')
print(f'Площадь поверхности сферы: {sphere_surface_sq}')