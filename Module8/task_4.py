print('Задача 4. Продвинутая функция sum\n')


def get_sum(*nums):
    summ = 0
    for num in nums:
        if isinstance(num, list):
            summ += get_sum(*num)
        else:
            summ += num
    return summ


print(get_sum([[1, 2, [3]], [1], 3]))
