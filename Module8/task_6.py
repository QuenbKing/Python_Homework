print('Задача 6. Быстрая сортировка\n')


def get_lists(my_nums_list):
    less = []
    equally = []
    over = []
    reference_number = my_nums_list[len(my_nums_list) - 1]
    for num in my_nums_list:
        if num < reference_number:
            less.append(num)
        elif num == reference_number:
            equally.append(num)
        else:
            over.append(num)
    return less, equally, over


def fast_sort(my_nums_list):
    less, equally, over = get_lists(my_nums_list)
    if len(less) != 0:
        less = fast_sort(less)
    if len(over) != 0:
        over = fast_sort(over)
    return less + equally + over


nums_list = [5, 8, 9, 4, 2, 9, 1, 8]
print(fast_sort(nums_list))
