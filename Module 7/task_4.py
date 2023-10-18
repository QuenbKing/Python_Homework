import random

print('Задача 4. По парам\n')

original_list = [random.randint(0, 100) for _ in range(10)]
new_list = [(original_list[i], original_list[i+1]) for i in range(0, len(original_list) - 1, 2)]
print(f'Оригинальный список: {original_list}')
print(f'Новый список: {new_list}')