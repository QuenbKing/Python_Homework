print('Задача 5. Функция сортировки\n')


def tpl_sort(tpl):
    if all(type(num) is int for num in tpl):
        return tuple(sorted(tpl))
    else:
        return tpl


my_tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(my_tpl))