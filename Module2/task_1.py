print('Задание 1. Генерация списка\n')

last_num = int(input('Введите число: '))
odd_nums = []

for num in range(1, last_num + 1, 2):
    odd_nums.append(num)

print(f'Список из нечётных чисел от одного до N {odd_nums}')
