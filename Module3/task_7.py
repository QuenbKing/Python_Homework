print('Задание 7. Считалка\n')

people_amt = int(input('Количество человек: '))
num = int(input('Какое число в считалке? '))
people_nums = list(range(1, people_amt + 1))
start_index = 0

while len(people_nums) != 1:
    print(f'Текущий круг людей {people_nums}')
    print(f'Начало счёта номера {people_nums[start_index]}')
    retired_num_index = (start_index + num - 1) % len(people_nums)
    print(f'Выбывает человек под номером {people_nums[retired_num_index]}')
    if retired_num_index == len(people_nums) - 1:
        start_index = 0
    else:
        start_index = retired_num_index
    people_nums.pop(retired_num_index)


print(f'\nОстался человек под номером {people_nums[0]}')

