print('Задание 7. Три списка\n')

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

first_res = [num for num in array_1 if (num in array_2) and (num in array_3)]
first_set = set(array_1) & set(array_2) & set(array_3)
second_res = [num for num in array_1 if (num not in array_2) and (num not in array_3)]
second_set = set(array_1) - set(array_2) - set(array_3)

print('Задача 1')
print(f'Решение без множеств: {first_res}')
print(f'Решение с множествами: {first_set}')
print('Задача 2')
print(f'Решение без множеств: {second_res}')
print(f'Решение с множествами: {second_set}')