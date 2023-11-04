print('Задание 6. Бегущие цифры\n')

my_list = [1, 4, -3, 0, 10]
offset_list = []
print(f'Изначальный список: {my_list}')

offset = int(input('Введите сдвиг: '))
for index in range(len(my_list)):
    offset_list.append(my_list[(len(my_list) + (index - offset)) % len(my_list)])
print(f'Сдвинутый список: {offset_list}')