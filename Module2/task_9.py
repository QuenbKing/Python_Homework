print('Задание 9. Обратный анализ чётных чисел\n')

my_list = [1, 4, 3, 2, 5, 8, 7, 10, 9, 26, 11, 22, 13]
my_list.sort()

for index in range(len(my_list) - 1, -1, -1):
    if my_list[index] % 2 == 0:
        print(my_list[index], end=' ')