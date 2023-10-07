print('Задание 8. Сортировка\n')

my_list = [1, 4, -3, 0, 10]
print(f'Изначальный список: {my_list}')
for i in range(len(my_list)):
    for j in range(i, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(f'Отсортированный список: {my_list}')

'''
my_list = [1, 4, -3, 0, 10]
print(f'Изначальный список: {my_list}')
my_list.sort()
print(f'Отсортированный список: {my_list}')
'''
