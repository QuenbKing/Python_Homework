print('Задание 7. Список списков\n')

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
res = [num for first_layer in nice_list for second_layer in first_layer for num in second_layer]
print(res)