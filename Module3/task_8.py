print('Задание 8. Симметричная последовательность\n')


def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    return num_list == reverse_list


nums_count = int(input('Количество чисел: '))
nums = []
for _ in range(nums_count):
    num = int(input('Число: '))
    nums.append(num)
print(f'Последовательность: {nums}')

new_nums = []
res = []
for i_new_nums in range(0, len(nums)):
    for j_new_nums in range(i_new_nums, len(nums)):
        new_nums.append(nums[j_new_nums])
    if is_palindrome(new_nums):
        for i_res in range(0, i_new_nums):
            res.append(nums[i_res])
        res.reverse()
        break
    new_nums = []

print(f'Нужно приписать чисел: {len(res)}')
print(f'Сами числа: {res}')
