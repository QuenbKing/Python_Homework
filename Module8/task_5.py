print('Задача 5. Список списков — 2\n')


def unpack_list(my_list):
    if len(my_list) == 0:
        return my_list
    if isinstance(my_list[0], list):
        return unpack_list(my_list[0]) + unpack_list(my_list[1:])
    return my_list[:1] + unpack_list(my_list[1:])


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(unpack_list(nice_list))
