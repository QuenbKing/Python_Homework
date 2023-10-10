print('Задание 6. Двумерный список\n')

nums_count = 12
res = [[list_num + num * (nums_count // 3) for num in range(3)]
       for list_num in range(1, nums_count // 3 + 1)]
print(res)